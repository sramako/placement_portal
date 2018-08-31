import os
import string
import copy

classes = []

d = {}

for i in os.listdir('./Data'):
    if os.path.isdir('./Data/'+i):
        classes.append('./Data/'+i)
classes

sp = '1234567890`-=[];,./~!@#$%^&*()_+{}|:<>?\'\"\\'

sp = list(sp)

for clas in classes:
    d[clas] = []

    files = []
    for j in os.listdir(clas):
        if os.path.isfile(clas+'/'+j):
            files.append(clas+'/'+j)

    for f in files:
        file = open(f,'r')
        s = file.read()
        file.close()
        s = s.strip('\n').split(' ')

        for word in range(0,len(s)):
            rem = []
            for i in s[word]:
                if (i not in sp) and ( ord(i)<128 ):
                    rem.append(i)
            s[word] = string.join(rem,'')
        s = filter(lambda a: a!='',s)
        d[clas]+=s
    d[clas] = set(d[clas])

k = d.keys()

file = open('NB/keys','w')
for i in k:
    file.write(i+'\n')
file.close()

bow = dict()

for i in range(0,len(d)):
    file=open('NB/'+str(i),'w')
    for j in d[k[i]]:
        if (len(j)>2) and ('\n' not in j):
            j=j.lower()
            #print j
            if j in bow:
                bow[j].append(i)
            else:
                bow[j] = [i]
            file.write(j+'\n')
    file.close()

#print bow

data = []

file = open('input','r')
for line in file:
    line = line[:-1]
    s = line
    s = s.strip('\n').split(' ')

    for word in range(0,len(s)):
        rem = []
        for i in s[word]:
            if (i not in sp) and ( ord(i)<128 ):
                rem.append(i)
        s[word] = string.join(rem,'')
    s = filter(lambda a: a!='',s)
    for i in s:
        if len(s)>2 and ('\n' not in j):
            data.append(i)

file.close()
#print data
print bow
p = [0]*len(k)

for i in data:
    if i in bow:
        print i
        s = set(bow[i])
        for j in s:
            a = bow[i].count(j)+0.0
            v = a / len(bow[i])
            #print '\t',j,v*100,'%'
            p[j] += v

print p
p2 = copy.deepcopy(p)
p2.sort()
p2=p2[::-1]
for i in p2:
    print round(i,4),'%','\t\t',k[p.index(i)]
