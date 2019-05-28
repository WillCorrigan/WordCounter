from bs4 import BeautifulSoup
import requests

url = 'https://tl.net/forum/mafia/547420-72-24-midnight-sun-mafia?page=259'
page = requests.get(url, timeout=5)
soup = BeautifulSoup(page.content, "html.parser")
block = soup.find_all('div', {'class': 'solid'})
poster = soup.find_all('div', {'class': 'fpost-username'})
posted = soup.find_all('article', {'class': ['section','forumPost']})



for post in soup.findAll('article', {'class': ['section','forumPost']}):
	for div in soup.find_all("div", {'class':'quote'}):
		div.decompose()
		print soup
	# print post.text.encode("utf-8")







# for post in soup.findAll('article', {'class': ['section','forumPost']}):
# 	for div in soup.find_all("div", {'class':'quote'}):
# 		div.decompose()
# 	print post.text.encode("utf-8")

# for poster in soup.find('div', {'class': 'fpost-username'}).find('span', recursive=False):
# 	print poster.encode("utf-8")





# posters = {
# 'name':'Koshi', 
# 'post':'test post'
# }


# for post in content.findAll('article', {'class': ['section','forumPost']}):
# 	for div in content.find_all("div", {'class':'quote'}):
# 		div.decompose()
# 	print post.text.encode("utf-8")


# for hi in content.find('div', {'class': 'fpost-username'}).find('span', recursive=False):
# 	print hi.encode("utf-8")