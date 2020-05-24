import pandas as pd
#read csv
epl = pd.read_csv("EPL_Set.csv")
i = 1
while i == 1:
	print("Welcome to the Premier League Researcher! Which date would you like to look at? dd/mm/yy")
	dt = input()
	dt1 = epl [epl["Date"]== dt]
	dt_pres = dt1[['Date','HomeTeam','FTHG','FTAG','AwayTeam']]
	if dt_pres.empty:
		print('No matches were played on that date! Would you like to try again? y or n')
		answer = str(input())
		if answer == 'n':
			i = 2
			print('Thanks for playing!')
		else:
			print('Lets play again!')
	else:
		print("Here were the results on that day")
		print(dt_pres)
		print('Would you like to search for another date? y or n')
		answer = str(input())
		if answer == 'n':
			i = 2
			print('Thanks for playing!')
		else:
			print('Lets play again!')
