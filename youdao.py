import requests
import json


def get_data(word=None):

    url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    payload = {'i':word,'from':'AUTO','to':'AUTO','smarttrsult':'dict','salt':'15681103675993',
            'sign':'e686b9cf2d3fdfc88eb0b610f3b8c7b2','doctype':'json','version':'2.1',
            'keyfrom':'fanyi.web','action':'FY_BY_CLICKBUTTION'}

    request = requests.post(url, data=payload)
    content = json.loads(request.text)
    print(content['translateResult'][0][0]['tgt'])
if __name__ == '__main__':
    get_data('我爱数据')


