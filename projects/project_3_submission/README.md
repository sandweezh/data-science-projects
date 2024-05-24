<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# **Project 3: Web APIs & NLP**

### Group: 5
### Name:  Gilbert Hartato / Han Kiong / Wee Zheng

### Context
---
Mental health is an increasingly serious issue in Singapore, with depression being the most common mental illness, particulary in youths. One of the leading factors in the rising trend of depression in youths is due to heavy social media usage, due to cyberbullying and a pressure to constantly present a positive self image online. Given that it is difficult to control how much time youths spend on social media, it is more effective to make use of social media instead to address the issue of rising depression rates in youths, and give them the best support possible. 

### **Problem Statement**
---
**How might we detect whether Youths are at risk of depression based on their online posts?**

Another objective of this project is to create a `NLP predictive model` to identify based on social media post, if youth is at risk of depression. The success of the model will be evaluated based on `sensitivity` score.


### **Data Dictionary**
--- 

|Feature|Type|Dataset|Description|
|---|---|---|---|
|id|*str*|depression_happy_processed|Unique ID for each post|
|author|*str*|depression_happy_processed|Represents the username of the post owner|
|score|*integer*|depression_happy_processed|The post number of posts upvotes minus downvotes|
|total comment|*float*|depression_happy_processed|Total number of comments on the reddit post |
|created_utc|*integer*|depression_happy_processed|The time stamp when the post is created in UNIX time form|
|subteddit|*str*|depression_happy_processed|Name of the subreddit where the post is extracted|
|title_and_body|*str*|depression_happy_processed|Content of the post|
|tokenize|*str*|depression_happy_processed|List of tokenized words from title_and_body|
|lemmatized|*str*|depression_happy_processed|List of lemmatized words|
|stemmed|*str*|depression_happy_processed|List of stemmed words|


### **Our Predictive Model**
--- 
**Metrics to be measured** : `Sensitivity`

**Summary of the models baseline `sensitivity` score**

||Naive Bayes|Logistic Regression|k Nearest Neighbor|
|---|---|---|---|
|CounterVectorizer|95.51%|89.13%|73.34%|
|TF-IDF|95.6%|84.56%|5.09%|

We select `Naive Bayes with TF-IDF` as our baseline model based on highest sensitivity score

**Summary of Naive Bayes with TF-IDF Model Score**

||Baseline|Hypertuned|
|---|---|---|
|train score|85.36%|83.99%|
|test score|79.99%|80.70%|
|sensitivity|95.6%|92.41%|

We select hypertuned `Naive Bayes with TF-IDF` as our model since it has the best `sensitivity` score and the model fits better than baseline 


### **Conclusion**
---

- We might identify youth at risk of depression by detecting words that indicate Depression
- The most indicative of Depression: depression, fuck, anymore
- Depression is a serious and prevalent in our society issue that needs to be addressed at a young age 
- Instead of waiting for youths to seek help, with our model, we can be more proactive in identifying those at risk of depression through observing their language.


### **Recommendations**
---

- Social Media companies can apply our predictive model when youths post online 
- Those who are then identified by our model to be at risk of suffering from depression can then be referred to support organisations (eg. Care Corner, Tinkle Friend) 


### **Future Plans**
---

- Work with MOE and apply our model to their database of students’ termly check in surveys so that schools can also take action to support the student 
- Incorporate our model into the social media platform, similar to autocorrect function which detects misspelt words
- Explore possible partnerships with search engines to do predictions based on their searches 
- Model future improvement:
    - The model may not be able to detect words in short form or slang, which are distinct to their own countries. Adding this slang words to our train datasets could further improve its metrics score.
    - The model may falsely detect sarcastic posts.