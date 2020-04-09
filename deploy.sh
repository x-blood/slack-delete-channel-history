#!/bin/sh

# Create Package
aws cloudformation package \
  --template-file template.yml \
  --output-template-file template-output.yml \
  --s3-bucket sam-sandbox-package \
  --profile xblood

# Deploy
aws cloudformation deploy \
  --template-file template-output.yml \
  --stack-name slack-delete-channel-history \
  --parameter-overrides \
  SlackToken=${SLACK_DELETE_CHANNEL_HISTORY_TOKEN} \
  SlackChannel=${SLACK_DELETE_CHANNEL_HISTORY_CHANNEL} \
  SlackCount=${SLACK_DELETE_CHANNEL_HISTORY_COUNT} \
  --capabilities CAPABILITY_IAM \
  --profile xblood

