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
* *As a  User,* I would like to able to view this application on all device widths.
* *As a  Gym Owner,* I would like to be able to view reviews about my gym.
* *As a  Gym Owner,*  I would like to be able to update the details about my gym if someone has mistakenly provided inaccurate information. 

### Design

- When designing the application I wanted to keep it relatively simplistic as I feel it gives it a modern touch.

- I was conscious that my concept was to have users write their reviews and view data about gyms so I didn't want to overload the website with surplus information and images which in turn would overload the user.

- I used a dark navbar and dark typography theme as this is a gym website and as gym goers know - there aren't many weights that are brightly coloured (well not the heavy ones). 

- I utilised the forms from bootstrap and adapted them accordingly using the colour scheme that has been applied throughout.

- The font I selected as the primary font is *Rubik* as I felt it was bold and strong and fitted nicely in with the theme of the website. “Sans-Serif” is used as the default backup font in cases where the primary font has difficulty loading.
 
- The navbar is coloured with Bootstraps built-in design. It is a dark navbar and matches the theme of the page, I decided to continue with this dark theme throughout the webpage using the dark option for the footer and the data table.

- All buttons are deisgned again using Bootstraps inline design options. I have used the 'dark' option for any subit buttons and the 'danger'. On the home page I decided to use the outline button for the gym name as I felt if I had used a block colour it would take away from the background image on the page and wouldn't have been aesthetically pleasing. 


### Wireframing

When I was inititally thinking of the project I went online to have a look at other possible websites to get inspiration, this is when I discovered the lack of such websites. This probably made it harder to decide what style website to go with as I had to keep within my capablities and not get too imaginative. I created wireframes using Balsamiq, displaying what I would like the application to look like on all devices.

[Back to Top](#table-of-contents)

## Technology Used

* HTML, CSS & Python 
* <a href="https://getbootstrap.com/"> Bootstrap Framework</a> - I decided to use this as opposed to Materialize as I have used Bootstrap before and I found it more user friendly. This framework ensured mobile-first design and a responsive application. 
* <a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/#js">Javascript & JQuery</a> - I used the supplied technology for my Navbar to have collapse functionality.
* <a href="https://www.awseducate.com/student/s/awssite">PyCharm IDE</a> - AWS Cloud9 was the IDE I used to create the project.
controlling throughout the life-cycle of the project build.
* <a href="https://git-scm.com/">Git</a> - Git was used to push to my local repository throughout the creation process.
* <a href="https://github.com/auxfuse/Milestone1">Github</a> - My repository host that I pushed to throughout the project.
* <a href="https://www.heroku.com/">Heroku</a> - I pushed to Heroku to deploy my project and view the app running from here. 

#### Other Sources

* <a href="https://www.mongodb.com/cloud/atlas">MongoDB Atlas</a> - The database I used to create and store the data for the application.
* <a href="https://balsamiq.com/">Balsamiq</a> - Used to create wireframes for the project.
* <a href="https://realfavicongenerator.net/">Favicon Generator</a> ~ Used to create favicon
* <a href="https://validator.w3.org/">W3C HTML Validator</a>
* <a href="https://validator.w3.org/">W3C CSS Validator</a>
* <a href="https://jshint.com/">JSHint</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font Awesome Icons</a> ~ For social icons in footer

## Features

* Users are immediately greeted with a welcome message and a paragraph about the website. What the website is about and the functionality is explained clearly.
* There is a list of gyms that users can see on the home page and it is explained to them if they wish to update or edit any of the gyms all they have to do is click on the gym name!
* The user can edit any of the gyms that are listed on the website and are provided with two prepopulated fields for gym type and and membership cost.
* There is an option for a user to write a review on a gym provided it is on the database. This will then be posted to the review section of the website for other users to see - they will be able to tell who wrote the review and when and about which gym.
* The user also has an option to delete an entry when they click on the gym name. 
* If a user chooses to delete an entry a modal will pop up asking if they are sure they want to delete the entry.
* The footer has social links linking to all the main social technologies


[Back to Top](#table-of-contents)

#### Left To Implement:

* A user login/sign up
* An email to functionality to allow users to email me if there is an issue or perhaps set up a email alert when new reviews are posted
* Search functionality to allow users to search for a gym based on location,cost, type etc.

## Testing 

 - Using [Browserling](https://www.browserling.com/) I tested the website across multiple browsers to ensure responsiveness and compatibility. 
 
 - Using Google Chrome developer tools I tested the websites responsiveness across various devices ie. iPhone, Android and Tablets. 
 
 - Manually tested all the hover styling on the navbar and also the links - all operating correctly.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to validate HTML code

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate CSS code. 

- [Code Beautify JavaScript Validator](https://codebeautify.org/jsvalidate) was used to validate Javascript code. 

- Manually tested all forms to ensure that if I edited a gyms information it would change

- Manually tested add gym form to make sure the new data appeared on the home page

- Manually tested the delete function to ensure data was removed from the application

- Manually wrote reviews to check and see if reviews were posting to the correct html.file in the right format. 

#### Issues When Testing

- When I was adding a new gym some aspects of the new information were not adding to the datatable on the home page, I realised that in my form I did not have an 'id' specified for the form to pull the data. 

- When scrolling down on the home page there was a white space where the navbar should have been. I googled sack overflow and many developer websites and tried suggested fixes however it is something I will have to do more research into.

## Deployment

* I created this project in the AWS Cloud9 IDE. Within the terminal using git I pushed to my <a href="https://github.com/cgaynor91/Working_It_Out">repository</a> on Github. 
* I created an app on Heroku and deployed from same.
* In Heroku deployment method was set to Github with automatic deploys set from the master branch.
* The app was then deployed via this link: "https://git.heroku.com/working-it-out.git".

#### To clone the repository:
* Select the Repository from Github.
* Click on the "Clone or download" green button
* Click on the "clipboard icon" to the right of the Git URL to copy the web URL.
* Open your IDE and navigate to terminal window
* Change the directory to where you want to clone the repository to.
* Paste the Git URL copied from above and click "Ok".

[Back to Top](#table-of-contents)

## Credits

### Content

- Text was taken from the <a href="thegymadvisors.ie">The Gym Advisors </a> 

### Media

- The background image was taken from Google Image Search

### Help With Code

- I got the code for my modal on [Bootstrap](https://www.w3schools.com/bootstrap/bootstrap_modal.asp).
- I also found myself re-watching a lot of the videos and tutorials on [Code Institute](https://codeinstitute.net/), especially The Data Centric Development module. 

### Acknowledgements

I would like to thank tutor support for helping me with all the initial issues I had using the aws Cloud9 IDE. 
