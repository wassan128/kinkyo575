import oauth2
import re
import tweepy


class Tweets():
    def __init__(self, api):
        self.api = api
        self.screen_name = api.me().screen_name

    def get(self, demand=256):
        cnt = 0
        data = []
        exclude_ptn = re.compile(r"^[(?:RT)@]")

        tl = tweepy.Cursor(self.api.user_timeline, screen_name=self.screen_name, exclude_replies=True).items()
        for tweet in tl:
            if cnt >= demand:
                break
            try:
                text = tweet.text
                if text and not exclude_ptn.search(text):
                    data.append(text)
                    cnt += 1
            except UnicodeEncodeError:
                pass
       
        return data

    def post(self, status):
        res = "ok"
        try:
            self.api.update_status(status=status)
        except tweepy.TweepError:
            res = "error"
            
        return res


