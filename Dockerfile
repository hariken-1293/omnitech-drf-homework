# # ベースイメージとして Python 3.11 slim を使用
# FROM python:3.11-slim

# # 作業ディレクトリを設定
# WORKDIR /backend

# # Pythonのパッケージ管理ツールを最新化
# RUN pip install --upgrade pip

# # requirements.txtをコンテナにコピーして、パッケージをインストール
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # アプリケーションコードをコピー
# COPY backend/app .

# # # .env ファイルをコンテナ内にコピー
# # COPY .env /backend/app/.env


# # デフォルトでコンテナ起動時に実行されるコマンド
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]


# ベースイメージとして Python 3.11 slim を使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /backend

# Pythonのパッケージ管理ツールを最新化
RUN pip install --upgrade pip

# requirements.txtをコンテナにコピーして、パッケージをインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# デフォルトでコンテナ起動時に実行されるコマンド
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]
