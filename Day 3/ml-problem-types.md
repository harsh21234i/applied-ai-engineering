# Day 3 — Machine Learning Problem Types

## Supervised Learning

Supervised learning trains a model using a labelled dataset. Every training
example contains input features and a known target. The model learns the
relationship between the features and the target.

## Classification

Classification predicts a predefined category or class.

Examples:
- Predict whether a ride will be cancelled: Yes or No
- Classify an email as Spam or Not Spam

## Regression

Regression predicts a measurable numerical value.

Examples:
- Predict ride duration: 23.4 minutes
- Predict a house price: ₹45,00,000

## Unsupervised Learning

Unsupervised learning uses an unlabelled dataset without a known target.
It discovers hidden patterns, structures, or groups in the data.

## Clustering

Clustering is an unsupervised-learning technique that groups similar data
points together.

Examples:
- Group customers according to their behaviour
- Group similar documents according to their content

## Reinforcement Learning

Reinforcement learning involves an agent interacting with an environment.
The agent observes a state, takes an action, receives a reward or penalty,
and learns a policy that maximizes its long-term reward.

## Classification vs Regression

Classification predicts a category, such as Cancelled or Not Cancelled.

Regression predicts a measurable numerical quantity, such as a ride
duration of 23.4 minutes.

A classification label may be stored as 0 or 1, but these numbers still
represent categories.

## Business Problem Mapping

| Business requirement                          | ML approach            | Reason                        |
|-----------------------------------------------|------------------------|-------------------------------|
| Predict ride duration                         | Regression             | Needs numerical represntation |
| Predict ride cancellation                     | Classification         | Needs to check                |
| Discover customer groups                      | Clustering             | To create the group           |
| Learn the best delivery route through rewards | Reinforcement          | Rewards and state             |
| Calculate GST using a fixed percentage        | Rule based programming |   The exact calculation formula is already known                             |