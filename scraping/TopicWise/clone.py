import os
from yattag import Doc

os.system('cd Data; ls */*| grep -v "topic" > ../files')

file = open('files','r')

for line in file:
    line = line[:-1]
    print line
    os.system('cp Data/'+line+' temp')

    file2 = open('temp')
    s = file2.read()
    file2.close()
    """
    file2 = open('template.html')
    t = file2.read()
    file2.close()
    """
    s = s.split('\n')

    doc, tag, text = Doc().tagtext()
    with tag('html'):
        for i in s:
            with tag('p'):
                text(i)
    result = doc.getvalue()

    os.system('cp template.html web/'+line+'.html')
    file2 = open('web/'+line+'.html','a')
    file2.write(result)
    file2.close()

file.close()
