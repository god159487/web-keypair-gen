import os

bind = "0.0.0.0:8080"

tmp_workers = os.getenv("GUNICORN_WORKERS")
workers = 1
timeout = 0
if tmp_workers and tmp_workers.isdecimal():
    workers = int(tmp_workers)

tmp_threads = os.getenv("GUNICORN_THREADS")
threads = 8  # worker type はsyncになる.
if tmp_threads and tmp_threads.isdecimal():
    threads = int(tmp_threads)

# アクセスログを標準出力
accesslog = "-"
capture_output = True

# アクセスログの出力フォーマット指定
access_log_format = (
    '{"remote_ip":"%(h)s","request_id":"%({X-Request-Id}i)s",'
    '"response_code":"%(s)s","request_method":"%(m)s","request_path":"%(U)s",'
    '"request_querystring":"%(q)s","request_timetaken":"%(D)s",'
    '"response_length":"%(B)s"}'
)
# エラーログのログレベル
loglevel = "info"
