This is homework 4 of Big Data Analytics course: **TF-IDF for text classification using Regularized Logistic Regression**

I used **spark, spark machine learning, spark data frames, RDD's, and map reduce** to solve all problems.

the sms_spam.csv file was used to conduct the following tasks:

1. remove stop words from the text column
2. perform a **term frequency / inverse document frequency transformation** on text
3. define top 10 most/least important words indicated by the TFIDF score
4. **model overfit** explanation 
5. Create a **pipeline capable of predicting binary target using logistic regression**
6. Fit pipeline using a **CrossValidator** object with the number of cross validation folds = 3. 
7. Score the model using **ROC AUC** as the metric. 
8. Create a ROC scatter plot from fitted model TPR/FPR data.
9. Define a grid of **elastic net regularization** parameters by adding a ParamGridBuilder to the previous pipeline 
10. define the best model's **L1 and L2 regularization** parameters
11. Analyze the L1 feature selection:the total number of features, the number of features that L1 regularization eliminated
12. Analyze and Explain the best model weights

