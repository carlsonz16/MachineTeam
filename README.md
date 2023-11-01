# Senior Design Project - Final Report

## Our Team - Machine Team
*Zach Carlson, Jake D'Amico, Sean Tarbuck, Rylee Charlton*

*Project Advisor - Dr. Fred Annexstein*

### Project Abstract
The sports betting market has seen rapid expansion due to the increased legalization of betting in multiple regions. This growth has been fueled by the emergence of online platforms, advanced technologies, and the widespread adoption of mobile betting applications. Leveraging algorithms that incorporate data from credible sources, sports betting websites provide users with a competitive edge. This approach facilitates well-informed betting decisions based on reliable information, leading to heightened prediction accuracy, increased success rates, and potentially greater profits. Furthermore, the use of trustworthy sources ensures data reliability, fostering user trust and transparency. Consequently, this integration of advanced algorithms and credible data contributes to a more sophisticated and reliable betting experience for enthusiasts.


## Project Description
Our project aims to delve deep into the realm of Machine Learning and Artificial Intelligence using Python. Our primary objective is to create a machine-learned model that can analyze sports statistics and generate predictions. These predictions will be utilized to develop a website where users can retrieve these predictions to influence future bets. The project emphasizes both achieving practical results and the educational journey of gaining a comprehensive understanding of Machine Learning and AI.


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


## Project Tasks and Timeline
### Task List
1. Research the current state of sports prediction methodologies and tools. ***- All members***
2. Specify the sports events we would like to focus on. ***- Zach***
3. Investigate potential datasets and APIs related to our selected sports events.  ***- Zach, Sean***
4. Collect data for past games, including features like teams, players, scores, and other relevant statistics. ***- Zach, Sean***
5. Design an initial model architecture for the sports predictions. ***- All members***
6. Develop a prototype model using relevant ML libraries (TensorFlow, PyTorch, Scikit-learn, etc.) ***- Zach, Jake***
7. Develop and conduct tests for the model to gauge performance, both back and forward testing, to refine the model. ***- Zach***
8. Develop a schema to store data used for our model efficiently. ***- All members***
9. Design the web app UI/UX and decide on a framework (React, Vue, Angular, etc.). ***- All members***
10. Develop the necessary front-end components for the website.***- All members***
11. Integrate the ML model into the site's backend to display predictions (Flask, Django etc.)  ***- Zach, Jake***
12. Create meaningful features that can contribute to prediction accuracy (e.g., team rankings, player statistics). ***- All members***
13. Implement any needed database solutions, if any. ***- All members***
14. Document program architecture (including machine learning model specifics and data pipeline specifics). ***- Rylee, Jake***
15. Write comprehensive front-end and developer documentation. ***- Rylee***
16. Develop and run tests for the web application to ensure we are alerted when functionalities break. ***- Zach***
17. Configure recovery solutions for site downtime. 
18. Refine the UI/UX based on user feedback. ***- Sean***
19. Deploy the web app to a suitable hosting platform/service. ***- Sean***


### Milestones List 
1. **Research (Milestone):**
   - **Project Deliverable:** Research findings and summaries.
   - **Explanation:** This milestone involves researching the current state of sports prediction methodologies and tools. All team members contribute to gathering information about existing approaches and technologies in the field.

2. **Machine Learning Research (Milestone):**
   - **Project Deliverable:** Report on the compatibility and potential use of different Machine Learning libraries with Python.
   - **Explanation:** Sean will complete research on the use of Machine Learning with Python, which will be used to create our models.

3. **Sports Selection Defined (Milestone):**
   - **Project Deliverable:** Document specifying the sports events to focus on.
   - **Explanation:** Zach leads the effort to narrow down the scope by selecting specific sports events that our program will target, ensuring a clear direction for data collection and modeling.

4. **Data Sources Identified (Milestone):**
   - **Project Deliverable:** List of potential datasets and APIs.
   - **Explanation:** Zach and Sean collaborate to identify relevant data sources, such as APIs and datasets, that can be used to collect historical sports data for modeling.

5. **Data Collection and Initial Model Design (Milestone):**
   - **Project Deliverable:** Initial dataset collected and documented model architecture.
   - **Explanation:** This milestone involves collecting initial data and designing the initial model architecture. All members contribute to the high-level design.

6. **Prototype Model Development (Milestone):**
   - **Project Deliverable:** Functional prototype of the prediction model.
   - **Explanation:** Zach and Jake work together to develop a functional prototype of the machine learning model using appropriate libraries.

