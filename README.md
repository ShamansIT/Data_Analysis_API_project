# Data_Analysis_API_project

## Project Descriptions

## Data Reference
***
### Reference
[Link](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### Descriptions
Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP). The trip data was not created by the TLC, and TLC makes no representations as to the accuracy of these data.

For-Hire Vehicle (“FHV”) trip records include fields capturing the dispatching base license number and the pick-up date, time, and taxi zone location ID (shape file below). These records are generated from the FHV Trip Record submissions made by bases. Note: The TLC publishes base trip record data as submitted by the bases, and we cannot guarantee or confirm their accuracy or completeness. Therefore, this may not represent the total amount of trips dispatched by all TLC-licensed bases. The TLC performs routine reviews of the records and takes enforcement actions when necessary to ensure, to the extent possible, complete and accurate information.

### Data Dictionary

| Field Name             | Description                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| VendorID               | A code indicating the TPEP provider that provided the record.                                                |
|                        | - 1 = Creative Mobile Technologies, LLC                                                                      |
|                        | - 2 = VeriFone Inc.                                                                                          |
| tpep_pickup_datetime  | The date and time when the meter was engaged.                                                               |
| tpep_dropoff_datetime | The date and time when the meter was disengaged.                                                             |
| Passenger_count        | The number of passengers in the vehicle. (Driver-entered value)                                              |
| Trip_distance         | The elapsed trip distance in miles reported by the taximeter.                                                |
| PULocationID          | TLC Taxi Zone in which the taximeter was engaged.                                                            |
| DOLocationID          | TLC Taxi Zone in which the taximeter was disengaged.                                                          |
| RateCodeID            | The final rate code in effect at the end of the trip.                                                        |
|                        | - 1 = Standard rate                                                                                          |
|                        | - 2 = JFK                                                                                                    |
|                        | - 3 = Newark                                                                                                 |
|                        | - 4 = Nassau or Westchester                                                                                  |
|                        | - 5 = Negotiated fare                                                                                        |
|                        | - 6 = Group ride                                                                                             |
| Store_and_fwd_flag    | Indicates whether the trip record was held in vehicle memory before sending to the vendor.                   |
|                        | - Y = Store and forward trip                                                                                 |
|                        | - N = Not a store and forward trip                                                                           |
| Payment_type          | A numeric code signifying how the passenger paid for the trip.                                               |
|                        | - 1 = Credit card                                                                                            |
|                        | - 2 = Cash                                                                                                   |
|                        | - 3 = No charge                                                                                              |
|                        | - 4 = Dispute                                                                                                |
|                        | - 5 = Unknown                                                                                                |
|                        | - 6 = Voided trip                                                                                            |
| Fare_amount           | The time-and-distance fare calculated by the meter.                                                          |
| Extra                 | Miscellaneous extras and surcharges. Currently includes the $0.50 and $1 rush hour and overnight charges.  |
| MTA_tax               | $0.50 MTA tax that is automatically triggered based on the metered rate in use.                            |
| Improvement_surcharge | $0.30 improvement surcharge assessed trips at the flag drop.                                                 |
|                        | The improvement surcharge began being levied in 2015.                                                        |
| Tip_amount            | Tip amount. Automatically populated for credit card tips; cash tips are not included.                        |
| Tolls_amount          | Total amount of all tolls paid in the trip.                                                                  |
| Total_amount          | The total amount charged to passengers. Does not include cash tips.                                          |
| Congestion_Surcharge  | Total amount collected in the trip for NYS congestion surcharge.                                             |
| Airport_fee           | $1.25 for pick up only at LaGuardia and John F. Kennedy Airports.                                            |

