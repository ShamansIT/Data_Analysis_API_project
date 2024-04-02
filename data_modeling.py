"""_summary_

    Returns:
        _type_: _description_
        
Author: Serhii Spitsyn
"""
import pandas as pd
import requests
from io import StringIO 
from csv_data_dao import CVSDataDAO
from api_resource_manager import ApiResourceManager

#check data model with sample file
#df = pd.read_csv("sample.csv")

# Define API URL
api_manager = ApiResourceManager()
base_name = "GTTD"
year = '2015'
api_url = api_manager.api_resource(base_name+year)

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

    # Convert from object format to data
    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
    df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

    # Delete the column 'store_and_fwd_flag'
    df = df.drop(columns=['store_and_fwd_flag'])

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
 
    rate_code_type = {
        1:"Standard rate",
        2:"JFK",
        3:"Newark",
        4:"Nassau or Westchester",
        5:"Negotiated fare",
        6:"Group ride"
    }

    rate_code_dim = df[['ratecodeid']].reset_index(drop=True)
    rate_code_dim['rate_code_id'] = rate_code_dim.index
    rate_code_dim['rate_code_name'] = rate_code_dim['ratecodeid'].map(rate_code_type)
    rate_code_dim = rate_code_dim[['rate_code_id','ratecodeid','rate_code_name']]

    pickup_location_dim = df[['pickup_longitude', 'pickup_latitude']].reset_index(drop=True)
    pickup_location_dim['pickup_location_id'] = pickup_location_dim.index
    pickup_location_dim = pickup_location_dim[['pickup_location_id','pickup_latitude','pickup_longitude']] 

    dropoff_location_dim = df[['dropoff_longitude', 'dropoff_latitude']].reset_index(drop=True)
    dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index
    dropoff_location_dim = dropoff_location_dim[['dropoff_location_id','dropoff_latitude','dropoff_longitude']]

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
  
#    print(payment_type_dim.info())
#    print(dropoff_location_dim)
#    print(rate_code_dim.info())
#    print(trip_distance_dim.info())
#    print(passenger_count_dim.info())
#    print(datetime_dim.info())
#    print(df.info())
          
    fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id') \
                .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id') \
                .merge(rate_code_dim, left_on='trip_id', right_on='rate_code_id') \
                .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id') \
                .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id')\
                .merge(datetime_dim, left_on='trip_id', right_on='datetime_id') \
                .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id') \
                [['trip_id','vendorid', 'datetime_id', 'passenger_count_id',
                'trip_distance_id', 'rate_code_id', 'pickup_location_id', 'dropoff_location_id',
                'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
                'improvement_surcharge', 'total_amount']]
    
    # Analyze passenger count distribution
    passenger_count_distribution = passenger_count_dim['passenger_count'].value_counts()
    print("Passenger Count Distribution:")
    print(passenger_count_distribution)

    # Analyze trip distance distribution
    trip_distance_distribution = trip_distance_dim['trip_distance'].describe()
    print("\nTrip Distance Statistics:")
    print(trip_distance_distribution)

    # Analyze rate code distribution
    rate_code_distribution = rate_code_dim['rate_code_name'].value_counts()
    print("\nRate Code Distribution:")
    print(rate_code_distribution)

    # Analyze payment type distribution
    payment_type_distribution = payment_type_dim['payment_type_name'].value_counts()
    print("\nPayment Type Distribution:")
    print(payment_type_distribution)

    # Analyze fare amount statistics
    fare_amount_stats = fact_table['fare_amount'].describe()
    print("\nFare Amount Statistics:")
    print(fare_amount_stats)

    # Visualize trip distance distribution
    import matplotlib.pyplot as plt
    plt.hist(trip_distance_dim['trip_distance'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Trip Distance Distribution')
    plt.xlabel('Trip Distance')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Visualize fare amount distribution
    plt.hist(fact_table['fare_amount'], bins=20, color='lightgreen', edgecolor='black')
    plt.title('Fare Amount Distribution')
    plt.xlabel('Fare Amount')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    
else:
    print("No data fetched from API. Exiting...")
