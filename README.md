# slack-delete-channel-history
CloudWatch Eventsによって起動し、特定のチャンネルのメッセージを削除する。  

## SETUP

### 1. Serverless Framework
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