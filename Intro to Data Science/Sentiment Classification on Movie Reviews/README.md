# Project Name
This project is a part of the [Intro to Data Science course](https://github.com/harper-he/Python/tree/master/Intro%20to%20Data%20Science#course-information).  Other assignments can be found at the [Intro to Data Science course repo](https://github.com/harper-he/Python/tree/master/Intro%20to%20Data%20Science).

## Project Intro/Objective
The purpose of this project is to use	Sentiment	Analysis on a	set	of movie	reviews	given	by reviewers and	
try	to	understand	what	their	overall	reaction	to	the	movie was, i.e. if	they	liked	the	movie	or	they	
hated	it.	We	aim	 to	utilize	 the	relationships	of	 the	words	in	 the	 review	 to	predict	 the overall	
polarity	of	the	review.

### Methods Used
* tokenization
* lemmatization
* Bag of words
* TF-IDF
* decision tree
* k nearest neighbors 
* Naïve Bayes
* etc.

### Technologies
* Python
* Scikit-learn 
* NLTK
* Pandas

## Project Description:
The movie reviews from amazon from [Stanford Network Analysis Project](http://snap.stanford.edu/data/web-Movies.html) website was used for this project
In the text preprocessing phrase, I removed stop words and lemmatized the review text;
In the text to features phrase, I tokenized the review text and normalize them (if necessary);
In the model training phrase, I used decision tree, k nearest neighbors and Naïve Bayes algorithms to train the model.
In the model evaluation phrase, I used cross validation method for each model and compare the accuracy, precision, recall and F1 score of them to get the best model.





