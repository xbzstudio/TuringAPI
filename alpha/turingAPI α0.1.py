import urllib3
import urllib.parse as parse
import json
import asyncio

class icodeUser():
       http=urllib3.PoolManager()
       isLogin=False
       cookie=None
       userId=None
       info={}
       def getInfo(self):
              return json.loads(self.http.request('GET','https://icodecontest-online-api.youdao.com/api/user/info',headers={'Cookie':self.cookie,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49})'}).data.decode('utf-8'))

       
       def checkLogin(self):
              isLogin=True if self.getInfo()['code']==0 else False
              return True if self.getInfo()['code']==0 else False      

       
       def __init__(self,cookie=None):
              self.cookie=cookie
              self.info=self.getInfo()['data']
              self.userId=self.info['userId']
              self.isLogin=self.checkLogin()


       def login(self,cookie):
              self.cookie=cookie
              self.info=self.getInfo()['data']
              self.userId=self.info['userId']
              self.isLogin=self.checkLogin()


       def getWorkId(self,site):
              return parse.urlparse(site)[2].split('/')[2]


       def comment(self,url,data):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/comment',body=('{"id":"'+str(self.getWorkId(url))+'","content":"'+str(data)+'"}').encode('utf-8'),headers={'Accept': 'application/json, text/plain, */*','Content-Type': 'application/json;charset=UTF-8','Cookie': self.cookie,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.78 (Edition GX-CN)})'})


       def like(self,url,mode=1):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/like?id={id}&type={mode}'.format(id=self.getWorkId(url),mode=str(mode)),body='request'.encode('utf-8'),headers={'Cookie':self.cookie})


       def enshrine(self,url,mode=1):
              return self.http.request('POST',('https://icodeshequ.youdao.com/api/user/works/enshrine?worksId={idd}'.format(idd=self.getWorkId(url))) if mode==1 else ('https://icodeshequ.youdao.com/api/user/works/cancelEnshrine?worksId={idd}'.format(idd=self.getWorkId(url))),body='request'.encode('utf-8'),headers={'Cookie':self.cookie})


       def report(self,url,rpdata,reportType=1):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/report',body=json.dumps({'worksIdStr':self.getWorkId(url),'category':reportType,'description':rpdata}).encode('utf-8'),headers={'Content-type': 'application/json;charset=UTF-8','Cookie':self.cookie,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49})'})


       def submit_scratch(self,workJson,public=1,title='Scratch Project',description='submit_scratch',thumbnail='http://ydschool-online.nosdn.127.net/svg/0c3a986d5266bd5a186014aebd219e05c9696de777dea2b5dfe658dc661e572c.png'):
              fields = [("category", (None, 'lab')), ("code", (None, workJson)), ("codeType", (None, 'json')), ("theme", (None, 'scratch')),("subtheme", (None, 'scratch')),("description", (None, description)),("fork", (None,0)),("publish", (None,public)),("thumbnail", (None, thumbnail)),("title", (None, title))]
              fields=urllib3.encode_multipart_formdata(fields=fields)
              return self.http.request('POST','https://icode.youdao.com/api/work/submit',body=fields[0],headers={"Content-Type":fields[1],'Cookie':self.cookie,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"})


       def submit_python(self,code,publishType=1,title="Python Project",description="submit_python",imgUrl="https://ydschool-video.nosdn.127.net/1622107517404%E9%BB%98%E8%AE%A4%E5%B0%81%E9%9D%A21.jpg"):
              return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/publish?publishType={publishType}',body=json.dumps({'code':code,'description':description,'imgUrl':imgUrl,'title':title}).encode('utf-8'),headers={'Content-Type': 'application/json','Cookie':self.cookie,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"})

a=icodeUser('OUTFOX_SEARCH_USER_ID_NCOO=1527393399.3500757; OUTFOX_SEARCH_USER_ID="850067477@10.169.0.81"; wap_abtest=3; mp_MA-BF02-71D44E7C0390_hubble={"sessionReferrer": "https://c.youdao.com/icode/download.html","updatedTime": 1642341282245,"sessionStartTime": 1642341282243,"sendNumClass": {"allNum": 2,"errSendNum": 0},"deviceUdid": "3b5ebaeb-62d8-4aef-bfcb-9b4864461163","persistedTime": 1634956503267,"LASTEVENT": {"eventId": "da_screen","time": 1642341282245},"sessionUuid": "c1c89549-afc0-4f52-9adf-78b47c15f8b1"}; P_INFO=bhgj97672537caiz@163.com|1663165958|0|youdaodict|00&99|hen&1663163048&x19_client#gud&440100#10#0#0|&0|x19_client&g83_client&ma75_client|bhgj97672537caiz@163.com; DICT_PERS=v2|cqq||DICT||web||7776000000||1663373982054||113.119.176.155||qqB60D8500058F9FBEA41D76E17167C37A||QK6MeBkMOGROlOMYf0LJLRJuOMeyO4wZ0gBPM6SOfUWR6BhMOERLlf0p40fPL64l50QyOMe46LpK0JShMYEkfQBR; DICT_SESS=v2|qQxpZq6nW0kWO4gBhLzWRkY0LTFh4p4RqFk4YW0feS0k5nLwFhfpF0eunMQBkf6Z0gB6MeKh46uRgy6LYGnfUE0JKhfPFnHQS0; DICT_LOGIN=3||1663389144353; xiaotuling=icode:session:5811ef2611357f07d97c53c570e9d67d')
print(a.submit_python('  #引入 turtle 库\nfrom turtle import *\n#设置海龟移动的速度 0=最快 10=快 6=正常 3=慢 1=最慢\nspeed(6)\n#画个小爱心\nleft(45)\ncolor(\"red\",\"pink\")  #你可以尝试改变爱心的颜色哦～\nbegin_fill()\nfd(200)\ncircle(100,180)\nright(90)\ncircle(100,180)\nfd(200)\nend_fill()\ndone()\n\n',1,'test2','test2','https://ydschool-video.nosdn.127.net/1622107517404%E9%BB%98%E8%AE%A4%E5%B0%81%E9%9D%A21.jpg').data.decode('utf-8'))
