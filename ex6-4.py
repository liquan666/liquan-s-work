txt=input()
words=txt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(coumts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=item[i]
    print("{0:<10}{1:>5}".format(word,count))
    
