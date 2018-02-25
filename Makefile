games:
	httrack 'https://www.prochessleague.com/games.html' -O $@ -\* +\*.pgn 

players_list.zip:
	curl -L -o $@ 'http://ratings.fide.com/download/players_list.zip'

players_list_foa.txt: players_list.zip
	unzip $<

