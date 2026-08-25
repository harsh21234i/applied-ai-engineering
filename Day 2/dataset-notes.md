# Ride Dataset Analysis

## Problem

The objective is to predict the duration of a new ride in minutes using
historical completed-ride data.

## Dataset Shape

- Number of rows: 10
- Number of columns: 9
- One row represents: One completed ride


## Identifier

- ride_id

The ride ID identifies a database record and should not normally be used
to predict ride duration.

## Features

The model inputs are:

- distance_km
- pickup_hour
- traffic
- weather
- vehicle_type
- is_weekend
- passenger_count

## Target

- actual_duration_min

This is the correct historical answer that the model will learn to predict.

## Feature Types

| Column | Role | Data type |
|---|---|---|
| ride_id | Identifier | ID |
| distance_km | Feature | Continuous numerical |
| pickup_hour | Feature | Discrete numerical/time-derived |
| traffic | Feature | Ordinal categorical |
| weather | Feature | Nominal categorical |
| vehicle_type | Feature | Nominal categorical |
| is_weekend | Feature | Boolean categorical |
| passenger_count | Feature | Discrete numerical |
| actual_duration_min | Target | Continuous numerical |

## Data Format

The CSV file contains structured data because every ride follows the same
rows-and-columns schema.

## Feature and Target Notation

X represents the feature columns:

distance_km, pickup_hour, traffic, weather, vehicle_type, is_weekend and
passenger_count.

y represents the target column:

actual_duration_min.

## Example Training Record

For ride 101:

- X = [5.2, 9, heavy, clear, bike, no, 1]
- y = 24 minutes

The model receives the features and learns that the actual duration for
this historical example was 24 minutes.

## Required Transformations

Before model training:

- Remove ride_id from the model inputs
- Convert categorical values into numerical representations
- Validate numerical ranges
- Check for missing values
- Separate features X from target y