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

    # get user input for city (chicago, new york city, washington)
    # keep asking until they give a valid answer
    city = ''
    while city not in CITY_DATA:
        city = input('Please enter a city - chicago, new york city, or washington: ').lower()
        if city not in CITY_DATA:
            print('That wasn\'t a valid city, try again.')

    # get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month not in valid_months:
        month = input('Enter a month (january through june) or "all": ').lower()
        if month not in valid_months:
            print('Invalid month, please try again.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in valid_days:
        day = input('Enter a day of the week or "all": ').lower()
        if day not in valid_days:
            print('That day wasn\'t recognized, please try again.')

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
    # read in the csv for whichever city was picked
    df = pd.read_csv(CITY_DATA[city])

    # convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # pull out month, day, and hour into their own columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if user didn't pick "all"
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # get the number for the month so we can match it
        month_num = months.index(month) + 1
        df = df[df['month'] == month_num]

    # filter by day if user didn't pick "all"
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # using a list here so index 0 = january, etc.
    month_list = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = df['month'].mode()[0]
    print('Most Common Month: ' + month_list[common_month - 1])

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end)

    # display most frequent combination of start station and end station trip
    # combine the two station columns into one string to find the most common pair
    combo = df['Start Station'] + ' to ' + df['End Station']
    common_trip = combo.mode()[0]
    print('Most Common Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # duration is in seconds so convert to hours and minutes
    total_time = df['Trip Duration'].sum()
    total_mins = total_time / 60
    total_hours = int(total_mins // 60)
    leftover_mins = int(total_mins % 60)
    print('Total Travel Time: {} hours, {} minutes'.format(total_hours, leftover_mins))

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    avg_mins = int(avg_time // 60)
    avg_secs = int(avg_time % 60)
    print('Average Trip Duration: {} minutes and {} seconds'.format(avg_mins, avg_secs))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('User Types:')
    for user_type, count in user_type_counts.items():
        print('  {}: {}'.format(user_type, count))

    # Display counts of gender
    # washington doesn't have gender data so check first
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nGender:')
        for gender, count in gender_counts.items():
            print('  {}: {}'.format(gender, count))
    else:
        print('\nNo gender data for this city.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nBirth Year Info:')
        print('  Oldest rider birth year:', earliest_year)
        print('  Youngest rider birth year:', recent_year)
        print('  Most common birth year:', common_year)
    else:
        print('\nNo birth year data for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Shows raw data 5 rows at a time if the user wants to see it."""
    i = 0
    show = input('\nWould you like to see raw data? Enter yes or no: ').lower()
    while show == 'yes':
        print(df.iloc[i:i+5])
        i += 5
        if i >= len(df):
            print('No more rows to display.')
            break
        show = input('See 5 more rows? Enter yes or no: ').lower()


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


if __name__ == "__main__":
	main()