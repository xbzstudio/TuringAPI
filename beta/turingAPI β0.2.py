#!/usr/bin/env python
# -*- coding:UTF-8 -*-


import urllib3
import urllib.parse as parse
import json
import asyncio
import time

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


       def deleteComment(self,commentId):
              return self.http.request('POST',f'https://icodeshequ.youdao.com/api/works/comment/delete?commentId={str(commentId)}',body='有道小图灵我测你吗'.encode('utf-8'),headers={'Cookie':self.cookie,"User-Agent":self.userAgent})


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
              return self.http.request('GET',f'https://icodeshequ.youdao.com/_next/data/Sac30BLmIoGahv5ucv2RL/discovery.json?page={page}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/_next/data/Sac30BLmIoGahv5ucv2RL/discovery.json?page={page}').data.decode('utf-8'))['pageProps']['initModel']['list']


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


class event():
       taskIndexs={}
       tasks=[]

       def __init__(self,tasks={},lambdaTasks=[]):
              self.tasks=lambdaTasks
              for i in tasks:
                     self.tasks.append([tasks[i][0],tasks[i][1]])
                     self.taskIndexs[i]=len(self.tasks)-1
              
       def setTasks(self,tasks={},lambdaTasks=[]):
              self.tasks=lambdaTasks
              for i in tasks:
                     self.tasks.append([tasks[i][0],tasks[i][1]])
                     self.taskIndexs[i]=len(self.tasks)-1

       async def runTask(self,taskName=None,lambdaTaskIndex=None):
              loop=asyncio.get_running_loop()
              if lambdaTaskIndex==None:
                     func=self.tasks[self.taskIndexs[taskName]][0]
                     values=self.tasks[self.taskIndexs[taskName]][1]
                     lens=len(values)
              else:
                     func=self.tasks[lambdaTaskIndex][0]
                     values=self.tasks[lambdaTaskIndex][1]
                     lens=len(values)
              if lens==0:
                     await loop.run_in_executor(None,func)
              elif lens==1:
                     await loop.run_in_executor(None,func,values[0])
              elif lens==2:
                     await loop.run_in_executor(None,func,values[0],values[1])
              elif lens==3:
                     await loop.run_in_executor(None,func,values[0],values[1],values[2])
              elif lens==4:
                     await loop.run_in_executor(None,func,values[0],values[1],values[2],values[3])
              elif lens==5:
                     await loop.run_in_executor(None,func,values[0],values[1],values[2],values[3],values[4])
              elif lens==6:
                     await loop.run_in_executor(None,func,values[0],values[1],values[2],values[3],values[4],values[5])
              else:
                     await loop.run_in_executor(None,func,values[0],values[1],values[2],values[3],values[4],values[5],values[6])

       async def Run(self,taskNames=[],lambdaTaskIndexs=[]):
              if taskNames+lambdaTaskIndexs==[]:
                     rtasks=[]
                     rtasks=[asyncio.create_task(self.runTask(lambdaTaskIndex=i)) for i in range(len(self.tasks))]
                     await asyncio.wait(rtasks)
              else:
                     rtasks=[]
                     rtasks=[asyncio.create_task(self.runTask(taskName=i)) for i in taskNames]
                     rtasks+=[asyncio.create_task(self.runTask(lambdaTaskIndex=i)) for i in lambdaTaskIndexs]
                     await asyncio.wait(rtasks)

       def runEvent(self,taskNames=[],lambdaTaskIndexs=[]):
              if taskNames==[] and lambdaTaskIndexs==[]:
                     asyncio.run(self.Run())
              elif taskNames==[] and len(lambdaTaskIndexs)>0:
                     asyncio.run(self.Run(lambdaTaskIndexs=lambdaTaskIndexs))
              elif lambdaTaskIndexs==[] and len(taskNames)>0:
                     asyncio.run(self.Run(taskNames=taskNames))
              else:
                     asyncio.run(self.Run(taskNames,lambdaTaskIndexs))


       def addTask(self,taskFunc,taskValues=[],taskName=None):
              if taskName==None:
                     self.tasks.append([taskFunc,taskValues])
              else:
                     self.tasks.append([taskFunc,taskValues])
                     self.taskIndexs[taskName]=len(self.tasks)-1
              
       def delTask(self,taskName=None,taskIndex=None):
              if taskName==None:
                     del self.tasks[taskIndex]
              else:
                     del self.tasks[self.taskIndexs[taskName]]
                     del self.taskIndexs[taskName]


class eventPool():
       events=[]
       eventIndexs={}

       def __init__(self,events={},lambdaEvents=[]):
              self.events=lambdaEvents
              for i in events:
                     self.events.append(events[i][1])
                     self.eventIndexs[events[i][0]]=len(self.events)-1
              
       def setEvents(self,events={},lambdaEvents=[]):
              self.events=lambdaEvents
              for i in events:
                     self.events.append(events[i][1])
                     self.eventIndexs[events[i][0]]=len(self.events)-1

       async def RunEvents(self,eventNames=[],lambdaEventIndexs=[]):
              if eventNames+lambdaEventIndexs==[]:
                     tasks=[asyncio.create_task(i.Run()) for i in self.events]
                     await asyncio.wait(tasks)
              else:
                     tasks=[asyncio.create_task(self.events[i].Run()) for i in lambdaEventIndexs]
                     tasks+=[asyncio.create_task(self.events[self.eventIndexs[i]].Run()) for i in eventNames]
                     await asyncio.wait(tasks)

       def run(self,eventNames=[],lambdaEventIndexs=[]):
              if eventNames==[] and lambdaEventIndexs==[]:
                     self.RunEvents()
              elif eventNames==[] and len(lambdaEventIndexs)>0:
                     self.RunEvents(lambdaEventIndexs=lambdaEventIndexs)
              elif len(eventNames)>0 and lambdaEventIndexs==[]:
                     self.RunEvents(eventNames=eventNames)
              else:
                     self.RunEvents(eventNames,lambdaEventIndexs)

       

