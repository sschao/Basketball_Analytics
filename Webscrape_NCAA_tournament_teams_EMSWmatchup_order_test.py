from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


filename = "NCAA_basketball_tournament_EMSW_matchup_order.csv"
f = open(filename, "w")
#opens file and writes it meaning the existing file with the same name will be erased
headers = "Year,Seed,Team Name\n"
f.write(headers)

my_url = 'https://www.sports-reference.com/cbb/postseason/2015-ncaa.html'
#URL name


year = int(my_url[-14:-10])

for year in range(2015,2019):
	winner_list = []
	loser_list = []
	Uclient = uReq(my_url)
	page_html = Uclient.read()
	Uclient.close()

	page_soup = soup(page_html, "html.parser")

	rounds = page_soup.findAll("div",{"class":"round"})

	for each_round in rounds:
		games = each_round.findAll("div", {"class":None})
		for game in games:
			try:	
				winners = game.findAll("div", {"class":"winner"})
				winner = winners[0]
				winning_team = winner.a.contents[0]
				w_seed = winner.span.text



				losers = game.findAll("div", {"class":None})
				loser = losers[0]
				losing_team = loser.a.contents[0]
				l_seed = loser.span.text


				if winning_team not in winner_list and losing_team not in winner_list: 
					winner_list.append(winning_team)
					loser_list.append(losing_team)
					if int(w_seed) < int(l_seed):
						f.write(str(year) + "," + w_seed + "," + winning_team + "\n")					
						f.write(str(year) + "," + l_seed + ","+ losing_team  +  "\n")
					elif int(w_seed) > int(l_seed):
						f.write(str(year) + "," + l_seed + ","+ losing_team  +  "\n")
						f.write(str(year) + "," + w_seed + "," + winning_team + "\n")				
				
				else:
					pass
			except IndexError:
				pass
	my_url = 'https://www.sports-reference.com/cbb/postseason/' + str(year+1)+ '-ncaa.html'				
f.close()