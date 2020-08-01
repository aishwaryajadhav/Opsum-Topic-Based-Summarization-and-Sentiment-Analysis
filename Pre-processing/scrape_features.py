#*******************code for web scraping topic features for mobiles*************************
#==============================================================================

wiki = "https://gadgets.ndtv.com/huawei-honor-9i-4444"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,"lxml")
#print(soup.prettify)

right_ele=soup.find_all('div', class_='pd_detail_wrp margin_b30')

diction = {}

for ele in right_ele:
    diction.add(ele.div.string.lower().strip())
    #subs = ele.table  
    l = ele.table.findAll("tr")
    for k in l:
        line = k.td.string.lower()
        line = re.sub('\((\w+\s\w+)|(\w+)\)', '', line)
        line = line.replace('(',"").strip()
        diction.add(line)

#==============================================================================
d = set(['GENERAL', 'Release date', 'Form factor', 'Dimensions (mm)', 'Weight (g)', 'Battery capacity (mAh)', 'Removable battery', 'Colours', 'DISPLAY', 'Screen size (inches)', 'Touchscreen', 'Resolution', 'HARDWARE', 'Processor', 'Processor make', 'RAM', 'Internal storage', 'Expandable storage', 'Expandable storage type', 'Expandable storage up to (GB)', 'CAMERA', 'Rear camera', 'Rear Flash', 'Front camera', 'Front Flash', 'SOFTWARE', 'Operating System', 'CONNECTIVITY', 'Wi-Fi', 'Wi-Fi standards supported', 'GPS', 'Bluetooth', 'NFC', 'Infrared', 'USB OTG', 'Headphones', 'FM', 'Number of SIMs', 'SIM 1', 'SIM Type', 'GSM/CDMA', '3G', '4G/ LTE', 'Supports 4G in India (Band 40)', 'SIM 2', 'SIM Type', 'GSM/CDMA', '3G', '4G/ LTE', 'Supports 4G in India (Band 40)', 'SENSORS', 'Compass/ Magnetometer', 'Proximity sensor', 'Accelerometer', 'Ambient light sensor', 'Gyroscope', 'Barometer', 'Temperature sensor'])
s=set()
for k in d:
    line = re.sub('\((\w+\s\w+)|(\w+)\)', '', k)
    line = line.replace('(',"").replace(')',"").strip().lower()
    s.add(line)

#==============================================================================
ends here



#==============================================================================
topics={}
index={}
for items in myset:
    if int(myset[items])>=7:
        topics[items]=0
#==============================================================================

       
          
#==============================================================================
          
for sentence in final_input:
    count=0
    for topic in topics:
        index[topic]=count
        if topic in sentence:
            topics[topic]=topics[topic]+1
            clusters[count].append(sentence)
        count+=1
        
#refer to battery cluster as follows
###clusters[index["battery"]]
print("\n\n\nNumber of sentences in each cluster\n")
 
#==============================================================================

