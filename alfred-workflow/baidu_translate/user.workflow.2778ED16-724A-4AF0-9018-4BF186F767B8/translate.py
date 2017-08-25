#coding:utf-8
import httplib
import md5
import urllib
import random
import json,sys
from workflow import Workflow, web

# ref  http://www.deanishe.net/alfred-workflow/tutorial_1.html#writing-your-python-script
appid = 'xx'  # replace your's baidu open api
secretKey = 'xx' # replace your's baidu open api

def main(wf):
    if len(wf.args):
         query = wf.args[0]
    else:
         query = None

    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = query
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

    s="test"
    results=[]
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
     
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        res = response.read()
        jres = json.loads(res)
        s = jres["trans_result"][0]["dst"]
        wf.add_item(title=s,
                 subtitle='zh-en',
                 icon='')

        # Send the results to Alfred as XML
        wf.send_feedback()

    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()



if __name__ == u"__main__":

    wf = Workflow()
    sys.exit(wf.run(main))
