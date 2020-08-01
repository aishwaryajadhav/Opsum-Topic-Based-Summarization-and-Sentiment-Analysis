from string import punctuation
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from operator import itemgetter
import urllib.request as urllib2
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import json

feat_vec = np.array((0,0,0))

myset={}
tagged_sent=[]
topics={}


#***********************clustering and atomization********************************
def cluster_split(a):  
    #stop_words1=set({'ourselves', 'hers', 'between', 'yourself', 'but', 'there', 'about', 'once', 'during', 'having', 'with', 'they', 'own', 'an', 'be', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'me', 'were', 'her', 'himself', 'this', 'should', 'our', 'their', 'while', 'both',  'to', 'ours', 'had', 'she', 'all', 'when', 'at', 'any', 'before', 'them', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'why', 'so', 'can', 'did', 'now', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'whom', 't', 'being', 'if', 'theirs', 'my', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'})
    prev=-1
    
    for b in a:
        left=[]
        right=[]
        
        for (x,y) in b:
            if(x!="."):
                left.append(x)
                right.append(y)
                
        indices_NT = [i for i, x in enumerate(left) if (x=="'t" or x=="n't")]
    
        u=0
        for x in indices_NT:
            x-=u
            u+=1
            #print(left[x])
            left[x]=left[x-1]+left[x]
            #print(left[x])
            right[x]="VB"
            del left[x-1]       
            del right[x-1]
      
        indices_NT = [i for i, x in enumerate(left) if (x.startswith("''") or x.startswith("``"))]
        u=0
        for x in indices_NT:
            x-=u
            u+=1
            #print(left[x])
            del left[x] 
            del right[x] 
        
        indices = [i for i, x in enumerate(right) if x == "CC"]
        z=0 
        y=0
        indices.append(len(left))
        
        for x in indices:
            
            if x!=len(left):
                candidate = right[y:x]
                   
                kk=0
                n=0
                adj=0
                
                for t in candidate:
                    if kk==2:
                        sent_f=left[z:x]
                        z=x+1
                        break    
                    
                    if adj==0 and (t.startswith("JJ") or t.startswith("VB")):
                        kk=kk+1
                        adj=1
                    if n==0 and (t.startswith("NN") or t.startswith("PR")):
                        kk=kk+1
                        n=1
                        
                y = x+1
            else:
                sent_f=left[z:]

            q=0            
            this_it=[]
            for topic in topics:
                if topic in sent_f:
                    clusters[topic].append(sent_f)
                    q=1
                    this_it.append(topic)
            
            if q==0:
                if prev==-1:
                    clusters["phone"].append(sent_f)
                    prev=["phone"]
                else:
                    for p in prev:
                        clusters[p].append(sent_f)

            else:
                prev=this_it




tagged_sent = json.load(open('op_tagged.json'))
myset = json.load(open('op_freq.json'))
myset = myset[0]

topics={"camera","battery","memory","screen","processor","storage","price","performance","software","internet","phone"}
clusters = {k: [] for k in topics}

cluster_split(tagged_sent)
print()

ggh=[]
ggh.append(clusters)

f1=open('clusters.json','w')
json.dump(ggh,f1,indent=4)


#******************************cluster printing********************************
#==============================================================================
#==============================================================================
# for topic in topics:
#     print(topic+":")
#     for i in clusters[topic]:
#         print(i)
#     print()
#==============================================================================
#==============================================================================

