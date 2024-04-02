"""
Visualizes Taxi Trip Data.

This script provides functions to visualize various aspects of taxi trip data,
including trip distances, passenger counts, payment types, fare amounts, and relationships
between trip distance and total amount.

Parameters:
- trip_distance_dim: DataFrame, contains trip distance data.
- passenger_count_dim: DataFrame, contains passenger count data.
- payment_type_dim: DataFrame, contains payment type data.
- fact_table: DataFrame, contains fact data related to taxi trips.
- plot_data: dict, contains information for plotting such as plot type, data type, and year.

Dependencies:
- matplotlib.pyplot as plt: provides plotting capabilities.
- pandas: provides data manipulation capabilities, including handling DataFrames.

Returns:
None

Author: Serhii Spitsyn
"""
import matplotlib.pyplot as plt

def trip_distance_plot(trip_distance_dim, plot_data):  
    # Plotting the distribution of trip distances
    if not trip_distance_dim.empty and 'trip_distance' in trip_distance_dim:
        plt.figure(figsize=(10, 6))
        plt.hist(trip_distance_dim['trip_distance'], bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of Trip Distances for {plot_data["plot"][plot_data["data"]]} in {plot_data["year"]}')
        plt.xlabel('Trip Distance')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        print(f"No data available to plot in Distribution of Trip Distances for {plot_data['plot'][plot_data['data']]} in {plot_data['year']}")

def passenger_count_plot(passenger_count_dim, plot_data):
    # Plotting the distribution of passenger counts
    passenger_count_series = passenger_count_dim['passenger_count'].value_counts()
    if not passenger_count_series.empty:
        plt.figure(figsize=(8, 6))
        passenger_count_series.plot(kind='bar', color='salmon')
        plt.title(f'Distribution of Passenger Counts for {plot_data["plot"][plot_data["data"]]} in {plot_data["year"]}')
        plt.xlabel('Passenger Count')
        plt.ylabel('Frequency')
        plt.xticks(rotation=0)
        plt.grid(axis='y')
        plt.show()
    else:
        print(f"No data available to plot in Distribution of Passenger Counts for {plot_data['plot'][plot_data['data']]} in {plot_data['year']}")

def payment_counts_plot(payment_type_dim, plot_data):
    # Plotting a pie chart for payment types
    plt.figure(figsize=(10, 8))
    payment_counts = payment_type_dim['payment_type_name'].value_counts()
    colors = ['lightgreen', 'lightcoral', 'lightskyblue', 'lightyellow', 'lightpink', 'lightgrey']
    payment_counts.plot(kind='pie', autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
    plt.title(f'Payment Types Distribution for {plot_data["plot"][plot_data["data"]]} in {plot_data["year"]}', fontsize=16)
    plt.ylabel('')
    plt.legend(payment_counts.index, loc="best", fontsize=10)
    plt.tight_layout()
    plt.show()

def fare_amount_plot(fact_table, plot_data):
    # Plotting the distribution of fares
    if not fact_table.empty and 'fare_amount' in fact_table:        
        plt.figure(figsize=(10, 6))
        plt.hist(fact_table['fare_amount'], bins=30, color='orange', edgecolor='black')
        plt.title(f'Distribution of Fare Amounts for {plot_data["plot"][plot_data["data"]]} in {plot_data["year"]}')
        plt.xlabel('Fare Amount')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        print(f"No data available to plot in Distribution of Fare Amounts for {plot_data['plot'][plot_data['data']]} in {plot_data['year']}")

def trip_Distance_vs_total_amount(fact_table, plot_data):
    # Scatter plot for trip distances vs. total amounts
    if not fact_table.empty and 'trip_distance_id' in fact_table:    
        plt.figure(figsize=(10, 6))
        plt.scatter(fact_table['trip_distance_id'], fact_table['total_amount'], color='green', alpha=0.5)
        plt.title(f'Trip Distance vs. Total Amount for {plot_data["plot"][plot_data["data"]]} in {plot_data["year"]}')
        plt.xlabel('Trip Distance')
        plt.ylabel('Total Amount')
        plt.grid(True)
        plt.show()
    else:
        print(f"No data available to plot in Distribution of Fare Amounts for {plot_data['plot'][plot_data['data']]} in {plot_data['year']}")

def distance_distribution(trip_distance_dim, plot_data):
    # Visualize trip distance distribution
    if not trip_distance_dim.empty and 'trip_distance' in trip_distance_dim:  
        plt.hist(trip_distance_dim['trip_distance'], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Trip Distance Distribution for {plot_data["plot"][plot_data["data"]]} in {plot_data["year"]}')
        plt.xlabel('Trip Distance')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        print(f"No data available to plot in Trip Distance Distribution for {plot_data['plot'][plot_data['data']]} in {plot_data['year']}")

def amount_distribution(fact_table, plot_data):
    # Visualize fare amount distribution
    if not fact_table.empty and 'fare_amount' in fact_table:      
        plt.hist(fact_table['fare_amount'], bins=20, color='lightgreen', edgecolor='black')
        plt.title(f'Fare Amount Distribution for {plot_data["plot"][plot_data["data"]]} in {plot_data["year"]}')
        plt.xlabel('Fare Amount')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        print(f"No data available to plot in Fare Amount Distribution for {plot_data['plot'][plot_data['data']]} in {plot_data['year']}")  
