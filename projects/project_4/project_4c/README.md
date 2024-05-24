# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Predict Dengue Cases

## Introduction

You have just graduated from General Assembly Data Science Immersive program and managed to secure an interview with the National environmental Agency (NEA). You have been assigned into a group with other interviewees and were given a take home test. You will be required to work together and present as a group during the interview. Time to look at the test!

[Dengue fever](https://www.healthhub.sg/a-z/diseases-and-conditions/192/topic_dengue_fever_MOH) is spread though the bite of the Aedes mosquito. To prevent dengue fever, one must prevent the breeding of the Aedes mosquitoes. Aedes mosquitoes are identified by the black and white stripes on their bodies. It prefers to breed in clean, stagnant water easily found in our homes. You can get rid of the Aedes mosquito by frequently checking and removing stagnant water in your premises. The NEA has a stringent B-L-O-C-K **STOP Dengue Now** campaign.

In this exercise, you are required to predict Dengue Cases in Singapore. You will be using data of two potential predictors for dengue:

1. Weather information: Rainfall and temperature patterns are one of the main drivers of dengue transmission as mosquitoes require standing water to reproduce

2. Google trends: Search terms containing ‘dengue’ have been successfully used to predict dengue cases in a number of countries. This is probably because those who are more susceptible to the virus, are also more likely to be googling about it


## Dataset

You will have to curate your dataset from: 
1. http://www.weather.gov.sg/climate-historical-daily/
2. https://data.gov.sg/dataset/weekly-number-of-dengue-and-dengue-haemorrhagic-fever-cases (Currently has weekly number of cases from 2014 to 2018)
3. https://trends.google.com/trends/explore?date=today%205-y&geo=SG&q=%2Fm%2F09wsg


#### Navigating Group Work

This project will be executed as a group. To make your team as effective and efficient as possible you should create a shared GitHub repo and project planning document as described in the deliverables section below.

## Deliverables

**GitHub Repo**

1. Create a GitHub repository for the group. Each member should be added as a contributor.
2. Retrieve the dataset and upload it into a directory named `assets`.
3. Generate a .py or .ipynb file that imports the available data.

**Project Planning**

1. Define your deliverable - what is the end result?

**EDA**

1. Describe the data. What does it represent? What data types are present? What does each data points' distribution look like? Discuss these questions, and your own, with your partners. Document your conclusions.
2. What kind of cleaning is needed? Document any potential issues that will need to be resolved.

**Note:** As you know, EDA is the single most important part of data science. This is where you should be spending most of your time. Knowing your data, and understanding the status of its integrity, is what makes or breaks a project.

**Modeling**

1. The goal is of course to build a model and make predictions that NEA can use to know the number of dengue cases and trends in the subsequent period (duration to be determined by student). Your team should have a clean Jupyter Notebook that shows your EDA process, your modeling and predictions.
2. Conduct a cost-benefit analysis. This should include annual cost projections for dengue prevention programme (e.g. Project Wolbachia) and the effect of such programme. *(Hint: How would we quantify the benefit of programme? To get "maximum benefit," what does that look like and how much does that cost?)*

**Presentation**
* Audience: You are presenting to interviewers from the data science department. Some members of the audience will be data scientists, biostatisticians and epidemiologists who will understand your models and metrics and will want more information. Others will be decision-makers, focusing almost exclusively on your cost-benefit analysis. Your job as a group is to convince both groups of the best course of action in the same meeting and be able to answer questions that either group may ask.
* The length of your interview should be about 15 minutes (a rough guideline: 1 minute intro, 5 minutes on model, 2 minutes on cost-benefit analysis, 2 minute recommendations/conclusion, 5 minute QnA).  

---

**Your project due date is as specified by the instructional team**

---

## Rubric
Teaching team will evaluate your project using the following criteria.  You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below while working through your project.

**Note:** Presentation will be done as a group while codes will be prepared and submitted by each student.

For Project 4 the evaluation categories are as follows:<br>

**The Data Science Process**
- Problem Statement
- Organization
- Data Structures
- Python Syntax & Control Flow
- Probability & Statistics
- Modeling
- Presentation
- Conclusion and Recommendations

**Project will be evaluated on the three levels as below for each item in the rubric.** <br>

| Evaluation Criteria |
| ----- |
| *Below expectations* |
| *Meets expectations* |
| *Exceeds expectations* |


### The Data Science Process

**Problem Statement**
- Is it clear what the goal of the project is?
- What type of model will be developed?
- How will success be evaluated?
- Is the scope of the project appropriate?
- Is it clear who cares about this or why this is important to investigate?

**Organization**
- Does the notebook have a clear structure?
- Does the notebook have a title and appropriate sectioning?
- Are the notebook comments clear and informative?
- Are assumptions both stated and justified?

**Data Structures**
- Are data structures created and used correctly?
- Are data structures used appropriately and within context of the problem?
- Do data structures follow Python and programming best practices?

**Python Syntax and Control Flow**
- Is the code well-formed and organized?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follow general best practices and style guidelines?

**Probability and Statistics**
- Is there a clear understanding of how probability and statistics affects the analysis being performed?
- Are descriptive statistics calculated in all relevant situations?
- Are inferential statistics calculated in all relevant situations?
- Are probabilities and statistics relevant to the analysis?
- Are probabilities and statistics used to draw meaningful or insightful conclusions?

**Modeling**
- Is the model choice appropriate to the analysis?
- Are the model hyperparameters optimally selected?
- Is the data free from nulls and correctly typed for the given model?
- Are the model results extracted and explianed visually, numerically, or narratively?
- Does the model evaluation reflect generalizeable performance?

**Conclusion and Recommendations**
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Is it clear how the final recommendations were reached?
- Are the conclusions/recommendations clearly stated?
- Does the conclusion answer the original problem statement?
- Does the student address how findings of this research can be applied for the benefit of stakeholders?
- Are future steps to move the project forward identified?

**Presentation**
- Was the presentation given within the alloted timeframe?
- Is the problem framed appropriately for the audience?
- Is the level of technicailty appropriate for the target audience?
- Did the speaker's voice have volume and clarity?
- Are the presentation's visuals helpful and supportive of the problem statement?


*In order to pass the project, students must earn a minimum score of 'Meets Expectations' for each section*.
- Earning a *'Below Expectations'* in one or more of the above section would result in a failing project.
- Sections evaluated to be *'Below Expectations'* will be accompanied with instructor comments.
- While a minimum of *'Meets Expectations'* in each section is the required threshold for graduation, students should aim to score higher. While it may be passing, students may want to solicit specific feedback in order to significantly improve the project before showcasing it as part of a portfolio or the job search.