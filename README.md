# 近況圧縮575

<img src="https://raw.githubusercontent.com/wassan128/kinkyo575/images/s1.png" alt="近況圧縮575ログイン画面" width="500px"/>

## これは
* ツイートから575を生成するTwitter連携アプリです。
* サーバーサイドはPython3で書きました。
* herokuにホスティングしています(2018/1/2現在)。[フリープランのメモリ不足問題](https://devcenter.heroku.com/articles/error-codes#r14-memory-quota-exceeded)で時々寝ています(すみません)。

## 特徴
* 575の生成にあたって形態素解析を使っています。
* スマホ対応しています。
* サイト内で#057577というカラーコードを使用しました。

# 使い方
* [近況圧縮575](https://kinkyo575.herokuapp.com/)にアクセスします。
* 「ログインして近況を圧縮」をクリックします(Twitter連携認証ページに飛びます)。
* 連携を許可するとアプリページに遷移し、数十秒程度で575の生成・表示がされます。
* 気に入った575はクリック、確認ウィンドウで「はい」を選択することでツイートできます。
* 勝手にツイートされることはありませんのでご安心ください。

<img src="https://raw.githubusercontent.com/wassan128/kinkyo575/images/s2.png" alt="ツイート確認ウィンドウ" width="500px"/>

# ライセンス
MIT

