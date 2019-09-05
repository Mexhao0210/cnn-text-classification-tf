def split():
    with open('./data/processed_tweets.txt','r',encoding='utf-8',errors='ignore') as tweet,open('./data/train_post','w',encoding='utf-8',errors='ignore') as post,open('./data/train_label','w',encoding='utf-8',errors='ignore') as label:
        for s in tweet.readlines():
            s=s.lower()
            arr=s.split('\t')
            label.write(arr[0])
            label.write('\n')
           # arr.pop(0)
           # content=' '.join(arr)
            post.write(arr[1])
           # post.write('\n')
    tweet.close()
    post.close()
    label.close()

split()
