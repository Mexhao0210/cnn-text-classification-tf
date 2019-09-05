s=set()
with open('train_label','r',encoding='utf-8') as l:
    for i in l.readlines():
        s.add(i)
print(len(s))
