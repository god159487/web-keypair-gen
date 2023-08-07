FROM node:16.17.0-buster AS frontend-builder

WORKDIR /opt/app/
COPY ./frontend/package*.json ./

RUN npm install

COPY ./frontend/public/ /opt/app/public
COPY ./frontend/src/ /opt/app/src
COPY ./frontend/index.html /opt/app
COPY ./frontend/jsconfig.json /opt/app/
COPY ./frontend/vite.config.js /opt/app/

COPY env.txt /opt/app/.env

RUN npm run build


FROM python:3.8-slim-buster AS backend-builder

WORKDIR /opt/app/

# アプリケーション実行に必要なパッケージをインストール
COPY ./backend/Pipfile* ./
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy



FROM python:3.8-slim-buster AS runner

WORKDIR /opt/app/

# アプリケーションに必要なファイルをfrontend-builderからコンテナ内にコピーする
COPY --from=frontend-builder /opt/app/dist/ ./static/
# アプリケーションに必要なファイルをbackend-builderからコンテナ内にコピーする
COPY --from=backend-builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=backend-builder /usr/local/bin/flask /usr/local/bin/flask
COPY --from=backend-builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
# アプリケーションに必要なファイルをローカルからコンテナ内にコピーする
COPY ./backend/src/ ./
COPY fbAdminConfig.json ./
COPY fbconfig.json ./

ENTRYPOINT ["gunicorn", "app:create_app()", "--config=gunicorn.conf.py"]

EXPOSE 8080
