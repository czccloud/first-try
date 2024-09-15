import requests
from lxml import etree
import os
 
URL = "https://pic.netbian.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Content-Type": "text/html; charset=utf-8"}









def get_path(url):
    req = requests.get(url, headers=headers)
    req.encoding = req.apparent_encoding
    return etree.HTML(req.text)
def get_img():
    if not os.path.isdir("图包"):
        os.mkdir("图包")
    rre = get_path(URL)
    result = rre.xpath('//*[@class="clearfix"]/li')
    for mage in result:
        imgSrc = mage.xpath('./a/span/img/@src')
        aHref = mage.xpath('./a/@href')
        name = mage.xpath('./a/b/text()')
        # 缩略图地址
        s = f"{imgSrc[0]}"
        # 原图请求地址
        aHrefStr = f"{aHref[0]}"
        # 图片名称
        imgName = f"{name[0]}".replace('*', '')
        with open("图包" + "/{}.jpg".format(imgName), "wb") as img:
            mageUrl = get_path(URL + aHrefStr)
            imgSrc2 = mageUrl.xpath('//*[@class="photo-pic"]/a/img/@src')
            # 原图地址
            imgSrcUrl = f"{imgSrc2[0]}"
            imgContent = requests.get(URL + imgSrcUrl)
            img.write(imgContent.content)
if __name__ == '__main__':
    get_img()