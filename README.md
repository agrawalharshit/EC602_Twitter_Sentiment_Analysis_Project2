# EC602_Twitter_Sentiment_Analysis_Project2
Twitter Data Analysis: Use Twitter data for sentiment analysis. Identify the tweets which are hate tweets and which are not. 

This program is written in Python3 and using (Tweepy, TextBlob) library to do analysis. 

It is often argued, if machines can understand emotions or sentiments like humans do. \
...Is it possible to build a programme, which can justify the sentiments just by analysing a piece of text? \
...Is it possible to know whether the content at hand is positive, negative or neutral? **Yes it is!** 

A method of **Opinion Mining**, often referred to as Sentiment Analysis to extract sentiments by using classification algorithms. Sentiment analysis refers to the task of natural language processing to determine whether a piece of text contains some subjective information and what subjective information it expresses, i.e., whether the attitude behind this text is positive, negative or neutral. Understanding the opinions behind user-generated content automatically is of great help for commercial and political use, among others. The task can be conducted on different levels, classifying the polarity of words, sentences or entire documents.

In our approach, Tweepy API for python was used to extract tweets from Twitter Database. The basis of extraction were hashtags, which were the major highlight of twitter, the microblogging website. Using Tweepy and polarity based algorithms; we were able to actually define, the positive, negative and neutral attributes of the text, and generate a percentage wise breakup, hence performing *sentiment analysis.*

### Environmental setup steps

Step 1: Install Python
1.	Check if python is already installed on your system : `$python –version`
2.	If Python 2.7 or later is not installed, install Python with your distribution's package manager. The command and package name varies
`$sudo apt-get install python3`
3.	Check if python is now installed on your system: `$python3 –version`

Step 2: Installing API’s \
1.	Tweepy - `$sudo pip-install tweepy`

Step 3: Run the program
1. git the repository
2. run `$python twitter.py`
