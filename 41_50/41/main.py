import ucimlrepo

# fetch dataset (id: 367)
dota2_games_results = ucimlrepo.fetch_ucirepo(id=367)

# metadata 
print(dota2_games_results.metadata) 