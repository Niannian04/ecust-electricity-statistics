import json

import requests


def sendMsgToWechat(token: str, title: str, text: str, template: str) -> None:
    '''
    token:PushPlus token
    title:text's title
    text:text's body
    template:html,txt,json,markdown
    Send message to Wechat(SMS,E-mail,Dingtalk...) via PushPlus.
    default channel is wechat
    '''
    url = "http://www.pushplus.plus/send"
    data = {
        'token': token,
        'title': title,
        'content': text,
        'template': template
    }
    requests.post(url=url,
                  data=(
                      json.dumps(data).encode(encoding='utf-8')
                  )
                  )
