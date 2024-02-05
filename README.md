# 図書管理アプリ

## アプリ概要
本の貸出予約、返却等ができるアプリです。

## 必要環境
Windows 11  
Python 3.11.5  
Django 4.2.5  
MySQL 8.0.35
mysqlclient 2.2.0

## 環境構築手順(編集中)
### 前提条件
・WindowsOSのローカル環境で動作させることを想定しています。  
・当該環境にはGit、Python、MySQLが既にインストールされているものとします。

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
1. portfolio>projectディレクトリに移動し、以下のコマンドを実行します
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
1. コマンドプロンプトを起動し、手順1で複製したportfolio>projectディレクトリに移動します(manage.pyがあるディレクトリ)
2. 以下のコマンドを実行します
   ```
   python manage.py shell
   ```
3. シェルが起動するので以下のコマンドを実行します
   ```
   >>> from django.core.management.utils import get_random_secret_key
   >>> get_random_secret_key()
   ```
4. Djangoの秘密鍵が生成されるのでコピーします
5. portfolio>project>projectディレクトリに移動します(settings.pyがあるディレクトリ)
6. local_settings.pyという名前でファイルを作成し、Djangoの秘密鍵とデータベースの情報を記述して保存します。

```
SECRET_KEY = '手順7-4でコピーした秘密鍵'
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
1. コマンドプロンプトを開き、portfolio>projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドを実行してマイグレーションファイルを生成します
   ```
   python manage.py makemigrations
   ```
3. 以下のコマンドを実行し、マイグレーションを実行します
   ```
   python manage.py migrate
   ```

### 6. 管理者の作成
1. コマンドプロンプトを開き、portfolio>projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドを実行します
   ```
   python manage.py createsperuser
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
1. コマンドプロンプトを開き、手順6で複製したportfolio>projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドを実行し、Djangoの開発用サーバを起動します
   ```
   pythoon manage.py runserver
   ```
5. Webブラウザから以下のURLにアクセスします  
   http://127.0.0.1:8000/library
6. 図書管理アプリのログイン画面が表示されたら開発用サーバの起動は完了です
