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
    while True:
        city = input('What city would you like to explore chicago, new york city, or washington? ').lower()
        if (city in['chicago', 'new york city', 'washington']):
            break
        else:
            print('That is not a valid city, please enter one of the three cities.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month you would like to explore or all: ').lower()
        if (month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
            break
        else: print('Sorry, that is not a valid entry.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of the week you would like to explore or all: ').lower()
        if (day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']):
            break
        else: print('Sorry, that is not a valid entry.')


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # My code was not returning one value with just value_counts() so I looked on the channel and Raheel the mentor had said to use idxmax() so I tried that and it worked to only return the first value.

    most_common_month = df['month'].value_counts().idxmax()
    print('The most popular month for bike travel is: {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day'].value_counts().idxmax()
    print('The most popular day for bike travel is: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print('The most popular hour for bike travel is: {}'.format(most_common_hour))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most popular start station is: {}'.format(most_common_start))

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('The most popular end station is: {}'.format(most_common_end))

    # TO DO: display most frequent combination of start station and end station trip
    # Raheel one of the mentors had told someone on the channel to use loc for this function so I tried that.
    df['frequent_comb'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_comb = df['frequent_comb'].mode().loc[0]
    print('The most frequent trip taken is from: {}'.format(most_frequent_comb))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {} seconds.'. format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: {} seconds.'.format(mean_travel_time))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Here are the user types: {}'.format(user_types))

    # TO DO: Display counts of gender
    if ('Gender' in df):
        gender_counts = df['Gender'].value_counts()
        print('Here are the user counts by gender: {}'.format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
    # I was having  issues with my code retunring .0 at the end of the year so the mentor Raheel told me to use {:.0f} to get the year to return normally.
    if ('Birth Year' in df):
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The earliest birth year is {:.0f}, the most recent birth year is {:.0f}, and the most common birth year is {:.0f}.'.format(earliest_birth_year, most_recent_birth_year, most_common_birth_year))


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def raw(df):
    """Displays 5 lines of raw data.
    Asks user if they want to see 5 lines of raw data.
    Returns 5 more lines of raw data if user inputs yes."""

    data = 0
    print(df[0:5])

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            data += 5
            print(df[data : data+5])

        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
