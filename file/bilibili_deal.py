# coding=utf-8

import os,shutil
title=0
path='99390809'
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)
    if filenames[1].find('.flv')>1:
        path1=folderName+'\\'+filenames[0]
        temp=open(path1,'r', encoding='UTF-8')    #B读取视频名字
        content=temp.read()
        temp.close()
        site=content.find('PartName')
        site1=site+11
        str=''
        while content[site1]!='"':
            str=str+content[site1]
            site1=site1+1                       #E
        print(str)
        if title==0:
            temp=open(path1,'r', encoding='UTF-8')     #B读取视频所在文件夹名字
            content=temp.read()
            temp.close()
            site=content.find('Title')
            site1=site+8
            str=''
            while content[site1]!='"':
                str=str+content[site1]
                site1=site1+1                       #E
            path2=str
            os.makedirs(path2)
            title=1
        shutil.copy(folderName+'\\'+filenames[1],path2+'\\'+str+'.flv')


