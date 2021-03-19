import pandas as pd
import matplotlib.pyplot as plt

data_file_path = './data/players.csv'
head_index = 1 
tail_index = 1
growth_limit = 4
potential_limit = 84

players_data_frame = pd.read_csv(data_file_path)


## 1th step : show head and tail
print("~~~~~~~~~~~~~~~~~~~~HEAD~~~~~~~~~~~~~~~~~~~~")
print(players_data_frame.head(head_index))

print("~~~~~~~~~~~~~~~~~~~~TAIL~~~~~~~~~~~~~~~~~~~~")
print(players_data_frame.tail(tail_index))

# 2st step: Identify missing values
print("~~~~~~~~~~~~~~~~~~~~missing values~~~~~~~~~~~~~~~~~~~~")
print(players_data_frame.isna().sum())
# print(players_data_frame['NationalPosition'].isnull()) ## a example of column with miss value
# print(players_data_frame['Weight'].isnull())

# 3th step: avg, max, min of Weight
print("~~~~~~~~~~~~~~~~~~~~min, max, avg~~~~~~~~~~~~~~~~~~~~")
weight_col = players_data_frame['Weight']#.fillna(players_data_frame.mean()) # fill the NaN values of numeric columns with the average value, given by the df.mean() function.
min_weight = weight_col.min()
max_weight = weight_col.max()
avg_weight = weight_col.mean()
print(f"min: {min_weight}, max: {max_weight}, avg: {avg_weight}")  

# 4th step: Most frequent (you can use mode method: players_data_frame['Nationality'].mode()) , Least frequent 
print("~~~~~~~~~~~~~~~~~~~~Most amd Least frequent~~~~~~~~~~~~~~~~~~~~")
countries_count = players_data_frame['Nationality'].value_counts()
print(f"most frequent contry: {countries_count.head(1)}")
print(f"least frequent contry: {countries_count.tail(1)}")

# 5th step: find promising players
print("~~~~~~~~~~~~~~~~~~~~promising players~~~~~~~~~~~~~~~~~~~~")
max_growth_players = players_data_frame.Growth > growth_limit
max_potential_players = players_data_frame.Potential > potential_limit
promising_players = players_data_frame[max_growth_players & max_growth_players]
print(promising_players.Name)

# 6th step: 
print("~~~~~~~~~~~~~~~~~~~~chart~~~~~~~~~~~~~~~~~~~~")
# promising_players.plot(x="Name", y="Positions", style='o')
# plt.scatter(promising_players.Name, promising_players.Positions)
# plt.show()

# 7th step: find best club
print("~~~~~~~~~~~~~~~~~~~~best clubs~~~~~~~~~~~~~~~~~~~~")
clubs = promising_players.Club
print(clubs.value_counts().head(1))

# 8th step: Chelsea score
print("~~~~~~~~~~~~~~~~~~~~chelsea value~~~~~~~~~~~~~~~~~~~~")
chelsea_promising_players = promising_players[promising_players.Club == "Chelsea"]
chelsea_promising_players_value = chelsea_promising_players.ValueEUR.sum()
print(chelsea_promising_players_value)

# 9th step: NationalTeam
print("~~~~~~~~~~~~~~~~~~~~players with out NationalTeam that contract until 2021~~~~~~~~~~~~~~~~~~~~")
with_out_national_team = players_data_frame.NationalTeam == "Not in team" 
contract_until_2021 = players_data_frame.ContractUntil == 2021
p_w_c = players_data_frame[with_out_national_team & contract_until_2021]
print(p_w_c.Name)

# 10th step: Taremi
print("~~~~~~~~~~~~~~~~~~~~Taremi~~~~~~~~~~~~~~~~~~~~")
taremi = players_data_frame[players_data_frame.Name == 'M. Taremi'].head(1) # two item
print(f"taremi-> pos:{taremi.Positions},")
print(f"income: {taremi.WageEUR},")
print(f"club: {taremi.Club}")