import requests


def wechat_push_text():
    json = {
        "msgtype": "text",
        "text": {
            "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
        }
    }
    resp = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=410331a5-a18a-4e13-91de-ed04bdd8f48c',
                         json=json)
    js = json.loads(resp.text)
    print(js)


with open('commit_log.md', 'r') as f:
    log = f.read()
    wechat_push_text()

