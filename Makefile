# バックエンドのローカルイメージをビルド
.PHONY: local-build
local-build:
	docker-compose -f ./local/docker-compose.yml build

# フロントエンドとバックエンドを起動
.PHONY: local-up
local-up:
	docker-compose -f ./local/docker-compose.yml up -d
	npm run --prefix ./frontend serve

# バックエンドのコンテナを停止
.PHONY: local-down
local-down:
	docker-compose -f ./local/docker-compose.yml down --volumes --remove-orphans

# コンテナのプロセスを確認
.PHONY: local-ps
local-ps:
	docker-compose -f ./local/docker-compose.yml ps

# バックエンドのログを確認
.PHONY: local-logs
local-logs:
	docker-compose -f ./local/docker-compose.yml logs keypair-generator.local

# バックエンドのコンテナに入る
.PHONY: local-bash
local-bash:
	docker-compose -f ./local/docker-compose.yml exec keypair-generator.local /bin/bash

# フロントエンドとバックエンドのデプロイイメージをビルド
.PHONY: deploy-build
deploy-build:
	docker-compose -f ./deploy/docker-compose.yml build

# フロントエンドとバックエンドのコンテナを起動
.PHONY: deploy-up
deploy-up:
	docker-compose -f ./deploy/docker-compose.yml up

# フロントエンドとバックエンドのコンテナを停止
.PHONY: deploy-down
deploy-down:
	docker-compose -f ./deploy/docker-compose.yml down --volumes --remove-orphans

# コンテナのプロセスを確認
.PHONY: deploy-ps
deploy-ps:
	docker-compose -f ./deploy/docker-compose.yml ps

# ログを確認
.PHONY: deploy-logs
deploy-logs:
	docker-compose -f ./deploy/docker-compose.yml logs keypair-generator.deploy

# コンテナに入る
.PHONY: deploy-bash
deploy-bash:
	docker-compose -f ./deploy/docker-compose.yml exec keypair-generator.deploy /bin/bash
