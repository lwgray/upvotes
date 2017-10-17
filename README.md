What does it do?
-------------------
Say you wanted to submit a post on reddit and you wanted a lot of people to like it.  

I believe that the title of your post(I think you would agree) is important in determining how many upvotes(likes) you will receive.  


Where did this idea come from?
------------------------------
This idea was partially fleshed out at [hackumbc](http://hackumbc.org) with a prototype hosted [here](http://http://54.197.149.55) ***IMPORTANT*** Just enter in "Title". Do not enter "subreddit" [Read more about how this project came together](https://devpost.com/software/calzone-trhmwb)

So how did you do it?
---------------------
To explore this idea, I turned to Machine learning to predict how many upvotes you would get based on your post's title.  I have built a simple Machine learning model with python using mainly scikit-learn package.  The model is currently trained on 38,000 posts from /r/politics subreddit.  

The  workflow is a simple 2-step process.  I first apply Tf-idf vectorizer.  This performs word tokenizing, n-grams, and idf.  Secondly, I fit with Ridge Linear Regression to predict the upvotes.

Take a look at the Code
-----------------------
code in upvotes.ipynb

What is the problem?
--------------------
This method alone doesn't provide a great prediction.  I want to add in new features but I am not sure how to.  I think adding in the following would improve the prediction.
    
    1. Length of title (maybe shorter titles are better???)
    2. How old is the post? ( I would think that the older the post the more the upvotes)

Technically, how do I do this?   HELP ME.. post an issue
