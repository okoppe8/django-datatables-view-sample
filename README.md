# django-datatables-view-sample

[django-datatables-view](https://pypi.org/project/django-datatables-view/)を実際に動かして試せるサンプルアプリです。

解説：（QiitaのURL）

# 使い方

１．事前にpython(3.5以上)をインストールする。

２．gitでプロジェクトをダウンロードする

```
git clone https://github.com/okoppe8/django-datatables-view-sample.git
```

※ gitがない場合は左上の「Clone or Download」→ 「Download ZIP」でもOK

３．セットアップコマンドを実行する

windows

```
cd django-datatables-view-sample
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
```

MacOS/Linux

```
cd django-datatables-view-sample
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

４．開発用サービスを立ち上げてURLを開く

windows

```
manage.py runserver
```

MacOS/Linux

```
python manage.py runserver
```

URL

```
http://localhost:8000
```