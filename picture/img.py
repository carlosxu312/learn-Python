# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
first_url="http://www.xiaohuar.com/hua/"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
#包装一个请求
rep= request.Request(url=first_url,headers=header)

respopen=request.urlopen(rep)
html= respopen.read();
#提取所有的img
suop=BeautifulSoup(html,'html.parser',from_encoding='gbk')
#获取所有的img
imgs= suop.find_all('img',src=re.compile(r'/d/file/\d+/\w+\.jpg'))
for img in imgs:
    ur="http://www.xiaohuar.com/%s" % img['src']
    req=request.Request(url=ur,headers=header)
    data=request.urlopen(req).read()
    #保存图片
    with open('%s.jpg' % img['alt'],'wb') as f:
        f.write(data)

