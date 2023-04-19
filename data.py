'''
Grace Sopha
final project for open source programming - this program will analyze the crime data and visualize it
'''
import requests
import pandas as pd
import json

# Base url for Chicago Open Data Portal crime API; plus addin of date and location filters
baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

# Set date range for data jan2019 - march2020
datebetw = "?$where=date between '2019-01-01T12:00:00' and '2020-03-01T14:00:00'"

# syntax for below filter is  'within_box(location_col, NW_lat, NW_long, SE_lat, SE_long)'
#using my apartment 3522 S State St, Chicago, IL
#using south loop, chicago
boxurl = 'within_box(location, 41.830240, -87.626820, 41.871570, -87.627450)'

# Create the overall URL to interogate API with our data and location filters
ourl = baseurl + datebetw + ' AND ' + boxurl

text =  requests.get(ourl).json()  
 
# create pandas dataframe dictionary container object 
df = pd.DataFrame(
    text, columns=['date', 'block', 'primary_type', 'description', 'arrest', 'location_description'])


