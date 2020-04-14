import requests
import pandas as pd
from bs4 import BeautifulSoup

def data_downloader():
 URL = "https://www.worldometers.info/coronavirus/#countries"
 page= requests.get(URL).text

 soup = BeautifulSoup(page, "lxml")
 results = soup.find("table",id="main_table_countries_today")
 content = results.tbody.find_all("tr")

 countries=[]
 total_cases=[]
 new_cases=[]
 total_deaths=[]
 new_deaths=[]
 total_recovered=[]
 active_cases=[]
 serious_cases=[]
 total_cases_1m=[]
 total_deaths_1m=[]
 total_tests=[]
 tests_1m=[]

 for tr in content:
     td = tr.find_all('td')
     countries.append(td[0].text)
     total_cases.append(td[1].text)
     new_cases.append(td[2].text)
     total_deaths.append(td[3].text)
     new_deaths.append(td[4].text)
     total_recovered.append(td[5].text)
     active_cases.append(td[6].text)
     serious_cases.append(td[7].text)
     total_cases_1m.append(td[8].text)
     total_deaths_1m.append(td[9].text)
     total_tests.append(td[10].text)
     tests_1m.append(td[11].text)
 #print(content)
 indices=[i for i in range(1, len(countries)+1)]
 headers = ['Countries', 'Total Cases','New Cases','Total Deaths', 'New Deaths', 'Total Recovered',
            'Active Cases', 'Serious Cases', 'Total Cases per million', 'Total Deaths per million', 'Total Tests', 'Tests per million']
 df= pd.DataFrame(list(zip(countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, serious_cases,
                           total_cases_1m, total_deaths_1m, total_tests, tests_1m)),columns=headers, index=indices)
 print(df)
 df.to_csv('Coronapandemic.csv')


data_downloader()
