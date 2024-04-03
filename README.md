# Data_Analysis_API_project

## Project Descriptions
***
This script interacts with an API to fetch taxi trip data, processes it into structured dataframes, and visualizes various aspects of the data including trip distances, passenger counts, payment types, fare amounts, and relationships between trip distance and total amount.

## Usage
***
1. Run the script.
2. Choose the taxi group (Yellow Taxi or Green Taxi) by entering the corresponding number.
3. Enter the year for which you want to analyze the data.
4. Specify the number of rows to be analyzed (limit 50,000).
5. The script will fetch data from the API, process it, and generate visualizations.

## Data Reference
***
### Reference
[Link for data API site](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### Descriptions Data
***
Taxi trip records for period 2009-2022 year for Yellow Taxi and for period 2015-2022 year for Green Taxi, include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, payment types, and driver-reported passenger counts. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP). The trip data was not created by the TLC, and TLC makes no representations as to the accuracy of these data.

### Data Dictionary

| Field Name             | Description                  |
|------------------------|------------------------------|
| VendorID               | A code indicating the TPEP provider that provided the record. |
| tpep_pickup_datetime  | The date and time when the meter was engaged. |
| tpep_dropoff_datetime | The date and time when the meter was disengaged. |
| Passenger_count        | The number of passengers in the vehicle. (Driver-entered value) |
| Trip_distance         | The elapsed trip distance in miles reported by the taximeter. |
| RateCodeID            | The final rate code in effect at the end of the trip. |
| Store_and_fwd_flag    | Indicates whether the trip record was held in vehicle memory before sending to the vendor. |
| PULocationID          | TLC Taxi Zone in which the taximeter was engaged. |
| DOLocationID          | TLC Taxi Zone in which the taximeter was disengaged. |
| Payment_type          | A numeric code signifying how the passenger paid for the trip. |
| Fare_amount           | The time-and-distance fare calculated by the meter. |
| Extra                 | Miscellaneous extras and surcharges. |
| MTA_tax               | $0.50 MTA tax that is automatically triggered based on the metered rate in use. |
| Tip_amount            | Tip amount. |
| Tolls_amount          | Total amount of all tolls paid in the trip. |
| Improvement_surcharge | $0.30 improvement surcharge assessed trips at the flag drop. |
| Total_amount          | The total amount charged to passengers. Does not include cash tips. |

### Data Sample Table

| VendorID | tpep_pickup_datetime | tpep_dropoff_datetime | passenger_count | trip_distance | RatecodeID | store_and_fwd_flag | PULocationID | DOLocationID | payment_type | fare_amount | extra | mta_tax | tip_amount | tolls_amount | improvement_surcharge | total_amount | congestion_surcharge | airport_fee |
|----------|-----------------------|------------------------|-----------------|---------------|------------|--------------------|--------------|--------------|--------------|-------------|-------|---------|------------|--------------|-----------------------|--------------|----------------------|-------------|
| 1        | 2015-01-01 00:11:33   | 2015-01-01 00:16:48    | 1               | 1.0           | 1          | N                  | 41           | 166          | 1            | 5.7         | 0.5   | 0.5     | 1.4        | 0.0          | 0.0                   | 8.4          |                      |             |
| 1        | 2015-01-01 00:18:24   | 2015-01-01 00:24:20    | 1               | 0.9           | 1          | N                  | 166          | 238          | 3            | 6.0         | 0.5   | 0.5     | 0.0        | 0.0          | 0.0                   | 7.3          |                      |             |
| 1        | 2015-01-01 00:26:19   | 2015-01-01 00:41:06    | 1               | 3.5           | 1          | N                  | 238          | 162          | 1            | 13.2        | 0.5   | 0.5     | 2.9        | 0.0          | 0.0                   | 17.4         |                      |             |
| 1        | 2015-01-01 00:45:26   | 2015-01-01 00:53:20    | 1               | 2.1           | 1          | N                  | 162          | 263          | 1            | 8.2         | 0.5   | 0.5     | 2.37       | 0.0          | 0.0                   | 11.87        |                      |             |

### Relationshit schema
!["Relationshit schema"](image\Relationshit_schema.png "Relationshit schema")
## Image Layout Example

### Distribution of Trip Distances
!["Distribution of Trip Distances"](image\plot_layout_1.png "Distribution of Trip Distances")

### Distribution of Passenger
!["Distribution of Passenger"](image\plot_layout_2.png "Distribution of Passenger")

### Payment Types Distribution
!["Payment Types Distribution"](image\plot_layout_3.png "Payment Types Distribution")

### Distribution of Fare Amounts
!["Distribution of Fare Amounts"](image\plot_layout_4.png "Distribution of Fare Amounts")

### Trip Distance vs. Total Amount
!["Trip Distance vs. Total Amount"](image\plot_layout_5.png "Trip Distance vs. Total Amount")

### Trip Distance Distribution
!["Trip Distance Distribution"](image\plot_layout_6.png "Trip Distance Distribution")

### Fare Amount Distribution
!["Fare Amount Distribution"](image\plot_layout_7.png "Fare Amount Distribution")
