# Machine Learning Homework - Exoplanet Exploration


## Background

Over a period of nine years in deep space, the NASA Kepler space telescope has been out on a planet-hunting mission to discover hidden planets outside of our solar system.

To help process this data, this project will create machine learning models capable of classifying candidate exoplanets from the raw dataset.

This assignment will:

1. Preprocess the raw data
2. Tune the models using GridSearchCV
3. Compare two models

- - -

### Models

* Logistic Regression
* Random Forest Classifier


### Comparison

#### Logistic Regression

	Accuracy
Base Model	84.325%
Tuned Model	87.185%

 precision    recall  f1-score   support

     CANDIDATE       0.77      0.68      0.73       411
     CONFIRMED       0.76      0.81      0.79       484
FALSE POSITIVE       0.98      1.00      0.99       853

      accuracy                           0.87      1748
     macro avg       0.84      0.83      0.83      1748
  weighted avg       0.87      0.87      0.87      1748


#### Random Forest Classifier

	Accuracy
Base Model	89.359%
Tuned Model	89.76%

          precision    recall  f1-score   support

     CANDIDATE       0.82      0.76      0.79       411
     CONFIRMED       0.83      0.85      0.84       484
FALSE POSITIVE       0.97      1.00      0.98       853

      accuracy                           0.90      1748
     macro avg       0.87      0.87      0.87      1748
  weighted avg       0.90      0.90      0.90      1748




