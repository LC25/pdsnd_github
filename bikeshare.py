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
        city = str(input('\nWhich city\'s data would you like to look at: Chicago, New York City or Washington? ')).lower()
        if city.lower() not in ('chicago', 'new york city', 'washington'):
           print("\nSorry, this did not work. Please type either Chicago, New York City or Washington.")
        else:
        #correct city named - exit loop
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('\nWhich month are you interested in (January, February, March, April, May, June or all)? ')).lower()
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Sorry, this did not work. Please input a valid month (see above) or all.")
        else:
        # appropriate month listed - exit loop.
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('\nWhich day do you want to look at? (Monday, Tuesday, ..., Sunday or all)? '))
        if day.lower() not in ('monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("\nSorry, this did not work. Please input a valid day of the week or all. ")
        else:
        # appropriate day listed - exit loop.
            break
    
        
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]

    print('Most common rental month: ', popular_month)

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most common rental day:', popular_day)

    # Display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most common rental hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    print('Most commonly used start station:', popular_start)

    # Display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    print('Most commonly used end station:', popular_end)

    # Display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " -- " + df['End Station']
    popular_trip = df['trip'].mode()[0]

    print('Most frequent trip is:', popular_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_duration = df['Trip Duration'].sum()

    print('The total travel time (in mins) is:', total_duration)
    
    # Display mean travel time
    mean_duration = df['Trip Duration'].mean()

    print('The mean travel time (in mins) is:', round(mean_duration, 2), '\n')
    
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('These are the counts of users by type:\n', user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()

        print('\nThese are the counts of users by gender:\n', gender)
    else:
        print('\nThere is not gender data available for this city selection.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        oldest_birth_year = df['Birth Year'].min()
        youngest_birth_year = df['Birth Year'].max()
        mode_birth_year = df['Birth Year'].mode()[0]
    
        print('\nThe earliest birth year is: {} \nThe most recent birth year is: {} \nThe most common birth year is: {}'.format(oldest_birth_year, youngest_birth_year, mode_birth_year))
    else:
        print('\nThere is not year of birth data available for this city selection.')

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
