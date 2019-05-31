#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import itertools
import sys
from time import sleep
from collections import defaultdict
import concurrent.futures

############################## Cluster Fuck Begins Here ###################################

base_url = 'https://tl.net/forum/mafia/547420-72-24-midnight-sun-mafia?page='
all_urls = list()
filtered = []
usernames = []
zipper = []
splitList = []

############### Functions  ##############

def generate_urls():
    for i in range(1,261):
        all_urls.append(base_url + str(i))
    
def scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    print(res.status_code, res.url)
    tempusernames = []
    tempposts = []
    testzip = []

    for post in soup.findAll('article', {'class': ['section','forumPost']}):
    	for div in soup.find_all("div", {'class':'quote'}):
    		div.decompose()
    	tempposts.append(post.text.encode("utf-8").strip())
    		
    for i in soup.find_all('div', {'class': 'fpost-username'}):
    	tempusernames.append(i.findAll('span')[0].text)
    
    zipper.append(list(zip(tempusernames, tempposts)))
    
  
    		

def WordCount(username):
    for posts in zipper:
        for a in posts:
            if a[0] == username:
                    splitList.append(str(a[1]).split())
           




############# Execute ###############

generate_urls()

# for i in range(len(all_urls)):
# 	scrape(all_urls[i])

with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor: 
	executor.map(scrape, all_urls)


playerList = ["BloodyC0bbler", "wherebugsgo", "Koshi", "Holyflare", "VisceraEyes", "Conversion", "Jockmcplop", "iGrok", "raynpelikoneet", "ruXxar", "disformation", "Artanis[Xp]", "Calix"]


for playerName in playerList:
	WordCount(playerName)
	flat_list = []
	for sublist in splitList:
		for item in sublist:
			flat_list.append(item)
	print(playerName)		
	print(len(flat_list))
	splitList = []
	flat_list = []