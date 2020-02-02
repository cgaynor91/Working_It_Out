<h1 align="center">
Data Centric Development
<br> Third Milestone Project
</h1>
***
For my third milestone project I decided to create a web application that allowed users to view local gyms in their area, see reviews from other gym goers or write a review themselves, all information would be stored and updated on a database which will allow the application to progress and grow as more and more information is recorded to the database.

There does not seem to be a "one-stop" application where a user can go and see a list of gyms in their local area with real life reviews. If a user was to visit the gyms actual webpage there would be reviews on the site however, as it is with most business websites, a lot of the reviews are fabricated by owners/employees or relatives of the business.

My vision was to create an application where users could read honest reviews about local gyms in their areas that might help them find a gym that would suit them. This website would also benefit local gyms as their details are advertised and they are able to get real life feedback from their customers.

## Table of Contents:
* [What is the project?](#what-does-it-do-and-what-does-it-need-to-fulfill)
* [Project Functionality](#functionality-of-project)
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
* [Technology Used](#technology-used)
* [Features](#features)
    * [Future Features](#future-features)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


***

## Welcome to Working It Out!

## What is the project?

This project is the third milestone project of the Fullstack Web Developer Course and it incorporates the previous modules covered with a emphasis on the most recent modules covered - Python Fundamentals, Practical Python and Data Centric Development

The project brief requires you to 
> Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. <br>

There is a focus in the brief to 

>Create functionality for users to create, locate, display, edit and delete records (CRUD functionality). <br>

The application I have developed I believe meets the briefs specifications in that it  will allow a user to create, read, update and delete details and reviews about local gyms, data of which will be stored in the MONGODB database. <br>

The app I have created is called <a href="">Working It Out</a>.

### Project Functionality
As I mentioned the application contains the CRUD required functionalities and it utilises MongoDB as the data handling, document based database. User functionality is created using HTML templates, Flask and styled with CSS. The frontend framework is dependent on the popular Bootstrap Framework, aiding the layout and the structure of the page and helping with responsive design. 

The application allows user to read, update, create and delete data about local gyms and read reviews left by other application users. These functions are completed utilising the connection the MongoDB database which is updated in turn. 

Users are only allowed to review a gym that is already on the database, however if they wish to add a gym that isn't on the database that functionality has been provided. When the user is writing their review they are given a calendar option which allows them to input the date they reviewed the gym. 

They are also given a dropdown menu when reviewing the gym of what the cost is and what type of gym it is, pay as you go, membership only etc.

The project is version controlled via Git & Github and is deployed via Heroku. All environment variables are held in a git ignored file.

[Back to top](#table-of-contents)

## UX

### User Experience

* *As a  User,* I want to view the local gyms that are available to me in my area.
* *As a  User,*  I want to be able to read reviews from other gym goers and see what their experiences were like.
* *As a  User,* I want to be able to navigate from page to page easily.
* *As a  User,* I would like for the website to be informative and helpful.
* *As a  User,* I would like to be able to write my own review of my gym or a gym I attended
* * *As a  User,* I would like to able to view this application on all device widths.
* *As a  Gym Owner,* I would like to be able to view reviews about my gym.
* *As a  Gym Owner,*  I would like to be able to update the details about my gym if someone has mistakenly provided inaccurate information. 
### Design Ideas

- When designing the application I wanted to keep it relatively simplistic as I feel it gives it a modern touch.

- I was conscious that my concept was to have users write their reviews and view data about gyms so I didn't want to overload the website with surplus information and images which in turn would overload the user.

- I used a dark navbar and dark typography theme as this is a gym website and as gym goers know - there aren't many weights that are brightly coloured (well not the heavy ones). 

- I utilised the forms from bootstrap and adapted them accordingly using the colour scheme that has been applied throughout.

- The font I selected as the primary font 

-  