# Senior Design Project - Final Report

## Our Team - Machine Team
*Zach Carlson, Jake D'Amico, Sean Tarbuck, Rylee Charlton*

*Project Advisor - Dr. Fred Annexstein*

## Project Abstract
The sports betting market has seen rapid expansion due to the increased legalization of betting in multiple regions. This growth has been fueled by the emergence of online platforms, advanced technologies, and the widespread adoption of mobile betting applications. Leveraging algorithms that incorporate data from credible sources, sports betting websites provide users with a competitive edge. This approach facilitates well-informed betting decisions based on reliable information, leading to heightened prediction accuracy, increased success rates, and potentially greater profits. Furthermore, the use of trustworthy sources ensures data reliability, fostering user trust and transparency. Consequently, this integration of advanced algorithms and credible data contributes to a more sophisticated and reliable betting experience for enthusiasts.


## Project Description
Our project aims to delve deep into the realm of Machine Learning and Artificial Intelligence using Python. Our primary objective is to create a machine-learned model that can analyze sports statistics and generate predictions. These predictions will be utilized to develop a website where users can retrieve these predictions to influence future bets. The project emphasizes both achieving practical results and the educational journey of gaining a comprehensive understanding of Machine Learning and AI.

## User Guides
<a href="https://github.com/carlsonz16/MachineTeam/blob/main/Docs.md">User Documentation</a>

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

## Concerns
1. Legal
    - We want to be able to get the data of these teams and players from reputable sources such as ESPN and we also would like to get the betting lines from reputable sources like FanDuel or DraftKings and we are unsure the legality of pulling data from those sources. We don't know if it goes in violation of their terms and conditions and we don't want them to think we are trying to take their data to hack them at all. We need to figure out what the terms and conditions are of these sites so that we can proceed as legally as possible.
2. Financial
    - With sports betting you need to have money to sports bet. We would like to be able to test the model in a controlled envrionment such as a sportsbook but in order to bet on these sites you have to have money that you are willing to possibly lose. Being poor college students we are unsure how we will conduct this with as little money as possible.
3. Ethical
    - We think that it might not be as ethical to some of these sports betting sites if we have a model that is able to more accurately predict if we can win a bet or not. We want to explore if there is any significant negative impact on anybody for us creating this model.

