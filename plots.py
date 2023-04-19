'''
Grace Sopha
final project for open source programming - this program will analyze the crime data and visualize it
'''
from tkinter.font import BOLD
from turtle import color
from data import *
import matplotlib.pyplot as plt 
import numpy as np
 
#method for bar chart
#top 5 crimes
def types () :
    try :
        s = df[['primary_type']] #  get a series from data frame

        #from the top 5 crimes, count the number of occurences
        crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))

        #use five rows
        data=crime_count.iloc[-10:-5] # retrieving select rows by loc method

        #reverse the data
        print(data[::-1])

        #bar graph
        data.plot(kind='barh', color=['pink'])
        
        plt.subplots_adjust(left=0.33, right=0.89)

        #labeling graph
        plt.title('Chicago Top 5 Crimes and Occurrence')
        plt.xlabel('Number of Occurrences')
        plt.ylabel('Crime Type')

        # Show graphic
        plt.show()
    except :
        print('Error')

#method for pie chart
#10 locations of crime
def location () :
    try :
        #grab location description
        s = df[['location_description']]
        #from the top locations, count the number of occurences
        location_count = pd.DataFrame(s.groupby('location_description').size().sort_values(ascending=True).rename('counts'))
        
        #grab ten rows
        data = location_count.iloc[-15:-5] # retrieving select rows by loc method
        #display to console
        print(data)

        #create a pie chart with percentages
        data.plot(kind='pie', subplots = True, autopct='%1.1f%%')

        #labeling graph
        plt.title('Chicago Crime Location Occurrences')
        plt.xlabel('Location')
        plt.legend(loc='upper left', bbox_to_anchor=(-0.35, 1.1))
        plt.show()
    except :
        print('Error')

#method for line graph
#arrests compared to non-arrests
def arrests () :
    try :
        #grab arrest column
        s = df[['arrest']]
        free = s.loc[df['arrest'] == False]
        arrest = s.loc[df['arrest'] == True]

        #number of arrests vs non-arrests
        free_count = free.groupby('arrest').size().rename('free')
        arrest_count = arrest.groupby('arrest').size().rename('arrest')

        #compare the two
        chart = pd.DataFrame((arrest_count,free_count),index=('Arrested','Not Arrested'))

        #bar graph
        chart.plot(kind='barh', color=['pink','orange'])
        #display to console
        print(chart)

        #labeling graph
        plt.title('Chicago Arrests vs Non-Arrests')
        plt.xlabel('Number of Occurrences')
        plt.ylabel('Arrest Status')

        plt.show()
        print()
    except :
        print('Error')
