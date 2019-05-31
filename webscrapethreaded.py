#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import itertools
import sys
from time import sleep
from collections import Counter
# from multiprocessing import Pool
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
    for i in range(1,11):
        all_urls.append(base_url + str(i))
    
def scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    print(res.status_code, res.url)
    for post in soup.findAll('article', {'class': ['section','forumPost']}):
    	for div in soup.find_all("div", {'class':'quote'}):
    		div.decompose()
    		filtered.append(post.text.encode("utf-8").strip())
    for i in soup.find_all('div', {'class': 'fpost-username'}):
    	usernames.append(i.findAll('span')[0].text)
    			


def WordCount(username):
	for a in range(len(zipper)):
		if zipper[a][0] == username:
			splitList.append(str(zipper[a][1]).split())




############# Execute ###############

generate_urls()

# for i in range(len(all_urls)):
# 	scrape(all_urls[i])

with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor: 
	executor.map(scrape, all_urls)


zipper = list(zip(usernames, filtered))

playerList = ["BloodyC0bbler", "wherebugsgo", "Koshi", "Holyflare", "VisceraEyes", "Conversion", "Jockmcplop", "iGrok", "raynpelikoneet", "ruXxar", "disformation", "Artanis[Xp]", "Calix"]

for playerName in range(len(playerList)):
	# print("please type username")
	userinput = playerList[playerName]
	WordCount(userinput)
	flat_list = []
	for sublist in splitList:
		for item in sublist:
			flat_list.append(item)
	print(playerList[playerName])		
	print(len(flat_list))
	splitList = []
	flat_list = []

















# ############################## Iterates Through Every TL Mafia Page - Adds to Lists ###########################

# for i in range(10):
# 	url = 'https://tl.net/forum/mafia/547420-72-24-midnight-sun-mafia?page=' + str(i)
# 	page = requests.get(url, timeout=5)
# 	soup = BeautifulSoup(page.content, "html.parser")
# 	block = soup.find_all('div', {'class': 'solid'})
# 	poster = soup.find_all('div', {'class': 'fpost-username'})
# 	posted = soup.find_all('article', {'class': ['section','forumPost']})



# 	for post in soup.findAll('article', {'class': ['section','forumPost']}):
# 		for div in soup.find_all("div", {'class':'quote'}):
# 			div.decompose()
# 		filtered.append(post.text.encode("utf-8").strip())


# 	for i in soup.find_all('div', {'class': 'fpost-username'}):
# 		usernames.append(i.findAll('span')[0].text)


# ########################### Zips Lists Into One List ##########################################

# zipper = zip(usernames, filtered)



# ################################# Get the Word Count of an Inputted User #########################

# def WordCount(username):
# 	for a in range(len(zipper)):
# 		if zipper[a][0] == username:
# 			# print zipper[a][1]
# 			splitList.append(str(zipper[a][1]).split())


# time.sleep(10)
# print("please type username")
# userinput = raw_input()
# WordCount(userinput)
# flat_list = []
# for sublist in splitList:
# 	for item in sublist:
# 		flat_list.append(item)
# print len(flat_list)