7. **Testing and Model Refinement (Milestone):**
   - **Project Deliverable:** Test results and refined model.
   - **Explanation:** Zach conducts comprehensive testing of the model, both backward and forward testing, to refine its performance and accuracy.

8. **Data Schema and UI/UX Design (Milestone):**
   - **Project Deliverable:** Data schema and UI/UX design concepts.
   - **Explanation:** The team collaborates to design the data schema for efficient data storage and the user interface/user experience (UI/UX) for the web application.

9. **Front-End Development (Milestone):**
   - **Project Deliverable:** Developed front-end components.
   - **Explanation:** All members contribute to developing the necessary front-end components for the web application based on the UI/UX design.

10. **ML Model Integration (Milestone):**
    - **Project Deliverable:** Integrated Machine Learning model into the backend.
    - **Explanation:** Zach and Jake integrate the machine learning model into the web application's backend to display predictions to users.

### Project Deliverables:

11. **Feature Engineering (Deliverable):**
    - **Explanation:** All members work on creating meaningful features that can enhance the accuracy of sports predictions.

12. **Database Implementation (Deliverable):**
    - **Explanation:** The team implements any necessary database solutions to store and manage data efficiently.

13. **Documentation of Program Architecture (Deliverable):**
    - **Explanation:** Rylee and Jake document the program architecture, including specifics about the machine learning model and data pipeline.

14. **Front-End and Developer Documentation (Deliverable):**
    - **Explanation:** Rylee creates comprehensive documentation for both end-users and developers to understand and use the web application.

15. **Testing and Test Alerts (Deliverable):**
    - **Explanation:** Zach develops and runs tests for the web application to ensure that functionalities are working correctly and that issues are promptly identified.

16. **Recovery Solutions Configuration (Deliverable):**
    - **Explanation:** Configure solutions for site downtime, ensuring that the application can recover from failures.

17. **UI/UX Refinement (Deliverable):**
    - **Explanation:** Sean leads the effort to refine the user interface and user experience based on user feedback and usability testing.

18. **Web App Deployment (Deliverable):**
    - **Explanation:** Sean takes charge of deploying the web application to a suitable hosting platform or service to make it accessible to users.


### Timeline
*Assuming this semester is used as a planning semester and production will start Spring semester of 2024*
![GanttChart](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%206/gant.png)

### Effort Matrix
Here's a breakdown of the expected division of labor for each task, indicating the primary team member responsible for each task and their estimated percentage of effort or hours of effort:

| Task                                                         | Primary Responsible Member | Estimated Effort |
|--------------------------------------------------------------|-----------------------------|-------------------|
| 1. Research sports prediction methodologies and tools         | All Members                 | 10% each         |
| 2. Research Machine Learning with Python                      | Sean                        | 20%              |
| 3. Specify sports events to focus on                          | Zach                        | 10%              |
| 4. Investigate potential datasets and APIs                    | Zach, Sean                  | 25% each         |
| 5. Collect data for past games                                | Zach, Sean                  | 25% each         |
| 6. Design initial model architecture                          | All Members                 | 10% each         |
| 7. Develop prototype model with ML libraries                  | Zach, Jake                  | 30% each         |
| 8. Develop and conduct model tests for performance            | Zach                        | 15%              |
| 9. Develop a schema for efficient data storage                | All Members                 | 10% each         |
| 10. Design web app UI/UX and select a framework                | All Members                 | 10% each         |
| 12. Develop front-end components for the website              | All Members                 | 15% each         |
| 13. Integrate ML model into the site's backend                 | Zach, Jake                  | 25% each         |
| 14. Create meaningful features for prediction accuracy         | All Members                 | 10% each         |
| 15. Implement any needed database solutions                    | All Members                 | 10% each         |
| 16. Document program architecture                              | Rylee, Jake                 | 15% each         |
| 17. Write comprehensive documentation (front-end & developer)  | Rylee                       | 20%              |
| 18. Develop and run tests for the web application              | Zach                        | 15%              |
| 21. Configure recovery solutions for site downtime             | All Members                 | 10% each         |
| 22. Refine UI/UX based on user feedback                         | Sean                        | 20%              |
| 23. Deploy the web app to a hosting platform/service           | Sean                        | 20%              |


## PPT Slideshow
[Presentation](https://docs.google.com/presentation/d/18rP2mFoe99REIxquvZ4SXVQtCudlpp2a68en-eUUvq4/edit#slide=id.g290da63ae18_4_21)

## Self-Assessment Essays

## Professional Biographies

## Budget

## Appendix
