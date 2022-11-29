
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


       def getWorkId(self,site):  #get work's id
              return parse.urlparse(site)[2].split('/')[2]


       def comment(self,workId,data):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/comment',body=('{"id":"'+str(workId)+'","content":"'+str(data)+'"}').encode('utf-8'),headers={'Accept': 'application/json, text/plain, */*','Content-Type': 'application/json;charset=UTF-8','Cookie': self.cookie,'User-Agent': self.userAgent})


       def like(self,workId,mode=1):
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


       def deleteComment(self,commentId=None,replyId=None):
              if replyId==None:
                     return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/comment/delete?commentId={str(commentId)}',body='有道小图灵我测你吗'.encode('utf-8'),headers={'Cookie':self.cookie,"User-Agent":self.userAgent})
              else:
                     return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/reply/delete?replyId={replyId}',body='你这个底层蝼蚁跳梁小丑没我帅呵呵你这个傻逼'.encode('utf-8'),headers={'Cookie':self.cookie,'User-Agent':self.userAgent})


       def deleteMessage(self,messageId):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/user/message/deleteComment',body=json.dumps({'id':messageId}).encode('utf-8'),headers={'Accept':'application/json, text/plain, */*','Content-Type':'application/json','Cookie':self.cookie,"User-Agent":self.userAgent})

       
       def uploadFile(self,fileName,fileType,fileData):
              return self.http.request('POST',f'https://tiku-outside.youdao.com/nos/scratch/asset/{fileName}.{fileType}/',body=fileData,headers={"User-Agent":self.userAgent})


       def reSubmitScratch(self,workId,workJson=' ',publish=1,title='scratch_prject',description=' ',thumbnail='http://ydschool-online.nosdn.127.net/svg/ba5c9cb2e5dfd89d836c43c88fcf90b153f142413da26257b220cab3d774eadf.png',yourDetail=None):
              if yourDetail==None:
                     fields = [("category", (None, 'lab')), ("code", (None, workJson)), ("codeType", (None, 'json')), ("theme", (None, 'scratch')),("subtheme", (None, 'scratch')),("description", (None, description)),("fork", (None,0)),("publish", (None,publish)),("thumbnail", (None, thumbnail)),("title", (None, title)),('workid',(None,workId))]
                     fields=urllib3.encode_multipart_formdata(fields=fields)
                     return self.http.request('POST','https://icode.youdao.com/api/work/submit',body=fields[0],headers={"Content-Type":fields[1],'Cookie':self.cookie,"User-Agent":self.userAgent})
              else:
                     fields = yourDetail
                     fields=urllib3.encode_multipart_formdata(fields=fields)
                     return self.http.request('POST','https://icode.youdao.com/api/work/submit',body=fields[0],headers={"Content-Type":fields[1],'Cookie':self.cookie,"User-Agent":self.userAgent})


       def reSubmitPython(self,workId,code,publish=1,save=0,title="Python Project",description="submit_python",imgUrl="https://ydschool-video.nosdn.127.net/1622107517404%E9%BB%98%E8%AE%A4%E5%B0%81%E9%9D%A21.jpg"):
              return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/publish?publishType={publish}',body=json.dumps({'code':code,'description':description,'imgUrl':imgUrl,'title':title,'id':workId}).encode('utf-8'),headers={'Content-Type': 'application/json','Cookie':self.cookie,"User-Agent":self.userAgent}) if not save else self.http.request('POST','https://icodeshequ.youdao.com/api/works/save',body=json.dumps({'code':code,'description':description,'title':title} if (workId==None) else {'code':code,'description':description,'title':title,'id':workId}).encode('utf-8'),headers={'Content-Type':'application/json','Cookie':self.cookie,'User-Agent':self.userAgent})


       def getWorkDetail(self,workId,isParse=0):
              #print('finish a task')
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/detail?id={workId}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/detail?id={workId}').data.decode('utf-8'))['data']


       def getWorkComments(self,workId,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/comment/list?id={workId}&page={page}&size={getNum}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/comment/list?id={workId}&page={page}&size={getNum}').data.decode('utf-8'))['dataList']


       def getMessage(self,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/commentMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}) if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/commentMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}).data.decode('utf-8'))['dataList']


       def getPersonInfo(self,userId,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/index/hisStatics?userId={userId}',headers={'Cookie':self.cookie}) if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/index/hisStatics?userId={userId}',headers={'Cookie':self.cookie}).data.decode('utf-8'))['data']


       def getMoreWorks(self,userIdOrWorkId,isParse=0):
              if 'viewNum' in self.getPersonInfo(userIdOrWorkId,1): #是一个userId
                     return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/more_works/list?userId={userIdOrWorkId}&currentWorksId=21a8bbf470ef4203abd549c641aac7a6') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/more_works/list?userId={userIdOrWorkId}&currentWorksId=21a8bbf470ef4203abd549c641aac7a6').data.decode('utf-8'))['dataList']
              else:      #是一个workId
                     userIdOrWorkId=self.getWorkDetail(userIdOrWorkId,1)['userId']
                     return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/more_works/list?userId={userIdOrWorkId}&currentWorksId=21a8bbf470ef4203abd549c641aac7a6') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/more_works/list?userId={userIdOrWorkId}&currentWorksId=21a8bbf470ef4203abd549c641aac7a6').data.decode('utf-8'))['dataList']


       def getPersonWorks(self,userId,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisWorksList?page={page}&size={getNum}&userId={userId}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisWorksList?page={page}&size={getNum}&userId={userId}').data.decode('utf-8'))['dataList']


       def getPersonEnshrines(self,userId,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisEnshrines?page={page}&size={getNum}&userId={userId}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisEnshrines?page={page}&size={getNum}&userId={userId}').data.decode('utf-8'))['dataList']


       def discoveryWorks(self,page,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/_next/data/oaW1PKMM8euJOF2QmW82a/discovery.json?page={page}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/_next/data/oaW1PKMM8euJOF2QmW82a/discovery.json?page={page}').data.decode('utf-8'))['pageProps']['initModel']['list']


       def getWorks(self,page,getNum,sortType,theme='all',codeLanguage='all',keyword='',isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/index/works/list?page={page}&size={getNum}&sortType={sortType}&theme={theme}&codeLanguage={codeLanguage}&keyword={keyword}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/index/works/list?page={page}&size={getNum}&sortType={sortType}&theme={theme}&codeLanguage={codeLanguage}&keyword={keyword}').data.decode('utf-8'))['dataList']

       def deleteWork(self,workId):
              return self.http.request('DELETE',f'https://icodeshequ.youdao.com/api/works/delete?id={workId}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent})


       def getMyWorks(self,page,getNum,status=2,theme='all',codeLanguage='all',keyword='',isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/list?page={page}&size={getNum}&status={status}&theme={theme}&codeLanguage={codeLanguage}&keyword={keyword}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}) if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/list?page={page}&size={getNum}&status={status}&theme={theme}&codeLanguage={codeLanguage}&keyword={keyword}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}).data.decode('utf-8'))['dataList']


       def getEnshrinesMessage(self,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/enshrinesMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}) if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/enshrinesMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}).data.decode('utf-8'))['dataList']


       def getSystemMessage(self,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/systemMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}) if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/message/systemMessage?page={page}&size={getNum}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent}).data.decode('utf-8'))['dataList']


       def readMessage(self,messageId):
              return self.http.request('PUT',f'https://icodeshequ.youdao.com/api/user/message/read?id={messageId}',headers={'Cookie':self.cookie,'User-Agent':self.userAgent})


       def reply(self,commentId,data,replyId=None):
              return self.http.request('POST','https://icodeshequ.youdao.com/api/works/reply',body=json.dumps({'commentId':commentId,'content':data,'replyId':replyId}).encode('utf-8'),headers={'Accept':'application/json, text/plain, */*','Content-Type':'application/json','Cookie':self.cookie,'User-Agent':self.userAgent})


       def getReplies(self,commentId,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/reply/list?commentId={commentId}&page={page}&size={getNum}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/works/reply/list?commentId={commentId}&page={page}&size={getNum}').data.decode('utf-8'))['dataList']


       def praiseComment(self,commentId=None,replyId=None,mode=1):
              if replyId==None:
                     return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/comment/praise?commentId={commentId}' if mode==1 else f'https://icodeshequ.youdao.com/api/works/comment/cancelPraise?commentId={commentId}',body='{}'.encode('utf-8'),headers={'Content-Type': 'application/json;charset=UTF-8','Cookie':self.cookie,'User-Agent':self.userAgent})
              else:
                     return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/reply/praise?replyId={replyId}' if mode==1 else f'https://icodeshequ.youdao.com/api/works/reply/cancelPraise?replyId={replyId}',body='{}'.encode('utf-8'),headers={'Content-Type': 'application/json;charset=UTF-8','Cookie':self.cookie,'User-Agent':self.userAgent})

                     
       def getWorkSubmitInfo(self,workId,isParse=0):
              return self.http.request('GET',f'https://icode.youdao.com/api/work/get?id={workId}') if not isParse else json.loads(self.http.request('GET',f'https://icode.youdao.com/api/work/get?id={workId}').data.decode('utf-8'))



class task():
       func=None    #执行函数
       name=None    #任务名称
       args=[]      #直接传参
       kwargs={}    #关键字传参
       returnFunc=None   #数据关联传参时处理第一次返回值的函数，返回格式为[args,kwargs]
       association=None  #数据关联时关联的任务名称
       event=None   #所属事件流
       associationFunc=None   #拿到数据后调用处理的函数


       def __init__(self,func,name=None,args=[],kwargs={},returnFunc=None,event=None,association=None,associationFunc=None):
              self.func=func
              self.name=name
              self.args=args
              self.kwargs=kwargs
              self.returnFunc=returnFunc
              self.event=event
              self.association=association
              self.associationFunc=associationFunc


       def runFunc(self):    #运行任务函数
              if self.association != None:
                     #print(f'task wait {self.name}')
                     self.waitForDone()
                     #print(f'wait done {self.name}')
              #print(f'run func {self.name}')
              returned = self.func(*self.args,**self.kwargs)
              #print(f'func done {self.name}')
              #print(f'start return {self.name}')
              if self.name != None:
                     if self.returnFunc != None:
                            self.event.returns[self.name] = self.returnFunc(returned,self)
                     else:
                            self.event.returns[self.name]=returned
                     if self.name in self.event.association:
                            #print(f'start association to events {self.name}')
                            self.associationToEvents(self.event.returns[self.name])
                            #print(f'association to events done {self.name}')
              else:
                     self.event.anonymousReturns.append(returned)
              #print(f'return done {self.name}')

       def waitForDone(self):    #等待关联的任务完成
              while not self.association in self.event.returns:
                     pass
              if self.associationFunc != None:
                     temp=self.associationFunc(self.event.returns[self.association],self)
                     self.args=temp[0]
                     self.kwargs=temp[1]
              else:
                     self.args=self.event.returns[self.association][0]
                     self.kwargs=self.event.returns[self.association][1]

       def associationToEvents(self,returned):   #将结果传到别的events当中（跨events数据关联，也就是数据互补）
              for i in self.event.association[self.name]:
                     self.event.eventPool.events[self.event.eventPool.indexs[i]].returns[self.name] = returned       #通过链式连接，指向最高级eventPool

       async def runTask(self):        #运行任务
              #print(f'run task {self.name}')
              loop=asyncio.get_running_loop()
              await loop.run_in_executor(None,self.runFunc)

       def run(self):
              asyncio.run(self.runTask())
       
class event():
       tasks=[]
       name=None
       returns={}
       anonymousReturns=[]
       association = {}   # 需要关联的taskName : [关联到的eventName1 , eventName2.....]
       eventPool=None
       def __init__(self,tasks=[],name=None,association={},eventPool=None):
              self.tasks=tasks
              self.name=name
              self.association=association
              self.eventPool=eventPool
       
       async def runEvent(self):
              tasks=[asyncio.create_task(i.runTask()) for i in self.tasks]
              await asyncio.wait(tasks)
              if self.name != None:
                     if self.eventPool != None:
                            self.eventPool.eventReturns[self.name]=[self.returns,self.anonymousReturns]

       def run(self):
              asyncio.run(self.runEvent())

class eventPool():
       events=[]
       eventReturns={}
       indexs={}    #eventName : index
       async def runEvents(self,nameList=[],indexList=[]):
              self.eventReturns={}
              if nameList==[]:
                     if indexList==[]:
                            tasks=[asyncio.create_task(i.runEvent()) for i in self.events]
                     else:
                            tasks=[asyncio.create_task(self.events[i].runEvent()) for i in indexList]
              else:
                     tasks=[asyncio.create_task(i.runEvent()) for i in self.events if i.name in nameList] + [asyncio.create_task(self.events[i].runEvent()) for i in indexList]
              await asyncio.wait(tasks)
       def run(self,nameList=[],indexList=[]):
              asyncio.run(self.runEvents(nameList,indexList))

def addTask(event,func,name=None,args=[],kwargs={},returnFunc=None,association=None,associationFunc=None):
       event.tasks.append(task(func,name,args,kwargs,returnFunc,event,association,associationFunc))

def deleteName(event,taskName):
       for i in range(len(event.tasks)):
              if event.tasks[i].name==taskName:
                     del event.tasks[i]

def findTask(event,taskName):
       for i in range(len(event.tasks)):
              if event.tasks[i].name==taskName:
                     return i
       return False

def addEvent(eventPool,tasks=[],name=None,association={}):
       eventPool.events+=[event(tasks,name,association,eventPool)]
       if name != None:
              eventPool.indexs[name] = len(eventPool.event)-1

def deleteEvent(eventPool,eventName):
       del eventPool.events[eventPool.indexs[eventName]]

def findEvent(eventPool,eventName):
       return eventPool.indexs[eventName]