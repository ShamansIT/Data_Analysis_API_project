"""
Taxi Trip Data Visualization and Processing.

This script interacts with API to fetch taxi trip data, processes it into structured dataframes,
and visualizes various aspects of the data including trip distances, passenger counts, payment types,
fare amounts, and relationships between trip distance and total amount.

Parameters:
- None

Dependencies:
- pandas: Provides data manipulation capabilities.
- requests: Allows interaction with APIs.
- io.StringIO: Provides string-like file objects.
- ApiResourceManager: Custom module for managing API resources.
- plot_output: Custom module for generating plots.

Returns:
None

Author: Serhii Spitsyn
"""
if __name__ == "__main__":
    import pandas as pd
    import requests
    from io import StringIO 
    from api_resource_manager import ApiResourceManager
    import plot_output

    # Check input for base_name (taxi group)
    while True:
        data_base_name = input("Choose name of taxi group:\n1 - Yellow Taxi\n2 - Green Taxi\nEnter the corresponding number: ")
        if data_base_name in ['1', '2']:
            break
        else:
            print("Invalid input! Please choose 1 or 2.")

    # Define taxi group names based on user input
    if data_base_name == '1':
        taxi_group = 'YTTD'  # Yellow Taxi
    elif data_base_name == '2':
        taxi_group = 'GTTD'  # Green Taxi

    start_year = 2009
    if taxi_group == 'GTTD':
        start_year = 2013

    taxi_name_for_plt = {
        '1' : "Yellow Taxi",
        '2' : "Green Taxi",
    }

    # Check input for year
    while True:
        year_input = input(f"Enter year between {start_year} to 2022: ")
        if year_input.isdigit() and start_year <= int(year_input) <= 2022:
            break
        else:
            print("Invalid input! Please enter a year between 2015 and 2022.")

    # Check input limit rows to download
    while True:
        limit_input = input(f"The amount of analyzed information directly affects the result.\nNotice that the number of lines increases the loading time.\nEnter number of rows (limit 50 000): ")
        if limit_input.isdigit() and 0 <= int(limit_input) <= 50_000:
            break
        else:
            print("Invalid input! Please enter number rows beetween 1 to 50 000.")

    # Define API URL
    api_manager = ApiResourceManager()
    api_url = api_manager.api_resource(taxi_group+year_input, limit_input)

    # Fetch data from API
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        data = None

    # Convert data to DataFrame
    if data:
        df = pd.read_csv(StringIO(data)) 

    #    print(df.info())

        # List of columns that you want to check for datetime conversion
        columns_to_check_pickup = ['lpep_pickup_datetime', 'pickup_datetime', 'tpep_pickup_datetime']
        for col in columns_to_check_pickup:
            if col in df.columns:
                df['lpep_pickup_datetime'] = pd.to_datetime(df[col])

        columns_to_check_dropoff = ['lpep_dropoff_datetime', 'dropoff_datetime', 'tpep_dropoff_datetime']
        for col in columns_to_check_dropoff:
            if col in df.columns:
                df['lpep_dropoff_datetime'] = pd.to_datetime(df[col])

        columns_to_check_vendor = ['vendorid', 'vendor_id']
        for col in columns_to_check_vendor:
            if col in df.columns:
                df.rename(columns={col: 'vendorid'}, inplace=True)
                
        columns_to_check_ratecode = ['ratecodeid', 'rate_code']
        for col in columns_to_check_ratecode:
            if col in df.columns:
                df.rename(columns={col: 'ratecodeid'}, inplace=True)

    #    print(df.info())

        # Delete the column 'store_and_fwd_flag'
        column_to_drop = 'store_and_fwd_flag'
        if column_to_drop in df.columns:
            df = df.drop(columns=[column_to_drop])

        df = df.drop_duplicates().reset_index(drop=True)
        df['trip_id'] = df.index
    
        datetime_dim = df[['lpep_pickup_datetime','lpep_dropoff_datetime']].reset_index(drop=True)
        datetime_dim['lpep_pickup_datetime'] = datetime_dim['lpep_pickup_datetime']
        datetime_dim['pick_hour'] = datetime_dim['lpep_pickup_datetime'].dt.hour
        datetime_dim['pick_day'] = datetime_dim['lpep_pickup_datetime'].dt.day
        datetime_dim['pick_month'] = datetime_dim['lpep_pickup_datetime'].dt.month
        datetime_dim['pick_year'] = datetime_dim['lpep_pickup_datetime'].dt.year
        datetime_dim['pick_weekday'] = datetime_dim['lpep_pickup_datetime'].dt.weekday

        datetime_dim['lpep_dropoff_datetime'] = datetime_dim['lpep_dropoff_datetime']
        datetime_dim['drop_hour'] = datetime_dim['lpep_dropoff_datetime'].dt.hour
        datetime_dim['drop_day'] = datetime_dim['lpep_dropoff_datetime'].dt.day
        datetime_dim['drop_month'] = datetime_dim['lpep_dropoff_datetime'].dt.month
        datetime_dim['drop_year'] = datetime_dim['lpep_dropoff_datetime'].dt.year
        datetime_dim['drop_weekday'] = datetime_dim['lpep_dropoff_datetime'].dt.weekday

        datetime_dim['datetime_id'] = datetime_dim.index

        datetime_dim = datetime_dim[['datetime_id', 'lpep_pickup_datetime', 'pick_hour', 'pick_day', 'pick_month', 
                                    'pick_year', 'pick_weekday','lpep_dropoff_datetime', 'drop_hour', 'drop_day', 
                                    'drop_month', 'drop_year', 'drop_weekday']]

        passenger_count_dim = df[['passenger_count']].reset_index(drop=True)
        passenger_count_dim['passenger_count_id'] = passenger_count_dim.index
        passenger_count_dim = passenger_count_dim[['passenger_count_id','passenger_count']]

        trip_distance_dim = df[['trip_distance']].reset_index(drop=True)
        trip_distance_dim['trip_distance_id'] = trip_distance_dim.index
        trip_distance_dim = trip_distance_dim[['trip_distance_id','trip_distance']]
    
        # Check if 'pickup_longitude' exists in the DataFrame
        if 'pickup_longitude' not in df:
            # Handle the case where 'pickup_longitude' does not exist
            pickup_location_dim = pd.DataFrame(columns=['pickup_location_id', 'pickup_latitude', 'pickup_longitude'])
        else:
            # Extract 'pickup_longitude' and 'pickup_latitude' columns
            pickup_location_dim = df[['pickup_longitude', 'pickup_latitude']].reset_index(drop=True)
            # Create 'pickup_location_id' as index
            pickup_location_dim['pickup_location_id'] = pickup_location_dim.index
            # Rearrange columns
            pickup_location_dim = pickup_location_dim[['pickup_location_id', 'pickup_latitude', 'pickup_longitude']]


        # Check if 'pickup_longitude' and 'dropoff_longitude' exist in the DataFrame
        if 'pickup_longitude' not in df or 'dropoff_longitude' not in df:
            # Handle the case where either 'dropoff_longitude' or 'dropoff_longitude' does not exist
            dropoff_location_dim = pd.DataFrame(columns=['dropoff_location_id', 'dropoff_latitude', 'dropoff_longitude'])
        else:
            # Extract 'dropoff_longitude' and 'dropoff_latitude' columns
            dropoff_location_dim = df[['dropoff_longitude', 'dropoff_latitude']].reset_index(drop=True)
            # Create 'dropoff_location_id' as index
            dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index
            # Rearrange columns
            dropoff_location_dim = dropoff_location_dim[['dropoff_location_id', 'dropoff_latitude', 'dropoff_longitude']]

        payment_type_name = {
            1:"Credit card",
            2:"Cash",
            3:"No charge",
            4:"Dispute",
            5:"Unknown",
            6:"Voided trip"
        }
        payment_type_dim = df[['payment_type']].reset_index(drop=True)
        payment_type_dim['payment_type_id'] = payment_type_dim.index
        payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(payment_type_name)
        payment_type_dim = payment_type_dim[['payment_type_id','payment_type','payment_type_name']]

    #    Check all data table field information   
    #    print(payment_type_dim.info())
    #    print(dropoff_location_dim.info())
    #    print(trip_distance_dim.info())
    #    print(passenger_count_dim.info())
    #    print(datetime_dim.info())
    #    print(df.info())
            
        fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id') \
                    .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id') \
                    .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id') \
                    .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id')\
                    .merge(datetime_dim, left_on='trip_id', right_on='datetime_id') \
                    .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id') \
                    [['trip_id','vendorid', 'datetime_id', 'passenger_count_id',
                    'trip_distance_id', 'pickup_location_id', 'dropoff_location_id',
                    'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
                    'total_amount']]

        #Dict to export plot
        plot_data = {
            "plot" : taxi_name_for_plt,
            "data" : data_base_name,
            "year" : year_input,
            "limit" : limit_input,
        }

        # Plotting the distribution of trip distances
        plot_output.trip_distance_plot(trip_distance_dim, plot_data)  
        # Plotting the distribution of passenger counts
        plot_output.passenger_count_plot(passenger_count_dim, plot_data)
        # Plotting a pie chart for payment types
        plot_output.payment_counts_plot(payment_type_dim, plot_data)
        # Plotting the distribution of fares
        plot_output.fare_amount_plot(fact_table, plot_data)
        # Scatter plot for trip distances vs. total amounts    
        plot_output.trip_Distance_vs_total_amount(fact_table, plot_data)
        # Visualize trip distance distribution    
        plot_output.distance_distribution(trip_distance_dim, plot_data)
        # Visualize fare amount distribution
        plot_output.amount_distribution(fact_table, plot_data)        
    
    else:
        print("No data fetched from API. Exiting...")
