# slack-delete-channel-history
CloudWatch Eventsによって起動し、特定のチャンネルのメッセージを削除する。  

## Setup

### 1. venv
```
python -m venv myvenv
make venv_activate
```

### 2. 必要なパッケージの取得
```
# venvをアクティベートした後で
make pip_install
```

## 3. Serverless Framework
```
# node v10.18.0以上
npm install -g serverless
npm install --save serverless-python-requirements
npm install --save serverless-pseudo-parameters
```

## Deploy
```
make deploy PROFILE=${AWS_PROFILE_NAME}
```