# Data_Analysis_API_project

## Project Descriptions

## Data Reference
***
### Reference
[Link](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### Descriptions
Yellow taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP). The trip data was not created by the TLC, and TLC makes no representations as to the accuracy of these data.

For-Hire Vehicle (“FHV”) trip records include fields capturing the dispatching base license number and the pick-up date, time, and taxi zone location ID (shape file below). These records are generated from the FHV Trip Record submissions made by bases. Note: The TLC publishes base trip record data as submitted by the bases, and we cannot guarantee or confirm their accuracy or completeness. Therefore, this may not represent the total amount of trips dispatched by all TLC-licensed bases. The TLC performs routine reviews of the records and takes enforcement actions when necessary to ensure, to the extent possible, complete and accurate information.

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


