# 図書管理アプリ

## アプリ概要
本の貸出予約、返却等ができるアプリです。

## 必要環境
Windows 11  
Python 3.11.5  
Django 4.2.5  
MySQL 8.0.35  

## 環境構築手順(編集中)
### 前提条件
・WindowsOSのローカル環境で動作させることを想定しています。  
・当該環境にはGitが既にインストールされているものとします。

### 目次
1. Pythonのインストール
2. Djangoのインストール
3. MySQLのインストール
4. データベースの作成
5. mysqlclientのインストール
6. リポジトリのクローン
7. local_settings.pyの作成
8. マイグレーション
9. 管理者の作成
10. 開発用サーバの起動

### 1. Pythonのインストール
1. 下記のURLからPythonの公式サイトにアクセスします  
   https://www.python.org/
2. メニューから「Downloads」をクリックします
3. 過去のバージョンの一覧から「Python 3.11.5」を探してクリックします
4. 画面を下にスクロールし、Filesから「Windows installer(64-bit)」をクリックします
5. ダウンロードした「python-3.11.5-amd64.exe」を起動します
6. 「Add python.exe to PATH」にチェックを入れ、「Install Now」をクリックします
7. インストールが終わると「Setup was successful」と表示されるので「close」をクリックして画面を閉じます

### 2. Djangoのインストール
1. コマンドプロンプトで以下のコマンドを実行します
   ```
   pip install django==4.2.5
   ```

### 3. MySQLのインストール
1. 下記のURLからMySQLの公式サイトにアクセスします  
   https://www.mysql.com/jp/
2. メニューから「ダウンロード」をクリックします
3. 画面を下にスクロールすると「MySQL Community (GPL) Downloads »」というリンクがあるのでクリックします
4. 「MySQL Community Server」をクリックします
5. 「Windows (x86, 64-bit), MSI Installer」と書かれた右側のDownloadボタンをクリックします
6. オラクルのアカウント作成を促されますが画面下部の「No thanks, just start my download.」のリンクをクリックします
7. ダウンロードした「mysql-8.x.x-winx64.msi」を起動し、「Next」をクリックします
8. 「I accept the terms in the License Agreement」にチェックを入れて「Next」をクリックします
9. インストールタイプは「Typical」を選択し、Nextをクリックします
10. 「Install」をクリックします
11. 「Run MySQL Configurator」にチェックを入れて「finish」をクリックします
12. MySQL Configuratorが起動するので「Next」をクリックします
13. 「Type and Networking」の項目では必要無ければ規定値のまま「Next」をクリックします
14. 「Accounts and Roles」の項目で任意のrootパスワードを設定します（ここで設定したパスワードは後で使用する為忘れないよう控えて下さい）
15. 他の項目は必要無ければ規定値のまま「Next」をクリックして進めます
16. 「Apply Configuration」の項目では「Execute」をクリックします
17. インストールが終了したら「Next」、「finish」をクリックして画面を閉じます
18. Windowsのスタート画面を開き、歯車アイコンの設定を開きます
19. メニューからシステムを選択し、バージョン情報を開きます
20. 「システムの詳細設定」をクリックします
21. 「詳細設定」タブにある「環境変数」ボタンを押します
22. システム環境変数の中から「Path」を選択し、「編集」ボタンを押します
23. 「新規」ボタンをクリックします
24. コマンドプロンプトでmysqlコマンドを使えるようにする為、規定値で設定した場合は以下のパスを入力します
    ```
    C:\Program Files\MySQL\MySQL Server 8.0\bin
    ```
25. 変更を適用する為、OKボタンをクリックして設定画面を閉じます
26. 再起動します
27. コマンドプロンプトで以下のコマンドを実行します
    ```
    mysql --version
    ```
28. 以下のようにバージョン情報が表示されたらMySQLのインストールは完了です
    ```
    mysql  Ver 8.x.x for Win64 on x86_64 (MySQL Community Server - GPL)
    ```

#### 4. データベースの作成
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

### 5. mysqlclientのインストール
1. コマンドプロンプトで以下のコマンドを実行します
   ```
   python -m pip install mysqlclient
   ```

### 6. リポジトリのクローン
1. Git Bashを起動します
2. Djangoプロジェクトを配置したいディレクトリに移動します
3. 以下のコマンドを実行します
   ```
   git clone https://github.com/imuraa/portfolio.git
   ```

### 7. local_settings.pyの作成
1. コマンドプロンプトを起動し、手順6で複製したportfolio>projectディレクトリに移動します(manage.pyがあるディレクトリ)
2. 以下のコマンドを実行します
   ```
   python manage.py shell
   ```
3. シェルが起動するので以下のコマンドを実行します
   ```
   from django.core.management.utils import get_random_secret_key
   get_random_secret_key()
   ```
4. Djangoの秘密鍵が生成されるのでコピーします
5. portfolio>project>projectディレクトリに移動します(settings.pyがあるディレクトリ)
6. local_settings.pyという名前でファイルを作成します
7. local_settings.pyにはDjangoの秘密鍵とデータベースの情報を記述して保存します。

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

### 8. マイグレーション
1. コマンドプロンプトを開き、portfolio>projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドを実行してマイグレーションファイルを生成します
   ```
   python manage.py makemigrations
   ```
3. 以下のコマンドを実行し、マイグレーションを実行します
   ```
   python manage.py migrate
   ```

### 9. 管理者の作成
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

### 10. 開発用サーバの起動
1. コマンドプロンプトを開き、手順6で複製したportfolio>projectディレクトリに移動します（manage.pyがあるディレクトリ）
2. 以下のコマンドを実行し、Djangoの開発用サーバを起動します
   ```
   pythoon manage.py runserver
   ```
5. Webブラウザから以下のURLにアクセスします
   http://127.0.0.1:8000/library
6. 図書管理アプリのログイン画面が表示されたら開発用サーバの起動は完了です
