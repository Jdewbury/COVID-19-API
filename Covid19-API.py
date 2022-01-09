import requests
import json
import pandas as pd

#Request all information necessary from the URL
response = requests.get("https://api.covid19api.com/summary").text
#print(response) check


#Convert json library into a python dictionary
response_info = json.loads(response)
#print(response_info) check


#Create empty list to display
country_list = []


#Go through python dictionary and collect the country name and total confirmed cases
for country_info in response_info['Countries']:
    country_list.append([country_info['Country'], country_info['TotalConfirmed']])


#Create a Pandas dataframe 
country_df = pd.DataFrame(data=country_list, columns=['Country', 'Total_Confirmed'])


#Display Dataframe 
#Number indicates how many rows we want to display 
#194 available rows to display
print(country_df.head(194))