## PPT Slideshow
[Presentation](https://docs.google.com/presentation/d/18rP2mFoe99REIxquvZ4SXVQtCudlpp2a68en-eUUvq4/edit#slide=id.g290da63ae18_4_21)

## Self-Assessment Essays
- [Rylee](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/Charltrj_Assignment3.md)
- [Zach](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/Individual%20Assessment%20Zach%20Carlson)
- [Sean](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/Assignment%203%20-%20Sean%20Tarbuck.md)
- [Jake](https://github.com/carlsonz16/MachineTeam/blob/main/HomeworkEssays/Assignment%203/D'Amico%20IndvCapstone.md)
## Professional Biographies
### Jake D'Amico 
**Co-Op Experience**

- Worked three semesters with a team at Siemens doing mostly frontend but some backend web development.
- Primarily used Angular, JavaScript, and C#.
- Also spent a semester with the same team developing performance tests for new site functionalities and the framework for exporting those results to SQL with C# and Selenium.

**Major Skills**

- JavaScript, Python, C#, C/C++, HTML, CSS, Angular, SQL

**Interests/Projects I'd Like to Pursue**

- The use of 3D JavaScript libraries such as three.js to create web experiences
- Physics engines with C++
- Python Machine Learning, specific image/sound recognition
- Sound-based authentication systems
- Progressive Web Apps

  
### Sean Tarbuck
**About**

My name is Sean Tarbuck and I am currently a 5th year student studying computer science at the University of Cincinnati. 

**Contact**

Email: Tarbucsm@mail.uc.edu

**Co-op Experience**
1. Sites & Document Management Co - op - Lubrizol
  - May 2023 - August 2023
  - Honed many critical development skills including: PowerShell, PNP, Nintex, REST, Graph
  - Responsible for developing a user access and permissions application 
2. OT & Lab Services Co - op - Lubrizol	        
  - August 2022 - December 2022
  - Demonstrated strong leadership when facilitating cyber security-oriented tabletop exercises to promote increased awareness and preparedness for cyber-related emergencies
  - Fostered open communication and collaboration among team members to build readiness during cyber-related emergencies
  - Provided recommendations for cyber security-related emergency response processes and procedures that contributed to the development of a comprehensive and effective cyber security program
3. Media and Technology Co - op - Lubrizol			
  - January 2022 - April 2022
  - Implemented and led organizational improvements for a global communication display software
  - Proficiently used Microsoft Platform tools to assist in the development of Media Center projects and tasks
4. Hybrid Data Centers Co - op - Lubrizol        	                                              
  - May 2021 - August 2021
  - Responsible for the development of data center monitoring interfaces and tools using SolarWinds for quicker, more effective responses to incidents, and overall analysis of data center health
  - Responsible for planning, organizing, and executing in place server upgrades for all print servers
5. Cybersecurity Analyst Co - op - Lubrizol        	                      
  - August 2020 - December 2020
  - Maintained the security of data and information through active management of provided security tools 
  - Efficiently used security technologies such as O365, Trustwave, XSOAR, ThreatGrid, and Proofpoint
  - Assisted with the development of processes and procedures to improve incident response times and overall SOC functions

**Areas of Interest / Project Sought**

I currently do not have an exact idea what I would like to create for my senior design project, however, some potential areas of interest include: 
  - Cloud
  - Machine Learning 
  - Artificial Intelligence


    
### Zach Carlson
**About**

My name is Zach Carlson, and I am a 5th year Computer Science student at the University of Cincinnati. My main passions associated with computer science are Artificial Intelligence, algorithms, software development, and web development. 

**Contact**

My email address is carlsozl@mail.uc.edu 

**Co-op Experience**

1.	American Cutting Edge
    -	Worked from August 2020 – December 2020
    -	IT Intern
    -	Derived a Price Analysis, executed inventory management in the backend of the website organized containers for an on-going company warehouse move, and also constructed numerous monthly reports.
2.	American Cutting Edge
    -	Worked from May 2021 – August 2021
    -	IT Intern
    -	Led inventory consolidation, executed creation of part numbers, Worked on Front-end Development for a new company website.
3.	Siemens
    -	Worked from January 2022 – May 2022
    -	Strategic Student Program Software Development Co-Op
    -	Worked as a Web Developer using JavaScript, AngularJS, and HTML on Siemens created website called Solution Link.
4.	Siemens
    -	Worked from August 2022 – December 2022
    -	Strategic Student Program Software Development Co-Op
    -	Worked as web developer using HTML, JavaScript, AngularJs, C#, and SQL on a company website called Solution Link. Coded new filters and tabs for numerous pages. Changed titles in HTML to constants to maintain reusability.
5.	Siemens
    -	Worked from May 2023 – August 2023 
    -	Strategic Student Program Software Development Co-Op
    -	Developed and deployed new features for company website Solution Link using HTML, CSS, JavaScript, Angular JS and C#. Fixed numerous website bugs, improved frontend and backend website development skills.

**Projects Sought**

I currently don’t have a clear grasp as to what I would like to create for my Senior Design Project. I have a couple of ideas, but I am not set on one yet.
-	Artificial Intelligence Model
-	Machine Learning Data Model
-	Website 
-	Stock Prediction Model
-	Sports Prediction Model
-	Artificial Intelligence Video Game


### Rylee Charlton
**Contact information**

Rylee Charlton

charltrj@mail.uc.edu

**Co-op Work Experience**

Internal Computer Support InternSchneider Downs Inc,, *May 2021-Present (7 semesters)*
- Configure and monitor servers, backups, and cloud infrastructure.
- Research and resolve daily alerts associated with servers, backups, and cloud infrastructure.
- Configure, maintain, and monitor Microsoft Windows servers and VMware in a network environment.
- Assist with the management of the network environment including VPN and other network communication devices.
- Implement infrastructure security best practices and policies.
- Administration of Active Directory, Group Policy, Office 365 (including Exchange), VDI, Azure, and other cloud offerings.
- Lead and/or assist with network and systems implementations, upgrades, and maintenance.
- Create documentation, training materials, and videos.

**Skills**

- Programming: C++, Python, Java
- Active Directory, Group Policy, Office 365, Exchange Hybrid, VMware Horizon, and Azure
- Windows/Linux environment

**Areas of Interest**

- Systems Administration/Network Configuration
- Security Data Analysis 
- Cloud Computing
  
**Project Sought**

- Possible Android Application (Friend finder based on user preferences)
- Possible relation to co-op

  
## Budget
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
