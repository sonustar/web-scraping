from bs4 import BeautifulSoup
import requests
import json 
import re 

# with open("index.html","r") as f :
#     doc = BeautifulSoup(f,"html.parser")

# print the full html file : 
# print(doc)

#  to get by tag : 
# tag = doc.p
# print(tag)

#how to modify : Not needed now 
# tag.string = " WOo "


# find by tag name : finds all with the tag and returns in an array !!
# tags = doc.find_all("h1")
# print(tags)


#if you want only the content :  doc.string 
#Modify : doc.string = "Hello"




# URL of the web page you want to scrape
url = 'https://hlf.readthedocs.io/en/latest/whatis.html'

# Making a GET request : 
response = requests.get(url)


if response.status_code == 200 : 

    answer_text = BeautifulSoup(response.text,"html.parser")
    
    # printing all the text which are in the h1 tag: 
    # print(result.find_all("h1"))
    # search by tag:  


     # Create a dictionary with the question and answer
    data = {
            "question": "What is Hyperledger Fabric?",
            "answer": answer_text.find_all("p")[0].get_text()
    }

    with open('hyperledger_fabric.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        
        print("Data has been written to hyperledger_fabric.json")

# with open("a.txt","w") as f :
#     doc = BeautifulSoup(f,"html.parser")

# index 2 :
with open("index2.html","r") as f :
    doc = BeautifulSoup(f,"html.parser")


tags = doc.find_all("input", type="text")
for tag in tags:
	tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
	file.write(str(doc))


# How to get access of the attributes : 
# tag['value']

# how to update : 
# tag['value'] = 'new-value'

# it gives all the tag attributes : 
# tag.attrs

# find tags with the text : < value="">text</> :
# tag = doc.find("option" , string="Undergraduate" , value="undergraduate")

# find through class-name 
# doc.find(class_ = "info")

# finds all which has $.... and limit says how many we want !! 
# tag = doc.find_all(string=re.compile("\$.*"),limit=2)


# for all placeholder to change : 
tags = doc.find_all("input", type="text")
for tag in tags:
	tag['placeholder'] = "I changed you!"

# opens a new file and modifies it : 
with open("changed.html", "w") as file:
	file.write(str(doc))
