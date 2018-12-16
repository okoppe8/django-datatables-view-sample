# django-datatables-view-sample

[django-datatables-view](https://pypi.org/project/django-datatables-view/)を動かして試せるサンプルアプリです。

解説：（QiitaのURL）

# 使い方

１．事前にpython(3.5以上)をインストールする。

２．gitでプロジェクトをダウンロードする

```
git clonet https://github.com/okoppe8/django-datatables-view-sample.git
```

※ gitがない場合は左上の「Clone or Download」→ 「Download ZIP」でもOK

３．セットアップコマンドを実行する

```
cd django-datatables-view-sample
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
manage.py runserver
```

```
cd django-datatables-view-sample
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

４．ブラウザを立ち上げてURLを開く

```
http://localhost:8000
```
