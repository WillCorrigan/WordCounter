#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import itertools
import sys
from collections import Counter
from multiprocessing  import Pool


filtered = []
usernames = []

for i in range(262):
	url = 'https://tl.net/forum/mafia/547420-72-24-midnight-sun-mafia?page=' + str(i)
	page = requests.get(url, timeout=5)
	soup = BeautifulSoup(page.content, "html.parser")
	block = soup.find_all('div', {'class': 'solid'})
	poster = soup.find_all('div', {'class': 'fpost-username'})
	posted = soup.find_all('article', {'class': ['section','forumPost']})



	for post in soup.findAll('article', {'class': ['section','forumPost']}):
		for div in soup.find_all("div", {'class':'quote'}):
			div.decompose()
		filtered.append(post.text.encode("utf-8").strip())



	for i in poster:
		usernames.append(i.findAll('span')[0].text)


zipper = zip(usernames, filtered)
splitList = []






def WordCount(username):
	for a in range(len(zipper)):
		if zipper[a][0] == username:
			# print zipper[a][1]
			splitList.append(str(zipper[a][1]).split())



print("please type username")
userinput = raw_input()
WordCount(userinput)
flat_list = []
for sublist in splitList:
	for item in sublist:
		flat_list.append(item)
print len(flat_list)





# for poster in soup.findAll('div', {'class': 'fpost-username'}):
# 	print poster





# for post in soup.findAll('article', {'class': ['section','forumPost']}):
# 	for div in soup.find_all("div", {'class':'quote'}):
# 		div.decompose()
# 	print post.text.encode("utf-8")









# for post in content.findAll('article', {'class': ['section','forumPost']}):
# 	for div in content.find_all("div", {'class':'quote'}):
# 		div.decompose()
# 	print post.text.encode("utf-8")


# for hi in content.find('div', {'class': 'fpost-username'}).find('span', recursive=False):
# 	print hi.encode("utf-8")