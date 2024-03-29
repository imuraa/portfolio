# 分散型図書管理アプリ

## アプリ概要
建物内に分散して保管されている書籍をデータベースで管理し、  
図書館のようにアプリ上で貸出・返却手続きができるようにする為のWEBアプリです。  
<img width="803" alt="検索機能①" src="https://github.com/imuraa/portfolio/assets/146056765/7bb072c0-670f-450a-a925-61f90ccf1ef8">

### 機能一覧
・ログイン機能  
・ユーザ登録機能  
・本の登録機能  
・本の検索機能  
・本の貸出予約/返却機能  
・貸出返却履歴の表示機能  
・返却期限切れ警告機能  

### 本の登録
データベースに管理したい本を登録することができます。  
ISBNコードを入力するだけでGoogleBooksAPIから自動で  
本のタイトル、著者名、出版社などの情報を取得できます。 
![書籍の登録](https://github.com/imuraa/portfolio/assets/146056765/1a7f4654-db18-419f-a91d-133eae6a927a)

### 本の検索
借りたい本を検索することができます。  
本のタイトルや著者名、ISBNコードを使って検索できます。  
![本の検索](https://github.com/imuraa/portfolio/assets/146056765/cbc4d23f-ce6f-4b3a-ac2b-e928dd59d22b)

### 本の貸出予約/返却
本の貸出予約と返却ができます。  
カレンダーから借りる期間を設定することが出来ます。  
カレンダーで予約の空き状況を確認できます。  
![本を借りる](https://github.com/imuraa/portfolio/assets/146056765/c622bf94-3ae1-4568-89cf-142035413407)

## 必要環境
Windows 11  
Python 3.11.5  
Django 4.2.5  
MySQL 8.0.35  
mysqlclient 2.2.0

## 環境構築手順
### 前提条件
・WindowsOSのローカル環境で動作させることを想定しています。  
・Python、MySQLは既にインストールされているものとし、ここでの説明は省略します。

### 目次
1. リポジトリのクローン
2. 必要モジュールの一括インストール
3. データベースの作成
6. local_settings.pyの作成
7. マイグレーション
8. 管理者の作成
9. 開発用サーバの起動

### 1. リポジトリのクローン
1. Git Bashを起動します
2. Djangoプロジェクトを配置したいディレクトリに移動します
3. 以下のコマンドを実行します
   ```
   git clone https://github.com/imuraa/portfolio.git
   ```
   
### 2. 必要モジュールの一括インストール
1. コマンドプロンプトでportfolio/projectディレクトリに移動し、以下のコマンドを実行します
   ```
   pip install -r requirements.txt
   ```

### 3. データベースの作成
1. コマンドプロンプトで以下のコマンドを実行し、MySQLサーバに接続します
   ```
   mysql -u root -p
   Enter password:MYSQL_ROOT_PASSWORD
   Enter password(again):MYSQL_ROOT_PASSWORD
   ```
2. Djangoアプリで使用するデータベースを作成します
   ```
   mysql> CREATE DATABASE YOUR_DATABASE_NAME;
   ```
3. 以下のコマンドを実行し、作成したデータベースの名前が表示されればデータベースの作成は完了です
   ```
   mysql> show databases;
   ```
   ```
   +--------------------+
   | Database           |
   +--------------------+
   | xxxxx              |
   | YOUR_DATABASE_NAME |
   | xxxxx              |
   | xxxxx              |
   +--------------------+
   ```
   
4. 以下のコマンドでMySQLサーバの接続を終了します
   ```
   mysql> exit;
   ```

### 4. local_settings.pyの作成
1. コマンドプロンプトでportfolio/projectディレクトリに移動し、以下のコマンドを実行します(manage.pyがあるディレクトリ)
   ```
   python manage.py shell
   ```
2. シェルが起動するので以下のコマンドを実行します
   ```
   >>> from django.core.management.utils import get_random_secret_key
   >>> get_random_secret_key()
   ```
3. Djangoの秘密鍵が生成されるのでコピーします
4. portfolio/project/projectディレクトリに移動します(settings.pyがあるディレクトリ)
5. local_settings.pyという名前でファイルを作成し、Djangoの秘密鍵とデータベースの情報を記述して保存します。

```
SECRET_KEY = '手順4-3でコピーした秘密鍵'
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'YOUR_DATABASE_NAME',
    'USER': 'MYSQL_USER',
    'PASSWORD': 'MYSQL_PASSWORD',
  }
}   
```  

### 5. マイグレーション
1. コマンドプロンプトでportfolio/projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドでマイグレーションファイルを生成します
   ```
   python manage.py makemigrations
   ```
3. 以下のコマンドでマイグレーションを実行します
   ```
   python manage.py migrate
   ```

### 6. 管理者の作成
1. コマンドプロンプトでportfolio/projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドを実行します
   ```
   python manage.py createsuperuser
   ```
3. 管理者のユーザ名、メールアドレス、パスワードを設定します
   ```
   Username(leave blank to use 'xxx'):
   Email address:
   Password:
   Password(again):
   ```
4. 以下のメッセージが表示されれば管理者の作成は完了です
    ```
    Superuser created successfully.
    ```

### 7. 開発用サーバの起動
1. コマンドプロンプトでportfolio/projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドでDjangoの開発用サーバを起動します
   ```
   python manage.py runserver
   ```
5. Webブラウザから以下のURLにアクセスします  
   http://127.0.0.1:8000/library
6. 分散型図書管理アプリのログイン画面が表示されたら開発用サーバの起動は完了です  
   ユーザ登録、本の登録などは管理者画面から行うことが出来ます  
   http://127.0.0.1:8000/admin
