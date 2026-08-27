# Day 4 — ML Training Strategy

## Prediction Moment

The ride-duration prediction will be generated when a customer enters the pickup and destination locations and requests a ride, before the ride begins.

## Dataset Anatomy

### Features (X)

- `distance_km`
- `traffic_level`
- `weather`
- `request_hour`

### Target (y)

- `duration_minutes`

### Number of Samples

Each data row represents one completed ride. The CSV header is not counted as a sample.

## Feature Availability Audit

| Feature         | Available at prediction time? | Safe to use? | Reason                                                                  |
|-----------------|-------------------------------|--------------|-------------------------------------------------------------------------|
| distance_km     | Yes                           | Yes          | The distance can be estimated before the ride begins                    |
| traffic_level   | Yes                           | Yes          | Current traffic information can be collected when the ride is requested |
| weather         | Yes                           | Yes          | Current weather information is available before the ride begins         |
| request_hour    | Yes                           | Yes          | It is available from the ride-request timestamp                         |
| dropoff_time    | No                            | No           | It becomes available only after the ride finishes                       |
| actual_duration | No                            | No           | It is the target that the model must predict                            |

## Dataset-Splitting Strategy

I will use a time-based split because the model will use historical rides to predict the duration of future rides. It provides a more realistic production evaluation than randomly mixing older and newer rides.

| Dataset    | Percentage | Purpose                                          |
|------------|-----------:|--------------------------------------------------|
| Training   |        70% | Used to teach the model and learn its parameters |
| Validation |        15% | Used to compare models and improve model choices |
| Test       |        15% | Used for the final unbiased evaluation           |

The oldest rides will be used for training the model.

The rides after them will be used for validation and model selection.

The newest rides will be used for final testing.

## Leakage Prevention

To prevent data leakage:

1. Use only features available when the ride is requested.
2. Split the dataset before calculating preprocessing values.
3. Keep the test dataset untouched during model development.
4. Remove duplicate rides and prevent the same ride from appearing in multiple datasets.
5. Do not use `dropoff_time`, `actual_duration`, or other information generated after the ride begins.
6. Learn missing-value replacements, scaling values, and encodings only from the training dataset.

## Generalization

A model generalizes well when it learns meaningful patterns from the training data and produces accurate predictions for new rides that it has never seen before.

A good model should learn relationships involving distance, traffic, weather, and time instead of memorizing individual historical rides.

### Result Interpretation

| Training error | Test error | Interpretation                                                                       |
|---------------:|-----------:|--------------------------------------------------------------------------------------|
|      2 minutes | 12 minutes | Overfitting—the model performs well on training data but poorly on unseen data       |
|     11 minutes | 13 minutes | Underfitting—the model performs poorly on both training and unseen data              |
|      3 minutes |  4 minutes | Good generalization—the model performs well on both datasets with a small difference |

## Training Workflow

1. Collect and clean historical ride data.
2. Separate the input features (`X`) from the target (`y`).
3. Divide the data into training, validation, and test sets.
4. Train the model using only the training set.
5. Compare and improve model choices using the validation set.
6. Evaluate the selected model once using the untouched test set.
7. Save the trained model and load it inside the prediction API.
8. Monitor production performance and retrain the model when the data changes.