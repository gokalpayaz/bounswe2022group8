# Group 8 - Milestone 3 - Group Review

### Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [A Summary of work performed by each team member](#2-summary-of-work)
3. [Status of deliverables of Milestone 3](#3-status-of-deliverables)
4. [Progress according to requirements](#4-progress-according-to-requirements)
5. [API Endpoints](#5-api-endpoints)
6. [User Interface / User Experience](#6-user-interface-and-user-experience)
7. [Annotations](#7-annotations)
8. [Standards](#8-standards)
9. [Individual Reports](#9-individual-reports)
10. [Final Release Notes](#10-final-release-notes)
11. [System Manual](#11-system-manual)


**Important:** 
* Final deployment tagged version link: https://github.com/bounswe/bounswe2022group8/releases/tag/customer-presentation-3
* [Project Plan](https://github.com/bounswe/bounswe2022group8/wiki/CmpE-451-Project-Plan)
* [Requirements](https://github.com/bounswe/bounswe2022group8/wiki/Requirements)
* [Use Case Diagram](https://github.com/bounswe/bounswe2022group8/wiki/Use-case-diagram)
* [Sequence Diagram](https://github.com/bounswe/bounswe2022group8/wiki/Sequence-Diagrams)
* [Class Diagram](https://github.com/bounswe/bounswe2022group8/wiki/Class-Diagram)

## 1. Executive Summary
### Project Status Summary
After the second milestone we had 2 weeks to develop and improve our applications and in those 2 weeks our team did their best. As you might know at the second milestone stage; login, signup functionality, along with homepage, art item page, profile page, profile settings page, comment functionality, password update through settings were implemented on web and mobile applications. Additionally on web, discovery page and static exhibition pages were implemented; on mobile application forgot password functionality was implemented and the mobile app design was updated so that our project got a consistent identity. 

For the third milestone stage we connected our exhibition page, we have fully implemented the annotation functionality. Users can annotate both images and texts. The lexical search functionality has been implemented and connected with the frontend. We have implemented our recommendation algorithm which is based on the popularity of the art items and exhibition. This recommendation algorithm tracks the user interests as well. This functionality is also connected with the discovery page, as well. Like and unlike images and comments api endpoints has been fully implemented and connected with the both frontends. We have also implemented the bidding system for our artists and art collectors. We supply a platform where artists and art followers meet. Artists can sell their art items without a gallery commission. Following and unfollowing other users functionality has been fully implemented and connected with the both frontends. 

### *Future Plans*

### Reflections Related to the Final Milestone Demo
The Final Milestone Demo, we delivered on 27th of December 2022 was an outcome of almost 10 months of work. As a result of tremendous amount of effort and sleepless nights we finalized our product. It was a stable and error-free version of our project. Even though we had to re-plan our roadmap not to miss the deadlines, still we implemented most of the essential features of our given task. On the Final Milestone Demo day, we tried to show our implementations over personas and mock-ups as much as possible, however in terms of consistency we haven't stick to the same personas and scenarios throughout the three milestones. This might somewhat confused the customers and lost their influence. On the other hand our strong side was our design choices. As an instant customer feedback, our design (color palette, text style, contrast, coherence, etc.) was always appreciated by audience and customers. Simple and elegant choices of design attracted customer attention and boosted the positive feedbacks to the project.


**Note:** Our current project plan can be found [here](https://github.com/bounswe/bounswe2022group8/wiki/CmpE-451-Project-Plan).

### **Changes in Development Process**

In the second Milestone, we couldn't showcase many of the backend functionalities we have implemented because 
we had problems with the planning of the Front, Mobile, and Backend synchronization. After Milestone 2, we had a missing functionalities
in the backend, so we decided to push harder for the remaining functionalities' implementations and 
started helping Frontend and Mobile teams with more strict planning of synchronization. This way we could have show all of the implemented functionalities of 
the backend in the demo presentation. 
We had a well-structured pull request template, meeting schedule, issue labeling and documentation so we can say that we didn't need to change anything
in the management system other than the synchronization of the subgroups. 

Features implemented in the remaining time were: 
1. Text and image annotations
2. Lexical search
3. Recommendation system that tracks the user activity
4. Bidding system for the art items
5. Offline and virtual exhibitions


### **What could have been done differently**

&nbsp; &nbsp;&nbsp; Although we were very excited to see many of the features come to life, unfortunately some of the things we were planning on, didn’t make the cut. This was partly due to us and some planning errors and partly due to factors out of our control.  Looking back at our timeline, one crucial thing would be starting our implementations earlier and with more pace. Meaning, we should have implemented a bigger chunk of our functionalities before milestone 1, not just the main data structures and login/logout.   
&nbsp; &nbsp; &nbsp;  In addition to that, recognizing process tracking (if everyone is where they are supposed to be in terms of implementation) and communication between subgroups, as major tasks of their own from the beginning, would have been helpful. When not planned for, these things either lead to unfair burden on some people or cause stalls in the development process. Although it sucks to admit it, everyone participating in everything mentality can only get us so far, and at some point it is more efficient to allocate management and tracking tasks to some people.  
&nbsp; &nbsp; &nbsp;  Another thing would be, either having more people on the team learn how to use certain software development tools as a backup, or choosing more common and primitive tools and technologies (familiar to more people on the team) to work with. So that, it is easier to jump in and help if a subgroup is struggling with time. But then, we wouldn’t have this amazing looking interface, so not really. Considering the number of features and our experiences in development (with the learning curves), it was pretty obvious early on that we would struggle with time. Imagining this was a real life scenario, in order for all of the features to come to life, only viable solution I can think of is asking the customer either for more people on the team ready to work or an extension. After all, like couture, some things shouldn’t be rushed.

## 2. Summary of Work

<details>
    <summary> Serdar Akol </summary>
    
|  Task Type   | Task Description   |Related Link(s) |
 |  :----:        |  :----:   |  :----: |
 |  Planning |  Attended the Week 11 BE Meeting.  |  [Week 11 BE Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-11-BE-Meeting-%235-(13.12.2022)) |
 |  Planning |  Attended the Week 11 Meeting.  |  [Week 11 Meeting Notes 16](https://github.com/bounswe/bounswe2022group8/wiki/Week-11-Meeting-Notes-16%F0%9F%97%92%EF%B8%8F) |
 |  Planning |  Attended the Week 10 Meeting.  |  [Week 10 Meeting #14](https://github.com/bounswe/bounswe2022group8/wiki/Week-10-Meeting-%2314) |
| PR review | Reviewing the bid related PR| [hotfix/BE-38: new_bids reset](https://github.com/bounswe/bounswe2022group8/pull/397)|
|  Milestone |  Adding more than 10 art items and creating 2 exhibitions | [MIL-28 Creating 10 artitem/online exhibitons](https://github.com/bounswe/bounswe2022group8/issues/424)  |
|  Milestone |  Creating a comprehensive scenario that covers all functionalities | [MIL-27 The Comprehensive Scenario](https://github.com/bounswe/bounswe2022group8/issues/423)  [the comprehensive scenario](https://github.com/bounswe/bounswe2022group8/blob/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/the_comprehensive_scenario.md)|
|  Milestone |  Creating user manuals for both web and mobile applications | [MIL-26 User Manual](https://github.com/bounswe/bounswe2022group8/issues/422) [web user manual](https://github.com/bounswe/bounswe2022group8/blob/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/web_app_user_manual.md) [mobile user manual](https://github.com/bounswe/bounswe2022group8/blob/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/mobile_app_user_manual.md)|
|  Milestone |  Writing the project status summary | [MIL-25 Project Status summary](https://github.com/bounswe/bounswe2022group8/issues/421) |



</details>

<details>
    <summary> Elif Bayraktar </summary>
    
| Hours spent | Task Type             | Task Description |
|  :----:       |  :----:   |  :----: |
|  6 hours   |  coding   |  Added user history as a separate app, created model, and signals, connected. [feature/BE-32 : User History](https://github.com/bounswe/bounswe2022group8/pull/354)  [issue](https://github.com/bounswe/bounswe2022group8/issues/353)|
|  5 hours   |  review   |  Reviewed [PR BE-30](https://github.com/bounswe/bounswe2022group8/pull/354), made some minor contributions.  |
|  2 hours   |  coding   |  Updated art item category, predefined choices. [feature/BE-35: Art Item Category](https://github.com/bounswe/bounswe2022group8/pull/358) [issue](https://github.com/bounswe/bounswe2022group8/issues/357) |
|  1 hour 30 minutes  + |  research   |  Researched for recommendation system.  |
|  4 hour 30 minutes   |  coding   |  Created level system. [feature/BE-36: User Level](https://github.com/bounswe/bounswe2022group8/pull/364) [issue](https://github.com/bounswe/bounswe2022group8/issues/361) |
|  2 hours   |  coding   |  Created models for bidding system. [feature/BE-38: Bidding System](https://github.com/bounswe/bounswe2022group8/pull/371) [issue](https://github.com/bounswe/bounswe2022group8/issues/369) |
|  4 hours   |  coding   |  APIs for the bidding system. [feature/BE-38: Bidding System](https://github.com/bounswe/bounswe2022group8/pull/371) [issue](https://github.com/bounswe/bounswe2022group8/issues/369) |
|  4 hours   |  coding   |  Created APIs for updating art item sale status, list of newly bidded art items in profile page. [feature/BE-38: Bidding System](https://github.com/bounswe/bounswe2022group8/pull/371) [issue](https://github.com/bounswe/bounswe2022group8/issues/369)  |
|  12 hours   |  coding   |  Created recommendation system. [feature/BE-40: Recommendation System](https://github.com/bounswe/bounswe2022group8/pull/386) [issue](https://github.com/bounswe/bounswe2022group8/issues/372) |
|  30 minutes   |  review   |  Reviewed unittest PR. [feature/BE-39: Backend Unittests [1]](https://github.com/bounswe/bounswe2022group8/pull/382)  |
|  30 minutes   |  coding   |  Bugfix PR. [hotfix/BE-38: new_bids reset](https://github.com/bounswe/bounswe2022group8/pull/397)  |
|  8 hours   |  testing/coding/learning   |  Created tests for Recommendation and Bidding systems. [feature/BE-43: Backend Unittests [2]](https://github.com/bounswe/bounswe2022group8/pull/404) [issue](https://github.com/bounswe/bounswe2022group8/issues/403)|
|  8 hours   |  documentation   |  Reviewing updating requirements for release and milestone. Updating use case diagram, part of executive summary, personal reports. [MIL-22: Software Requirements Specification](https://github.com/bounswe/bounswe2022group8/issues/414), [MIL-29: Status of the requirements](https://github.com/bounswe/bounswe2022group8/issues/425), [MIL-32: Use Case Diagram Update](https://github.com/bounswe/bounswe2022group8/issues/428), [MIL-39: Executive/ what could have been done differently](https://github.com/bounswe/bounswe2022group8/issues/440) |
|  ?   |  planning   |  Took part in all of the backend and general meetings.  |
|  ?   |  learning/planning   |  Attended all of the classes and PSs.  |
    


</details>

<details>
    <summary> Metehan Dündar </summary>
    
|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
|  :----:      |  :----:          |  :----:        |  :----:        |
|  Planning  |  Week12 General Meeting After Presentation     |  60 minutes  |   |
|  Planning  |  Attended all weeks' lab session for planning the course of the project.     |  300 minutes  |   |
|  Research  |  Researched about dart language to implement raw, column, widget etc. |  60 minutes  |   | 
|  Implementation  |  Implemented the following & follower users' page |  300 minutes  | [feature/MOB-21](https://github.com/bounswe/bounswe2022group8/tree/feature/MOB-21)   |
|  Presentation  |  Preparing for presentation of the mobile team and its application at final customer meeting |  60 minutes  |   | 

</details>


<details>
    <summary> Mustafa Emre Erengül </summary>
   
|  Task Type   | Task Description |  Time Spent    |Related Link(s) |
|  :----:        |  :----:   |  :----: |  :----: |
|  Planning  |  Review the plan for the final milestone during the lab time.     |  90 minutes  |   |
|  Planning  |  Attended Week10 Group Meeting.    |  130 minutes  |  [Week10- Group Meeting #7](https://github.com/bounswe/bounswe2022group8/wiki/Week-10-Meeting-%237-(07.12.2022)) |
| Implementation | Visiting Other User's Profile is implemented. | 180 minutes | [feature/MOB-22(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/391)  |
| Implementation | Following and Unfollowing functionality is implemented. | 240 minutes | [feature/MOB-22(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/391)  |
| Implementation | Search page with art item search and user search is created. | 180 minutes | [feature/MOB-25(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/402)  |
| Research | Research about how to implement the search functionality. | 60 minutes |
| Implementation | Searching functionality is activated. | 240 minutes | [feature/MOB-25(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/402)  |
| Implementation | Following/Followers page is made. | 150 minutes | [feature/MOB-25(Pull Request)](https://github.com/bounswe/bounswe2022group8/pull/402)  |

</details>


<details>
    <summary> Sinem Koçoğlu </summary>
    
|  Task Type   | Task Description   |Related Link(s) |
|  :----:        |  :----:   |  :----: |
|  Implementation | Implementation of annotations on frontend and fixing related bugs  | [#308](https://github.com/bounswe/bounswe2022group8/issues/308), [PR](https://github.com/bounswe/bounswe2022group8/pull/376), [PR](https://github.com/bounswe/bounswe2022group8/pull/389) [PR](https://github.com/bounswe/bounswe2022group8/pull/417) |
| Implementation | Implementation of bidding system on frontend | [#377](https://github.com/bounswe/bounswe2022group8/issues/377), [PR](https://github.com/bounswe/bounswe2022group8/pull/392)   |
| Implementation | Providing backend connection for recommendation pages | [#393](https://github.com/bounswe/bounswe2022group8/issues/393), [PR](https://github.com/bounswe/bounswe2022group8/pull/408) | 
| Documentation | Updating scenario2-Artists with respect to the final version of the app | [wiki](https://github.com/bounswe/bounswe2022group8/wiki/Scenario-2) |
| Documentation/Review | Reviewed annotation and bidding related requirements |  [#414](https://github.com/bounswe/bounswe2022group8/issues/414) |  
| Code Review | Reviewed PRs belonging to frontend. | [FE-29](https://github.com/bounswe/bounswe2022group8/pull/396), [FE-28](https://github.com/bounswe/bounswe2022group8/pull/394), [FE-25](https://github.com/bounswe/bounswe2022group8/pull/375), [FE-24](https://github.com/bounswe/bounswe2022group8/pull/374), [FE-18](https://github.com/bounswe/bounswe2022group8/pull/360), [FE-12](https://github.com/bounswe/bounswe2022group8/pull/355)|  

 
</details>

<details>
    <summary> Sena Mumcu </summary>
 
|  Task Type   | Task Description   |Related Link(s) |
|  :----:        |  :----:   |  :----: |
|  Planning        |  Attended Week11 BE Meeting   |  [Meeting Notes](https://github.com/bounswe/bounswe2022group8/wiki/Week-11-BE-Meeting-%235-(13.12.2022)) |
|  Implementation      |  Implementation of search related APIs   |  See [PR](https://github.com/bounswe/bounswe2022group8/pull/292) |
| Milestone 3       |  Wrote the changes we made in our planning and development process since milestone 2   |  see [issue](https://github.com/bounswe/bounswe2022group8/issues/427) |
|  Milestone 3        |  Prepared the system manual for the backend team   |  see [issue](https://github.com/bounswe/bounswe2022group8/issues/429) |
    
</details>

<details>
    <summary> Furkan Keskin </summary>
 
|  Task Type   | Task Description   |Related Link(s) |
|  :----:        |  :----:   |  :----: |
| Implementation | Implementation of others' profile page | [#241](https://github.com/bounswe/bounswe2022group8/issues/241), [PR](https://github.com/bounswe/bounswe2022group8/pull/360) |
| Implementation | Implementation of Follow/Unfollow related interfaces and backend connections | [PR](https://github.com/bounswe/bounswe2022group8/pull/360)|
| Implementation | Implementation of Like functionality on frontend  | [#362](https://github.com/bounswe/bounswe2022group8/issues/362), [PR](https://github.com/bounswe/bounswe2022group8/pull/374)   |
| Implementation| Implementation of Forgot/Reset password on frontend | [#260](https://github.com/bounswe/bounswe2022group8/issues/260), [PR](https://github.com/bounswe/bounswe2022group8/pull/355) |
| Implementation | Improvement on the guest users' user experience  | [PR](https://github.com/bounswe/bounswe2022group8/pull/360)  |
| Implementation | Significant improvements on the recommendation pages  | [PR](https://github.com/bounswe/bounswe2022group8/pull/360)   |
| Implementation | Implemented category interface/dropdown selection on frontend  | [#363](https://github.com/bounswe/bounswe2022group8/issues/363), [PR](https://github.com/bounswe/bounswe2022group8/pull/375)  |
| Implementation | Implementation of delete artitem/exhibition interfaces and backend connections  | [#373](https://github.com/bounswe/bounswe2022group8/issues/373), [PR](https://github.com/bounswe/bounswe2022group8/pull/375)  |
| Implementation | Implementation of tag selection/multi selection dropdown, tag by search page interface and the necessary tag related connections to backend  | [#378](https://github.com/bounswe/bounswe2022group8/issues/378), [PR](https://github.com/bounswe/bounswe2022group8/pull/394) |
| Implementation | Implementation of online exhibition upload interface, online exhibition page and the necessary backend connections and redirections   | [#383](https://github.com/bounswe/bounswe2022group8/issues/383), [PR](https://github.com/bounswe/bounswe2022group8/pull/396)  |
| Implementation | Implementation of search result page and searchbar backend connections | [#406](https://github.com/bounswe/bounswe2022group8/issues/406), [PR](https://github.com/bounswe/bounswe2022group8/pull/415) |
| Code Review    | Reviewed some frontend and backend PRs  | [BE-37](https://github.com/bounswe/bounswe2022group8/pull/368), [FE-19](https://github.com/bounswe/bounswe2022group8/pull/376), [BE-30.1](https://github.com/bounswe/bounswe2022group8/pull/390), [FE-27](https://github.com/bounswe/bounswe2022group8/pull/392), [BE-30.2](https://github.com/bounswe/bounswe2022group8/pull/395), [FE-31](https://github.com/bounswe/bounswe2022group8/pull/408)   |


</details>   
    
<details>
    <summary> Karahan Sarıtaş </summary>

|  Task Type   | Task Description   |Related Link(s) |
 |  :----:        |  :----:   |  :----: |
 |  Planning |  Documentation of the Week 11 BE Meeting.  |  [Week 11 BE Meeting #5](https://github.com/bounswe/bounswe2022group8/wiki/Week-11-BE-Meeting-%235-(13.12.2022)) |
|  Implementation | Implementation of exhibition related APIs  | [#343](https://github.com/bounswe/bounswe2022group8/issues/343), [PR](https://github.com/bounswe/bounswe2022group8/pull/344), [PR](https://github.com/bounswe/bounswe2022group8/pull/385) |
| Implementation | Implementation of Annotation Service, writing unittests, documenting the APIs using Swagger, dockerizing the application, helping during the deployment and helping the integration with frontend. | [#348](https://github.com/bounswe/bounswe2022group8/issues/348), [PR](https://github.com/bounswe/bounswe2022group8/pull/359), [PR](https://github.com/bounswe/bounswe2022group8/pull/389) |
| Implementation | Fixing a bug related to Nginx on web | [#388](https://github.com/bounswe/bounswe2022group8/issues/388), [PR](https://github.com/bounswe/bounswe2022group8/pull/387) |
| Implementation | Implementation of an additional API that returns the artitems based on tags. | [#367](https://github.com/bounswe/bounswe2022group8/issues/367), [PR](https://github.com/bounswe/bounswe2022group8/pull/368)   |
| Implementation | Implementing unit tests for all APIs I've implemented so far. | [#370](https://github.com/bounswe/bounswe2022group8/issues/370), [PR](https://github.com/bounswe/bounswe2022group8/pull/382) | 
| Documentation | Creating a MIT license for the project | [#365](https://github.com/bounswe/bounswe2022group8/issues/365) |
| Documentation | Documenting the API endpoints and giving example inputs/outputs for Milestone | [#407](https://github.com/bounswe/bounswe2022group8/issues/407) |
| Documentation | Creating a tag that marks the final release version | [#413](https://github.com/bounswe/bounswe2022group8/issues/413) | 
| Documentation | Updating the class diagram with respect to the final version of our program | [#419](https://github.com/bounswe/bounswe2022group8/issues/419) |
| Documentation | Revising annotation related requirements |  [#414](https://github.com/bounswe/bounswe2022group8/issues/414) |
| Milestone | Overall maintenance of the project and fixing last-minute bugs if any |  - |
| Code Review | Reviewed a majority of the PRs belonging to backend/frontend/mobile. For specific details, please refer to each individual link. | [BE-36](https://github.com/bounswe/bounswe2022group8/pull/364), [BE-35](https://github.com/bounswe/bounswe2022group8/pull/358), [BE-32](https://github.com/bounswe/bounswe2022group8/pull/354), [BE-38](https://github.com/bounswe/bounswe2022group8/pull/371), [FE-19](https://github.com/bounswe/bounswe2022group8/pull/389), [BE-33](https://github.com/bounswe/bounswe2022group8/pull/381), [BE-40](https://github.com/bounswe/bounswe2022group8/pull/386), [BE-43](https://github.com/bounswe/bounswe2022group8/pull/404), [MOB-28](https://github.com/bounswe/bounswe2022group8/pull/411), [FE-32](https://github.com/bounswe/bounswe2022group8/pull/415), [FE-33](https://github.com/bounswe/bounswe2022group8/pull/417) |  


</details>



<details>
    <summary> Doğukan Türksoy </summary>
 
Task Type | Task Description | Related Link(s)
-- | -- | --
Implementation | Implementation of bugs after Milestone2 | [MOB-21](https://github.com/bounswe/bounswe2022group8/issues/379)
Implementation | Implementation of backend connection of annotations | [MOB-28](https://github.com/bounswe/bounswe2022group8/pull/411)
Implementation | Search page backend connection implemented | [MOB-29](https://github.com/bounswe/bounswe2022group8/pull/416)
Documentation | Creating System Manual for Frontend and Android | [link](https://github.com/bounswe/bounswe2022group8/wiki/System-Manual)
Code Review | Reviewed PRs belonging to mobile. | [BE-30](https://github.com/bounswe/bounswe2022group8/pull/333) [MOB-22](https://github.com/bounswe/bounswe2022group8/issues/398), [MOB-25](https://github.com/bounswe/bounswe2022group8/pull/402)
Deployment | Frontend Deployment | [MIL-33: Deployment](https://github.com/bounswe/bounswe2022group8/issues/430)
Deployment | Backend Deployment | [MIL-33: Deployment](https://github.com/bounswe/bounswe2022group8/issues/430)
Deployment | Android Deployment | [MIL-33: Deployment](https://github.com/bounswe/bounswe2022group8/issues/430)
Deployment | Annotation Deployment | [MIL-33: Deployment](https://github.com/bounswe/bounswe2022group8/issues/430)

</details>



<details>
    <summary> Mustafa Cihan </summary>
    
|  Task Type   | Task Description   | Related Link(s) |
|  :----:        |  :----:   |   :----: |
|  Research |  Annotations for mobile  |  [MOB-22](https://github.com/bounswe/bounswe2022group8/issues/398)|    
|  Design |  Designing text annotation system for mobile  |  [MOB-22](https://github.com/bounswe/bounswe2022group8/issues/398)|    
|  Implementation |  Text annotations for mobile  |  [MOB-22](https://github.com/bounswe/bounswe2022group8/issues/398)  |
|  Implementation |  Like Functionality  |  [MOB-23](https://github.com/bounswe/bounswe2022group8/issues/399)|
|  Doucmentation |   Status of The Annotations in Mobile Application | [MIL-30](https://github.com/bounswe/bounswe2022group8/issues/426) |
|  Documentation |  Adding Mobile UI to Document |  [MIL-38](https://github.com/bounswe/bounswe2022group8/issues/436) |
  
    
</details>


## 3. Status of Deliverables

## 3. Status of Deliverables
|Deliverable|Status|Changes| 
|-----|:--------:|:------:| 
|Software Requirements Specification | Completed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Requirements)|
|Software Design (UML):Use-Case Diagram | Completed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Use-case-diagram)|
|Software Design (UML):Class Diagram | Completed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Class-Diagram)|
|Software Design (UML):Sequence Diagram | Completed | [Latest version](https://github.com/bounswe/bounswe2022group8/wiki/Sequence-Diagrams)|
|[Scenario: Art Follower User](https://github.com/bounswe/bounswe2022group8/wiki/Scenario:-Art-Follower-User) | Completed | - |
|[Scenario: Verified User/Artist Scenario](https://github.com/bounswe/bounswe2022group8/wiki/Scenario-2) | Completed | - |
|[Scenario: Collaboration Scenario](https://github.com/bounswe/bounswe2022group8/wiki/Scenario-3) | Completed | - |
|[Project Plan](https://github.com/bounswe/bounswe2022group8/wiki/CmpE-451-Project-Plan)| Completed | - |
|Individual Contribution Reports | Completed | [Latest version](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_3/Group%20Review.md#9-individual-reports)|
|[Web App](http://34.125.134.88/#) | Completed | - |
|Mobile App - APK | Completed | [Latest version](https://drive.google.com/drive/folders/1NaEdDko7TS6xYg-C_MleVoO33yP-qhrz)|
|Group Review | Completed | [Latest version](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_3/Group%20Review.md)|


## 4. Progress According to Requirements

* The requirements page of the application [here](https://github.com/bounswe/bounswe2022group8/wiki/Requirements). Here status of the requirements are marked as (Completed), (In progress) or (Not started).
* Requirements satisfied so far: [Realized Requirements](https://github.com/bounswe/bounswe2022group8/wiki/Realized-Requirements). Here you can find the latest version of the Software Requirements Specification, with updates and changes.

## 5. API Endpoints
**@author: Karahan Sarıtaş**

* You can find the documentations of our API endpoints in the following URLs:
   * Application APIs: http://34.125.134.88:8000/api/v1/swagger/schema/ 
   * Annotation APIs: http://34.125.134.88:7000/api/v1/swagger/schema/

* We used Swagger to document our APIs and provide exemplary inputs/outputs for other teams. Please notice that you have to authorize yourself in order to test some of the APIs (since these can be called only by logged-in users in our application - not by guest users).
* There is this button called ```Authorize``` on the right corner in Swagger page. We have to use it to test APIs that require authorization. For example, in order to test the ```logout``` API, first you have to log in to the application and have a token with you. Try the ```login``` endpoint first, copy paste the token returned to you and click on the ```Authorize``` button. Input the token in the following format: "Token xxx". Replace `xxx` with the token and don't forget to put a space between the first word and your token. You can refer to this [PR](https://github.com/bounswe/bounswe2022group8/pull/245) for more details if you want.
* By using Swagger, you can test any API you want either with the example input we provided or some other input that complies with the specification.
* You can use the button below to test any functionality you want. All inputs are already prepared for you - you just have to sign-in or register to the application and use the generated token for authentication-required APIs. <br>
* You can find our collection as a [json file](https://raw.githubusercontent.com/bounswe/bounswe2022group8/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/CmpE451%20API.postman_collection.json) within this directory.
* Public Workspace: https://documenter.getpostman.com/view/16425196/2s8Z6x1sYP#02d71c3b-ce09-4b8a-a281-189d1c91441a (You can use the `Run in Postman` button at the top-right corner.)
* Let me provide the Postman Collection [here](https://github.com/bounswe/bounswe2022group8/blob/feature/MIL/Deliverables/CMPE451_Customer_Presentation_Milestone_3/CmpE451%20API%20-%20Production.postman_collection.json). `{{host}}` stands for `34.125.134.88`.

---
To give you an example, let me provide some consecutive API calls in a scenario.
1) Firstly, you should be registering to the application using `http://{{host}}:8000/api/v1/auth/register/` endpoint. You can call it with the following body:
```json
{
  "email": "plantinga@cornell.edu.tr",
  "username": "alvin.plantinga",
  "password": "revisionistwestern3",
  "password_confirm": "revisionistwestern3"
}
```
It will return an output in the following format:
```json
{
    "user": {
        "email": "plantinga@cornell.edu.tr",
        "username": "alvin.plantinga"
    },
    "token": "b03191f004b98d4207b178ecd25ff645f464e9d37d9730dc47c8a175f8216b45"
}
```
2. Then you should proceed with creating an art item. Input body is already provided for you. You should just change the token from the headers. Copy paste the generated token from the call above, and update the value of `Authorization` header. Then call the `http://{{host}}:8000/api/v1/artitems/me/upload/` API with the following input:
```json
{
    "title" : "A work of art",
    "description" :"An example of fine art, such as a painting or drawing.",
    "category": "SK",
    "artitem_image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="}
```
Output will be something like this:
```json
{
    "id": 9,
    "owner": {
        "id": 6,
        "username": "alvin.plantinga",
        "name": "",
        "surname": "",
        "profile_path": "avatar/default.png"
    },
    "title": "A work of art",
    "description": "An example of fine art, such as a painting or drawing.",
    "category": "SK",
    "tags": [],
    "artitem_path": "artitem/artitem-9.png",
    "likes": 0,
    "number_of_views": 0,
    "created_at": "27-12-2022 03:26:52",
    "sale_status": "NS",
    "minimum_price": 0,
    "bought_by": null
}
```
To avoid verbosity, the base64 string given above represents an extremely small image. But you can upload real images using the input bodies already provided for you in the collection.
3. Try to create an online exhibition using `http://{{host}}:8000/api/v1/exhibitions/me/online/`. 
```json
{       
    "title" : "Exploring Global Climate Change Through Photography",
    "description" :"Art exhibition at 5th Avenue.",
    "start_date": "2022-12-08T13:00:00.000Z",
    "end_date": "2022-12-19T13:00:00.000Z",
    "collaborators": [],
    "artitems_gallery": [],
    "artitems_upload": [
    {
        "title" : "Portrait of Joel Miller, a ruthless and cynical smuggler eventually tasked with smuggling and protecting Ellie Williams.",
        "description" :"Joel Miller from TLOU universe.",
        "tags": [],
        "category": "OT",
        "artitem_image": 
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="},
    {
        "title" : "Shipwreck",
        "description" :"Realistic depictions of coastal scenes and seascapes.",
        "tags": [],
        "category": "OT",
        "artitem_image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="}],
    "poster": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="
}
```
Output of this call will be something like this:
```json
{
    "id": 1,
    "owner": {
        "id": 1,
        "username": "alvin.plantinga",
        "name": "",
        "surname": "",
        "profile_path": "avatar/default.png"
    },
    "title": "Exploring Global Climate Change Through Photography",
    "description": "Art exhibition at 5th Avenue.",
    "poster": {
        "id": 2,
        "owner": 1,
        "title": "Exploring Global Climate Change Through Photography",
        "description": "Art exhibition at 5th Avenue.",
        "category": "PT",
        "tags": [],
        "artitem_path": "artitem/artitem-10.png",
        "created_at": "27-12-2022 03:28:22"
    },
    "collaborators": [],
    "artitems_gallery": [],
    "start_date": "08-12-2022 16:00:00",
    "end_date": "19-12-2022 16:00:00",
    "created_at": "27-12-2022 03:28:22",
    "updated_at": "27-12-2022 03:28:22",
    "status": "Finished",
    "artitems_upload": [
        {
            "id": 3,
            "title": "Shipwreck",
            "tags": [],
            "description": "Realistic depictions of coastal scenes and seascapes.",
            "category": "OT",
            "artitem_path": "artitem/artitem-11.png",
            "likes": 0,
            "created_at": "27-12-2022 03:28:23"
        },
        {
            "id": 4,
            "title": "Portrait of Joel Miller, a ruthless and cynical smuggler eventually tasked with smuggling and protecting Ellie Williams.",
            "tags": [],
            "description": "Joel Miller from TLOU universe.",
            "category": "OT",
            "artitem_path": "artitem/artitem-11.png",
            "likes": 0,
            "created_at": "27-12-2022 03:28:23"
        }
    ]
}
```
4. You can put your art item on sale starting from a minimum price of 200 dollars, using the API `http://{{host}}:8000/api/v1/artitems/<int:artitemid>/bids/` with the following body:
```json
{
  "sale_status": "FS",
  "minimum_price": 200
}
```
Output will be as follows:
```json
{
"detail": "The art item is successfully put on sale."
}
```
* You can do much more with all those APIs provided in the collection. Keep on exploring!

## 6. User Interface and User Experience

<details>
    <summary>Web</summary>
    
#### Home Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Home.js)
* UI: 
    ![home1](https://user-images.githubusercontent.com/98259272/206314671-eb4af8f4-8797-4566-bda5-080aaa9887b0.png)
    ![home2](https://user-images.githubusercontent.com/98259272/206314697-bda8a10b-5ae5-4067-9288-fba2c832e600.png)
    ![home3](https://user-images.githubusercontent.com/98259272/206314712-4f061c77-5682-43dc-a6df-b2e7f52e8bc3.png)
#### Login Pop-up
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/LoginModal.js) 
* UI:
    ![login](https://user-images.githubusercontent.com/98259272/206314720-4d8d4686-a2ed-4e5f-bedc-91f47cd60b48.png)

#### Sign up Pop-up
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/SignupModal.js)
* UI:
    ![sign up](https://user-images.githubusercontent.com/98259272/206314739-5d915561-841c-4fc1-aa34-1ae606aba007.png)
    
#### Reset Password Pop-up
    
 * [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/ResetPasswordModal.js)
 * UI:
    ![forgotpassword](https://user-images.githubusercontent.com/98259272/206521742-d41bf4a8-331b-4567-ae2a-d8400b53404a.png)

#### Profile Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Profile.js)
* UI:
    ![profile1](https://user-images.githubusercontent.com/98259272/210138542-a4dba10e-7fe3-4dfd-8cae-843b12dc7dcf.png)
    ![profile2](https://user-images.githubusercontent.com/98259272/210138544-6d9a8ee2-7547-47b5-be06-63a73167d702.png)
    ![profile3](https://user-images.githubusercontent.com/98259272/210138545-78989429-4b97-4d5f-b189-19599f8c8259.png)
  
#### Upload Card
    
* [Code-upload-artitem](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/UploadArtitemCard.js)
* UI:
    ![upload1](https://user-images.githubusercontent.com/98259272/210138548-6b7404e5-eae1-47a7-a701-3fbe4251f37b.png)
    
* [Code-upload-exhibition1](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/UploadOnlineExhibitionCard.js)
* [Code-upload-exhibition2](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/components/ArtItemSelection.js)
* UI:
    ![upload2](https://user-images.githubusercontent.com/98259272/210138551-04283d01-23af-4c3e-a81a-aa77aa4ac0c6.png)
    ![upload2 1](https://user-images.githubusercontent.com/98259272/210138549-6ef01423-6eed-48b5-8b3a-5ead9bcf8f18.png)
    ![upload2 2](https://user-images.githubusercontent.com/98259272/210138550-a97b9e06-504d-4d60-85ab-c2014d7dc8cf.png)
 
#### Other Users Profile Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/ProfileOther.js)
* UI:
    ![otherusersprofile](https://user-images.githubusercontent.com/98259272/210138540-f6cd9e9a-f491-48be-9996-15a868e6590a.png)

#### Art Item Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/ArtItem.js)
* UI:
    ![artitem1](https://user-images.githubusercontent.com/98259272/210138527-e1fc6ee6-23ec-4932-8b12-9c34187ea80d.png)
    ![artitem2](https://user-images.githubusercontent.com/98259272/210138528-8b719066-ae7f-40cc-a39a-d099f5d42d6b.png)
   
#### Exhibition
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Exhibition.js)
* UI:
    ![exhibition](https://user-images.githubusercontent.com/98259272/210138538-1bd16514-59bb-4f0c-aad9-d78cd74ab00a.png)   
    
#### Sidebar
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/layout/Sidebar.js)
* UI:
    ![sidebar](https://user-images.githubusercontent.com/98259272/210138547-49549a87-143c-4f9a-bc6d-00c30f561f87.png)
  
#### Discover Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Recommendation.js)
* UI:
   ![discover1](https://user-images.githubusercontent.com/98259272/210138529-5a493d50-c19b-47d3-9ee7-a01b0c2a4eae.png)
    ![discover2](https://user-images.githubusercontent.com/98259272/210138530-58ee5e31-be01-495d-8708-b51944a1af98.png)
    ![discover3](https://user-images.githubusercontent.com/98259272/210138531-265ca202-6f2b-4fd8-8002-c3139092ddcc.png)
  
#### Discover Art Items Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/RecommendedPages/RecommendedArtitems.js)
* UI:
    ![discoverartitem](https://user-images.githubusercontent.com/98259272/210138532-5f2355fd-fde6-4209-8523-38cabcca5050.png)
    
#### Discover Exhibitions Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/RecommendedPages/RecommendedExhibitions.js)
* UI:
   ![discoverexhibitions](https://user-images.githubusercontent.com/98259272/210138534-efc91a73-5815-45d2-ae5a-f0173f4cf7df.png)

#### Discover Users Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/RecommendedPages/RecommendedUsers.js)
* UI:
    ![discoverusers](https://user-images.githubusercontent.com/98259272/210138535-56efb0c7-2e09-45c8-9f25-f2bec5a8dde5.png)   
    
#### Settings Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/Settings.js) 
* UI:
    ![settings1](https://user-images.githubusercontent.com/98259272/206314803-0b12152a-c167-4cc4-8b89-373c2ef5c228.png)
    ![settings2](https://user-images.githubusercontent.com/98259272/206314814-b4355a4a-b507-4bf0-b828-a7f4b9c68880.png)

#### Search Results Page
    
* [Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/frontend/src/pages/SearchResults.js)
* UI:
    ![searchresults](https://user-images.githubusercontent.com/98259272/210138546-a134c03d-0371-46f2-bf9c-57816e35ae39.png)
    
</details>   

<details>
    <summary>Mobile</summary>
       
#### Landing Page

##### [Landing Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/landing_page.dart)

<img width="497" alt="Ekran Resmi 2023-01-02 22 42 25" src="https://user-images.githubusercontent.com/49492904/210272822-a4aacf1c-2a3a-4888-a855-d4af158fa131.png">

##### [Signup Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/signup_page.dart)
<img width="495" alt="Ekran Resmi 2023-01-02 22 44 44" src="https://user-images.githubusercontent.com/49492904/210272963-90f55fc9-1ef7-4746-aa70-cbabc0c4019e.png">

##### [Forgot Password Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/forgot_password.dart)
<img width="491" alt="Ekran Resmi 2023-01-02 22 46 01" src="https://user-images.githubusercontent.com/49492904/210273058-47af8f6e-8fe8-4c6d-9792-01b2774b4d41.png">

##### [Login Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/login_page.dart)
<img width="492" alt="Ekran Resmi 2023-01-02 22 46 28" src="https://user-images.githubusercontent.com/49492904/210273088-970cb60e-4f72-4281-a8cc-d43c27204cf9.png">

##### [Home Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/home_page.dart)
![WhatsApp Image 2023-01-02 at 22 57 28](https://user-images.githubusercontent.com/49492904/210273851-41e79dd1-fc78-4efb-9ccf-8ce7aa20c6db.jpeg)

##### [Art Item Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/artitem_page.dart)[ Annotation Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/widgets/TextAnnotation.dart)
![WhatsApp Image 2023-01-02 at 22 57 28-2](https://user-images.githubusercontent.com/49492904/210274014-bd9ef480-0109-410e-89df-1cd1f47cebf1.jpeg)
![WhatsApp Image 2023-01-02 at 22 57 29](https://user-images.githubusercontent.com/49492904/210274046-1928a328-9f92-40a1-bc9e-4ff8c5c9560e.jpeg)
![WhatsApp Image 2023-01-02 at 22 57 29-2](https://user-images.githubusercontent.com/49492904/210274067-52ba1e27-7f99-4753-afdf-0232b843fe51.jpeg)
![WhatsApp Image 2023-01-02 at 22 57 29-3](https://user-images.githubusercontent.com/49492904/210274083-8130978b-157d-46d0-877a-bcfc2e607070.jpeg)

##### [Comment Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/comment_page.dart)
![WhatsApp Image 2023-01-02 at 22 57 28-3](https://user-images.githubusercontent.com/49492904/210274104-4c944f29-7e0d-4a5e-b9fa-3e634d56f7a9.jpeg)

##### [Profile Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/widgets/self_profile.dart)
![WhatsApp Image 2023-01-02 at 22 57 29-4](https://user-images.githubusercontent.com/49492904/210274158-e67c9e28-070b-4d5d-ac6c-49d9138a3b2b.jpeg)

##### [Search Page Code](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/search_page.dart)
![WhatsApp Image 2023-01-02 at 22 57 30](https://user-images.githubusercontent.com/49492904/210274238-7bff9876-08c2-4c21-b2ba-c2a0ef2d6513.jpeg)
![WhatsApp Image 2023-01-02 at 22 57 30-2](https://user-images.githubusercontent.com/49492904/210274248-915fbbab-3298-40a0-b9ed-c6894501c218.jpeg)
![WhatsApp Image 2023-01-02 at 22 57 30-3](https://user-images.githubusercontent.com/49492904/210274261-f9ac1356-2eec-437a-9ab6-c779bc9d77e8.jpeg)

##### [Upload Art Item Page](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/art_item_upload.dart)
![WhatsApp Image 2023-01-02 at 22 58 29](https://user-images.githubusercontent.com/49492904/210274361-ef255cfc-83de-49a3-95ff-9abd5b110ccb.jpeg)

#### [Change Password Page](https://github.com/bounswe/bounswe2022group8/blob/master/App/mobile/lib/change_password.dart)
![WhatsApp Image 2023-01-02 at 22 58 28](https://user-images.githubusercontent.com/49492904/210274393-6858e54f-dffb-4fd0-9f76-901efe4f6ddd.jpeg)

</details>


## 7. Annotations
### Frontend
* @recogito/recogito-js react library is used to handle text annotations on title and description of artitems on artitem page. 
* @recogito/annotorious react library is used image annotations on image on artitem page.
* Both libraries conforms to the web annotation standards and compatible with React.js. Also, both provides opportunity to add more fields to data modal in order to meet the needs of the backend. By the functions and user editor both libraries provide, annotation user interface was handled faster and features to display information about annotations such as creator username and created time were provided to users and handled at coding side in a better way.
### Mobile
* There is not any specific library to make annotations on flutter. Therefore we have developed a annotation system for our project.
* Only text annotations are available in mobile project. Unfortunaltelly we could not design and implement image annotation.
* Users can add new text annotations, show/hide annotations created by other users and delete their previous annotations.
* Text annotation conforms to the W3C standarts which are explained in next section.

### Backend
* Annotation service is completely up and ready for the usage of frontend/mobile, serving on http://34.125.134.88:7000/. 
* Swagger documentation with detailed input/output examples can be examined on http://34.125.134.88:7000/api/v1/swagger/schema/.
* Unittests covering the functionalities provided by Annotation APIs can be found [here](https://github.com/bounswe/bounswe2022group8/blob/master/App/annotations/api/test.py). 
* The work we have completed towards the application of the W3C
standards with respect to Annotations can be found in the next section.

## 8. Standards

### Annotations
* Annotations are implemented as a separate service located [here](https://github.com/bounswe/bounswe2022group8/tree/master/App/annotations). It uses a separate database than the actual database of the application. Our models can be found [here](https://github.com/bounswe/bounswe2022group8/blob/master/App/annotations/api/models.py).
* `Annotation` model directly represents an annotation relationship, whereas `Body` and `Target` constitute two essential participants of this relationship.
* Annotations may have 0 or more Bodies. Therefore it is created as a `ManyToMany` field. 
*  Annotations have 1 or more Targets. (As a part of our requirements, we only keep one target for each annotation.)
* An `Annotation` object may have different fields based on the use case. Here, you can find the properties of a **serialized** `Annotation` object.

|  Term  |  Type  | Description |
 |  :----:        |  :----:   |  :----: |
|  id | Property | The unique identity of the Annotation. | 
|  @context | Property | The context that determines the meaning of the JSON as an Annotation. | 
|  type | Relationship | The type of the Annotation. Related to `Type` object. | 
|  body | Relationship | The relationship between an annotation and its body. Related to `Body` object.  | 
|  target | Relationship | The relationship between an Annotation and its Target. | 
|  creator | Property | ID of the creator of the annotation. | 
|  created | Property| Date when the annotation is created. | 
|  modified | Property | Date when the annotation is modified. | 

Example:
> Scenario: User with the `user id = 1` and `username = peter.parker`, makes an image annotation. Annotated image is stored at https://cmpe451-production.s3.amazonaws.com/artitem/artitem-1.png (You can't open it directly since it's protected). Annotation consists of a rectangle located at `x = 357.59, y = 252.836, w = 492.50, h = 140.15` and a body associated with it: `"Dedicated to my brother"`. You can examine the resulting annotation down below:
```json
  {
    "id": "#a11bf464-e13e-4cf7-a8a0-7debfacca983",
    "body": [
      {
        "value": "Dedicated to my brother",
        "type": "TextualBody",
        "purpose": "commenting",
        "created": "2022-12-27T13:40:33.220980+03:00",
        "modified": "2022-12-27T13:40:33.221006+03:00",
        "creator": {
          "id": 1,
          "name": "peter.parker"
        }
      }
    ],
    "type": "Annotation",
    "target": {
      "id": "http://34.125.134.88/image1",
      "source": "https://cmpe451-production.s3.amazonaws.com/artitem/artitem-1.png",
      "type": "Image",
      "selector": {
        "value": "xywh=pixel:357.5931091308594,252.83668518066406,492.5091857910156,140.15553283691406",
        "type": "FragmentSelector",
        "conformsTo": "http://www.w3.org/TR/media-frags/"
      }
    },
    "creator": 1,
    "@context": "http://www.w3.org/ns/anno.jsonld"
  }
```
* A `Body` object may have different fields based on the use case. Here, you can find the properties of a `Body` object in our application.

|  Term  |  Type  | Description |
 |  :----:        |  :----:   |  :----: |
|  type | Relationship | The type of the Body. Related to `Type` object. | 
|  value| Property | Text value of the body. | 
|  format | Property | The format of the Web Resource's content. | 
|  creator | Relationship | Creator of the body. It's represented as a relationshio with `Creator` object. | 
|  created | Property| Date when the body is created. | 
|  modified | Property | Date when the body is modified. | 
|  purpose | Relationship | Date when the body is created. | 

An exemplary body object:
```json
{
"value": "Is it autumn though? Additionally, why are people running through the street?",
"type": "TextualBody",
"purpose": "commenting",
"created": "2022-12-27T14:37:30.766288+03:00",
"modified": "2022-12-27T14:37:30.766310+03:00",
"creator": {
    "id": 3,
    "name": "volkan.oge"
    }
}
```

* A `Target` object may have different fields based on the use case. Here, you can find tje properties of a `Target` object in our application.

|  Term  |  Type  | Description |
 |  :----:        |  :----:   |  :----: |
|  source | Property | The type of the Body. Related to `Type` object. | 
|  format | Property | Text value of the body. | 
|  language | Property | The format of the Web Resource's content. | 
|  type | Relationship | The type of the Target. Related to `Type` object. | 
| selector | Relationship | The selector(s) associated with the target. |

Here you can find an exemplary target from our application:
> Scenario: A user annotates the word `autumn` on an art item description. Starting and ending positions are stored as `TextPositionSelector`. Exact word is stored with `TextQuoteSelector`. Source image is https://cmpe451-production.s3.amazonaws.com/artitem/artitem-5.png. This means that the description (or title) of this art item is annotated.
```json
"target": {
    "id": "http://34.125.134.88/image8",
    "source": "https://cmpe451-production.s3.amazonaws.com/artitem/artitem-5.png",
    "type": "Image",
    "selector": [
        {
            "exact": "autumn",
            "type": "TextQuoteSelector"
        },
        {
            "start": 22,
            "end": 28,
            "type": "TextPositionSelector"
        }
    ]
}
```
* We also created `Type`, `Motivation`, `FragmentSelector`, `TextQuoteSelector`, `TextPositionSelector`, `Selector` and `Creator` models to represent the relationships between the models.

### Miscellaneous
* All passwords were hashed with the sha256 hashing algorithm and all data exchanges involving passwords took place over the encoded versions of these passwords. Of course, they are also encrypted in our database.

* Since we are an art application, images are the most important part of our application. That's why we paid special attention to the security of the images. Our images are stored in AWS S3 private bucket in a very secure way with Amazon assurance. These images cannot be accessed without the key of the bucket. So even if someone accesses the url of any user's image, they will not be able to open it directly. Most importantly, we have not hard coded any key in the code and we have always tried to implement best practices for security in general. 

* In the whole process of writing the application, we took care to get minimum data from our users. We made many things such as name and location optional. Each registered user has a unique and encrypted authentication token specific to the session and this token is stored in local storage. Except for this information, we have not kept any information about the user in local storage so far.

* We made sure to provide metadata in our application. We used alt attribute in almost every image and we used aria-label tag in many of our interactive elements.

* We tried not to write the whole application as a bunch of meaningless divs. We did our best to increase tag diversity by using different HTML tags for different purposes. 

## 9. Individual Reports 

<details>
    <summary> Serdar Akol </summary>
I am Serdar Akol, a team member of the Group 8. I started work on the Mobile development part of our project then transferred to the 
    backend team.

## Milestone 1
### Responsibilities 
* Researching different mobile application development tools.
* Setting the environment for the mobile development.
* Learning basic Flutter/Dart to implement the initial pages.
* Reviewing and updating the requirements.

### Contributions

|  Task Type   | Task Description   | Related Link(s) |
 |  :----:        |  :----:    |  :----: |
 | Requirements Elicitation| Review and revise the requirements _Annotation_ .  |  [#176](https://github.com/bounswe/bounswe2022group8/issues/176)|
 | Requirements Elicitation|  Review and revise the requirements _User Interaction and Guest Users_ . |   [#172](https://github.com/bounswe/bounswe2022group8/issues/172)|
 |  Revise | Review and revise the Mockups .  |  [#171](https://github.com/bounswe/bounswe2022group8/issues/171)|

## Milestone 2

* Implementing Like/Unlike feature for comments. 
* Implementing Account/User deletion API. 


### Main Contributions
My main contributions are also the ones listed above. Since, I have been transferred to backend team after the first milestone report. I have struggled to addopt to the team at first. But thanks to Karahan and all my other backend team, I could catch the team up. <br/>

**Code Related Issues**
* [Issue BE-27](https://github.com/bounswe/bounswe2022group8/issues/276)
* [Issue BE-28](https://github.com/bounswe/bounswe2022group8/issues/302)
  
**Management Related Issues**
* Unfortunatelly, I don't have any management related issues.

**Pull Requests**
* [feature/BE-27](https://github.com/bounswe/bounswe2022group8/pull/319)
* [feature/BE-28](https://github.com/bounswe/bounswe2022group8/pull/315)

**Additional**
    
PR reviews:
* [feature/BE-22](https://github.com/bounswe/bounswe2022group8/pull/274)
* [feature/BE-17](https://github.com/bounswe/bounswe2022group8/pull/251)  


## Milestone 3

### Responsibilities 
* reviewing the PR's of our team
* Contributing to the milestone report

### Contributions
* Reviewing the bid related PR [hotfix/BE-38: new_bids reset](https://github.com/bounswe/bounswe2022group8/pull/397)
* Creating user manuals for both web and mobile applications[MIL-26 User Manual](https://github.com/bounswe/bounswe2022group8/issues/422), [web user manual](https://github.com/bounswe/bounswe2022group8/blob/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/web_app_user_manual.md) ,[mobile user manual](https://github.com/bounswe/bounswe2022group8/blob/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/mobile_app_user_manual.md)

* Adding more than 10 art items and creating 2 exhibitions [MIL-28 Creating 10 artitem/online exhibitons](https://github.com/bounswe/bounswe2022group8/issues/424)

* Creating a comprehensive scenario that covers all functionalities [MIL-27 The Comprehensive Scenario](https://github.com/bounswe/bounswe2022group8/issues/423),   [the comprehensive scenario](https://github.com/bounswe/bounswe2022group8/blob/master/Deliverables/CMPE451_Customer_Presentation_Milestone_3/the_comprehensive_scenario.md)


* Writing the project status summary [MIL-25 Project Status summary](https://github.com/bounswe/bounswe2022group8/issues/421)



</details>

<details>
    <summary> Elif Bayraktar </summary>
    
I am Elif Bayraktar, a member of Group 8, backend team. 

## Milestone 1

### MIL 1 -Responsibilities
   1. Reviewing/updating requirements (Bidding system, Notifications, Level and Verification Systems)
   2. Updating Use Case diagram.
   3. Researching different authentication and authorization mechanisms to set up our project the right way.
   4. Implementing the itinital models for the project.
   5. Implementing serializers and creating the admin site.
   6. Implementation of alternative registration API, using django authentication.
   7. Researching and implementing CICD workflow.

<details>
    <summary> MIL 1- Summary of work </summary>

| Hours spent | Task Type             | Task Description |
|  :----:       |  :----:   |  :----: |
|  Week 1       |  :----:   |  :----: |
|  2 hours  |  planning   |  Attended [weekly meeting/lab](https://github.com/bounswe/bounswe2022group8/wiki/Week-1-Meeting-Notes-1). |
|  15 minutes       |  documentation   |  Caught up with the repo updated necessary things.  |
|  Week 2       |  :----:   |  :----: |
|  1 hour 45 minutes  |  planning   |  Attended [weekly meeting/lab](https://github.com/bounswe/bounswe2022group8/wiki/Week-2-Meeting-%232). |
|  2 hours  |  planning   |  Attended [weekly meeting](https://github.com/bounswe/bounswe2022group8/wiki/Week-2--Meeting-Notes-3). |
|  2 hours       |  revision/documentation   |  Revised the requirements, critically revised Bidding system, Notifications, Level and Verification systems. Here are related issues [GEN-10](https://github.com/bounswe/bounswe2022group8/issues/162), [GEN-11](https://github.com/bounswe/bounswe2022group8/issues/163), [GEN-14](https://github.com/bounswe/bounswe2022group8/issues/166), [GEN-15](https://github.com/bounswe/bounswe2022group8/issues/167) |
|  30 minutes  |  coding/upkeep   |  Updated issue template to include new member [GEN-12](https://github.com/bounswe/bounswe2022group8/issues/164). |
|  15 minutes  |  documentation/wiki  |  Updated [questions and answers](https://github.com/bounswe/bounswe2022group8/wiki/Agenda-&-Questions-&-Answers) page [GEN-13](https://github.com/bounswe/bounswe2022group8/issues/165). |
|  Week 3       |  :----:   |  :----: |
|  1 hour 45 minutes  |  planning   |  Attended [weekly meeting/lab](https://github.com/bounswe/bounswe2022group8/wiki/Week-3-Backend-Meeting-Notes-1). |
|  30 minutes       |  documentation   |  Updated Bidding System requirements in accordance with last group meeting's decisions.[GEN-14](https://github.com/bounswe/bounswe2022group8/issues/166)  |
|  30 minutes       |  code review   |  Reviewed the initial for pull request. [Pull request](https://github.com/bounswe/bounswe2022group8/pull/180)  |
|  5 hours  |  Research/Implementation   |  Researched authentication and authorization to set up the initial structure of the project the correct way. Implemented initial models. [BE-4](https://github.com/bounswe/bounswe2022group8/issues/187), [Pull request](https://github.com/bounswe/bounswe2022group8/pull/190) |
|  30 minutes  |  planning   |  Attended backend catch-up meeting. |
|  2 hours  |  coding/documentation   |  Wrote the [issue](https://github.com/bounswe/bounswe2022group8/issues/187) for initial models. Implemented serializers, decorator and created/configured admin site. [commit](https://github.com/bounswe/bounswe2022group8/pull/190/commits/c14653b56797783697286c367fc99f694e11f8ff) |
|  40 minutes |  coding   |  Implemented initial homepage with templates. [commit](https://github.com/bounswe/bounswe2022group8/pull/190/commits/12d8b04e1501b8eeac734901b24529ff90b81f5e) |
|  30 minutes  |  coding  |  Merging the branch, some updates. [comment](https://github.com/bounswe/bounswe2022group8/pull/190#issuecomment-1288081724) |
|  45 minutes  |  research/review  |  Extra research about alternative methods of authentication, checking new commits to the repo. |
|  45 minutes  |  research  |  Researching CI/CD. [BE-11](https://github.com/bounswe/bounswe2022group8/issues/209) |
|  Week 4       |  :----:   |  :----: |
|  2 hours  |  planning   |  Attended [weekly meeting/lab](https://github.com/bounswe/bounswe2022group8/wiki/Week-4--Meeting-Notes-4). |
|  45 minutes       |  documentation   |  Created [wiki page](https://github.com/bounswe/bounswe2022group8/wiki/Django-Practices) for best django practices, and research links. [GEN-26](https://github.com/bounswe/bounswe2022group8/issues/197)  |
|  3 hours  |  implementation   |  Implemented alternative register (and part of logout) API's that use django authentication rather than Knox. |
|  5 hours  |  devops   |  Setting up Docker. |
|  2.5 hours  |  learning/implementation/devops   |  Learned how to use GitHub Actions. Implemented a workflow including testing and dockerization. Need to make some updates for testing. [BE-11](https://github.com/bounswe/bounswe2022group8/issues/209) [Pull Request](https://github.com/bounswe/bounswe2022group8/pull/215) |
|  1.5+ hours  |  reviewing   | Keeping up with repo, reviewing/updating mockups. [GEN-19](https://github.com/bounswe/bounswe2022group8/issues/171) |
|  -  |  planning   |  Naming the app [GEN-28](https://github.com/bounswe/bounswe2022group8/issues/212) |
|  1.25 hours  |  documentation   |  Updating timesheets. |
|  2 hours  |  planning   |  Preparing for Milestone presentation. |
|  1.1 hours  |  documentation   |  Preparing Personal Contribution report for milestone deliverables. |
|  Week 5       |  :----:   |  :----: |
|  1 hour  |  documentation   |  Organized and added [BE Meeting#2 notes](https://github.com/bounswe/bounswe2022group8/wiki/Week-5--BE-Meeting-%232-(02.11.2022)) to wiki. [Issue link](https://github.com/bounswe/bounswe2022group8/issues/240) |
|         |  documentation   |  Adding work summary and work performed to Group Review Report, updating timesheet.  |

</details>


## Milestone 2

### MIL 2 -Responsibilities
* Creating APIs for password reset (both for with or without login)(x3 APIs in total).
* Configuring app settings and an email server for sending automated otp emails through the app for password reset.
* Updating the comment model to accommodate replies and the hierarchy (using django-mptt).
* Creating APIs for CRUD comment operations and get all comments of art item(x5 APIs in total).
* Creating Swagger documentation for all of these APIs.
* Researching about GitHub Packages, Personal Access Tokens and how to use them in workflows.
* Creating GitHub Workflow for building and pushing docker images.
* Writing the executive summary for the milestone2 report.
* PR Review: Swagger Integration feature/BE-14
* PR Review: hotfix/BE-14
* PR Review: Feature/BE-23 Tag APIs    
* PR Review: feature/BE-27 Account deletion API



### MIL 2 -Main Contributions
I already listed my main responsibilities and contributions above. Other than those, I tried to write detailed explanations about usage of the tools I integrated (such as github packages) and provided detailed explanations for my PRs. I tried to help teammates with testing their code when available.
    
**Code Related Issues**
* [BE-19: Implementation of Reset Password API (Forgot password & logged in)](https://github.com/bounswe/bounswe2022group8/issues/254)
* [BE-20: Comment System](https://github.com/bounswe/bounswe2022group8/issues/261)
* [BE-11: CI/CD Research and Implementation](https://github.com/bounswe/bounswe2022group8/issues/209)
    
**Management Related Issues**
* [MIL-8: Milestone 2 Group Review/Executive Summary](https://github.com/bounswe/bounswe2022group8/issues/295)
* [BE-11: CI/CD Research and Implementation](https://github.com/bounswe/bounswe2022group8/issues/209)


**Pull Requests**
* [PR:Feature/be 19 ](https://github.com/bounswe/bounswe2022group8/pull/259)
* [PR:Feature/be 20](https://github.com/bounswe/bounswe2022group8/pull/262)
* [PR:Feature/BE11](https://github.com/bounswe/bounswe2022group8/pull/215)
    

**Unit Tests**

* `test_comment_creation`
* `test_comment_deletion_cascaded` 

**Additional**
    
PR reviews:<br>
* [feature/BE-14](https://github.com/bounswe/bounswe2022group8/pull/245)
* [hotfix/BE-14](https://github.com/bounswe/bounswe2022group8/pull/255)
* [PR:feature/BE-27 Account deletion API](https://github.com/bounswe/bounswe2022group8/pull/319)
* [Feature/BE-23 Tag APIs](https://github.com/bounswe/bounswe2022group8/pull/292)


## Milestone 3

### MIL 3 - Responsibilities
* Figuring out and implementing how to track user activity. Creating a separate app for user history.
* Updating type/category structure of Art Items.
* Implementing User Level system including API and automatic update.
* Implementation of Bidding System. Both infrastructure models and APIs.
* Implementation of Recommendation System. 
  * Implementation of popularity separately for artitem, user and exhibitions, taking into account different parameters including aging with time.
  * Implementation of user interests model, necessary signals, connections for updating.
  * Implementation of recommendation APIs, including logged in and anonymous cases.
* Implementation of unittests.
* Creating a release draft and reviewing requirements for release.
* Revising all requirements marking their status.
* Update and addition of new requirements.
* Updating the use case diagram.
* Writing part of executive summary.
* Reviewing PRs, and keeping up with overall project status at all times.

### MIL 3 - Main Contributions
I listed above my main contributions. I tried to fulfill my responsibilities in time. I kept in touch with teammates, and tried to help run development process as smoothly as possible. Documented my work in detail.
    
**Code Related Issues**
* [BE-32 : User History](https://github.com/bounswe/bounswe2022group8/issues/353)
* [BE-35: Art Item Category](https://github.com/bounswe/bounswe2022group8/issues/357)
* [BE-36: User Level](https://github.com/bounswe/bounswe2022group8/issues/361)
* [BE-38: Bidding System](https://github.com/bounswe/bounswe2022group8/issues/369)
* [BE-40: Recommendation System](https://github.com/bounswe/bounswe2022group8/issues/372)
* [BE-43: BE Tests+](https://github.com/bounswe/bounswe2022group8/issues/403)


**Management Related Issues**
* [MIL-22: Software Requirements Specification](https://github.com/bounswe/bounswe2022group8/issues/414)
* [MIL-29: Status of the requirements](https://github.com/bounswe/bounswe2022group8/issues/425)
* [MIL-32: Use Case Diagram Update](https://github.com/bounswe/bounswe2022group8/issues/428)
* [MIL-39: Executive/ what could have been done differently](https://github.com/bounswe/bounswe2022group8/issues/440)

**Pull Requests**
* [feature/BE-32 : User History](https://github.com/bounswe/bounswe2022group8/pull/354)
* [feature/BE-35: Art Item Category](https://github.com/bounswe/bounswe2022group8/pull/358)
* [feature/BE-36: User Level](https://github.com/bounswe/bounswe2022group8/pull/364)
* [feature/BE-38: Bidding System](https://github.com/bounswe/bounswe2022group8/pull/371)
* [feature/BE-40: Recommendation System](https://github.com/bounswe/bounswe2022group8/pull/386)
* [feature/BE-43: Backend Unittests [2]](https://github.com/bounswe/bounswe2022group8/pull/404)
* [hotfix/BE-38: new_bids reset](https://github.com/bounswe/bounswe2022group8/pull/397)


**Unit Tests**
* `test_open_item_for_sale`
* `test_bid_on_art_item`
* `test_bid_on_art_item_fail`
* `test_get_all_bids_on_art_item`
* `test_get_bids_on_art_item_fail`
* `test_reply_to_bid`
* `test_get_bid`
* `test_recommendation_artitem`
* `test_recommendation_artitem_viewed`
* `test_recommendation_artitem_anonymous`
* `test_recommendation_exhibition_anonymous`
* `test_recommendation_user`
* `test_recommendation_user_following`
* `test_comment_creation`
* `test_comment_deletion_cascaded`
* I also added documentation of tests in the files.



**Additional**

PR Reviews:
* [feature/BE-30: Exhibitions](https://github.com/bounswe/bounswe2022group8/pull/344) 
* [feature/BE-39: Backend Unittests [1]](https://github.com/bounswe/bounswe2022group8/pull/382)
* [feature/MIL-20: API Endpoints](https://github.com/bounswe/bounswe2022group8/pull/412)
    

</details>



<details>
    <summary> Mustafa Cihan </summary>
    I am Mustafa Cihan, a team member of the Group 8. I specificly work on the Mobile development part of our project. 

## Milestone 1
### Milestone 1 Responsibilities
I am responsible for mobile application. For this milestone I mostly worked on frontend of mobile application. I designed landing page, login page, signup page and home page. Also I implemented pages that I designed. I set up inital mobile application that my team built desired functionalities. I am responsible for general mobile application development frame. 

### Milestone 1 Main Contributions
I designed and implemented landing page, login page, signup page and home page. I set up inital mobile application that my team built desired functionalities. I mainly worked on mobile app so I gave most of my effort to develop mobile application. 

**Code Related Issues**
* [MOB-1: Design and Code Flutter Files for Login and Sign-Up](https://github.com/bounswe/bounswe2022group8/issues/198)
* [MOB-4: Creating a Homepage](https://github.com/bounswe/bounswe2022group8/issues/213)
* [MOB-5: Adding error notifications on login and sign-up]()
* [MOB-3: Connecting Mobile App with Backend](https://github.com/bounswe/bounswe2022group8/issues/208) made [commit](https://github.com/bounswe/bounswe2022group8/commit/ab54c1f7421d943cb31c427005342a2c24466440)  to this issue.

**Management Related Issues**
* [GEN-27: Meeting Notes: Week#4 Meeting#4](https://github.com/bounswe/bounswe2022group8/issues/207)
* [MOB-2: Meeting Notes: Week#3 Mobile Meeting#1](https://github.com/bounswe/bounswe2022group8/issues/205)
* [GEN-25:Revise the Copyright Infringement Requirement](https://github.com/bounswe/bounswe2022group8/issues/178)
* [GEN-21: Create a Wikipage for Conventions](https://github.com/bounswe/bounswe2022group8/issues/173)
* [GEN-3: Week #1 Meeting #1 Notes](https://github.com/bounswe/bounswe2022group8/issues/155)

**Pull Requests**
* [feature/MOB-1](https://github.com/bounswe/bounswe2022group8/pull/204)
* [feature/MOB-4](https://github.com/bounswe/bounswe2022group8/pull/216)
* [feature/MOB-5](https://github.com/bounswe/bounswe2022group8/pull/219)
* Reviewed [Feature/MOB-3](https://github.com/bounswe/bounswe2022group8/pull/221)

## Milestone 2
### Milestone 2 Responsibilities
In this milestone I am responsible for redesigning and implementing art item page, homepage and comment page. I am also responsible for implementing like and unlike functionality. In comment page user can add comments and view comments. In art item page user can see art item definition likes and comments. 

### Milestone 2 Main Contributions
I redesigned most of the pages in a way that customers wanted. Mainly I worked on art item page, homepage and comment page. I designed these pages and implemented them. In art item page user can see art item definition likes and comments. I choose to not include these fields to homepage so users can easliy focus on the art item. So in art item page user can see definition of art item. By clicking comment button on art item user can go to comment sections and view comments and/or add comments. Also user can like or unlike art items.

**Code Related Issues**
* [MOB-16: Connecting Comment Page](https://github.com/bounswe/bounswe2022group8/issues/316)
* [MOB-15: Static Comment Page](https://github.com/bounswe/bounswe2022group8/issues/315)
* [MOB-14: Revising Homepage](https://github.com/bounswe/bounswe2022group8/issues/289)
* [MOB-13: Revise Signup and Login page](https://github.com/bounswe/bounswe2022group8/issues/287)
* [MOB-8: Creating Art Item Pages](https://github.com/bounswe/bounswe2022group8/issues/282)
* [MOB-6: Revising Landing Page](https://github.com/bounswe/bounswe2022group8/issues/238)
  
**Management Related Issues**
* Unfortunatelly, I don't have any management related issues.

**Pull Requests**
* [feature/MOB-6](https://github.com/bounswe/bounswe2022group8/pull/239)
* [Feature/MOB-13](https://github.com/bounswe/bounswe2022group8/pull/314)
* [feature/MOB-20](https://github.com/bounswe/bounswe2022group8/pull/331)

## Milestone 3
### Milestone 3 Responsibilities
In this milestone I am mainly responsible for annotations on mobile applications. Some other responsibilities are fixing bugs and making design changes in required pages.

### Milestone 3 Main Contributions
I tried to add both image and text annotation on mobile application. But I was unable to add image annotation. I made deep research about how can i make annotations. I tried to find annotation library in flutter project but unfortunatelly I couldn't find any. So i designed and implemented text annotation based on the researches that i made. I also fixed some bugs and made design changes in required pages.

**Code Related Issues**
* [MOB-24: Like Functionality](https://github.com/bounswe/bounswe2022group8/issues/399)
* [MOB-22: Text Annotations](https://github.com/bounswe/bounswe2022group8/issues/398)

**Management Related Issues**
* [MIL-30: Status of The Annotations in Mobile Application](https://github.com/bounswe/bounswe2022group8/issues/426)
* [MIL-38: Adding Mobile UI to Document](https://github.com/bounswe/bounswe2022group8/issues/436)

**Pull Requests**
* [feature/MOB-24](https://github.com/bounswe/bounswe2022group8/pull/401)
* [feature/MOB-22](https://github.com/bounswe/bounswe2022group8/pull/400)
* [Feature/MOB-21: Bug fixes after Milestone 2](https://github.com/bounswe/bounswe2022group8/pull/380)



</details>


<details>
    <summary> Metehan Dündar </summary>
I am Metehan Dündar, a member of group 8. I work on the mobile team.

## Milestone 1
### Milestone 1 Responsibilities
Revisioning of requirements and updating necessary changes. (Search and Location)
Implementation of logout API.
    
### Milestone 1 Main Contributions
I updated the specifications and participated in the choices we were making on the project's functionalities. I have been there at each of our meetings. I helped my team to present our product to the customers. Due to certain technical issues, I was unable to submit any code for this milestone. I make a commitment to putting in greater effort as we go.

**Milestone 1 Code Related Issues**
* [BE-3: PostgreSQL Integration to the application](https://github.com/bounswe/bounswe2022group8/issues/182)
* [BE-4: Setting up initial models](https://github.com/bounswe/bounswe2022group8/pull/190)
* [BE-10: [API] Implementation of Logout Endpoint](https://github.com/bounswe/bounswe2022group8/issues/199)
    
**Milestone 1 Management Related Issues**
* [GEN-5: Adding CmpE451 section to the personal Timesheet pages](https://github.com/bounswe/bounswe2022group8/issues/157)
* [GEN-19: Revise Mockups](https://github.com/bounswe/bounswe2022group8/issues/171)
* [GEN-28: Name for application](https://github.com/bounswe/bounswe2022group8/issues/212)
* [GEN-22: Revise Search](https://github.com/bounswe/bounswe2022group8/issues/174)
* [GEN-23: Revise Location](https://github.com/bounswe/bounswe2022group8/issues/175)

    
## Milestone 2
### Milestone 2 Responsibilities
* Changing label ordering/systems.
* Creating several logo designs.
* Presenting mobile application to customers as an art-dummy user.
* Implementing the forgot and confirm password pages.
* Research on Annotation.
    
### Milestone 2 Main Contributions
I already listed my main responsibilities and contributions above. Other than those, since I changed the team, many thanks to Dogukan, I fastly integrated to mobile team, and I contributed their coding works.

**Milestone 2 Code Related Issues**
* [MOB-21: Forgot & Confirm Password Pages)](https://github.com/bounswe/bounswe2022group8/issues/350)
    
**Milestone 2 Management Related Issues**
* [GEN-32: Logo for Application](https://github.com/bounswe/bounswe2022group8/issues/268)
* [GEN-33: Label Ordering](https://github.com/bounswe/bounswe2022group8/issues/273)
* [GEN-35: Application Name and Logo](https://github.com/bounswe/bounswe2022group8/issues/290)
    
**Milestone 2 Pull Requests**
* [feature/MOB-16](https://github.com/bounswe/bounswe2022group8/pull/319)
    
## Milestone 3
### Milestone 3 Responsibilities
For the mobile part of our project, we wanted to include some additional features after the Second Milestone. We distributed the tasks among the mobile team and I was responsible for implementing the pages for users who follow or are followed by other users.
    
### Milestone 3 Main Contributions
I was working on creating the pages for the profile's following and follower users. Since I haven't practiced coding in the Dart language, I had a lot of difficulty creating these pages as desired.

**Milestone 3 Code Related Issues**
* [MOB-25: Follower & Following Pages ](https://github.com/bounswe/bounswe2022group8/issues/410)
    
**Milestone 3 Management Related Issues**
* Presentation for Final Customer Milestone
    
**Milestone 3 Pull Requests**
* [feature/MOB-21 : Following & Follower Users' Page](https://github.com/bounswe/bounswe2022group8/tree/feature/MOB-21)

</details>

<details>
    <summary> Mustafa Emre Erengül </summary>

I am Mustafa Emre Erengül, a team member of the Group 8. I specificly work on the Mobile development part of our project.

## Milestone 1
### Milestone 1 Responsibilities
Setting the environment for the mobile development and learning basic Flutter/Dart to implement the initial pages. Creating the basic version of the mobile app which can run the functionalities that Backend team provided. Debugging the error-messages and dependency problems. Preparing a simple & stable version of the mobile app for the Milestone 1 Customer presentation.
    
### Milestone 1 Main Contributions
Help to launch the initial version of the mobile app. Contribute to creation of the 3 main pages (Sign-up, login and home pages) that are required for the Milestone 1. Also designing issues and the colour palette for the app background.<br/>

**Milestone 1 Code Related Issues**
* [MOB-1: Design and Code Flutter Files for Login and Sign-Up](https://github.com/bounswe/bounswe2022group8/issues/198) (reviewed & closed)
* [MOB-4: Creating a Homepage](https://github.com/bounswe/bounswe2022group8/issues/213) (reviewed & closed)
    
**Milestone 1 Management Related Issues**
* [GEN-4: Updating Wiki pages related to the last semester](https://github.com/bounswe/bounswe2022group8/issues/156) (opened)
* [GEN-5: Adding CmpE451 section to the personal Timesheet pages](https://github.com/bounswe/bounswe2022group8/issues/157) (opened)
* [GEN-7: Update the Communication Plan](https://github.com/bounswe/bounswe2022group8/issues/159) (contributed)
* [GEN-10: Review&Revise the Requirements](https://github.com/bounswe/bounswe2022group8/issues/162) (contributed)
* [GEN-22: Revise Search](https://github.com/bounswe/bounswe2022group8/issues/174) (completed)
* [GEN-23: Revise Location](https://github.com/bounswe/bounswe2022group8/issues/175) (completed)
* [MIL-5: Milestone 1 Group Review](https://github.com/bounswe/bounswe2022group8/issues/226) (opened)
    
**Milestone 1 Pull Requests**
* [feature/MOB-5](https://github.com/bounswe/bounswe2022group8/pull/219) (reviewed)

## Milestone 2
### Milestone 2 Responsibilities
In the mobile application part of our project, we had some implementations that we would like to add before the Second Milestone. So we shared the implementations among our mobile team. As a team member I was responsible for implementations of creating a profile page, settings (editing profile) page, change password page, updating profile photo page and a page that allows users to add a new art item to their profile.
    
### Milestone 2 Main Contributions
I implemented a profile page that allows users to display their uploaded art items and the exhibitions that they are attending. One can see user's username, name, surname, bio, location and profile photo by looking at this page. I also implement a settings page to enable users to make changes over this fields. Moreover a user can change his/her password and profile photo. Lastly I created an upload art item page which allows users to add new art items to their profile.  <br/>

**Milestone 2 Code Related Issues**
* [MOB-7: Creating a profile page](https://github.com/bounswe/bounswe2022group8/issues/281) (implemented)
* [MOB-9: Redesign of the main navigation bar](https://github.com/bounswe/bounswe2022group8/issues/283) (implemented)
* [MOB-10: Changing password and the profile photo](https://github.com/bounswe/bounswe2022group8/issues/284) (implemented)
* [MOB-11: Uploading a new art item to the profile](https://github.com/bounswe/bounswe2022group8/issues/285) (implemented)
* [MOB-12: Renewing the mobile app icon and the name](https://github.com/bounswe/bounswe2022group8/issues/286) (implemented)
    
**Milestone 2 Management Related Issues**
* [GEN-32: Logo for Application](https://github.com/bounswe/bounswe2022group8/issues/268) (contributed)
* [GEN-35: Application Name and Logo](https://github.com/bounswe/bounswe2022group8/issues/290) (completed)
    
**Milestone 2 Pull Requests**
* [feature/MOB-7 : Profile Page Implementation](https://github.com/bounswe/bounswe2022group8/pull/280)
* [feature/MOB-8 : Editing Profile and Uploading Art Item](https://github.com/bounswe/bounswe2022group8/pull/323)
* [feature/MOB-9 : Change Password & Profile Photo](https://github.com/bounswe/bounswe2022group8/pull/327)

***Milestone 2 Additional***
* [Feature/MOB-13](https://github.com/bounswe/bounswe2022group8/pull/314) (reviewed)
* [Feature/mob 18](https://github.com/bounswe/bounswe2022group8/pull/325) (reviewed)
    
## Milestone 3
### Milestone 3 Responsibilities
In the mobile application part of our project, we had some implementations that we would like to add before the FinalMilestone. So we shared the implementations among our mobile team. As a team member I was responsible for implementations of creating the search page and searching functionality, following/unfollowing a user, visiting other users profile page and following/followers page.
    
### Milestone 3 Main Contributions
I implemented a search page that allows users to search both other users or other user’s art items. One can now search with keywords to find their favorite art items. I also implement visiting other people’s profile feature so that one can see other user’s all art contributions. Moreover inside this page a user can follow/unfollow another user by simply clicking a follow button. Lastly I created following/followers page which allows users to who is following or being followed by a profile.  <br/>

**Milestone 3 Code Related Issues**
* [MOB-25: Follower & Following Pages](https://github.com/bounswe/bounswe2022group8/issues/410) (contributed)
* [MOB-26: Visiting Another User's Profile](https://github.com/bounswe/bounswe2022group8/issues/435) (implemented)
* [MOB-27: Following and Unfollowing Functionality](https://github.com/bounswe/bounswe2022group8/issues/438) (implemented)
* [MOB-28: Search Page and Searching Functionality](https://github.com/bounswe/bounswe2022group8/issues/439) (implemented)
    
**Milestone 3 Management Related Issues**
* [GEN-6: Logo for Application](https://github.com/bounswe/bounswe2022group8/issues/158) (completed)
* [MIL-36: Reflections to the Final Milestone Demo](https://github.com/bounswe/bounswe2022group8/issues/433) (completed)
* [MIL-37: Art Follower User Scenario](https://github.com/bounswe/bounswe2022group8/issues/434) (completed)
    
**Milestone 3 Pull Requests**
* [feature/MOB-22 : Visiting Other Profiles & Follow and Unfollow Buttons](https://github.com/bounswe/bounswe2022group8/pull/391)
* [feature/MOB-25 : Searching Users and Art Items](https://github.com/bounswe/bounswe2022group8/pull/402)

***Milestone 3 Additional***
* [feature/MOB-24](https://github.com/bounswe/bounswe2022group8/pull/401) (reviewed)
    
</details>

<details>
    <summary> Furkan Keskin </summary>
    
I'm Furkan Keskin and I'm a member of the group 8 frontend team.

## Milestone 1    
### MIL 1 - Responsibilities
* Research on frontend tools.
* Determining the color palette.
* Creation of the layout.
* Design and implementation of initial home page structure.
* Design and implementation of navigation bar, search bar and side bar.
* Implementation of login, signup pop-ups and backdrop.
* Design and implementation of image and gallery cards.
* Design and implementation of the footer.
* Preparing a welcome card.
* Preparing a sample gallery.
* Finding and styling logos compatible with our theme for the necessary parts.
    
### MIL 1 - Main Contributions
After researching the frontend tools with Sinem for a long time and deciding what to use, I reviewed a lot of art related websites to give ideas for design and functionality. I then created a draft color palette and layout (continuously updated throughout the development period). Afterwards, I did the entire design and styling of the home page including navigation bar, search bar, side bar, pop-ups, backdrop, cards, footer and necessary transitions of the components. During this process I also created a welcome card and a gallery of exhibitions to make our site look more aesthetically pleasing. Also, I put a lot of effort to make our site look good not only on big screens but also on small screens and implemented some styling differences for small screens. Finally, I designed and implemented the necessary components for authentication and created error messages for incorrect entries in sign up / log in forms.
    

**Code Related Issues**
* [FE-2](https://github.com/bounswe/bounswe2022group8/issues/185): Research on Frontend Tools 
* [FE-6](https://github.com/bounswe/bounswe2022group8/issues/231): Form errors and Log out
    
**Management Related Issues**
* [GEN-30](https://github.com/bounswe/bounswe2022group8/issues/230): Update the project plan
* [FE-1](https://github.com/bounswe/bounswe2022group8/issues/184): Meeting Notes: Week#3 Frontend Meeting#1
    
 **Pull Requests**
* [Feature/FE-3](https://github.com/bounswe/bounswe2022group8/pull/220)
* [Feature/FE-6](https://github.com/bounswe/bounswe2022group8/pull/223)
* Reviewed [Feature/FE-5](https://github.com/bounswe/bounswe2022group8/pull/218)
    
## Milestone 2
### MIL 2 - Responsibilities
* Form error interface.
* Finding a solution to the cache bug.
* Forgot Password interface.
* Settings Page interface and connections.
* Reset Password interface and connection.
* Profile Page interface and connections.
* Art Item Upload interface and connections.
* Handling the front end side of the image upload. (AWS s3, base 64, preview etc.)
* Art Item Page interface and connections.
* Comment Section interface and connections.
* Tag interface.
* Connecting the home and discover pages.
* Transitions between pages for a better user experience such as loading screens and notification pop-ups.
* Writing unit tests for some components.
* CSS and design improvements when Sinem needed help.
* Communication with the backend team for the integration stage.
* Project Plan updates.
* Note taker in a general meeting.
* Note taker in multiple front-end meetings.
* PR and issue reviews of the front end side.
* Testing some API endpoints from postman. (Some backend PR reviews as well)
* Providing sample art items/gallery for the presentation.
* Presenting the web side of the project.
* Filling in the Annotations section in the Milestone 2 report.
* Filling in the Standards section in the Milestone 2 report.
    
### MIL 2 - Main Contributions
Since we are a fairly small sub-team, my responsibilities were not exactly in line with the project plan and were updated regularly, but in general I was able to take the above responsibilities and deliver them. Though I didn't do a very good job with some of them. 

    
**Code Related Issues**
* [FE-7](https://github.com/bounswe/bounswe2022group8/issues/232)
* [FE-8](https://github.com/bounswe/bounswe2022group8/issues/233)
* [FE-10](https://github.com/bounswe/bounswe2022group8/issues/241)
* [FE-11](https://github.com/bounswe/bounswe2022group8/issues/257)
* [FE-12](https://github.com/bounswe/bounswe2022group8/issues/260)
* [FE-14](https://github.com/bounswe/bounswe2022group8/issues/266)
* [FE-20](https://github.com/bounswe/bounswe2022group8/issues/310)
* [FE-23](https://github.com/bounswe/bounswe2022group8/issues/338)
    
    
**Management Related Issues**
* [MIL-14](https://github.com/bounswe/bounswe2022group8/issues/340)
* [MIL-15](https://github.com/bounswe/bounswe2022group8/issues/341)
* [MIL-16](https://github.com/bounswe/bounswe2022group8/issues/342)
    
    
**Pull Requests**  
* [feature/FE-8](https://github.com/bounswe/bounswe2022group8/pull/253)
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/271)
* [feature/FE-20](https://github.com/bounswe/bounswe2022group8/pull/322)
* [feature/FE-21](https://github.com/bounswe/bounswe2022group8/pull/330)
* [feature/FE-22](https://github.com/bounswe/bounswe2022group8/pull/334)
* [hotfix/FE-20](https://github.com/bounswe/bounswe2022group8/pull/337)
* [feature/FE-23](https://github.com/bounswe/bounswe2022group8/pull/339)
    

**Unit Tests**

You can find frontend unit tests [here.](https://github.com/bounswe/bounswe2022group8/tree/master/App/frontend/src/components/__test__)

My unittests:
    
* `HomeFooter.test.js`
* `IntroImage.test.js`
* `LoginModal.test.js`
* `ResetPasswordModal.test.js`
* `Searchbar.test.js`
    
    
**Additional**
    
PR reviews:
* [feature/BE-18](https://github.com/bounswe/bounswe2022group8/pull/252)
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/256)
* [feature/BE-21](https://github.com/bounswe/bounswe2022group8/pull/270)
    
    
## Milestone 3
### MIL 3 - Responsibilities
* Implementation of other user's profile page.
* Implementation of like functionality on frontend.
* Implementation of follow/unfollow functionalities on frontend.
* Implementation of forgot/reset password interfaces and backend connections.
* Implementation of tag related interfaces and backend connections.
* Implementation of exhibiton related interfaces and backend connections.
* Implementation of search related interfaces and backend connections.
* Improvement on the styling when necessary.
* PR and issue reviews on the frontend.
* Backend PR reviews when necessary.
* Updating the project plan
    
### MIL 3 - Main contributions
For the final milestone, I took responsibility for the front-end of the features that we had targeted for the previous milestone but couldn't deliver. On top of that, I took responsibility for everything related to exhibition and search on the front-end. In short, for this milestone, I was directly involved in the implementation and design of the following features: other's profile page, like, follow/unfollow, reset/forgot password, tags, dropdowns, deletion of artitems/exhibitions, online exhibiton and search. Apart from these, I have been in constant contact with the backend during the whole project and whenever Sinem, the other member of the frontend team, needed help, I tried to help as much as I could. Lastly, I was responsible for monitoring and updating the project plan. 
    
**Code Related Issues**
* [FE-10](https://github.com/bounswe/bounswe2022group8/issues/241) 
* [FE-12](https://github.com/bounswe/bounswe2022group8/issues/260)
* [FE-24](https://github.com/bounswe/bounswe2022group8/issues/362) 
* [FE-25](https://github.com/bounswe/bounswe2022group8/issues/363)
* [FE-26](https://github.com/bounswe/bounswe2022group8/issues/373) 
* [FE-28](https://github.com/bounswe/bounswe2022group8/issues/378)  
* [FE-29](https://github.com/bounswe/bounswe2022group8/issues/383) 
* [FE-32](https://github.com/bounswe/bounswe2022group8/issues/406)   
    
**Management Related Issues**
    
**Pull Requests**
* [feature/FE-12](https://github.com/bounswe/bounswe2022group8/pull/355)
* [feature/FE-18](https://github.com/bounswe/bounswe2022group8/pull/360)
* [feature/FE-24](https://github.com/bounswe/bounswe2022group8/pull/374)
* [feature/FE-25](https://github.com/bounswe/bounswe2022group8/pull/375)
* [feature/FE-28](https://github.com/bounswe/bounswe2022group8/pull/394)
* [feature/FE-29](https://github.com/bounswe/bounswe2022group8/pull/396)
* [feature/FE-32](https://github.com/bounswe/bounswe2022group8/pull/415)

**Unit Tests**
    

**Additional**
  
PR reviews:
* [BE-37](https://github.com/bounswe/bounswe2022group8/pull/368)
* [FE-19](https://github.com/bounswe/bounswe2022group8/pull/376)
* [BE-30.1](https://github.com/bounswe/bounswe2022group8/pull/390)
* [FE-27](https://github.com/bounswe/bounswe2022group8/pull/392)
* [BE-30.2](https://github.com/bounswe/bounswe2022group8/pull/395)
* [FE-31](https://github.com/bounswe/bounswe2022group8/pull/408)
    
    
    


</details>


<details>
    <summary> Sinem Koçoğlu </summary>
    
I am Sinem Koçoğlu and I am member of group 8 frontend team.

## Milestone 1
    
### Mil-1 Responsibilities
* Creation of first design of login and signup pages.
* Research on frontend tools.
* Providing authentication for login and signup.
* Providing connection to backend.
* Dockerization of frontend.

### Mil-1 Main Contributions
I have created the first view for login and signup pages while creating the frontend project. I shared my knowledge about frontend tools with my teammate. Then, I studied and worked on authentication and tokenizaton for login and sign up. I configured backend and database on local in order to test if authentication and tokenization works well. I did research on dockerization of frontend projects and dockerize it.

**Code Related Issues**
* [FE-2](https://github.com/bounswe/bounswe2022group8/issues/185): Research on Frontend Tools 
* [FE-3](https://github.com/bounswe/bounswe2022group8/issues/186): Design and code CSS Files for Login and Sign Up 
* [FE-4](https://github.com/bounswe/bounswe2022group8/issues/203): Connection Between Backend and Frontend
* [FE-5](https://github.com/bounswe/bounswe2022group8/issues/217): Dockerize frontend

**Management Related Issues**
* [GEN-16](https://github.com/bounswe/bounswe2022group8/issues/168): Revise Profile Management 
* [GEN-17](https://github.com/bounswe/bounswe2022group8/issues/169): Revise Exhibition
* [GEN-25](https://github.com/bounswe/bounswe2022group8/issues/177): Meeting Notes: Week#2 Meeting#3

**Pull Requests**
* [Feature/FE-5](https://github.com/bounswe/bounswe2022group8/pull/218)
* Reviewed [Feature/FE-3](https://github.com/bounswe/bounswe2022group8/pull/220)
* 
**Additional Information**
* First, I have created project in [CodeSandBox](https://codesandbox.io/s/artcommunityplatform-ilgl9c?file=/src/Login.js) to experience css tools.Then, Furkan Keskin took the responsibility of creating design by using css. That's way, he uploaded the project to git.
* I did not create a pr to merge authentication file to the branch 'feature/FE-3' because I have already downloaded updated backend folder to my branch to test if everything worked well. Not to destruct folder structure, Furkan Keskin copied the only authentication file manually to his branch.

## Milestone 2


### Mil-2 Responsibilities
* Creation of the first design of profile page.
* Study different settings pages to discuss in lab session with Furkan Keskin.
* Improvement on profile page and first design of art item page.
* Creation and design of recommendation pages.
* Logo integration and typo correction on frontend.
* PR Review: hotfix/FE-20
* PR Review: feature/FE-23
* Adding user interfaces for web to the Milestone II document.
* Taking notes during Week#10 Meeting#7
* Providing follow functionality on frontend. (not completed due to health issues)
* Providing hover over text annotation on frontend. (not completed due to health issues)

### Mil-2 Main Contributions
I have created the first design of profile page. Then, worked on design of settings page but I couldn't create a good design. That's why, Furkan Keskin took the responsibility of it and I created the first view of art item page that was improved by Furkan Keskin later. Then, I took the responsibility of creation of recommendation pages of frontend. I made changes according to the feedback we got in Milestone I presentation. I couldn't complete my tasks due to some health issues. They will be provided until final milestone.
    
**Code Related Issues**
* [FE-10](https://github.com/bounswe/bounswe2022group8/issues/241)
* [FE-15](https://github.com/bounswe/bounswe2022group8/issues/267)
* [FE-16](https://github.com/bounswe/bounswe2022group8/issues/305)
* [FE-17](https://github.com/bounswe/bounswe2022group8/issues/307)

**Management Related Issues**
* [GEN-36](https://github.com/bounswe/bounswe2022group8/issues/336)


**Pull Requests**
* [feature/FE-16](https://github.com/bounswe/bounswe2022group8/pull/309)
* [feature/FE-15](https://github.com/bounswe/bounswe2022group8/pull/304)


**Unit Tests**

You can find frotend unittests [here](https://github.com/bounswe/bounswe2022group8/tree/master/App/frontend/src/components/__test__)

My unittests:
    
* SignupModal.test.js
* SettingsProfilePopUp.test.js
* SettingsPasswordPopUp.test.js


**Additional**
    
PR reviews:
* [hotfix/FE-20](https://github.com/bounswe/bounswe2022group8/pull/337)
* [feature/FE-23](https://github.com/bounswe/bounswe2022group8/pull/339)

## Milestone 3
### Responsibilities
* Implementation of annotations on frontend and fixing related bugs.
* Implementation of bidding system on frontend.
* Providing backend connection for recommendation pages.
* PR Review:
    * feature/FE-12
    * feature/FE-18
    * feature/FE-24
    * feature/FE-25
    * feature/FE-28
    * feature/FE-29
* Adding user interfaces for web to the Final Milestone document.
* Updating scenario2-Artists with respect to the final version of the app.
* Reviewed requirements related to annotation and bidding.

### Main Contributions
I have implemented anything related to annotation on frontend and fixed related bugs by communicating with Karahan Sarıtaş, member of backend team. Then, I worked on implementation of bidding system on frontend. After completion of it, I took the the responsibility of providing backend connection of recommendation pages. For Milestone, I reviewed requirements related to annotation and bidding system, added user interfaces for the web and updated 2nd user scenario-Artist.
    
**Code Related Issues**
* [FE-19](https://github.com/bounswe/bounswe2022group8/issues/308)
* [FE-27](https://github.com/bounswe/bounswe2022group8/issues/377)
* [FE-31](https://github.com/bounswe/bounswe2022group8/issues/393)

**Management Related Issues**

**Pull Requests**
* [feature/FE-19](https://github.com/bounswe/bounswe2022group8/pull/376)
* [bugfix/FE-19](https://github.com/bounswe/bounswe2022group8/pull/389)
* [hotfix/FE-33](https://github.com/bounswe/bounswe2022group8/pull/417)
* [feature/FE-27](https://github.com/bounswe/bounswe2022group8/pull/392)
* [feature/FE-31](https://github.com/bounswe/bounswe2022group8/pull/408)

**Unit Tests**
    

**Additional**
    
PR reviews:
* [FE-29](https://github.com/bounswe/bounswe2022group8/pull/396)
* [FE-28](https://github.com/bounswe/bounswe2022group8/pull/394)
* [FE-25](https://github.com/bounswe/bounswe2022group8/pull/375)
* [FE-24](https://github.com/bounswe/bounswe2022group8/pull/374)
* [FE-18](https://github.com/bounswe/bounswe2022group8/pull/360)
* [FE-12](https://github.com/bounswe/bounswe2022group8/pull/355)


</details>

<details>
    <summary> Sena Mumcu </summary>

I am Sena Mumcu and I am a  member of group 8 backend team.

## Milestone 1
    
### Mil-1 Responsibilities
* Creating the initial integration of PostgreSQL and out Django application.
* Implementing login API.
* Implementing logout API.
* Taking notes during Milestone 1 presentation.
* Evaluating backend tools and processes for Milestone Group Review.

### Mil-1 Main Contributions

I have created the initial integration of our Django application and PostgreSQL. I shared my knowledge about the possible
alternatives of PostgreSQL and we decided to move on with it. I worked in the implementation of the login and logout API with 
the help of Karahan and I evaluated the tools we have used in backend for the milestone group review.

**Code Related Issues**
* [BE-10](https://github.com/bounswe/bounswe2022group8/issues/199)
* [BE-9](https://github.com/bounswe/bounswe2022group8/issues/195)
* [BE-3](https://github.com/bounswe/bounswe2022group8/issues/182)


**Management-Related Issues**
* [GEN-29](https://github.com/bounswe/bounswe2022group8/issues/242)

    
**Pull Requests**
* [feature/BE-9](https://github.com/bounswe/bounswe2022group8/pull/200)
* [feature/BE-3](https://github.com/bounswe/bounswe2022group8/pull/183)
    
**Additional Information**

* Attended group meetings and reviewed my teammates' work.

    
## Milestone 2

### Mil-2 Responsibilities

* Implementing the Tag related API endpoints.
* Testing the API endpoints I have written and documenting them using Swagger.
* Reviewing and testing my backendteam-members' PRs.
* Researching user flags in Django to implement tag creation and deletion APIs.
* Presenting the artist use case scenario during the second customer review.
* Helping the new backend team member get onboard.

### Main Contribution
    
My main contributions include coding API endpoints as well as supporting the team in management related issues. I tried to review my teammates's work quickly as possible to help the team progress and did my best to implement API endpoints.

**Code Related Issues**

* [BE-23: [API] Tag Managing](https://github.com/bounswe/bounswe2022group8/issues/277)
* [BE-25: Research on Moderator Flags](https://github.com/bounswe/bounswe2022group8/issues/278)
* [BE-26: [API] Semantic and Lexical Search](https://github.com/bounswe/bounswe2022group8/issues/279)
    
**Management Related Issues**

* [MIL-10: Milestone 2 Requirements](https://github.com/bounswe/bounswe2022group8/issues/299)
* [Meeting Notes: Week 9 BE Meeting 4](https://github.com/bounswe/bounswe2022group8/issues/297)
* [Week 9 - Meeting #6(29.11.2022)](https://github.com/bounswe/bounswe2022group8/issues/296)
* [GEN-35: Application Name and Logo](https://github.com/bounswe/bounswe2022group8/issues/290)
* [BE-31: Meeting Notes: Week 7 Backend-Meeting #3](https://github.com/bounswe/bounswe2022group8/issues/264)
    
**Pull Requests**
* [Feature/BE-23 Tag APIs](https://github.com/bounswe/bounswe2022group8/pull/292)

**Unit Tests**
    
Unfortunately I didn't write any unit tests.

**Additional Information**
    
PR reviews

* [feature/BE-24](https://github.com/bounswe/bounswe2022group8/pull/294#issuecomment-1331032342)
* [feature/BE-22](https://github.com/bounswe/bounswe2022group8/pull/291#issuecomment-1331030915)
* [feature/BE-16](https://github.com/bounswe/bounswe2022group8/pull/249#issuecomment-1318197777)
* [feature/BE-15](https://github.com/bounswe/bounswe2022group8/pull/247#issuecomment-1318189615)

## Milestone 3

# Mil-3 Responsibilities

* Implementing search functionality
* Writing the system manual for the backend of the application
* Writing the 'Changes in Development Process' part of the executive summary
* Creating mock data for the last milestone presentation

# Main Contribution

My main contribution in the last milestone was implementing search functionality. The search bar searchs users and art items 
using lexical search. 

**Code Related Issues**
* [BE-26:[API] Semantic and Lexical Search](https://github.com/bounswe/bounswe2022group8/issues/279)

**Management-Related Issues**
* [MIL-32](https://github.com/bounswe/bounswe2022group8/issues/429)
* [MIL-31](https://github.com/bounswe/bounswe2022group8/issues/427)

**Pull Requests**
* [feature/BE-23](https://github.com/bounswe/bounswe2022group8/pull/292)

    
</details>

<details>
    <summary> Karahan Sarıtaş </summary>
    
I am [Karahan Sarıtaş](https://github.com/bounswe/bounswe2022group8/wiki/Karahan-Sar%C4%B1ta%C5%9F), a member of group 8. I'm working in the backend team, also trying to help frontend whenever it's needed. 

## Milestone 1
   
### MIL 1 -Responsibilities
* Revision of requirements and making necessary changes.
* Creating the initial structure of our Django project. Configuration of settings for both development and production environment.
* Dockerization of the backend service.
* Implementation of registration API.
* Implementation of login API.
* Implementation of logout API.
* Research on tokenization and authentication mechanisms.
* Helping frontend team for the connection.
* Dockerization of frontend and deployment. 

### MIL 1 - Main Contributions
I made the initial configurations for the project, adjusted the settings and dockerized it and worked on API endpoints related to registration, login and logout. I made some research on tokenization to prefer a suitable methodology for the project. Meanwhile, I also helped frontend team to integrate their application with ours, use tokens for authentication and actively participated in inter-team communication to make sure that everything works ok.
    
**Code Related Issues**
* [BE-1: Initial Configurations for the App](https://github.com/bounswe/bounswe2022group8/issues/179)
* [BE-5: Dockerize the Django Application with PostgreSql](https://github.com/bounswe/bounswe2022group8/issues/188)
* [BE-6: Organization of api folder](https://github.com/bounswe/bounswe2022group8/issues/192)
* [BE-9: [API] Implementation of Login Endpoint](https://github.com/bounswe/bounswe2022group8/issues/195)
* [BE-10: [API] Implementation of Logout Endpoint](https://github.com/bounswe/bounswe2022group8/issues/199)
* [BE-8: [API] Implementation of Register Endpoint](https://github.com/bounswe/bounswe2022group8/issues/194)
* [BE-12: Integration Between Frontend and Backend](https://github.com/bounswe/bounswe2022group8/issues/211)
* [MIL-4: Last changes for Deployment before Milestone 1](https://github.com/bounswe/bounswe2022group8/issues/224)

**Management Related Issues**
* [GEN-8: Week #2 Meeting #2 Notes](https://github.com/bounswe/bounswe2022group8/issues/160)
* [GEN-10: Review&Revise the Requirements](https://github.com/bounswe/bounswe2022group8/issues/162)  (general issue)
* [GEN-11: Revise the Notifications](https://github.com/bounswe/bounswe2022group8/issues/163)
* [GEN-14: Revise the Bidding System](https://github.com/bounswe/bounswe2022group8/issues/166)
* [GEN-15: Revise Verification and Level System](https://github.com/bounswe/bounswe2022group8/issues/167)
* [MIL-1: Milestone I Deliverables](https://github.com/bounswe/bounswe2022group8/issues/201)
* [MIL-2: Software Requirements Specification](https://github.com/bounswe/bounswe2022group8/issues/202)
* [BE-2: Meeting Notes Week #3 Backend Meeting #1](https://github.com/bounswe/bounswe2022group8/issues/181)


**Pull Requests**
* [feature/BE-1](https://github.com/bounswe/bounswe2022group8/pull/180)
* [feature/BE-5](https://github.com/bounswe/bounswe2022group8/pull/189)
* [feature/BE-6](https://github.com/bounswe/bounswe2022group8/pull/191)
* [feature/BE-9](https://github.com/bounswe/bounswe2022group8/pull/200)
* [bugfix/BE-5](https://github.com/bounswe/bounswe2022group8/pull/206) 
* [feature/BE-12](https://github.com/bounswe/bounswe2022group8/pull/210)

**Additional**
    
PR reviews:<br>
* [feature/BE-4](https://github.com/bounswe/bounswe2022group8/pull/190)
* [feature/BE-11](https://github.com/bounswe/bounswe2022group8/pull/215)  (on-hold for now)
* [feature/MIL-4](https://github.com/bounswe/bounswe2022group8/pull/225) (worked on this as a pair)<br>
    
Throughout the week, I took the whole responsibility of communication between backend and other teams. Tried to be present on Discord whenever someone needs help. 
 
## Milestone 2
    
### MIL 2 - Responsibilities
* Integration of Swagger to the backend for API documentation and testing.
* AWS S3 Bucket Integration for both development and production.
* Research on how we can transfer the images from frontend to backend - and store them properly. As a result of my research, I provided a detailed description of the architecture [here](https://github.com/bounswe/bounswe2022group8/issues/246), implemented the backend part of the system.
* Integration of Profile Page with backend APIs with Furkan from frontend team.
* Implementation of art item related APIs (x7 APIs in total).
* Implementation of follow/unfollow related APIs (x6 APIs in total).
* Implementation of profile related APIs (x4 APIs in total).
* Communication with frontend for the integration stage.
* Updating login and signup error messages.
* PR Review: Reset Password API
* PR Review: Comment related APIs
* PR Review: CI/CD Integration
* PR Review: Like/Unlike API
* Frontend PR Reviews: API Integrations
* Configuration of `.env` and `.production.env` files to hide all of our secret information including AWS credentials, database credentials, email information and S3 bucket information, for both development and production sites.
* Generation of the class diagram fron Django using `graphviz`.
* Updating the class diagram. Filling up the `API` section of the Milestone II document.
* Updating existing APIs in accordance with the requests coming from frontend and mobile during the milestone week.

###  MIL 2 - Main Contributions
Already listed all of my responsibilities and contributions above. Overall, I worked so hard to pushed the team forward, handled some of the challenging tasks in our path and guided people throughout the procedure. Critically reviewed pull requests of other team members.
    
**Code Related Issues**
* [BE-29: [API] Follow&Profile and Comment Enhancement](https://github.com/bounswe/bounswe2022group8/issues/321)
* [BE-24: Generate Class Diagram from Django](https://github.com/bounswe/bounswe2022group8/issues/293)
* [BE-22: [API] Implementation of Follow Action APIs](https://github.com/bounswe/bounswe2022group8/issues/272)
* [BE-21: Add Image Storage Path and Production Settings](https://github.com/bounswe/bounswe2022group8/issues/269)
* [BE-17: [API] Implementation of Art Item Related APIs - 1](https://github.com/bounswe/bounswe2022group8/issues/250)
* [BE-16: [API] Implementation of Profile Related APIs - 1](https://github.com/bounswe/bounswe2022group8/issues/248)
* [BE-15: Configure AWS S3 Bucket for Image Storage](https://github.com/bounswe/bounswe2022group8/issues/246)
* [BE-14: Add Swagger Integration](https://github.com/bounswe/bounswe2022group8/issues/244)


**Management Related Issues**
* [MIL-8: Milestone 2 Group Review](https://github.com/bounswe/bounswe2022group8/issues/295)
* [MIL-9: Software Requirements Specification](https://github.com/bounswe/bounswe2022group8/issues/298)
* [MIL-11:  Milestone 2 Deliverables](https://github.com/bounswe/bounswe2022group8/issues/300)
* [MIL-12: Update Class Diagram](https://github.com/bounswe/bounswe2022group8/issues/303)
* [MIL-13: Pre-Release Version 0.2.0](https://github.com/bounswe/bounswe2022group8/issues/335)


**Pull Requests**
* [feature/BE-14](https://github.com/bounswe/bounswe2022group8/pull/245)
* [feature/BE-15](https://github.com/bounswe/bounswe2022group8/pull/247)
* [feature/BE-16](https://github.com/bounswe/bounswe2022group8/pull/249)
* [feature/BE-17](https://github.com/bounswe/bounswe2022group8/pull/251)
* [feature/BE-18](https://github.com/bounswe/bounswe2022group8/pull/252)
* [bugfix/BE-17](https://github.com/bounswe/bounswe2022group8/pull/311)
* [hotfix/BE-14](https://github.com/bounswe/bounswe2022group8/pull/255)
* [feature/BE-21](https://github.com/bounswe/bounswe2022group8/pull/270)
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/271)
* [feature/BE-22 #1](https://github.com/bounswe/bounswe2022group8/pull/274)
* [feature/BE-22 #2](https://github.com/bounswe/bounswe2022group8/pull/291)
* [feature/BE-24](https://github.com/bounswe/bounswe2022group8/pull/294)
* [feature/BE-29](https://github.com/bounswe/bounswe2022group8/pull/320)
* [feature/BE-30](https://github.com/bounswe/bounswe2022group8/pull/333)
* [hotfix/BE-11](https://github.com/bounswe/bounswe2022group8/pull/301)

**Unit Tests**
* You can find my unittests from the related [folder](https://github.com/bounswe/bounswe2022group8/tree/master/App/backend/api/tests).
* `test_artitem_creation`
* `test_artitem_deletion_cascaded`
* `test_artitem_deletion`
* `test_follow_creation`
* `test_follow_deletion_cascaded`
* `test_follow_artitems`
* `test_username_syntax`
    
**Additional**
    
PR reviews:<br>
* [feature/BE-20](https://github.com/bounswe/bounswe2022group8/pull/262)
* [feature/BE-19](https://github.com/bounswe/bounswe2022group8/pull/259)
* [feature/BE-11](https://github.com/bounswe/bounswe2022group8/pull/215) 
* [feature/FE-10](https://github.com/bounswe/bounswe2022group8/pull/271) (We worked as pair on this)
* [feature/FE-20](https://github.com/bounswe/bounswe2022group8/pull/322)
* [feature/FE-22](https://github.com/bounswe/bounswe2022group8/pull/334)
* [feature/BE-28](https://github.com/bounswe/bounswe2022group8/pull/315) 
    
## Milestone 3

### MIL 3 - Responsibilities
* Maintenance of our Amazon S3 bucket throughout the development.
* Implementation of exhibition related APIs (both virtual exhibitions and offline exhibitions).
* Implementation of annotation service: 
   * Implementing a new Django application from scratch and configuring a separate database. ,
   * Implementation of models in compliance with [WADM](https://www.w3.org/TR/annotation-model/).
   * Implementation of image/text annotation APIs. 
   * Documentation using Swagger.
   * Dockerizing the application and helping the deployment.
   * Taking actions whenever it's necessary during the integration of annotations with frontend.
* Implementation of GET Art items by tag API.
* Implementation of backend unittests.
* Solving the refresh problem on web.
* Creating a license for the project.
* Creating a tag that marks the final release version.
* Revising requirements related to annotations.
* Actively communicating with frontend during the integrations and updating/correcting the existing functions via bugfix/hotfix upon requests.
* Updating the class diagram.
* Documentation of our application of W3C standards with respect to annotations.
* Documentation of our API endpoints and providing examples in the Group Review document.
* Reviewing all of the pull requests created by backend team, in addition to some pull requests created by frontend.

### MIL 3 - Main Contributions
As listed above, implemented exhibition and annotation related APIs. Dealt with some of the bugs, updated diagrams/documents and reviewed a majority of the pull requests. Increased the number of unittests we have on the backend, helped the deployment of our Annotation service, created a license/tag for the project. I've taken different responsibitilies throughout the last milestone period. I was also responsible for the maintenance of our Amazon S3 bucket and API Collections. 
    
**Code Related Issues**
* [BE-30: [API] Implementation of Exhibition Related APIs](https://github.com/bounswe/bounswe2022group8/issues/343)
* [BE-31: [API] Implementation of Annotation Service](https://github.com/bounswe/bounswe2022group8/issues/348)
* [BE-34: Meeting Notes: Week #11 Meeting #5](https://github.com/bounswe/bounswe2022group8/issues/356)
* [BE-37: [API] GET Art Items by Tag](https://github.com/bounswe/bounswe2022group8/issues/367)
* [BE-39: Backend Unit Tests](https://github.com/bounswe/bounswe2022group8/issues/370)
* [BE-41: [API] Exhibitions of Currently Logged-in User](https://github.com/bounswe/bounswe2022group8/issues/384)
* [FE-30: Nginx Refresh Bug](https://github.com/bounswe/bounswe2022group8/issues/388)


**Management Related Issues**
* [MIL-19: Create License](https://github.com/bounswe/bounswe2022group8/issues/365)
* [MIL-20: API Endpoints Documentation](https://github.com/bounswe/bounswe2022group8/issues/407)
* [MIL-21: Final Release Version 0.3.0](https://github.com/bounswe/bounswe2022group8/issues/413)
* [MIL-22: Status of the Requirements](https://github.com/bounswe/bounswe2022group8/issues/414)
* [MIL-23: Milestone 3 Deliverables](https://github.com/bounswe/bounswe2022group8/issues/418)
* [MIL-24: Class Diagram](https://github.com/bounswe/bounswe2022group8/issues/419)

**Pull Requests**
* [feature/BE-30: Exhibitions](https://github.com/bounswe/bounswe2022group8/pull/344)
* [feature/BE-31: Annotation Service](https://github.com/bounswe/bounswe2022group8/pull/359)
* [feature/BE-37: Get Art Item by Tags](https://github.com/bounswe/bounswe2022group8/pull/368)
* [feature/BE-41: Exhibitions of Currently Logged-in User](https://github.com/bounswe/bounswe2022group8/pull/385)
* [bugfix/FE-30: Nginx Refresh Bug](https://github.com/bounswe/bounswe2022group8/pull/387)
* [bugfix/BE-30 - [1]](https://github.com/bounswe/bounswe2022group8/pull/390)
* [bugfix/BE-30 - [2]](https://github.com/bounswe/bounswe2022group8/pull/395)
* [bugfix/FE-19](https://github.com/bounswe/bounswe2022group8/pull/389) (I was both a reviewer and a contributor on this)
* [feature/BE-39: Backend Unittests [1]](https://github.com/bounswe/bounswe2022group8/pull/382)
* [feature/MIL-20: API Endpoints](https://github.com/bounswe/bounswe2022group8/pull/412)
* [MIL-19: Create License](https://github.com/bounswe/bounswe2022group8/issues/365)


**Unit Tests**
* You can find my annotation related unittests [here](https://github.com/bounswe/bounswe2022group8/blob/master/App/annotations/api/test.py).
* You can find my application related unittest [here](https://github.com/bounswe/bounswe2022group8/tree/master/App/backend/api/tests). 
* Overall, I have 56 unittests (17 unittests for annotations and 39 unittests for application). Of course, I can't list all of them here, so let me list the features for which I've implemented unittests:
* `text annotation`
* `image annotation`
* `artitem functionalities` 
* `follow/unfollow`
* `signup/login/logout`
* `profile functionalities`
* `offline exhibitions`
* `online exhibitions`

**Additional**

PR Reviews:
* [feature/BE-36: User Level](https://github.com/bounswe/bounswe2022group8/pull/364)
* [feature/BE-35: Art Item Category](https://github.com/bounswe/bounswe2022group8/pull/358)
* [feature/BE-32 : User History](https://github.com/bounswe/bounswe2022group8/pull/354)
* [feature/BE-38: Bidding System](https://github.com/bounswe/bounswe2022group8/pull/371)
* [bugfix/FE-19](https://github.com/bounswe/bounswe2022group8/pull/389)
* [feature/BE-33](https://github.com/bounswe/bounswe2022group8/pull/381)
* [feature/BE-40: Recommendation System](https://github.com/bounswe/bounswe2022group8/pull/386)
* [feature/BE-43: Backend Unittests [2]](https://github.com/bounswe/bounswe2022group8/pull/404)
* [feature/MOB-28](https://github.com/bounswe/bounswe2022group8/pull/411)
* [Feature/FE-32](https://github.com/bounswe/bounswe2022group8/pull/415)
* [hotfix/FE-33](https://github.com/bounswe/bounswe2022group8/pull/417)
    
Cancelled PR: [feature/BE-26: Full Text Search](https://github.com/bounswe/bounswe2022group8/pull/405)
</details>

<details>
    <summary> Doğukan Türksoy </summary>
    

## Milestone 2

I am Doğukan Türksoy, a member of group 8. I am at mobile part of our project.

### Responsibilities
I am responsible for mobile part and deployment. 

### Main Contributions
For this milestone I mainly worked on backend-mobile connections of out project. I connected profile page, update profile page, upload art item page, reset password , home page, art item page and comment pages. Moreover, worked on the connection of AWS S3 bucket to the mobile for fetching images. I also deployed the frontend, backend and mobile. <br/>

***Code Related Issues***
* [MOB-18: Fetching images from AWS S3](https://github.com/bounswe/bounswe2022group8/issues/346)
* [MOB-20: Backend Connections of uploading image and updating profile](https://github.com/bounswe/bounswe2022group8/issues/345)
* [MOB-16: Connecting Comment Page](https://github.com/bounswe/bounswe2022group8/issues/316)

***Management Related Issues***
* [MIL-17: Deployment](https://github.com/bounswe/bounswe2022group8/issues/347)
* [MIL-18: User Interface / User Experience](https://github.com/bounswe/bounswe2022group8/issues/349)

***Pull Requests***
* [feature/MOB-20](https://github.com/bounswe/bounswe2022group8/pull/331)
* [Feature/MOB-18](https://github.com/bounswe/bounswe2022group8/pull/314)

## Milestone 3
### MIL 3 - Responsibilities
* Implementation of like functionality of mobile.
* Implementation of text annotation backend connections of mobile.
* Implementation of search functionality backend connections of mobile.
* Improvement on the styling when necessary.
* PR and issue reviews on the mobile.
* Backend PR reviews when necessary.
* Helping backend and frontend teams when necessary.
* System manuals for frontend and mobile
* All deployments (frontend, backend, annotations, mobile)

### MIL 3 - Main contributions
For the final milestone, I took responsibility for the backend connections for Mobile team. I managed backend connections and page transitions. I also deployed the app on cloud and created .apk file.

**Code Related Issues**
* [MOB-21](https://github.com/bounswe/bounswe2022group8/issues/379) 
* [MOB-29](https://github.com/bounswe/bounswe2022group8/issues/437)


**Management Related Issues**
* [MIL-33](https://github.com/bounswe/bounswe2022group8/issues/430)
* [MIL-34](https://github.com/bounswe/bounswe2022group8/issues/431)
* [MIL-35](https://github.com/bounswe/bounswe2022group8/issues/432)


**Pull Requests**
* [feature/MOB-21](https://github.com/bounswe/bounswe2022group8/pull/380)
* [feature/MOB-28](https://github.com/bounswe/bounswe2022group8/pull/411)
* [feature/MOB-29](https://github.com/bounswe/bounswe2022group8/pull/416)

   </details>

## 10. Final Release Notes
You can find final release notes [here](https://github.com/bounswe/bounswe2022group8/releases/tag/customer-presentation-3)


## 11. System Manual
You can find system manual [here](https://github.com/bounswe/bounswe2022group8/wiki/System-Manual)
