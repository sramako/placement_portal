from yattag import Doc
import os

topics = open('Data/topics','r')

doci, tagi, texti = Doc().tagtext()

with tagi('html'):
    with tagi('body'):

        for topic in topics:
            name = topic[:-1]
            url = 'Data/'+topic[:-1]+'/'

            with tagi('a', href=topic[:-1]+'/'+'index.html'):
                texti(name)
            with tagi('p'):
                texti(' ')

            subtopics = open(url+'subtopics','r')

            doc, tag, text = Doc().tagtext()
            with tag('html'):
                with tag('body'):
                    for subtopic in subtopics:
                        name2 = subtopic[:-1]
                        url2 = subtopic[:-1]

                        with tag('a', href=url2+'.html'):
                            text(name2)
                        with tag('p'):
                            text(' ')

            result = doc.getvalue()
            os.system('mkdir web/'+name)
            os.system('cp template.html web/'+name+'/index.html')
            file = open('web/'+name+'/index.html','a')
            file.write(result)
            file.close()
            subtopics.close()

topics.close()
resulti = doci.getvalue()
os.system('cp template.html web/index.html')
file = open('web/index.html','a')
file.write(resulti)
file.close()
