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
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisWorksList?page={page}&size={getNUm}&userId={userId}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisWorksList?page={page}&size={getNum}&userId={userId}').data.decode('utf-8'))['dataList']


       def getPersonEnshrines(self,userId,page,getNum,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisEnshrines?page={page}&size={getNum}&userId={userId}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/user/works/hisEnshrines?page={page}&size={getNum}&userId={userId}').data.decode('utf-8'))['dataList']


       def discoveryWorks(self,page,isParse=0):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/_next/data/Sac30BLmIoGahv5ucv2RL/discovery.json?page={page}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/_next/data/Sac30BLmIoGahv5ucv2RL/discovery.json?page={page}').data.decode('utf-8'))['pageProps']['initModel']['list']


       def getLeaderboard(self,page,getNum,theme='all',codeLanguage='all',isParse=1):
              return self.http.request('GET',f'https://icodeshequ.youdao.com/api/index/works/list?page={page}&size={getNum}&sortType=1&theme={theme}&codeLanguage={codeLanguage}') if not isParse else json.loads(self.http.request('GET',f'https://icodeshequ.youdao.com/api/index/works/list?page={page}&size={getNum}&sortType=1&theme={theme}&codeLanguage={codeLanguage}').data.decode('utf-8'))['dataList']


#a=icodeUser('OUTFOX_SEARCH_USER_ID_NCOO=279026281.3431625; OUTFOX_SEARCH_USER_ID="1792643811@10.112.57.88"; DICT_PERS=v2|cqq||DICT||web||7776000000||1663513725575||113.119.176.155||qqB60D8500058F9FBEA41D76E17167C37A||lY0f6ykLwK0QyOMPFkMYE06y6LwKh4zfRlGk4YEkfJLRYWRLqB0fTz0pFRfw4PMpFROW0LgzOLQK0U50LeK0MqK0; YOUDAO_MOBILE_ACCESS_TYPE=1; DICT_LOGIN=3||1663513725579; DICT_FORCE=true; xiaotuling=icode%3Asession%3Afee863ace3543f4a1566f7f19289e603; DICT_SESS=v2|GN2eh2YPW0guO4lG64PS0puRLkM6Mwy0OW0HTS0L6uRqFhMguP4p40OfhHpZ0M640UWPMzWRHpz0gz0feFRHlWRQukMzEOLey0; JSESSIONID=abcCM4rvINZVN8jl4mrny')
#b=icodeUser('DICT_FORCE=true; OUTFOX_SEARCH_USER_ID_NCOO=1656566759.9641347; OUTFOX_SEARCH_USER_ID="864305560@10.105.137.203"; xiaotuling=icode%3Asession%3A1c2899eb793985bdc61faac3f4e48f67; NTES_YD_SESS=C5Dy0lHw.o.mU1pYLJ3kBVQbItOUZ_NKn7n1vh.MeGWvVQXFV_orx5_bU6NWdzHbrycdJiWEESpT2DVBv3CCHj_sNg9vhZiAUbpnpI5ptWPZ.csVqDXGrge1XcPebZ2_ATHMIoUYIkMZEfUdRtHRl7b_MXsp1c6OY6YVsUt_Zsrx3gNylbtQMKvS.q_APFbD9WPUOF2JKkqsqAn9doQGtIZgOzKjU4aCx; S_INFO=1664677616|0|0&60##|15166043116; P_INFO=15166043116|1664677616|1|youdaodict|00&99|shd&1664674015&youdaodict#shd&370200#10#0#0|&0|null|15166043116; DICT_SESS=v2|Qy1gfoH0qR6LnLwyOLzm0TShfYMn4pLR6B64eLh4Yl0g40MJZ0HkGRUAhMeK6MYEROG0Mq4k4OW0gBh4QBOMPK0g40HYEnf6z0; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1664677617101||221.3.37.38||urs-phoneyd.63c7a5a54e76427ca@163.com||QFh4wBRHqFRquhLwBnLT4R6ZhfzEnLgB0wLkMpB64zM0e4nfQS6Leu0PLnfwBnMOW06uO4PLRHYMRJy6LqBRfPB0; DICT_LOGIN=3||1664677617105')

'''
async def func2(c):
       await asyncio.get_running_loop().run_in_executor(None,c.updateIntro,'John，你是我爹！我对不起你！我是个垃即！！')

async def func(c):
       await asyncio.get_running_loop().run_in_executor(None,c.reSubmitScratch,'1aeb4b952cde445bbee8ea8067900c18','{"targets":[{"isStage":true,"name":"Stage","variables":{"]i(LXs%]L:]N+lbx9cBn-得分-":["得分","0"],"b$_h_0WQZE4qP?^$/,L{":["速度",-5.5]},"lists":{},"broadcasts":{},"blocks":{},"comments":{},"currentCostume":0,"costumes":[{"assetId":"cd21514d0531fdffb22204e0ec5ed84a","name":"背景1","bitmapResolution":1,"md5ext":"cd21514d0531fdffb22204e0ec5ed84a.svg","dataFormat":"svg","rotationCenterX":0,"rotationCenterY":0}],"sounds":[],"volume":100,"layerOrder":0,"tempo":60,"videoTransparency":50,"videoState":"off","textToSpeechLanguage":null},{"isStage":false,"name":"Cat","variables":{},"lists":{},"broadcasts":{},"blocks":{"`*O6tilU[/`DDojN{[IG":{"opcode":"event_whenflagclicked","next":"Oow:)!ii,T|D44}-?*ck","parent":null,"inputs":{},"fields":{},"shadow":false,"topLevel":true,"x":242,"y":121},"Oow:)!ii,T|D44}-?*ck":{"opcode":"looks_switchcostumeto","next":null,"parent":"`*O6tilU[/`DDojN{[IG","inputs":{"COSTUME":[1,"#;ac~eA`w!PHJ(V2BGt}"]},"fields":{},"shadow":false,"topLevel":false},"#;ac~eA`w!PHJ(V2BGt}":{"opcode":"looks_costume","next":null,"parent":"Oow:)!ii,T|D44}-?*ck","inputs":{},"fields":{"COSTUME":["cat-a",null]},"shadow":true,"topLevel":false},"2?S1rN@9o7-+ayYqO_xt":{"opcode":"event_whenkeypressed","next":"j;6mFz7@[yIYU!A6X~Lb","parent":null,"inputs":{},"fields":{"KEY_OPTION":["space",null]},"shadow":false,"topLevel":true,"x":-112,"y":263},"j;6mFz7@[yIYU!A6X~Lb":{"opcode":"looks_nextcostume","next":null,"parent":"2?S1rN@9o7-+ayYqO_xt","inputs":{},"fields":{},"shadow":false,"topLevel":false}},"comments":{},"currentCostume":0,"costumes":[{"assetId":"6ce632927fcd145cf7c2e75b61d5ec89","name":"cat-a","bitmapResolution":1,"md5ext":"6ce632927fcd145cf7c2e75b61d5ec89.svg","dataFormat":"svg","rotationCenterX":230.1116209706811,"rotationCenterY":174.0212735643767},{"assetId":"77071c40b3c0895b706592020fdf03dc","name":"cat-b","bitmapResolution":1,"md5ext":"77071c40b3c0895b706592020fdf03dc.svg","dataFormat":"svg","rotationCenterX":235.21557775321247,"rotationCenterY":145.91666221618652}],"sounds":[{"assetId":"83c36d806dc92327b9e7049a565c6bff","name":"Meow","dataFormat":"wav","format":"","rate":48000,"sampleCount":40682,"md5ext":"83c36d806dc92327b9e7049a565c6bff.wav"}],"volume":100,"layerOrder":1,"visible":true,"x":0,"y":0,"size":100,"direction":90,"draggable":false,"rotationStyle":"all around"}],"monitors":[{"id":"]i(LXs%]L:]N+lbx9cBn-得分-","mode":"default","opcode":"data_variable","params":{"VARIABLE":"得分"},"spriteName":null,"value":"0","width":0,"height":0,"x":5,"y":5,"visible":false,"sliderMin":0,"sliderMax":100,"isDiscrete":true},{"id":"b$_h_0WQZE4qP?^$/,L{","mode":"default","opcode":"data_variable","params":{"VARIABLE":"速度"},"spriteName":null,"value":"-2","width":0,"height":0,"x":5,"y":34,"visible":false,"sliderMin":0,"sliderMax":100,"isDiscrete":true}],"extensions":[],"meta":{"semver":"3.0.0","vm":"0.2.0-prerelease.20190226023539","agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"}}',1,'John 我对不起你！','我对不起你啊....呜呜呜...John！我的爹！','http://ydschool-online.nosdn.127.net/svg/3ace2f62171c6b72cf5410ede63c2f9c539a47d4a45d0c1666263a562071cc99.png')

async def knsk():
       c=icodeUser('xiaotuling=icode%3Asession%3A5e4580fb5aea6555189cbbe8b3a504b2; NTES_YD_SESS=bsfPg5JydG7jWjhNXPMZ7Mzc9VRY11.6tgp_h8PxII7miAPuiaN2.HdlxTLkC2ysCK6v._NFJvc05h4xO5hcwl0eAgfDPvJW3zn1wMp1hPcpx_4qfaI5XjKJo9VTxqaO1eyqKH7Lps9sH5h838wS05tuiWXNIs.pEG1_Hzp1xgz9y1TLt8ejx3eD_e8O9iM25f9FQFic8GbYVU.cTAcViJHDYSqs7DtMw5aXEFRZ2C4rd; S_INFO=1664715898|0|0&60##|13779995863; P_INFO=13779995863|1664715898|1|youdaodict|00&99|fuj&1663506772&youdaodict#fuj&350200#10#0#0|&0|null|13779995863; DICT_SESS=v2|7W-WWhWAkR6Z0LYMRfUl0UGk4lf6MlGRgLRMgu0fkE0Pu6LYY6L6y06BnHOfOfqu0gSOMTuk4YG0e4PLYWRLpF0lfRMkY0fqBR; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1664715899495||112.48.43.246||urs-phoneyd.58b72793c04b44648@163.com||pyRLzA6Le4RwBk4kYh4gyRQL6LzMkfpL0PS0MTLRfw4RPykLeyPMPB0zY64lEk4pS0qB0MOA0HpL06u6LwBOfw40; DICT_LOGIN=3||1664715899500')
       tasks=list(map(lambda x : asyncio.create_task(func(c)) if x%2==0 else asyncio.create_task(func2(c)) , [i for i in range(1000)]))
       await asyncio.wait(tasks)
while True:
       asyncio.run(knsk())
       print('finished')
'''
c=icodeUser('xiaotuling=icode%3Asession%3A5e4580fb5aea6555189cbbe8b3a504b2; NTES_YD_SESS=bsfPg5JydG7jWjhNXPMZ7Mzc9VRY11.6tgp_h8PxII7miAPuiaN2.HdlxTLkC2ysCK6v._NFJvc05h4xO5hcwl0eAgfDPvJW3zn1wMp1hPcpx_4qfaI5XjKJo9VTxqaO1eyqKH7Lps9sH5h838wS05tuiWXNIs.pEG1_Hzp1xgz9y1TLt8ejx3eD_e8O9iM25f9FQFic8GbYVU.cTAcViJHDYSqs7DtMw5aXEFRZ2C4rd; S_INFO=1664715898|0|0&60##|13779995863; P_INFO=13779995863|1664715898|1|youdaodict|00&99|fuj&1663506772&youdaodict#fuj&350200#10#0#0|&0|null|13779995863; DICT_SESS=v2|7W-WWhWAkR6Z0LYMRfUl0UGk4lf6MlGRgLRMgu0fkE0Pu6LYY6L6y06BnHOfOfqu0gSOMTuk4YG0e4PLYWRLpF0lfRMkY0fqBR; DICT_PERS=v2|urs-phone-web||DICT||web||604800000||1664715899495||112.48.43.246||urs-phoneyd.58b72793c04b44648@163.com||pyRLzA6Le4RwBk4kYh4gyRQL6LzMkfpL0PS0MTLRfw4RPykLeyPMPB0zY64lEk4pS0qB0MOA0HpL06u6LwBOfw40; DICT_LOGIN=3||1664715899500')
comments=c.getWorkComments(c.getWorkId('https://icodeshequ.youdao.com/work/1c0012c931a5a9142d20944bc23a1c4b?from=discovery'),1,2000,1)
for i in comments:
       c.deleteComment(int(i['id'])).data.decode('utf-8')