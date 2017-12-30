from flask import abort, Flask, flash, jsonify, redirect, request, render_template, session
import os
import tweepy
from twitter_handle import Tweets
from generate import *


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
URL_CALLBACK = "http://localhost:5000/callback"

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


def is_login():
    if session.get("is_login"):
        api = get_interface()
        name = False
        if api:
            name = api.me().name
        return name
    else:
        return False

def get_interface():
    access_token = session.get("access_token")
    access_token_secret = session.get("access_token_secret")

    api = None
    if access_token and access_token_secret:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

    return api

def get_senryu():
    senryu = None
    api = get_interface()
    if api:
        twit = Tweets(api)
        data = twit.get()
        senryu = generate_575(data)
    return senryu
    

@app.route("/")
def index():
    islogin = is_login()
    return render_template("index.html", user=islogin)
 
@app.route("/auth")
def auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, URL_CALLBACK)
    redirect_url = auth.get_authorization_url()
    session["request_token"] = auth.request_token

    return redirect(redirect_url)   

@app.route("/callback")
def callback():
    session["verifier"] = request.args.get("oauth_verifier")
    try:
        token = session.pop("request_token", None)
        verifier = session.pop("verifier", None)

        if token is not None and verifier is not None:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, URL_CALLBACK)
            auth.request_token = token
            auth.get_access_token(verifier)
            session["access_token"] = auth.access_token
            session["access_token_secret"] = auth.access_token_secret
            session["is_login"] = True
            return redirect("/")
        else:
            return redirect("/auth")
    except:
        abort(401)

@app.route("/senryu")
def senryu():
   senryu = get_senryu()
   return jsonify(senryu)

@app.route("/post", methods=["POST"])
def post():
    text = request.data.decode("utf-8")

    api = get_interface()
    if api:
        twit = Tweets(api)
        res = twit.post("{}\n#近況圧縮575".format(text.replace("\n", " ").replace("　", "")))

    return jsonify({"res": res})

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.errorhandler(401)
def error_401(error):
    return "Error - 401"

@app.errorhandler(404)
def error_404(error):
    return "Error - 404"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(port=port)
