import time
import pandas as pd
import numpy as np

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
    city = input('select a city from chicago, new york city , washington :').lower()
    while city not in CITY_DATA.keys():
        print('select a valid city !!!')
        city = input('reselect a city from chicago, new york city , washington :').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april' , 'may' , 'june', 'all']
    month= input('select month :'+str(months)+ ' : ').lower()
    while month not in months : 
        print ('invalid month !!!')
        month=input('reselect valid python month'+str(months)+ ' : ').lower()
    else:
        month='all' 
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days =['monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input ( 'select day :'+str(days)+ ' : ').title()
    while day.lower() not in days :
        print ('invalid day !!!')
        day=input ('select day' + str(days) +' : ').title()
    else:
        day ='all'
    
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
    df=pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime (df['Start Time'])
    df['month'] =df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    if month != 'all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df =df[df['month']==month]
    if day !='all' :
        df=df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april' , 'may' , 'june', 'all']
    month = df['month'].mode()[0]
    day = df['day_of_week'].mode()[0]
    
    # TO DO: display the most common month
    print("most common month of travel : ", {months[month-1]})
    # TO DO: display the most common day of week
    print("most common day of travel  : ", {day})

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print('most common hour :',{most_common_hour})

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('most common start station is',most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("most common end station is : ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip']=df['Start Station'] + ' to ' + df['End Station']
    most_common_trip=df['trip'].mode()[0]
    print('most common trip is from : ', most_common_trip)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total travel time',total_travel_time)

    # TO DO: display mean travel time
    number_of_travel=df['Trip Duration'].count()
    mean_travel_time=total_travel_time/number_of_travel
    print("average trip duration equals : ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(df['User Type'].value_counts())
    print('\n\n')
    
    
    # TO DO: Display counts of gender
    
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print('Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most comon birth year is: {year.mode()[0]}')
           
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    raw = input('would you like to view 5 rows of individual trip data? Enter yes or no ?').lower()
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Do you wish to continue? Enter yes or no ?').lower()
            if ask.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ =="__main__":
    main()
