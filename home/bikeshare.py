import time
import pandas as pd
import numpy as np
import datetime


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "aprill", "may", "june", "july", "august", "septembe", "october", "november", "december", "all"]
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
    
    while True:
        city = input('Enter the City you want to analyze: ')
        if (city.lower() in cities):
            break
        else:
            print('invalid input, you must enter one of the cities')
        
   
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the Month you want to analyze: ')
        if(month.lower() in months):
            break
        else:
            print('invalid input, you must enter one of the months')
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the Day you want to analyze: ')
        if(day.lower() in days):
            break
        else:
            print('invalid input, you must enter one of the days')
       

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ["january", "february", "march", "aprill", "may", "june", "july", "august", "septembe", "october", "november", "december"]
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month         
    most_common_month = df['month'].value_counts().index[0]
    print(most_common_month)
    print('-'*20)
    
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().index[0]
    print(most_common_day)
    print('-'*20)
    
    # TO DO: display the most common start hour
    most_common_startHour = df['Start Time'].dt.hour.value_counts().index[0]
    print(most_common_startHour)
    print('-'*20)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startStation = df['Start Station'].value_counts().index[0]
    print(most_common_startStation)
    print('-'*20)
    
    
    # TO DO: display most commonly used end station
    most_common_endStation = df['End Station'].value_counts().index[0]
    print(most_common_endStation)
    print('-'*20)
    
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start & End Station'] = df['Start Station'] + "-" + df['End Station']
    most_common_startEndStation = df['Start & End Station'].value_counts().index[0]
    print(most_common_startEndStation)
    print('-'*20)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = datetime.timedelta(seconds=int(df['Trip Duration'].sum()))
    print(total)
    print('-'*20)

    # TO DO: display mean travel time
    mean = datetime.timedelta(seconds=int(df['Trip Duration'].mean()))
    print(mean)
    print('-'*20)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    number_of_users = df['User Type'].value_counts()
    print(number_of_users)
    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except:
        print('Data does not include genders')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_uear = df['Birth Year'].max()
        most_common_year = df['Birth Year'].value_count().index[0]
        print(earliest_year, most_recent_uear, most_common_year)
    except:
        print('Data does not include date of birth')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_more = 'yes'
        while show_more == 'yes':
            for i in df.iterrows():
                count = 0
                while count < 5:
                    print(i)
                    count += 1
                response = input('\nView 5 more data entries? Yes or No?\n')
                if response.lower() == 'no':
                    show_more = 'no'
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            


if __name__ == "__main__":
    main()
