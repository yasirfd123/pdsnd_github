#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:53:10 2023

@author: yasir


hello this change is for refactoring


second change to refactoring


third change


more changes
"""

import pandas as pd
import time


#df = pd.read_csv("chicago.csv")
#print(df)

CITY_DATA =  {"chicago": 'chicago.csv', "new york": "new_york_city.csv","washington": "washington.csv"}


def get_data():
    """ Asks user to input city name, month, and day of week 
        and handels any error
    """
    while True:
        city = input("\nWhich city would you like to filter? Choices: New York, Chicago, or washington\n").lower()
        if city not in ('chicago', 'new york','washington'):
            print("sorry, try only available cities")
            continue
        else:
            break
        
    while True:
        month = input("\n which month would like to explore? Jan, Feb, Mar, Apr, May, Jun or all?\n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("sorry, try only available month or all")
            continue
        else:
            break
    
    while True:
      day = input("\n which day do you want to explore? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all\n").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("sorry, try only available days or all")
        continue
      else:
        break

    return city, month, day


def get_info(city,month,day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != "all":
        months = ['january', 'february','march','april','may','june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != "all":
        df = df[df['day_of_week'] == day.title()]
        
    
    return df
    


def time_stats(df):
    
    start_time = time.time()
    

    most_common_month = df['month'].mode()[0]

    print("most common month is:", most_common_month)

    most_common_day = df['day_of_week'].mode()[0]

    print("most common day is:", most_common_day)

    most_common_hour = df['hour'].mode()[0]

    print("most common hour is:", most_common_hour)
    
    final_dur = time.time() - start_time
    print("This took %s seconds" % (final_dur))

    print('-'*20)

def stations (df):
    start_time = time.time()

    top_start_station = df['Start Station'].mode()[0]
    print('most common start station is: ',top_start_station)

    top_end_station = df['End Station'].mode()[0]
    print("most common end station is: ", top_end_station)

    comb_group = df.groupby(['Start Station', 'End Station'])
    freq_comb = comb_group.size().sort_values(ascending = False).head(1)
    print('most common start and end station combination is: ', freq_comb)
    final_dur = time.time() - start_time
    print("This took %s seconds" % (final_dur))
    print('-'*20)

def trip_duration(df):
    start_time = time.time()
	
    total_travel_time = df['Trip Duration'].sum()
    print('total trip duration is: ', total_travel_time)

    avg_travel_time = df['Trip Duration'].mean()
    print("mean travel time: ", avg_travel_time)
    final_dur = time.time() - start_time
    print("This took %s seconds" % (final_dur))
    print('-'*20)

def user_stats(df):
    start_time = time.time()

    try:
        
        print("User Types are: ", df['User Type'].value_counts())
    except KeyError:
        print("No data for that month")

    try:
        print("count of genders: ", df['Gender'].value_counts())
    except KeyError:
        print("No data for that month")
        
        
    try:   
        print('earliest birthday year', int(df['Birth Year'].min()))
    except KeyError:
        print("No data for that month")

    try:
        print('latest birthday year', int(df['Birth Year'].max()))
    except KeyError:
        print("No data for that month")

    try:
        print('most common birthday year', int(df['Birth Year'].mode()[0]))
    except KeyError:
        print("No data for that month")
        
    final_dur = time.time() - start_time
    print("This took %s seconds" % (final_dur))
    print('-'*20)


def pure_row(df):
    end_loc = 5
    start_loc = 0
    answer = input("would you like to view pure data? yes or no\n").lower()
    if answer == 'yes':
        while True:
            print(df.iloc[start_loc:end_loc])
            more_data = input("Would you like to view next 5 rows? yes or no\n").lower()
            if more_data != 'yes':
                break
            start_loc += 5
            end_loc += 5
    

def main():
	
    while True:
        city,month,day = get_data()
        df = get_info(city,month,day)
        time_stats(df)
        stations(df)
        trip_duration(df)
        user_stats(df)
        pure_row(df)
        again = input("would you like to view other cities' data? yes or no\n").lower()
        if again != 'yes':
            break

	

if __name__ == "__main__":
	main()