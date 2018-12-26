from NetSpider import *
import json
import re

def getImg(html):
    imgre = re.compile('"thumbURL":"(.*?)"')
    imglist = re.findall(imgre,html)
    return imglist

def download(urls,path):
    index = 1
    for url in urls:
        print("Download Image from page:{}".format(url))
        status = downloadImageFile(url,path,str(index)+'.jpg')
        try:
            if str(status)[0] == '4':
                print("未下载成功{}".format(url))
                continue
        except Exception as e:
            print("未下载成功{}".format(url))
        index += 1


#page = 'https://image.baidu.com/search/index?tn=baiduimage&word=杨幂'

#html= getHTMLText(page)
#download(getImg(html), 'c:/杨幂')


pagestr = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj'\
       '&ct=201326592&is=&fp=result&queryWord={}&cl=&lm=&hd=&latest='\
       '&copyright=&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic='\
       '&word={}&s=&se=&tab=&width=&height=&face=&istype='\
       '&qc=&nc=&fr=&pn={}&rn=30&gsm=1e&1545721051065='
for i in range(1,6):
    page = pagestr.format('杨幂','杨幂',i*40)
    print(page)
    try:
        rsp = requests.get(page,timeout=10)
        rsp.raise_for_status()
    except:
        print('对不起，百度图片访问失败！程序退出')
        
    imgdata=json.loads(rsp.text)
    imgs = imgdata['data']
    
    urls=[]
    for im in imgs:
        url = im.get('thumbURL')
        if url is not None:
            urls.append(url)
    download(urls, 'd:/baidupic')    
