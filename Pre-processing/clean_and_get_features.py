
#for alpha-numeric entities
def clean_it(sentence):
    cleaned=""
    i=len(sentence)-1
    while i>-1:
        if ord(sentence[i])<128:
            cleaned=sentence[i]+cleaned
        i=i-1
    return cleaned

#****************features************************************     
def process_content():
    try:
        for i in tokenized:
            #print("Theline is ")
            #print (i)
            
            words = nltk.word_tokenize(i)
            
            tagged = nltk.pos_tag(words)
            
            tagged_sent.append(tagged)
            
            string=[]
            string2=[]
            #text_file.write(str(len(tagged)) + "\n")
            for j in range(len(tagged)):
                fir,sec = tagged[j]
                string.append(sec)
                string2.append(fir)
                #print("yo")
            #print(tagged)
            k=0
            while k < len(tagged):
                if string[k].startswith('NN') and string[k+1].startswith('NN') and string[k+2].startswith('NN'):
                    feat_vec[2] = feat_vec[2] + 1
                    
                    strn = ""
                    strn +=  string2[k] +" " + string2[k+1] + " " +string2[k+2]
                    
                    try:
                        myset[strn] += 1
                    except Exception as e:
                        myset[strn] = 1                        
                    k=k+3
                    
                elif (string[k].startswith('NN') and string[k+1].startswith('NN')):
                    feat_vec[1] = feat_vec[1] + 1
                    
                    strn = ""
                    strn += string2[k] +" "+ string2[k+1]
                    #print(strn)
                    try:
                        myset[strn] += 1
                    except Exception as e:
                        myset[strn] = 1
                        
                    k=k+2
                    
                elif string[k].startswith('NN'): #or string[i+1].startswith('NN') or string[i+2].startswith('NN'):
                    feat_vec[0] = feat_vec[0] + 1
                    try:
                        myset[string2[k]] += 1
                    except Exception as e:
                        myset[string2[k]] = 1
                    k=k+1
                    
                else:
                    k=k+1
                    #print(i)   
    except Exception as e:
        print(str(e))

#*****************code for loading data and pos tagging and counting freq of words*****************
#==============================================================================
  
data = json.load(open('data2.json'))
# 
saved_column=[]
for i in data["reviews"]:    
     saved_column.append(i['review_text'])
 
print(len(saved_column))
# 
final_1 =[]
# 
for file in saved_column:
     file=clean_it(file)
     file = file.replace('\xa0',' ')
     s = file.split('.') 
     for string in s:
         string = string.strip().lower().replace(",","")
         if(string !=''):
             final_1.append(string)
 
print(final_1[:10])
 
test_text = ""
for f in final_1:
     test_text += f
     test_text += ". " 
     
train_text = state_union.raw("pos_tag.txt").lower()
# 
# 
sent_token = PunktSentenceTokenizer(train_text)
# 
tokenized = sent_token.tokenize(test_text)
# 
process_content()

print()
ggh=[]
ggh.append(myset)
#print(myset)

f1=open('op_freq.json','w')
json.dump(ggh,f1,indent=4)

f2=open('op_tagged.json','w')
json.dump(tagged_sent,f2,indent=4)


print("Done writting")
#==============================================================================
