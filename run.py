
# coding: utf-8

# In[1]:

#Chao Fan
#A53078965
#CSE 250A

from math import log
import re

word   = []
count  = []

wordFile = open('/Users/FAN/Desktop/CSE_COURSE/CSE250A/data/vocab.txt', 'r')
for w in wordFile.readlines():
    w = w.strip('\n')
    word.append(w)
    
countFile = open('/Users/FAN/Desktop/CSE_COURSE/CSE250A/data/unigram.txt', 'r')
for c in countFile.readlines():
    c = c.strip('\n')
    count.append(int(c))

total = sum(count)
for w in word:
    if w[0] == 'B':
        index = word.index(w)
        print (w, count[index] * 1.0 /total)


# In[2]:

bigram = [line.strip().split() for line in open("/Users/FAN/Desktop/CSE_COURSE/CSE250A/data/bigram.txt", 'r')]
w_tuples = []

w = "ONE"
ind_w = int (word.index(w))
count_w = count[ind_w]

for j in range (0, len(bigram)):
    if int (bigram[j][0]) ==  ind_w + 1:
        w_tuples.append(bigram[j])

for i in range (0, len(w_tuples)):        
    w_tuples[i] = [int (w) for w in w_tuples[i]]


w_sorted = sorted(w_tuples, key=lambda w: w[2], reverse = True)


for i in range(0, 10):
    index = w_sorted[i][1] - 1
    print (word[index], w_sorted[i][2] * 1.0 / count_w) 


# In[3]:

s = "The stock market fell by one hundred points last week"
s = s.upper()
s = re.sub("[^\w]", " ",  s).split()
pu = 1
pb = 1

for i in range (0, len(s)):
    index = word.index(s[i])
    p = 1.0 * count[index] / total
    pu *= p

Lu = log(pu)
print "Lu equals: ", Lu

ss = "<s>"
th = "THE"
p_den_ss = 0
p_num_ss = 0
index_th = word.index(th) + 1
index_ss = word.index(ss) + 1

for m in range(0, len(bigram)):
    if int (bigram[m][0]) == index_ss:
        p_den_ss += int (bigram[m][2]) 
            
for m in range(0, len(bigram)):        
    if (int (bigram[m][0]) == index_ss) & (int (bigram[m][1]) == index_th):
        p_num_ss = int (bigram[m][2]) * 1.0 / p_den_ss

        
for i in range(0, len(s) - 1):
    p_den = 0
    p_num = 0
    index_1 = word.index(s[i]) + 1
    index_2 = word.index(s[i+1]) + 1
    
    for m in range(0, len(bigram)):
        if int (bigram[m][0]) == index_1:
            p_den += int (bigram[m][2]) 
                    
    for m in range(0, len(bigram)):        
        if (int (bigram[m][0]) == index_1) & (int (bigram[m][1]) == index_2):
            p_num = int (bigram[m][2]) * 1.0 / p_den
        
    pb *= p_num
    
pb *= p_num_ss
Lb = log(pb)
if pb == 0:
    print "Lb equals: negative infinity"
else:
    print "Lb equals: ", Lb


# In[4]:

s = "The fourteen officials sold fire insurance"
s = s.upper()
s = re.sub("[^\w]", " ",  s).split()
pu = 1
pb = 1
l = []

for i in range (0, len(s)):
    index = word.index(s[i])
    p = 1.0 * count[index] / total
    pu *= p
    

Lu = log(pu)
print "Lu equals: ", Lu

ss = "<s>"
th = "THE"
p_den_ss = 0
p_num_ss = 0
index_th = word.index(th) + 1
index_ss = word.index(ss) + 1

for m in range(0, len(bigram)):
    if int (bigram[m][0]) == index_ss:
        p_den_ss += int (bigram[m][2]) 
            
for m in range(0, len(bigram)):        
    if (int (bigram[m][0]) == index_ss) & (int (bigram[m][1]) == index_th):
        p_num_ss = int (bigram[m][2]) * 1.0 / p_den_ss
        
for i in range(0, len(s) - 1):
    p_den = 0
    p_num = 0
    index_1 = word.index(s[i]) + 1
    index_2 = word.index(s[i+1]) + 1
    
    for m in range(0, len(bigram)):
        if int (bigram[m][0]) == index_1:
            p_den += int (bigram[m][2]) 
                    
    for m in range(0, len(bigram)):        
        if (int (bigram[m][0]) == index_1) & (int (bigram[m][1]) == index_2):
            p_num = int (bigram[m][2]) * 1.0 / p_den
    
    pb *= p_num
    
pb *= p_num_ss
if pb == 0:
    print "Lb equals: negative infinity"
else:
    print "Lb equals: ", log(pb)


# In[5]:

s = "The fourteen officials sold fire insurance"
s = s.upper()
s = re.sub("[^\w]", " ",  s).split()
pu = []
pb = []
pm = 1

for i in range (0, len(s)):
    index = word.index(s[i])
    p = 1.0 * count[index] / total
    pu.append(p)

ss = "<s>"
th = "THE"
p_den_ss = 0
p_num_ss = 0
index_th = word.index(th) + 1
index_ss = word.index(ss) + 1

for m in range(0, len(bigram)):
    if int (bigram[m][0]) == index_ss:
        p_den_ss += int (bigram[m][2]) 
            
for m in range(0, len(bigram)):        
    if (int (bigram[m][0]) == index_ss) & (int (bigram[m][1]) == index_th):
        p_num_ss = int (bigram[m][2]) * 1.0 / p_den_ss
        
pb.append(p_num_ss)
        
for i in range(0, len(s) - 1):
    p_den = 0
    p_num = 0
    index_1 = word.index(s[i]) + 1
    index_2 = word.index(s[i+1]) + 1
    
    for m in range(0, len(bigram)):
        if int (bigram[m][0]) == index_1:
            p_den += int (bigram[m][2]) 
                    
    for m in range(0, len(bigram)):        
        if (int (bigram[m][0]) == index_1) & (int (bigram[m][1]) == index_2):
            p_num = int (bigram[m][2]) * 1.0 / p_den
    
    pb.append(p_num)
    

for i in range(0, 100):
    pm = 1
    lambd = 0.01 * i
    for j in range (0, len(pb)):
        pm *= ((1 - lambd) * pu[j] + lambd * pb[j])
    print log(pm)
        
        


# In[ ]:




# In[ ]:



