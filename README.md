# Nested_Cross_Validation_on_Time_Series_Data_Model
Nested cross-validation is implemented on a time series data modelled using SARIMAX model 
 
Cross-validation is used to measure out-of-sample accuracy by averaging over several random partitions of the data into training and test samples. Nested cross-validation (CV) is often used to train a model in which hyperparameters also need to be optimized. Model selection without nested CV uses the same data to tune model parameters and evaluate model performance. This may cause hyper-parameter overfitting. 

Here nested cross-validation is performed on a demand-prediction data. The date-wise quantity values from 2015-jan-01 to 2016-dec-31 are extracted and used as the training-validation samples during nested cross validation. Data from 2017-jan-01 to 2017-dec-31 is used as the testing samples.
