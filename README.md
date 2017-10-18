What does it do?
-------------------
Say you wanted to submit a post on reddit and you wanted a lot of people to like it.  I believe that the title of your post(I think you would agree) is important in determining how many upvotes(likes) you will receive.  This tool will do this!!!!


Where did this idea come from?
------------------------------
This idea was made concrete at [hackumbc](http://hackumbc.org) with a prototype hosted [here](http://http://54.197.149.55) ***IMPORTANT*** Only enter "Title". Do not enter "subreddit"
[Read more about how this project came together](https://devpost.com/software/calzone-trhmwb)

So how did you do it?
---------------------
To explore this idea, I turned to Machine learning to predict how many upvotes you would get based on your post's title.  I have built a simple Machine learning model with python using mainly scikit-learn package.  The model is currently trained on 38,000 posts from /r/politics subreddit.  

The  workflow is a simple 2-step process.  I first apply Tf-idf vectorizer.  This performs word tokenizing, n-grams, and idf.  Secondly, I fit with Ridge Linear Regression to predict the upvotes.

Take a look at the Code
-----------------------
Code is in upvotes.ipynb

What is the problem?
--------------------
This method alone doesn't provide a great prediction.  I want to add in new features but I am not sure how to.  I think adding in the following would improve the prediction.
    
    1. Length of title (maybe shorter titles are better???)
    2. How old is the post? ( I would think that the older the post the more the upvotes)

Technically, how do I do this?   HELP ME.. post an issue

What solutions or Suggestions have others made?
-----------------------------------------------
  1. Try the simpler problem of classifying which posts are within the top 20%
  2. Check if your data is normally distributed - Short Answer, it's not :(
  3. Add in features such as time of day, day of week, is the title a question(yes,no)
  4. Use Logistic regression for binary classification
  5. Normalize votes to a metric of votes/time 

These comments came from reddit discussions:
  1. [/r/machinelearning](https://www.reddit.com/r/MachineLearning/comments/772hik/d_i_need_help_predicting_the_number_of_subreddit/)
  2. [/r/datascience](https://www.reddit.com/r/datascience/comments/772e7q/i_need_help_predicting_the_number_of_subreddit/)
