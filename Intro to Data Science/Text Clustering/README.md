Text Clustering <br>
Download the fine foods dataset from:
http://snap.stanford.edu/data/web-FineFoods.html
Perform the following:
* Identify all the unique words that appear in the \review/text" eld of the reviews. Denote the set of such words as L.
* Remove from L all stopwords in \Long Stopword List" from http://www.ranks.nl/stopwords. Denote the cleaned set as W.
* Count the number of times each word in W appears among all reviews (\review/text" field) and identify the top 500 words.
* Vectorize all reviews (\review/text" eld) using these 500 words.
* Cluster the vectorized reviews into 10 clusters using k-means. You are allowed to use any program or code for k-means (Weka has k-means too). This will give you 10 centroid vectors.
* From each centroid, select the top 5 words that represent the centroid (i.e., the words with the highest feature values)
* Submit the following:
1. Top 500 words + counts for these words
2. The top 5 words representing each cluster and their feature values (50 words + 50 values).
3. IMPORTANT: your code and a step-by-step readme to help reproduce your results. We should be able to get the same results by running your code and by following your readme for this problem to get graded.
