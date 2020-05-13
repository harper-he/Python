This is homework 5 of Big Data Analytics course： K-means Clustering via Principal Component Analysis

I used spark, spark machine learning, spark data frames, RDD's, and map reduce to solve all problems.

The colleges_data_science_programs dataset that contains information about dozens of "data science" programs across the US was used to conduct the following tasks:
1. concatenation of multiple columns
2. Create a pipeline that adds a column of features that contains the **tfidf of the text** column. 
3. Create a pipeline model that computes the two first **principal components** of the features column and creates a column named scores.
4. Create a scatter plot with the x axis containing the first principal component (loading) and the y axis containing the second principal component (loading).
5. Define the top 5 words and absolute loadings for the principal components 1 and 2, respetively. 
6. **Interpret the loadings** of principal components analysis.
7. Check the **variance explained by components** of the model.
8. Find the **best number of principal components**, the value $k$ ,such that ($k+1$)-th component is not able to explain more than 0.01 variance. a **for-loop** was used to find such best k. 
9. Create a pipeline for PCA where I fit the maximum possible number of principal components for this dataset. 
10. Create **a scree plot** and **a plot of cumulative variance explained**.
11. Create a pipeline that computes the first 2 principal components. Add a **kmeans** objects to the pipeline and compute **kmeans with k = 5**.
12. Create **a scatter plot PC2 vs. PC1 where each scatter dot is colored by the cluster assignment**. 
13. compare forward transform and inverse transform, the manual projection matches the projection made by the PCA object.
14. Using PCA loading vectors, perform an **inverse transform** on the **projection** variable and store the result.
15. Define proper number of principal components and Explain why.
