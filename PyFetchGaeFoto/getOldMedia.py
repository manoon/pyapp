__author__ = 'manoon'
import socks,socket,os,time
from BeautifulSoup import BeautifulSoup
import urllib,urllib2
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket
def getUrlList():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
     }
    print "start 2 get category",tibet
    req=urllib2.Request(tibet,headers=headers)
    f=urllib2.urlopen(req)
    s=f.read()
    print s
    soup=BeautifulSoup(s)
    print "*"*50
    titles=soup.findAll(attrs={"class":"topTitle"})
    print titles
    soup=BeautifulSoup(str(titles))
    pageurls=[]
    for link in soup.findAll("a"):
        pageurl=link.get('href')
        if 'p=' in pageurl:
            pageurls.append(pageurl)

    return pageurls

def getImg(url):
    try:#start to get img urls
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
             }
        req = urllib2.Request(url,headers=headers)
        data= urllib2.urlopen(req).read()
        soup=BeautifulSoup(data)
        items=[]
        for img in soup.findAll("img"):
            imgsrc=img.get('src')
            print imgsrc
            if "media" in imgsrc:
                print imgsrc
                items.append(imgsrc)
            else:
                print "no image in this post"
    except:
        print "get imgsrc error"
    else:
        print "done"

    try:#start to download images
        for item  in items:
            item=item.replace('http://www.xxoo.com','')
            item="http://xxoo.appsp0t.com"+item.replace('..','')
            print item

            picPath=item.split('/')[4]
            picDir="/Users/manoon/pic/"+str(picPath.split('/')[0])
            print picDir
            picName=item.split('/')[5]
            if (not(os.path.isdir(picDir))):
		        os.makedirs(picDir)
            iPicPath=picDir+"/"+picName
            print iPicPath

            headers = {
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
             }
            req = urllib2.Request(item,headers=headers)

            data= urllib2.urlopen(req).read()

            with open(iPicPath, "wb") as code:
                code.write(data)
    except:
        print "down error!"
    else:
        print "down okay!"


def Start():
    tibet="http://blog.xxoo.com/category/photos" #your category here
    urlList=getUrlList(tibet)
    for url in urlList:
        url="http://blog.xxoo.com"+url
        getImg(url)
        print 'getMediaOkay @',url
        time.sleep(5)

Start()

