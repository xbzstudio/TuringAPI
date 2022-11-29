#!/usr/bin/env python
# -*- coding:UTF-8 -*-


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
       userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49})'
       def getInfo(self):
              try:
                     a=json.loads(self.http.request('GET','https://icodecontest-online-api.youdao.com/api/user/info',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}).data.decode('utf-8'))['data']
                     return json.loads(self.http.request('GET','https://icodecontest-online-api.youdao.com/api/user/info',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}).data.decode('utf-8'))
              except:
                     return {'code':-1,'data':{'userId':None}}

       
       def checkLogin(self):
              self.isLogin=True if self.getInfo()['code']==0 else False
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


       def comment(self,workId,data):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/comment',body=('{"id":"'+str(workId)+'","content":"'+str(data)+'"}').encode('utf-8'),headers={'Accept': 'application/json, text/plain, */*','Content-Type': 'application/json;charset=UTF-8','Cookie': self.cookie,'User-Agent': self.userAgent})


       def like(self,url,mode=1):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/like?id={id}&type={mode}'.format(id=workId,mode=str(mode)),body='request'.encode('utf-8'),headers={'Cookie':self.cookie,'User-Agent':self.userAgent})


       def enshrine(self,workId,mode=1):
              return self.http.request('POST',('https://icodeshequ.youdao.com/api/user/works/enshrine?worksId={idd}'.format(idd=workId)) if mode==1 else ('https://icodeshequ.youdao.com/api/user/works/cancelEnshrine?worksId={idd}'.format(idd=workId)),body='request'.encode('utf-8'),headers={'Cookie':self.cookie,'User-Agent':self.userAgent})


       def report(self,workId,rpdata,reportType=1):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/report',body=json.dumps({'worksIdStr':workId,'category':reportType,'description':rpdata}).encode('utf-8'),headers={'Content-type': 'application/json;charset=UTF-8','Cookie':self.cookie,'User-Agent': self.userAgent})


       def submitScratch(self,workJson,public=1,title='Scratch Project',description='submit_scratch',thumbnail='http://ydschool-online.nosdn.127.net/svg/0c3a986d5266bd5a186014aebd219e05c9696de777dea2b5dfe658dc661e572c.png'):
              fields = [("category", (None, 'lab')), ("code", (None, workJson)), ("codeType", (None, 'json')), ("theme", (None, 'scratch')),("subtheme", (None, 'scratch')),("description", (None, description)),("fork", (None,0)),("publish", (None,public)),("thumbnail", (None, thumbnail)),("title", (None, title))]
              fields=urllib3.encode_multipart_formdata(fields=fields)
              return self.http.request('POST','https://icode.youdao.com/api/work/submit',body=fields[0],headers={"Content-Type":fields[1],'Cookie':self.cookie,"User-Agent":self.userAgent})


       def submitPython(self,code,title="Python Project",description="submit_python",imgUrl="https://ydschool-video.nosdn.127.net/1622107517404%E9%BB%98%E8%AE%A4%E5%B0%81%E9%9D%A21.jpg"):
              return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/publish?publishType=1',body=json.dumps({'code':code,'description':description,'imgUrl':imgUrl,'title':title}).encode('utf-8'),headers={'Content-Type': 'application/json','Cookie':self.cookie,"User-Agent":self.userAgent})


       def updateIntro(self,data):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/user/updateIntro',body=data.encode('utf-8'),headers={'Cookie':self.cookie,"User-Agent":self.userAgent})


       def deleteComment(self,commentId):
              return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/comment/delete?commentId={str(commentId)}',body='有道小图灵我测你吗'.encode('utf-8'),headers={'Cookie':self.cookie,"User-Agent":self.userAgent})


       def deleteMessage(self,messageId):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/user/message/deleteComment',body=json.dumps({'id':messageId}).encode('utf-8'),headers={'Accept':'application/json, text/plain, */*','Content-Type':'application/json','Cookie':self.cookie,"User-Agent":self.userAgent})

       
       def uploadFile(self,fileName,fileType,fileData):
              return self.http.request('POST',f'https://tiku-outside.youdao.com/nos/scratch/asset/{fileName}.{fileType}/',body=fileData,headers={"User-Agent":self.userAgent})


       def reSubmitScratch(self,workId,workJson=None,publish=None,title=None,description=None,thumbnail=None,yourDetail=None):
              if yourDetail==None:
                     fields = [("category", (None, 'lab')), ("code", (None, workJson)), ("codeType", (None, 'json')), ("theme", (None, 'scratch')),("subtheme", (None, 'scratch')),("description", (None, description)),("fork", (None,0)),("publish", (None,publish)),("thumbnail", (None, thumbnail)),("title", (None, title)),('workid',(None,workId))]
                     fields=urllib3.encode_multipart_formdata(fields=fields)
                     return self.http.request('POST','https://icode.youdao.com/api/work/submit',body=fields[0],headers={"Content-Type":fields[1],'Cookie':self.cookie,"User-Agent":self.userAgent})
              else:
                     fields = yourDetail
                     fields=urllib3.encode_multipart_formdata(fields=fields)
                     return self.http.request('POST','https://icode.youdao.com/api/work/submit',body=fields[0],headers={"Content-Type":fields[1],'Cookie':self.cookie,"User-Agent":self.userAgent})


       def reSubmitPython(self,workId,code,publish=1,title="Python Project",description="submit_python",imgUrl="https://ydschool-video.nosdn.127.net/1622107517404%E9%BB%98%E8%AE%A4%E5%B0%81%E9%9D%A21.jpg"):
              return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/publish?publishType=1',body=json.dumps({'code':code,'description':description,'imgUrl':imgUrl,'title':title,'id':workId}).encode('utf-8'),headers={'Content-Type': 'application/json','Cookie':self.cookie,"User-Agent":self.userAgent}) if publish else self.http.request('POST','https://icodeshequ.youdao.com/api/works/save',body=json.dumps({'code':code,'description':description,'title':title} if (workId==None) else {'code':code,'description':description,'title':title,'id':workId}).encode('utf-8'),headers={'Content-Type':'application/json','Cookie':self.cookie,'User-Agent':self.userAgent})


       def getWorkDetail(self,workId,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/detail?id={workId}') if isParse else self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/detail?id={workId}')['data']


       def getWorkComments(self,workId,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/comment/list?id={workId}&page={page}&size={getNum}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/comment/list?id={workId}&page={page}&size=10').data.decode('utf-8'))['dataList']


       def getMessage(self,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/commentMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}) if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/commentMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}).data.decode('utf-8'))['dataList']


       def getPersonInfo(self,userId,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/index/hisStatics?userId={userId}',headers={'Cookie':self.cookie}) if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/index/hisStatics?userId={userId}',headers={'Cookie':self.cookie}).data.decode('utf-8'))['data']




a=icodeUser('OUTFOX_SEARCH_USER_ID_NCOO=279026281.3431625; OUTFOX_SEARCH_USER_ID="1792643811@10.112.57.88"; DICT_PERS=v2|cqq||DICT||web||7776000000||1663513725575||113.119.176.155||qqB60D8500058F9FBEA41D76E17167C37A||lY0f6ykLwK0QyOMPFkMYE06y6LwKh4zfRlGk4YEkfJLRYWRLqB0fTz0pFRfw4PMpFROW0LgzOLQK0U50LeK0MqK0; YOUDAO_MOBILE_ACCESS_TYPE=1; DICT_LOGIN=3||1663513725579; DICT_FORCE=true; xiaotuling=icode%3Asession%3Afee863ace3543f4a1566f7f19289e603; DICT_SESS=v2|GN2eh2YPW0guO4lG64PS0puRLkM6Mwy0OW0HTS0L6uRqFhMguP4p40OfhHpZ0M640UWPMzWRHpz0gz0feFRHlWRQukMzEOLey0; JSESSIONID=abcCM4rvINZVN8jl4mrny')
print(a.submitPython('''print('鸡你太美')
#turingAPI test. (submitPython)
''').data.decode('utf-8'))