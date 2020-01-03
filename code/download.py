import json

def readurl():
  data = []
  with open('url.txt','r',encoding='utf-8') as file:
    data = json.load(file)
    file.close()
  return data

import requests
import urllib

def download(data):
  for i in range(len(data)):
    item = data[i]
    url = item['url']
    title = '..\\music\\'+item['title']+'.mp3'
    try:
      urllib.request.urlretrieve(url, title)
      # print(i+'/'+len(data), url, title)
    except e:
      print(e)


def main():
  data = readurl()
  download(data)
  pass

if __name__ == '__main__':
  main()
  pass