a=icodeUser('OUTFOX_SEARCH_USER_ID_NCOO=279026281.3431625; OUTFOX_SEARCH_USER_ID="1792643811@10.112.57.88"; DICT_PERS=v2|cqq||DICT||web||7776000000||1663513725575||113.119.176.155||qqB60D8500058F9FBEA41D76E17167C37A||lY0f6ykLwK0QyOMPFkMYE06y6LwKh4zfRlGk4YEkfJLRYWRLqB0fTz0pFRfw4PMpFROW0LgzOLQK0U50LeK0MqK0; YOUDAO_MOBILE_ACCESS_TYPE=1; DICT_LOGIN=3||1663513725579; DICT_FORCE=true; xiaotuling=icode%3Asession%3Afee863ace3543f4a1566f7f19289e603; DICT_SESS=v2|GN2eh2YPW0guO4lG64PS0puRLkM6Mwy0OW0HTS0L6uRqFhMguP4p40OfhHpZ0M640UWPMzWRHpz0gz0feFRHlWRQukMzEOLey0; JSESSIONID=abcCM4rvINZVN8jl4mrny')
#c=icodeUser('xiaotuling=icode%3Asession%3A5e4580fb5aea6555189cbbe8b3a504b2; NTES_YD_SESS=bsfPg5JydG7jWjhNXPMZ7Mzc9VRY11.6tgp_h8PxII7miAPuiaN2.HdlxTLkC2ysCK6v._NFJvc05h4xO5hcwl0eAgfDPvJW3zn1wMp1hPcpx_4qfaI5XjKJo9VTxqaO1eyqKH7Lps9sH5h838wS05tuiWXNIs.pEG1_Hzp1xgz9y1TLt8ejx3eD_e8O9iM25f9FQFic8GbYVU.cTAcViJHDYSqs7DtMw5aXEFRZ2C4rd; S_INFO=1664715898|0|0&60##|13779995863; P_INFO=13779995863|1664715898|1|youdaodict|00&99|fuj&1663506772&youdaodict#fuj&350200#10#0#0|&0|null|13779995863; DICT_SESS=v2|7W-WWhWAkR6Z0LYMRfUl0UGk4lf6MlGRgLRMgu0fkE0Pu6LYY6L6y06BnHOfOfqu0gSOMTuk4YG0e4PLYWRLpF0lfRMkY0fqBR; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1664715899495||112.48.43.246||urs-phoneyd.58b72793c04b44648@163.com||pyRLzA6Le4RwBk4kYh4gyRQL6LzMkfpL0PS0MTLRfw4RPykLeyPMPB0zY64lEk4pS0qB0MOA0HpL06u6LwBOfw40; DICT_LOGIN=3||1664715899500')
#b=icodeUser('DICT_FORCE=true; OUTFOX_SEARCH_USER_ID_NCOO=1656566759.9641347; OUTFOX_SEARCH_USER_ID="864305560@10.105.137.203"; xiaotuling=icode%3Asession%3A1c2899eb793985bdc61faac3f4e48f67; NTES_YD_SESS=C5Dy0lHw.o.mU1pYLJ3kBVQbItOUZ_NKn7n1vh.MeGWvVQXFV_orx5_bU6NWdzHbrycdJiWEESpT2DVBv3CCHj_sNg9vhZiAUbpnpI5ptWPZ.csVqDXGrge1XcPebZ2_ATHMIoUYIkMZEfUdRtHRl7b_MXsp1c6OY6YVsUt_Zsrx3gNylbtQMKvS.q_APFbD9WPUOF2JKkqsqAn9doQGtIZgOzKjU4aCx; S_INFO=1664677616|0|0&60##|15166043116; P_INFO=15166043116|1664677616|1|youdaodict|00&99|shd&1664674015&youdaodict#shd&370200#10#0#0|&0|null|15166043116; DICT_SESS=v2|Qy1gfoH0qR6LnLwyOLzm0TShfYMn4pLR6B64eLh4Yl0g40MJZ0HkGRUAhMeK6MYEROG0Mq4k4OW0gBh4QBOMPK0g40HYEnf6z0; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1664677617101||221.3.37.38||urs-phoneyd.63c7a5a54e76427ca@163.com||QFh4wBRHqFRquhLwBnLT4R6ZhfzEnLgB0wLkMpB64zM0e4nfQS6Leu0PLnfwBnMOW06uO4PLRHYMRJy6LqBRfPB0; DICT_LOGIN=3||1664677617105')
print(a.getPersonInfo('qqB60D8500058F9FBEA41D76E17167C37A',1))