# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4

## Introduction

For this project, you will be doing work that focuses on social impact.

The prompts are there to help jump-start your ideation process. If you would like to change or combine prompts, that's fine! If you want to find your own idea, even better. **Consult your assigned TA or Instructor for final approval before getting started.**  

Remember to start with a good problem statement!

## The Data

Some prompts have links to data sources, some don't. It's your responsibility to gather and clean your data. For most projects, this will be the bulk of your work.Start early!

Inspiration for several prompts came from [Data is Plural](https://tinyletter.com/data-is-plural).

## Prompts

### Aviation Accidents

The National Transportation Safety Board (NTSB) [tracks](https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx) all civilian aviation accidents (and "incidents") going back to 1962.

### Center for Disease Control

The Center for Disease Control has several datasets:
- [Vaccinations](https://data.cdc.gov/browse?category=Vaccinations)
- [Smoking and Tobacco Use](https://data.cdc.gov/browse?category=Smoking+%26+Tobacco+Use)
- [COVID-19](https://data.cdc.gov/browse?tags=covid-19)

### Economic Data

If you're interested in a project focused on the economy, the Bureau of Labor Statistics (BLS) has [several datasets](https://www.bls.gov/data/) ranging from employment to inflation.

### Voter Fraud (or lack thereof)
The Brookings Institute had an [interesting article](https://www.brookings.edu/blog/fixgov/2020/06/02/low-rates-of-fraud-in-vote-by-mail-states-show-the-benefits-outweigh-the-risks/) on voter fraud. Although no datasets are provided, there are several links to sources where you might be able to find some.

### Incarceration

The United States Sentencing Commission (USSC) has [data](https://www.ussc.gov/research/datafiles/commission-datafiles) on federal sentencing going back to 2002.

### Environment

The EPA has data on [air quality](https://cfpub.epa.gov/airnow/index.cfm?action=airnow.main), [precipitation](https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid={BDD5DD12-4942-41A6-B47D-9C2459F28A0A}), [stream flows](https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid={0599E344-4682-479D-9334-78FE576E2881}) [and more](https://edg.epa.gov/metadata/catalog/main/home.page).

### Protests

[The Mass Mobilization Project](https://massmobilization.github.io/) provides data on demonstrations worldwide, as well as the government responses.

### Charity

[Data.world](https://data.world/datasets/charity) has several datasets related to altruism: donations, organizations, and volunteerism. 

### CTE

Chronic Traumatic Encephalopathy (CTE) is a horrific brain disease, and occurs [frequently](http://www.bu.edu/articles/2017/cte-former-nfl-players/) in former NFL players. Gathering the data will take some work, but here are some starter links.
- [Kaggle](https://www.kaggle.com/jpmiller/nfl-competition-data)
- [Twelve Years of National Football League Concussion Data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3438866/)

### Politics
FiveThiryEight is a great news and commentary site for all things data. Their main foci are sports and politics. If you're interested in polling data, check out the "Data" links in the footer on [this page](https://projects.fivethirtyeight.com/2020-election-forecast/).

### Consumer Complaints

The Consumer Financial Protection Bureau maintains a [dataset](https://www.consumerfinance.gov/data-research/consumer-complaints/) on customer complaints to various financial organizations in the US.

### Professional Athletes

For this prompt, choose a professional sport and compare the distribution of birth months vs the US population. [Sports Reference](https://www.sports-reference.com/) is a good resource for men's and women's sports.

h/t [Malcolm Gladwell](https://youtu.be/kspphGOjApk?t=148)

### SEC

The Securities and Exchange Commission (SEC) is the go-to for [financial data](https://www.sec.gov/edgar/searchedgar/companysearch.html) on US publicly traded companies. The also have [press releases](https://www.sec.gov/litigation/litreleases.shtml) that pertain to various violations.

### US Treasury

The US Treasury Department has several datasets related to public debt. The [yield curve](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield) is a key indicator of economic health. They also maintain data on the sale of [securities](https://www.treasurydirect.gov/instit/annceresult/annceresult.htm).

They also have [auction data](https://home.treasury.gov/services/treasury-auctions) for items that are seized by the IRS.

### Federal Reserve

The Fed has a wide variety of [datasets](https://www.federalreserve.gov/datadownload/) related to the economy and financial markets.

### Still stuck?

Check out [/r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/), [Data.world](https://data.world/) and [Kaggle](https://www.kaggle.com/datasets) for inspiration.

## Requirements
For the purposes of a DSI project, you must meet a few technical requirements. They are:
1)  A `README.md` file in your project repo. Note that `README` files are automatically rendered by GitHub when you view a repo. Your README should contain:
    - A problem statement.
    - A succinct formulation of the question your analysis seeks to answer.
    - A table of contents, which should indicate which notebook or scripts a stakeholder should start with, and a link to an **executive summary**.
    - A paragraph description of the data you used, plus your data acquisition, ingestion, and cleaning steps.
    - A short description of software requirements (e.g., `Pandas`, `Scikit-learn`) required by your analysis.

2) Your notebook(s) should be **reproducible** and **error-free**. This means:
    - You should set a random seed at the start of every notebook. This will ensure that the random numbers generated in your notebook will be the same every time.
    - You need to provide a _relative path_ to your data, so that if I clone your repo to my machine I can run everything in your repo without error. (You also provide links to any publicly accessible data.)
    - Instructional team should be able to `Restart & Run All` in your notebook(s) and see that the _exact same_ results are reproduced.
    - To check that everything worked properly, you may consider forking your own repo to a different location on your computer and checking that all notebooks can run properly from top to bottom.

3) Bear in mind that the value you provide may come from data ingestion, data cleaning, EDA, and/ or a dashboard, etc. While a model may not be immediately apparent, be creative. *Without us telling you exactly what model to build, how could you build a model to increase performance or generate better insights when answering the problem you are facing?*


### Teams

Your local instructor will divide your class into teams. Chat with them to find out!

---

### Presentations

Each group will present their findings.

Your presentation must include:
- A summary of the problem you tackled.
- A walkthrough of how you set out to solve the problem.
- A demonstration of your solution. (i.e. You may demonstrate an app you developed, an example of how a model may be used, etc.)
- A summary of any models you fit and, if applicable, their performance.
- A brief discussion of limitations to your process. (i.e. data collection issues, missing values)
- A brief discussion of next steps.

Presentation requirements:
- A short presentation outlining your process and findings for a semi-technical audience.
- The length of your presentation should not exceed 25 minutes (a rough guideline: 3 minute intro, 12 minutes on model, 5 minutes on cost-benefit analysis, 5 minutes on recommendations/conclusion)
- Your presentation must include slides. (Google Slides, PowerPoint, Keynote, etc.)
- Use visuals that are appropriately scaled and interpretable.
- Make sure you provide clear conclusions/recommendations that follow logically from your analyses and narrative and answer your data science problem.

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