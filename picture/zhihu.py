# -*- coding:utf-8 -*-
import os
import re
import requests
def download(folder,url):
    if not os.path.exists(folder):
        os.makedirs(folder)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        name = url.split('/')[-1]
        f = open("./"+folder+'/'+name,'wb')
        f.write(req.content)
        f.close()
        return True
    else:
        return False

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

errs=[]

def fetch(url):
    r = requests.get(url,headers=header)
    text= r.text
    imgs=[]
    # jpg = re.compile(r'https://[^\s]*?_r\.jpg')
    # jpeg = re.compile(r'https://[^\s]*?_r\.jpeg')
    # gif = re.compile(r'https://[^\s]*?_r\.gif')
    # png = re.compile(r'https://[^\s]*?_r\.png')
    jpgn =re.compile(r'http://img.shida66.com/upload/special_cover_img/\d+/\d+/\d+/[^\s]*\.jpg')
    imgs+=jpgn.findall(text)
    # imgs+=jpeg.findall(text)
    # imgs+=gif.findall(text)
    # imgs+=png.findall(text)
    print("download :" )

    errors = []

    folder = url.split('.')[-1]
    for img_url in imgs:
        if download(folder,img_url):
            print("download :"+img_url)
        else:
            errors.append(img_url)
    return errors

urls='http://shida66.com'
print(urls)
fetch(urls)
# urls=['https://www.zhihu.com/question/22212644','https://www.zhihu.com/question/29814297',
#       'https://www.zhihu.com/question/31983868','https://www.zhihu.com/question/20399991']
# for url in urls :
#     print(url)
#     errs+=fetch(url)
#
# print("ERROR URLS:")
# print(errs)


'http://img.shida66.com/upload/index_banner_practice/2017/07/18/e79502dca37fe0deeedf12ee697b436d.jpg'
