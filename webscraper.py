from bs4 import BeautifulSoup
import requests

url = 'https://tl.net/forum/mafia/547420-72-24-midnight-sun-mafia?page=259'
page = requests.get(url, timeout=5)
soup = BeautifulSoup(page.content, "html.parser")
block = soup.find_all('div', {'class': 'solid'})
poster = soup.find_all('div', {'class': 'fpost-username'})
posted = soup.find_all('article', {'class': ['section','forumPost']})
filtered = []
usernames = []



for post in soup.findAll('article', {'class': ['section','forumPost']}):
	for div in soup.find_all("div", {'class':'quote'}):
		div.decompose()
	filtered.append(post.text.encode("utf-8").strip())



for i in poster:
	usernames.append(i.findAll('span')[0].text)

print usernames[0]
print filtered[0]

posterDict = dict(zip(usernames, filtered))
print(posterDict)






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