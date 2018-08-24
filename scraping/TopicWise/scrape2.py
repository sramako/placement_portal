import requests
from bs4 import BeautifulSoup
import time
import os

print("Fetching Data")
t1 = time.time()
page = requests.get('https://www.interviewbit.com/courses/programming/')
soup = BeautifulSoup(page.content,'html.parser')
t2 = time.time()
print(round(t2-t1,2))
print('*'*30+'\n\n')

topics = soup.find_all(class_ = 'topic-title')

u1 = "https://www.interviewbit.com/courses/programming/topics/"

print("Topics Found:\n"+"-"*15)

file1 = open("Data/topic_links","w")
file2 = open("Data/topics","w")

for i in range(0,len(topics)):
    s = topics[i].get_text()
    print(" + "+s)
    u2 = str.strip(s).lower().replace(' ','-')
    os.system('mkdir Data/'+u2.replace('&',''))
    file2.write(u2.replace('&','')+"\n")
    file1.write(u1+u2+"\n")

file1.close()
file2.close()
