import random
with open('processed_tweets.txt','r',encoding='utf-8',errors='ignore') as tweets, open('shuffled.txt','w',encoding='utf-8') as shu:
    doc=[]
    for i in tweets.readlines():
        doc.append(i)
    random.shuffle(doc)
    for i in doc:
        shu.write(i)
    tweets.close()
    shu.close()