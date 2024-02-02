# 図書管理アプリ

## アプリ概要
本の貸出予約、返却等ができるアプリです。

## 必要環境
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

#### 1. Pythonのインストール
1. 下記のURLからPythonの公式サイトにアクセスします  
   https://www.python.org/
2. メニューから「Downloads」をクリックします
3. 画面を下にスクロールすると過去のバージョンの一覧があるので、その中から「Python 3.11.5」を探してクリックします
4. 画面を下にスクロールし、Filesから「Windows installer(64-bit)」をクリックします
5. ダウンロードした「python-3.11.5-amd64.exe」を起動します
6. 「Add python.exe to PATH」にチェックを入れ、「Install Now」をクリックします
7. インストールが終わると「Setup was successful」と表示されるので「close」をクリックして画面を閉じます

#### 2. DJangoのインストール
1. WindowsキーとRキーを同時に押します
2. 「ファイル名を指定して実行」というウィンドウが表示されるので「cmd」と入力してOKを押します
3. コマンドプロンプトが表示されるので「pip install django==4.2.5」と入力してEnterキーを押します
4. インストールが終わると最後にSuccessfully installed Django-4.2.5と表示され、再び入力待ちの状態になります
5. 「python -m django --version」と入力してEnterキーを押し、「4.2.5」とバージョンが表示されたらDjangoのインストールは完了です

#### 3. MySQLのインストール
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
    C:\Program Files\MySQL\MySQL Server 8.0\bin
25. 変更を適用する為、OKボタンをクリックして設定画面を閉じます
26. 全ての画面を閉じたら再起動します
27. WindowsキーとRキーを同時に押します
28. 「ファイル名を指定して実行」というウィンドウが表示されるので「cmd」と入力してOKを押します
29. コマンドプロンプトが表示されるので、「mysql --version」と入力しEnterキーを押します
30. 「mysql  Ver 8.x.x for Win64 on x86_64 (MySQL Community Server - GPL)」とバージョン情報が表示されればMySQLのインストールは完了です

#### 4. データベースの作成
1. コマンドプロンプトで「mysql -u root -p」と入力しEnterキーを押します
2. 「Enter password:」と表示されるので、手順3-14で設定したパスワードを入力しEnterキーを押します
3. 「Enter password(again):」と表示されるので、もう一度パスワードを入力しEnterキーを押します
4. ログインに成功すると「mysql>」と表示され、SQLコマンドの入力待ち状態になります
5. 「CREATE DATABASE xxxx(任意のデータベース名);」と入力しEnterキーを押します
6. 「show databases;」と入力しEnterキーを押します
7. 5で作成したデータベースの名前が一覧に表示されればデータベースの作成は完了です
8. 「exit;」と入力しEnterキーを押し、SQLコマンドの入力待ち状態から元のコマンドプロンプトの状態に戻ります

#### 5. mysqlclientのインストール
1. コマンドプロンプトで「python -m pip install mysqlclient」と入力し、Enterキーを押します
2. インストールが開始します
3. 最後に「Successfully installed mysqlclient-x.x.x」と表示されたら完了です

#### 6. リポジトリのクローン
1. 本リポジトリの画面の緑のCodeボタンをクリックします
2. HTTPSを選択してURLをコピーします
3. Git Bashを起動します
4. Djangoプロジェクトを配置したいディレクトリに移動します
5. 「git clone コピーしたURL（`https://github.com/xxxx/xxxx.git`）」と入力し、Enterキーを押します
6. ローカルに「portfolio」フォルダが複製されたらリポジトリのクローンは完了です

#### 7. local_settings.pyの作成
1. コマンドプロンプトを開き、手順6で複製した「portfolio」ディレクトリに移動します
2. dirコマンドで「project」フォルダとREADME.mdファイルがあることを確認し、cdコマンドで「project」ディレクトリに移動します
3. dirコマンドで「manage.py」というファイルがあることを確認します
4. ここで「python manage.py shell」と入力しEnterキーを押します
5. シェルが起動するので「from django.core.management.utils import get_random_secret_key」と入力しEnterキーを押します
6. 次に「get_random_secret_key()」と入力しEnterキーを押します
7. Djangoの秘密鍵が生成されるので、コピーします
8. 更に「project」ディレクトリに移動します
9. dirコマンドでsettings.py等のファイルがあることを確認し、ここに「local_settings.py」という名前でファイルを作成します
10. local_settings.pyにはDjangoの秘密鍵とデータベースの情報を記述します。

```
SECRET_KEY = '手順7-7で生成した秘密鍵'
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': '手順4-5で作成したデータベース名',
    'USER': 'MySQLのユーザ名',
    'PASSWORD': 'MySQLのパスワード',
  }
}   
```  

11. local_settings.pyの内容を保存します

#### 8. マイグレーション
1. コマンドプロンプトを開き、手順6で複製した「portfolio」ディレクトリに移動します
2. dirコマンドで「project」フォルダとREADME.mdファイルがあることを確認し、cdコマンドで「project」ディレクトリに移動します
3. dirコマンドで「manage.py」というファイルがあることを確認します
4. ここで「pythoon manage.py makemigrations」と入力しEnterキーを押します
5. 次に「python manage.py migrate」と入力しEnterキーを押します

#### 9. 管理者の作成
1. コマンドプロンプトを開き、手順6で複製した「portfolio」ディレクトリに移動します
2. dirコマンドで「project」フォルダとREADME.mdファイルがあることを確認し、cdコマンドで「project」ディレクトリに移動します
3. dirコマンドで「manage.py」というファイルがあることを確認します
4. ここで「python manage.py createsperuser」と入力しEnterキーを押します
5. Username:と表示されるので任意のユーザ名を入力しEnterキーを押します
6. Email address:と表示されるのでメールアドレスを入力します　指定しない場合はそのままEnterキーを押します
7. Password:と表示されるので任意のパスワードを入力します
8. Password(again):と表示されるのでもう一度パスワードを入力します
9. 「Superuser created successfully.」と表示されたら管理者の作成は完了です

#### 10. 開発用サーバの起動
1. コマンドプロンプトを開き、手順6で複製した「portfolio」ディレクトリに移動します
2. dirコマンドで「project」フォルダとREADME.mdファイルがあることを確認し、cdコマンドで「project」ディレクトリに移動します
3. dirコマンドで「manage.py」というファイルがあることを確認します
4. ここで「pythoon manage.py runserver」と入力しEnterキーを押します
5. Webブラウザから以下のURLにアクセスします
   http://127.0.0.1:8000/library
6. 分散型図書管理アプリのログイン画面が表示されたら開発用サーバの起動は完了です
