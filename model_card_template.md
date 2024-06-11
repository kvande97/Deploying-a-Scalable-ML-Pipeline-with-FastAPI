# Model Card

## Model Details
- This model was created on 06/10/2024 as part of the Udacity Machine Learning DevOps course. 
- I used a Random Forest Classifier to predict the salary of a person based on the features in the dataset.

## Intended Use
- The model can be used to predict the salary (less than or greater than 50k) of a person based on census data.
- This is an example project of Production ML Model Depolyment, and should not be used in a production environment.

## Training Data
- The model was trained on 80% of the census data, which contains information about individuals such as age, education, occupation, and salary.

## Evaluation Data
- The model was evaluated on the remaining 20% of the census data.

## Metrics
- The model was evaluated using precision, recall, and F1 scores. The model achieved: 
    - Precision: 0.7213
    - Recall: 0.6353
    - F1: 0.6756

## Ethical Considerations
- The model should not be used to make decisions about individuals, such as hiring or lending, as bias was not tested as a part of this project. 


## Caveats and Recommendations
- Census data may not be representative of the population as a whole, and the model may not generalize well to other datasets.