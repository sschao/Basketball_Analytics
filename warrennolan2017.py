from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup




filename = "webscrape_ncaa_elo2017.csv"
f = open(filename, "w")
#opens file and writes it meaning the existing file with the same name will be erased
headers = "Team,Elo\n"
f.write(headers)

my_url = 'http://warrennolan.com/basketball/2017/elochess'
#URL name

Uclient = uReq(my_url)
page_html = Uclient.read()
Uclient.close()

page_soup = soup(page_html, "html.parser")

games_data = page_soup.findAll("tr")
for game_data in games_data[2:]:
		elo_data = game_data.findAll("td",{"class":"centerdata"})
		elo = elo_data[0].contents[0]
		team_data = game_data.a
		team = team_data["class"][0]
		f.write(team + "," + elo + "\n")

f.close()