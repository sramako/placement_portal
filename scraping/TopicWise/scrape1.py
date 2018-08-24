import requests
from bs4 import BeautifulSoup
import time
import re
import os

topics = open('Data/topics','r')
topic_links = open('Data/topic_links','r')

for line in topics:
    line = line[:-1]
    link = topic_links.readline()[:-1]
    print('\n\n'+link)

    dir = 'Data/'+line+'/'

    print("Fetching Data")
    t1 = time.time()
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    t2 = time.time()
    print(round(t2-t1,2))
    print('*'*30+'\n\n')

    list_que = soup.find_all(class_ = 'locked')
    #print(list_que)

    subtopic = []
    sublink = []
    links = soup.findAll('a', attrs={'href': re.compile("^/problems")})

    f = open(dir+'subtopics','w')

    for i in range(0,len(links)):
        subtopic.append(links[i].get_text().replace(' ','').strip('\n'))
        sublink.append(links[i].get('href'))
        print('\t'+subtopic[-1])
        f.write(subtopic[-1].replace('/','by')+'\n')
        #print(question_content)
    f.close()

    for i in range(0,len(sublink)):
        print(sublink[i])
        url = "https://www.interviewbit.com"+sublink[i]
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')

        question_content = soup.find_all(class_ = 'markdown-content')[0].get_text()

        f = open(dir+subtopic[i].replace('/','by'),'w')
        f.write(question_content)
        #print(question_content)
        f.close()
