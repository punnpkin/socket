#!python2
import threading
import urllib2
import time

start = time.time()
urls = [
    "http://news.ustb.edu.cn/attach/file/xinwendaodu/7e3307711614726a89fc9b720c085ea3.jpg",
    "http://news.ustb.edu.cn/attach/file/xinwendaodu/f5b714a353775a9db7c8ad2a2d016bd8.jpg",
    "http://news.ustb.edu.cn/attach/file/xinwendaodu/a7833c04e1669d166d13b2dd4194ad5d.jpg",
    "http://news.ustb.edu.cn/attach/file/xinwendaodu/b22ba465de56b604fad97edd26a06b07.jpg"
    ]

lock = threading.Lock()
img_id = 0

class FetchUrl(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.setDaemon(False)
        self.url = url

    def run(self):
        global img_id
        urlHandler = urllib2.urlopen(self.url)
        result = urlHandler.read()
        lock.acquire()
        img_id += 1
        lock.release()
        f = open("%d.jpg" % img_id, "wb")
        f.write(result)
        f.close()

for url in urls:
    "spawning a FetchUrl thread for each url to fetch"
    FetchUrl(url).start()

time.sleep(1)

