import requests

# The url for all countries data.
countries_url = 'https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json'
# print(countries_url)
all_country_data = requests.get(countries_url).json()
# print(all_country_data)

# The url for all Canada's data.
governnent_url = all_country_data[38]['legislatures'][0]['popolo_url']
# print(government_url)
all_government_data = requests.get(governnent_url).json()
# print(all_government_data)

#Gets data for Member of the House of Commons.
member_of_commons = all_government_data['persons'][279]
# print(member_of_commons)
name = member_of_commons['name']
print(name)
