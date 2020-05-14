This is homework 6 of Big Data Analytics course：**Wine Quality Exploration Analysis and Classification using PySpark and MLlib**

In this assignment, I would love to use **visualizations, machine learning**, and **inference** to learn more about the characteristics of a good wine and predict good wines. 

Spark, spark machine learning, spark data frames, RDD's, and map reduce were used to solve all problems.

The winequality-red.csv dataset was used to conduct the following tasks:
1. Check and deal with NA / NAN values appropriately. 
2. Convert the target variable's 10 classes into 2 classes.
3. Create visualizations that summarize the data and describe them
4. Create a **spark Random Forest Classifier** using all default parameters and calculate the **AUC**
5. Use spark Random Forest Classifier, ParamGridBuilder, and CrossValidator objects to perform a **random forest grid search**. Use **3 fold cross validation** and a BinaryClassificationEvaluator to evaluate the results. 
6. Extract and **explain specific hyper parameters** used from the grid search.
7. Extract **feature importances** determined by the best model produced by the grid search.
8. Print a tree in the forest from the final model and describe how the **root node is split**: What specific predictor variable is being split and what is the value that determines the left / right split. 
9. Explain why the top level predictor in the printed tree can be different that the top level predictor from the cross validated model.
10. Create a **spark GBT Classifier** using all default parameters and calculate the AUC.
11. Use spark GBTClassifier, ParamGridBuilder, and CrossValidator objects to perform a GBT grid search. Use 3 fold cross validation and a BinaryClassificationEvaluator to evaluate the results. 
12. **compare the feature importances** between GBT and random forest.


