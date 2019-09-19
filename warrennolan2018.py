from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup




filename = "webscrape_ncaa_elo2018.csv"
f = open(filename, "w")
#opens file and writes it meaning the existing file with the same name will be erased
headers = "Team,Elo\n"
f.write(headers)

my_url = 'http://warrennolan.com/basketball/2018/elochess'
#URL name

Uclient = uReq(my_url)
page_html = Uclient.read()
Uclient.close()

page_soup = soup(page_html, "html.parser")

games_data = page_soup.findAll("td",{"class":"leftdata cell-bottom-normal cell-right-normal "})

elo_scores = page_soup.findAll("td",{"class":"centerdata cell-bottom-normal cell-right-normal"})

i=0

for game_data in games_data:
	team = game_data.a.contents[0]
	elo_score = elo_scores[i]
	elo = elo_score.contents[0]

	f.write(team + "," + elo + "\n")
	i += 1

f.close()