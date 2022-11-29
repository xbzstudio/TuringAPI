print(
'''==============================
该安装工具版本为v2.0
您可以使用该工具自动安装或更新您的turingAPI
turingAPI安装源：qqcd小图灵账号发布的turingAPI源码作品
urllib3安装源：github qqcd发布的安装源项目
有任何问题请联系项目作者：qq3366487826  wx Misaka_Mikoto114514
==============================\n\n\n''')
input('按下回车以继续...')
print('\n')
try:
    import abc    #如果测试模块引入失败，把这里的abc改成另外一个你有的内置模块
    abc=abc  #如果测试模块引入失败，把这里定义abc的语句的赋值改为要引入的内置模块名称
    print('测试模块引入成功')
except:
    print('测试模块引入失败！请手动更换模块')
try:
    path=str(str(abc)[str(abc).find('from')+6:-2:1].replace('\\\\','\\')[0:[i for i in range(len(str(abc)[str(abc).find('from')+6:-2:1].replace('\\\\','\\'))) if str(abc)[str(abc).find('from')+6:-2:1].replace('\\\\','\\')[i]==('\ '[0])][-1]:1])+'\\turingAPI'
    print('Lib路径查询成功：',path)
except:
    print('Lib路径查询失败，推荐您将Python安装在Python Installer默认提供的位置(或您的模块引入不正确)')
try:
    import os
    import urllib.request as ur
    import json
    import shutil
    import webbrowser
    print('os , urllib , json , shutil , webbrowser引入成功')
except:
    print('os , urllib , json , shutil , webbrowser引入失败，请检查您的Python默认模块是否有异！')
try:
    if not (os.path.exists(str(path[0:-10:1])+'\\urllib3') or os.path.exists(str(path[0:-10:1])+'\\urllib3-main')):
        print('\n\n检测到您没有安装turingAPI的依赖项urllib3，按下回车下载urllib3的zip文件\n')
        if input('如果您确定你已经安装了urllib3，那么可以输入N来取消安装，或按下回车开始安装：') != 'N':
            webbrowser.open('https://codeload.github.com/mmmhss/urllib3-jx/zip/refs/heads/main')
            zippath=input('在下载完成后，请将下载的文件解压，并输入解压后的文件夹路径：')
            shutil.move(str(zippath.replace('\ '[0],'/'))+'/urllib3',str(path[0:-10:1]))
            print('urllib3安装完成')
        else:
            print('已跳过安装urllib3')
    if os.path.exists(path):
        shutil.rmtree(path)
        print('成功删除旧版本的文件')
    os.mkdir(path)
    code=json.loads(ur.urlopen('https://icodeshequ.youdao.com/api/works/detail?id=1e08b62a085344e8ae946c90dc5e1482').read().decode('utf-8'))['data']
    path+='\\__init__.py'
    file=open(path,'w',encoding='utf-8')
    file.write(code['code'])
    file.close()
    print('init文件写入成功\n\n\n')
    print('===============================================')
    print('turingAPI安装成功！现在您可以使用import turingAPI来验证您的turingAPI是否工作正常')
    print('安装的turingAPI版本为：',code['title'])
    print('turingAPI官网网址：https://mmmhss.github.io/turingAPI')
    print('turingAPI操作指南：https://xbz-studio.gitbool.io/turingapi')
    print('祝您使用愉快！')
    print('===============================================\n\n\n')
except:
    print('写入文件失败，请检查您的安装目录或源代码作品出现异常')

input('按下回车以退出...')
