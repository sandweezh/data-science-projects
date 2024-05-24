# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4

## Introduction

Welcome to your first week of work at the Disease And Treatment Agency, division of Societal Cures In Epidemiology and New Creative Engineering (DATA-SCIENCE). Time to get to work!

Due to the recent epidemic of West Nile Virus in the Windy City, we've had the Department of Public Health set up a surveillance and control system. We're hoping it will let us learn something from the mosquito population as we collect data over time. Pesticides are a necessary evil in the fight for public health and safety, not to mention expensive! We need to derive an effective plan to deploy pesticides throughout the city, and that is **exactly** where you come in!

## Dataset

The dataset, along with description, can be found here: [https://www.kaggle.com/c/predict-west-nile-virus/](https://www.kaggle.com/c/predict-west-nile-virus/).

**This is also where you will be submitting your code for evaluation**. We will be using the Kaggle Leaderboard to keep track of your score. The public leaderboard uses roughly 30% of the dataset to score an AUC (Area Under Curve) metric.

> If you do not already have a Kaggle account, you will need to sign up on the website.  Also note that you will be submitting a "Late Submission" on Kaggle because the official competition has ended.  You can use the leaderboard to see how your results compare against roughly 1300 other data science teams!

You can submit predictions as many times as you want to Kaggle, but there is a limit of 5 submissions per day.  Be intentional with your submissions!


#### Navigating Group Work

This project will be executed as a group.  To make your team as effective and efficient as possible you should do the create a shared GitHub repo and project planning document as described in the deliverables section below.

## Deliverables

**GitHub Repo**

1. Create a GitHub repository for the group. Each member should be added as a contributor.
2. Retrieve the dataset and upload it into a directory named `assets`.
3. Generate a .py or .ipynb file that imports the available data.

**Project Planning**

1. Define your deliverable - what is the end result?
2. Break that deliverable up into its components, and then go further down the rabbit hole until you have actionable items. Document these using a project managment tool to track things getting done.  The tool you use is up to you; it could be Trello, a spreadsheet, GitHub issues, etc.
3. Begin deciding priorities for each task. These are subject to change, but it's good to get an initial consensus. Order these priorities however you would like.
4. You planning documentation (or a link to it) should be included in your GitHub repo.

**EDA**

1. Describe the data. What does it represent? What types are present? What does each data points' distribution look like? Discuss these questions, and your own, with your partners. Document your conclusions.
2. What kind of cleaning is needed? Document any potential issues that will need to be resolved.

**Note:** As you know, EDA is the single most important part of data science. This is where you should be spending most of your time. Knowing your data, and understanding the status of its integrity, is what makes or breaks a project.

**Modeling**

1. The goal is of course to build a model and make predictions that the city of Chicago can use when it decides where to spray pesticides! Your team should have a clean Jupyter Notebook that shows your EDA process, your modeling and predictions.
2. Conduct a cost-benefit analysis. This should include annual cost projections for various levels of pesticide coverage (cost) and the effect of these various levels of pesticide coverage (benefit). *(Hint: How would we quantify the benefit of pesticide spraying? To get "maximum benefit," what does that look like and how much does that cost? What if we cover less and therefore get a lower level of benefit?)*
3. Your final submission CSV should be in your GitHub repo.

**Presentation**
* Audience: You are presenting to members of the CDC. Some members of the audience will be biostatisticians and epidemiologists who will understand your models and metrics and will want more information. Others will be decision-makers, focusing almost exclusively on your cost-benefit analysis. Your job is to convince both groups of the best course of action in the same meeting and be able to answer questions that either group may ask.
* The length of your presentation should not exceed 25 minutes (a rough guideline: 3 minute intro, 12 minutes on model, 5 minutes on cost-benefit analysis, 5 minutes on recommendations/conclusion).


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