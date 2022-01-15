import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Request all information necessary from the URL
response = requests.get("https://api.covid19api.com/summary").text
#print(response) check


#Convert json library into a python dictionary
response_info = json.loads(response)
#print(response_info) check

#Create empty list to display
country_name = []
country_count = []


#Go through python dictionary and collect the country name and total confirmed cases
for country_info in response_info['Countries']:
    country_name.append(country_info['Country'])
    country_count.append(country_info['TotalConfirmed'])

#Gather input from user
my_country = input('Please enter the Country you would like to see the total number of COVID-19 cases for: ')

#Recombine lists back into a disctionary
countries = {country_name[i]: country_count[i] for i in range(len(country_name))}

#Display information
print(f' The total COVID-19 cases in {my_country} is currently {countries[my_country]} ')


