from re import findall
from requests import get
import json
from pyperclip import copy
import csv


def getHaokan(url):
    res = get(url)
    text = res.text
    regex = findall("window.__PRELOADED_STATE__\s=\s(.*?);[\s]*document",text)
    jsonobj = json.loads(regex[0])
    title = findall("\<title>(.*?)\<\/title>",text)[0]
    return jsonobj['curVideoMeta']['clarityUrl'][-1]['url'],title

def getUrls(filename):
    data_list = []
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in data:
            data_list.append(i)
    for i in data_list:
        i.extend(getHaokan(i[0]))
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in data_list:
            spamwriter.writerow(i)
    return data_list

def downLoad(data_list):
    for i in data_list:
        mp4file=open(i[2]+'.mp4','wb')
        print("Downloading \t---",i[2],"--- ...")
        for chunk in get(i[1]).iter_content(100000):
            mp4file.write(chunk)
        mp4file.close()


try:
    filename = input("please drag the csv file to the window:")
    data = getUrls(filename)
    downLoad(data)
except Exception as e:
    print(e)

input()
