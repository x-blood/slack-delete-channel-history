import urllib.request
import urllib.parse
import datetime
import json
import time
import os
from datetime import timedelta


def lambda_handler(event, context):
    print('Start lambda_handler')

    token = os.environ['SLACK_DELETE_CHANNEL_HISTORY_APP_TOKEN']
    print('env token : %s', token)
    channel = event['TARGET_CHANNEL_ID']
    print('env channel : %s', channel)
    count = event['MAX_DELETABLE_OBJECT_COUNT']
    print('env count : %s', count)
    expired_date = event['EXPIRED_DATE']
    print('env expired_date : %s', expired_date)

    now = datetime.datetime.now()
    delta = timedelta(days=+expired_date)
    target_datetime = now - delta
    epoch_time = target_datetime.timestamp()
    print('epoch_time : %s' % epoch_time)

    hist_url = "https://slack.com/api/conversations.history"
    delete_url = "https://slack.com/api/chat.delete"
    post_url = "https://slack.com/api/chat.postMessage"

    hist_params = {
        'channel': channel,
        'token': token,
        'latest': epoch_time,
        'limit': count
    }

    req = urllib.request.Request(hist_url)
    hist_params = urllib.parse.urlencode(hist_params).encode('ascii')
    req.data = hist_params

    res = urllib.request.urlopen(req)

    body = res.read()
    data = json.loads(body)

    deleted_count = 0

    for m in data['messages']:
        print(m)
        delete_params = {
            'channel': channel,
            'token': token,
            'ts':  m["ts"]
        }
        req = urllib.request.Request(delete_url)
        delete_params = urllib.parse.urlencode(delete_params).encode('ascii')
        req.data = delete_params

        res = urllib.request.urlopen(req)
        body = res.read()

        print(body)

        deleted_count += 1
        time.sleep(2)

    req = urllib.request.Request(post_url)
    post_params = {
        'channel': channel,
        'token': token,
        'text': "%d日前の通知情報を自動的に削除しました。 *`削除した件数：%d`* " % (expired_date, deleted_count)
    }
    post_params = urllib.parse.urlencode(post_params).encode('ascii')
    req.data = post_params
    _ = urllib.request.urlopen(req)
