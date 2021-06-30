#全民K歌下载脚本
import requests
import re
import os

SONG=1
VIDEO=2

def download(url,typelist,saving_directory):
    res=requests.get(url)
    res.raise_for_status()
    regex1=re.compile(r'"playurl":"(.*?)"')
    regex2=re.compile(r'"playurl_video":"(.*?)"')
    regsong=re.compile(r'"song_name":"(.*?)"')
    regsinger=re.compile(r'"kg_nick":"(.*?)"')
    os.chdir(saving_directory)
    if SONG in typelist:
        song_name=re.findall(regsong,res.text)[0]+' '+re.findall(regsinger,res.text)[0]+'.m4a'
        tmp=re.findall(regex1,res.text)
        if not tmp[0]=='':
            song_res=requests.get(tmp[0])
            song_res.raise_for_status()
            print('Downloading '+song_name+' from '+ tmp[0]+' ...')
            m4afile=open(song_name,'wb')
            for chunk in song_res.iter_content(100000):
                m4afile.write(chunk)
            m4afile.close()
    if VIDEO in typelist:
        video_name=re.findall(regsong,res.text)[0]+' '+re.findall(regsinger,res.text)[0]+'.mp4'
        tmp=re.findall(regex2,res.text)
        if not tmp[0]=='':
            video_res=requests.get(tmp[0])
            video_res.raise_for_status()
            print('Downloading '+video_name+' from '+ tmp[0]+' ...')
            mp4file=open(video_name,'wb')
            for chunk in video_res.iter_content(100000):
                mp4file.write(chunk)
            mp4file.close()
    print('Finished!')
    return

if __name__=='__main__':
    link=input("输入K歌分享链接：")
    ss=input("是否需要m4a文件？(Y/n)")
    vv=input("是否需要mp4文件？(Y/n)")
    road=input("输入存储路径：")
    tplist=[]
    if ss!='n' or ss!='N':
        tplist+=[SONG]
    if vv!='n' or vv!='N':
        tplist+=[VIDEO]
    download(link,tplist,road)
        
                
                
                
                
