In this problem, you will analyze the review contents from Amazon Product Data provided by Julian
McAuley at http://jmcauley.ucsd.edu/data/amazon/ . This dataset contains product reviews and metadata
from Amazon, including 142.8 million reviews spanning May 1996 – July 2014. It includes reviews
(ratings, text, helpfulness votes), product metadata (descriptions, category information, price, brand, and
image features), and links (also viewed/also bought graphs).

For our tasks, we will use only 5-core subsets of Baby category. 5-core subsets mean that all users and items in the dataset have at least 5
reviews. 

Data Pre-processing 
You will write a Python code that extracts only review texts. Please submit the sample screenshot of the
output (included in your report file).

Sentiment Analysis 
Based on what we have learned from this class, you will explore the sentiment of the comments at the
sentence level. This includes how to process the words and how to conduct the sentiment analysis using
classifiers. Ultimately, you will provide two lists of sentences: one is marked as negative and the other as
positive.

In your report, please explain in detail the processing techniques that you have applied, the features you
used for the classification task, and your experiments. For the data preprocessing/cleaning task, we have
learned about several techniques such as tokenization, sentence creation, regular expression processing,
stop word filtering, etc. You should describe the techniques you used in this assignment.

For the classification task and the experiments, you should start with the “bag-of-words” features where
you collect all the words in the sentence_polarity corpus and select some number of most frequent words
to be the word features. You should use at least NaiveBayes classifier to train and test a classifier on your
feature sets. If possible, i.e., if time and space permit, you should use cross-validation to obtain precision,
recall, and F-measure scores. In your experiments, you should use at least two different sets of features and compare the results. For example, you may take the unigram word features as a baseline and see if the
features you designed improve the accuracy of the classification. Here are some of the types of
experiments that we have done so far:
• _Filter by stop words or other pre-processing methods
• _Representing negation
• _Using a sentiment lexicon with scores or counts: Subjectivity
