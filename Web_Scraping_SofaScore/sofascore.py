from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
import pandas as pd


all_matches_data = []
laliga_final_standings = []
premier_league_final_standings = []
serie_a_final_standings = []
bundesliga_final_standings = []
ligue1_final_standings = []

laliga_final_matches = []
premier_league_final_matches = []
serie_a_final_matches = []
bundesliga_final_matches = []
ligue1_final_matches = []

options = ChromeOptions()
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# A list of the direct URLs for the top 5 leagues
top_5_leagues = [
    "https://www.sofascore.com/tournament/football/england/premier-league/17",
    "https://www.sofascore.com/tournament/football/spain/laliga/8",
    "https://www.sofascore.com/tournament/football/england/premier-league/17",
    "https://www.sofascore.com/tournament/football/italy/serie-a/23",
    "https://www.sofascore.com/tournament/football/germany/bundesliga/35",
    "https://www.sofascore.com/tournament/football/france/ligue-1/34"
]


for i,league_url in enumerate(top_5_leagues):

    driver.get(league_url)
    time.sleep(1)
    
    scores = driver.find_element(By.CSS_SELECTOR, "div.Box.kiSsvW")
    standings = driver.find_element(By.CSS_SELECTOR, "div.TabPanel.bpHovE")
    time.sleep(1)

    if i == 0:
            print("Cookie pop-up not found or already handled.")
    else:
        # XPath for the round selector dropdown you highlighted
        
        league_name_xpath = '//*[@id="__next"]/main/div[2]/div/div/div[1]/div[4]/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/a/bdi'
        league_name = scores.find_element(By.XPATH, league_name_xpath)
        
        roundnumber_xpath = '//*[@id="__next"]/main/div[2]/div/div/div[1]/div[4]/div[1]/div[2]/div[3]/div/div/div[2]/div/div/span'
        roundnumber = scores.find_element(By.XPATH, roundnumber_xpath)

        matches_xpath = "//a[contains(@href, '/football/match/')]"
        matches = scores.find_elements(By.XPATH, matches_xpath)

        actual_matches = matches[:11]
        actual_matches = actual_matches[1:]
        #print(league_name.text)
        #print(roundnumber.text)
        #print("Matches:")
        for match_element in actual_matches:
                #print(match_element.text)
                data_list = match_element.text.split('\n')
                match_data = {'League': league_name}

                if len(data_list) >= 6: # Finished Match
                    match_data['Date'] = data_list[0]
                    match_data['Status'] = data_list[1]
                    match_data['Home Team'] = data_list[2]
                    match_data['Away Team'] = data_list[3]
                    match_data['Home Score'] = data_list[4]
                    match_data['Away Score'] = data_list[5]
                elif len(data_list) >= 4: # Upcoming Match
                    match_data['Date'] = "Upcoming"
                    match_data['Status'] = data_list[0] # This is the time
                    match_data['Home Team'] = data_list[2]
                    match_data['Away Team'] = data_list[3]
                    match_data['Home Score'] = None
                    match_data['Away Score'] = None
                
                if i == 1:
                    laliga_final_matches.append(match_data)
                elif i == 2:
                    premier_league_final_matches.append(match_data)
                elif i == 3:
                    serie_a_final_matches.append(match_data)
                elif i == 4:
                    bundesliga_final_matches.append(match_data)
                elif i == 5:
                    ligue1_final_matches.append(match_data)
        if i == 0:
            print(" skipping cookies")
        else:
            standing_xpath = "//a[contains(@href, '/team/football/')]"
            standing=standings.find_elements(By.XPATH, standing_xpath)
            for team in standing:

                jumbled_text = team.text
                data_list = jumbled_text.split('\n')

                if len(data_list) > 2:

                    rank = data_list[0]
                    team_name = data_list[1]
                    games_played = data_list[2]
                    games_won = data_list[3]
                    games_drawn = data_list[4]
                    games_lost = data_list[5]
                    goal_difference = data_list[6]

                    points = data_list[-1] 
                    team_data = {
              
                        "Rank": rank,
                        "Team": team_name,
                        "games_played": games_played,
                        "Games Won": games_won,
                        "Games Drawn": games_drawn,
                        "Games Lost": games_lost,
                        "Goal Difference": goal_difference,
                        "Points": points
                    }
                    if i == 1:
                        laliga_final_standings.append(team_data)
                    elif i == 2:
                        premier_league_final_standings.append(team_data)
                    elif i == 3:
                        serie_a_final_standings.append(team_data)
                    elif i == 4:
                        bundesliga_final_standings.append(team_data)
                    elif i == 5:
                        ligue1_final_standings.append(team_data)




#print("La Liga matches:")
df_laliga=pd.DataFrame(laliga_final_matches)
df_laliga=df_laliga.drop(columns=['League'])
df_laliga.to_csv('laliga_matches.csv', index=False)
#print(df_laliga)
##print("#" * 220)
#print("Premier League matches:")
df_premier_league=pd.DataFrame(premier_league_final_matches)
df_premier_league=df_premier_league.drop(columns=['League'])
df_premier_league.to_csv('premier_league_matches.csv', index=False)
#print(df_premier_league)
#print("#" * 220)
#print("Serie A matches:")
df_serie_a=pd.DataFrame(serie_a_final_matches)
df_serie_a=df_serie_a.drop(columns=['League'])
df_serie_a.to_csv('serie_a_matches.csv', index=False)
#print(df_serie_a)
#print("#" * 220)
#print("Bundesliga matches:")
df_bundesliga=pd.DataFrame(bundesliga_final_matches)
df_bundesliga=df_bundesliga.drop(columns=['League'])
df_bundesliga.to_csv('Bundesliga_matches.csv', index=False)
#print(df_bundesliga)
#print("#" * 220)
#print("Ligue 1 matches:")
df_ligue1=pd.DataFrame(ligue1_final_matches)
df_ligue1=df_ligue1.drop(columns=['League'])
df_ligue1.to_csv('Ligue_1_matches.csv', index=False)
#print(df_ligue1)
#print("#" * 220)





#print("#" * 220)

#print("La Liga Standings:")
df_laliga=pd.DataFrame(laliga_final_standings)
df_laliga.to_csv('laliga_standings.csv', index=False)
#print(df_laliga)
#print("#" * 220)
#print("Premier League Standings:")
df_premier_league=pd.DataFrame(premier_league_final_standings)
df_premier_league.to_csv('premier_league_standings.csv', index=False)
#print(df_premier_league)
#print("#" * 220)
#print("Serie A Standings:")
df_serie_a=pd.DataFrame(serie_a_final_standings)
df_serie_a.to_csv('serie_a_standings.csv', index=False)
#print(df_serie_a)
#print("#" * 220)
#print("Bundesliga Standings:")
df_bundesliga=pd.DataFrame(bundesliga_final_standings)
df_bundesliga.to_csv('bundesliga_standings.csv', index=False)
#print(df_bundesliga)
#print("#" * 220)
#print("Ligue 1 Standings:")
df_ligue1=pd.DataFrame(ligue1_final_standings)
df_ligue1.to_csv('ligue1_standings.csv', index=False)
#print(df_ligue1)
#print("#" * 220)
