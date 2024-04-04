# Senior Design Project - Final Report

## Our Team - Machine Team
*Zach Carlson, Jake D'Amico, Sean Tarbuck, Rylee Charlton*

*Project Advisor - Dr. Fred Annexstein*

## Project Abstract
Precise Picks is an application designed to provide users with accurate player statistics and predictions to enhance their online sports betting experience. The motivation to development Precise Picks stems from the recent rapid expansion of the sports betting market. Precise Picks leverages algorithms that incorporate data from credible sources, which facilitates well-informed betting decisions based on reliable information - leading to heightened prediction accuracy, increased success rates, and potentially greater profits. 


## Project Description
Our project aims to delve deep into the realm of Machine Learning and Artificial Intelligence using Python. Our primary objective is to create a machine-learned model that can analyze sports statistics and generate predictions. These predictions will be utilized to develop a website where users can retrieve these predictions to influence future bets. The project emphasizes both achieving practical results and the educational journey of gaining a comprehensive understanding of Machine Learning and AI.

## User Guides
<a href="https://github.com/carlsonz16/MachineTeam/blob/main/Docs.md">User Documentation</a>

## Test Plan and Results
Below shows the calculated accuracy score after running the machine learning algorithm on historical data.
![Key](https://github.com/carlsonz16/MachineTeam/blob/main/accuracy_score.png)

## Final PPT Slideshow
[Presentation](https://docs.google.com/presentation/d/1xMCwyZy7SEMkv-Q0ecKcEiUa6FD0WcdxREc4oAL2rMU/edit?usp=sharing)

## User Stories and Design Diagrams
### User Stories 
- As a user, I want to be able to get accurate stats and predictions of players I wish to bet on.
- As a user, I want to see the created Artificial Intelligence preform a desired task, so that I can gauge the progress of the AI.
- As a user, I want to be able to place bets that have high percentage chance of winning.
- As a user, I want to be able to see what bets are the best bang for my buck so that I have a high probability of making money.

### Design Diagrams 
**Key:**

![Key](https://github.com/carlsonz16/MachineTeam/blob/main/Design_Diagrams/Key.png)


**D0:**
*The basic overview of the system includes input using an undefined data source of sports statistics, 
training a ML model, and outputting the results to our web UI.*

![D0](https://github.com/carlsonz16/MachineTeam/blob/main/Design_Diagrams/new%20D0.png)

**D1:**
*D0 is expanded upon by defining multiple statistics sources as well as introducing a data preprocessing 
phase. To expand on the ML model, the test dataset is introduced which we will use to prove the validity 
of the model. We also introduce some of the possible web components we can create to allow users to 
view results easily.*

![D1](https://github.com/carlsonz16/MachineTeam/blob/main/Design_Diagrams/new%20D1.png)


**D2:**
*We again expand on D1 by specifically defining where the statistics could possibly come from, including 
known APIs as well as web scraping. The data preprocessing step is split to a data cleaning and then a 
data splitting phase, which will be used to generate the test dataset. The test dataset will be used to 
make sure the model is providing results up to our standard. After the data is serialized for storage and is sent to the database as well as our web components, which we currently assume we will use React*
![D2](https://github.com/carlsonz16/MachineTeam/blob/main/Design_Diagrams/new%20D2.png)



## Expo Poster

![Key](https://github.com/carlsonz16/MachineTeam/blob/main/PrecisePicks%20-%20Expo%20Poster.png)

## Self-Assessment Essays
### Initial:
- [Rylee](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/Charltrj_Assignment3.md)
- [Zach](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/Individual%20Assessment%20Zach%20Carlson)
- [Sean](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/Assignment%203%20-%20Sean%20Tarbuck.md)
- [Jake](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/D'Amico%20IndvCapstone.md)

### Final:

## Summary of Hours and Justification

### Zach Carlson ~(118 hours)
- Web-scraping algorithm for historical NBA stats from basketball-references.com took around 10 hours to get all the data from the 2016-2024 season. (10)
- After each season was obtained, another algorithm was ran to get the individual game scores. There are 2,460 games played per season so 22,140 individual games were scraped taking around 50 hours (around 6 hours per season). (50)
- After data was obtained from the web-scraping algorithm, a parsing algorithm was ran to get a csv that had all the data for the machine learned algorithm which took around 10 hours to parse all the data in a correct format. (10)
- The Machine learned algorithm was ran off the csv from the parsed data algorithm which took around 1 hour to run. (1)
- 4 hours was spent getting the future predictions based on the machine learned data. (4)
- Estimated 30 hours debugging. (30)
- Added in the betting odds for each game. After debugging and implementation around 3 hours were spent. (3)
- Miscellaneous website additions made totalling 10 hours. (10)  
### Sean Tarbuck
### Jake D'Amico
### Rylee Charlton
| Task                                                                                                                | Time Spent | Notes on findings                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Conduct research on various methodologies and tools commonly used in sports prediction, focusing on techniques specific to NBA game prediction. | 2          | Researched different APIs that were free to use to get historical data from previous NBA games                                       |
| Create wireframes and design the user interface and user experience for the web application. Select a suitable front-end framework for development. | 7          | Decided to use React as framework. Spent lots of time researching React and different tools to use alongside with the main react framework (Tailwinds CSS, MaterialWinds) |
| Develop front-end components for the website: Home, About, PlayerStats pages                                        | 10         | Configured design of webpage using different MaterialWinds CSS addins                                                                 |
| Created a way for team icons to display when referring to teams                                                    | 3          |                                                                                                                                        |
| Integrate Historical Data API                                                                                      | 5          | Spent time integrating the selected API for accessing historical NBA game data into the front-end application. Specifically, the player data and the formatting of that. |
| Weekly Team Meeting                                                                                               | 28         | Weekly meeting with team                                                                                                               |


## Summary of Expenses
- Currently no expenses since we are trying to find APIs that are free for public use.

## Appendix
**APIs**
- https://the-odds-api.com/
- https://rapidapi.com/api-sports/api/api-nba
- https://www.cloudbet.com/api/
- https://app.balldontlie.io/explore
  
**Watched Videos**
- https://www.youtube.com/watch?v=i_LwzRVP7bg&ab_channel=freeCodeCamp.org
- https://www.youtube.com/watch?v=7eh4d6sabA0&ab_channel=ProgrammingwithMosh
- https://www.youtube.com/watch?v=IDthta5sUGQ&pp=ygUlc3BvcnRzIGJldHRpbmcgbWFjaGluZSBsZWFybmluZyBtb2RlbA%3D%3D&ab_channel=SirajRaval

Meetings were held every week for at least 2 hours as per our team contract.
