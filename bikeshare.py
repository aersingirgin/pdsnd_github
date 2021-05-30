import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US Bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
      city=input("Please enter one city name between: chicago, new york, washington\n").lower()
      if city in('chicago','new york','washington'):
        print("Your choice is: ",city)
        break
      else:
        print("Please select one of the listed cities with lowercase")
        continue


    # get user input for month (all, january, february, ... , june)

    while True:
        month=input("\nPlease enter one month: january, february, march, april, may, june or all\n").lower()
        if month in('january','february','march','april','may','june','all'):
            print("Your choice is: ",month)
            break
        else:
            print("Please select one of the listed months with lowercase or 'all' for every month")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day=input("\nPlease enter one day of week or enter 'all'\n").lower()
        if day in('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print("Your choice is: ",day)
            break
        else:
            print("Please select one day of the week with lowercase or 'all' for every day")
            continue

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
    """city data load -agirgin3"""
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=days.index(day)+1
        df = df[df['day_of_week'] == day]

    return df

def raw_data(df):

    k=0
    s=input("\nDo you want to see first 5 line of raw data? 'yes' for more and 'no' for analysis\n").lower()
    if s=='yes':

        while s =='yes':
           k=k+5

           print(df.iloc[:k])
           s=input("\nDo you want to see 5 more line of data? 'yes' for more and 'no' for analysis\n").lower()
           continue

    if s=='no':

        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...")
    start_time = time.time()

    # display the most common month
    most_common_month=df['month'].mode()[0]
    print('\nMost common month: ', most_common_month)

    # display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print('\nMost common day: ', most_common_day)

    # display the most common start hour
    most_common_start_time=df['hour'].mode()[0]
    print('\nMost common start hour: ', most_common_start_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print ('\nMost commonly used start station:  ',start_station)
    print()

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly used end station:' , end_station)
    print()

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station'])['User Type'].value_counts().idxmax()
    print('\nMost frequent combination of start station and end station trip:',most_frequent_combination)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time: ', total_travel_time)
    print()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print()

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()

        print(gender_count)
        print()

    except KeyError:
        print('\n There is no data for Washington for Gender and Birth Year')

    # Display earliest, most recent, and most common year of birth

    try:
        earliest= df['Birth Year'].min()
        print('\nEarliest year of birth:', earliest)
        print()

        most_recent= df['Birth Year'].max()
        print('\nMost recent year of birth:', most_recent)
        print()

        most_common_year= df['Birth Year'].value_counts().idxmax()
        print('\nMost common year of birth:', most_common_year)
        print()

    except KeyError:
        print('\n There is no data for Washington for Gender and Birth Year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
