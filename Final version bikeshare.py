import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# Add Month and Day datas
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
R_DATA = ['yes', 'no']
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
        city_name = input ('\nWould you like to see data for Chicago, New York City, or Washington?\n')
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
            print("I will filter for {}\n".format(city_name.title()))                
            break             
        else:
             print('There went something wrong, please try Chicago, New York City or Washington')
                                           
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_name = input ('Which month - All, January, February, March, April, May, or June?\n')
        if month_name.lower() in MONTH_DATA:            
            month = month_name.lower()
            print("I will filter for {}\n".format(month_name.title()))               
            break                            
        else:
             print('There went something wrong, please try another month')

            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_name = input ('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n')
        if day_name.lower() in DAY_DATA:            
            day = day_name.lower()
            print("I will filter for {}\n".format(day_name.title()))                
            break                            
        else:
             print('There went something wrong, please try another day')   

    # Add question if the user wants to see raw datas
    while True:
        raw_data = input('Would you like to see the first 5 rows of the raw datas? Insert yes or no.\n')
        if raw_data.lower() in R_DATA:
            data = raw_data.lower()                
            if data.lower() == 'yes':            
                print('I will search for raw data')
            elif data.lower() == 'no':
                print('I will not search for raw data')
            break
        else:
            print('There went something wrong, please insert "yes" or "no"\n')
            
        
        
    print('-'*40)
    return city, month, day, city_name, raw_data


def load_data(city, month, day, city_name, data):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':        
        month = MONTH_DATA.index(month)        
        df = df.loc[df['month'] == month]
  
    if day != 'all':      
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:" ,common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is:" ,common_day)


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour is {} o´clock".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station:" ,common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station:" ,common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_stat_end = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station:" ,combination_stat_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Number rounded so that there are not so many decimal places
    total_travel_time = df['Trip Duration'].sum()
    Round_total_travel_time = round(total_travel_time)
    print("The total travel time is ca {}s seconds".format(Round_total_travel_time))    

    # TO DO: display mean travel time
    #Number rounded so that there are not so many decimal places
    mean_travel_time = df['Trip Duration'].mean()
    Round_mean_travel_time = round(mean_travel_time)
    print("The mean travel time is ca {}s seconds".format(Round_mean_travel_time))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df, city_name, data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_type = df['User Type'].value_counts()
    print("So many User Types:\n" ,count_of_user_type)           
    
    # TO DO: Display counts of gender
    if city_name.lower() != 'washington':
        counts_of_gender = df['Gender'].value_counts()
        print("\nSo many people with different Gender:\n" ,counts_of_gender)
    else:
        print('\nThere is no information for Gender in this csv')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if city_name.lower() != 'washington':
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_year_birth = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth is in {}".format(earliest_birth_year))
        print("Most recent year of birth is in {}".format(most_recent_birth_year))
        print("Common year of birth is in {}".format(common_year_birth))
    else:
        print('There is no information for Birth Year in this csv')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  
 
    # question if user wants to see more raw data    
    if data.lower() == 'yes':
        print(df.iloc[0:5])    
        x = 0
        while True:        
            raw_data = input('\nWould you like to see five more rows of raw data? Please insert "yes" or "no"\n')
            if raw_data.lower() == 'yes':                
                x = x + 5
                print(df.iloc[x:x+5])                                       
            else:
                print('I stop showing you more raw data') 
                break 
           
    
def main():
    while True:
        city, month, day, city_name, data = get_filters()
        df = load_data(city, month, day, city_name, data)        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city_name, data)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
