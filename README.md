**MS4 README**

## Table of Contents

1. [Overview](#overview)

2. [Site Goals](#site-goals)
    1. [UX Goals](#ux-goals)
    2. [Siteowners Goals](#siteowners-goals)
    3. [User Stories](#user-stories)
    4. [Siteowner Stories](#siteowner-stories)

3. [About The Site](#about-the-site)
    1. [Target Audience](#target-audience)

4. [Code Used](#code-used)
    1. [Frameworks](#frameworks)
    2. [Files Made](#files-made)
    3. [Apps Made](#apps-made)

5. [Design](#design)
    1. [Typography](#typography)
    2. [Colors](#colors)
    3. [Images](#images)

6. [Code Features](#code-features)

7. [Bugs](#bugs)

8. [Features to be Added](#features-to-be-added)

9. [Testing](#testing)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [JQuery Validation](#jquery-validation)
    4. [Browser Compatibility](#browser-compatibility)
    5. [Devices Tested On](#devices-tested-on)

10. [Deployment](#deployment)

11. [Credits](#credits)
     1. [Icons](#icons)
     2. [Imagery](#imagery)
     3. [CSS Framework](#css-framework)
     4. [JQuery Framework](#jquery-framework)


## **Overview**
 - This site was created for MS4 submission for Code Institute.
 - The site's name is Easy Gaming.
 - The source code can be found on GitHub
 - The site is deployed using Heroku

 - The purpose of this site is to help people find games they might like to play over a selection of consoles, from the 7th and 8th generations of game consoles.


 - There is currently one account made at the moment:

     **Username**: easygaming_admin **Password**: E45yG4m1ng

This account is the main admin account of the site, and has also been used to test site functionality, for example: to check order history, add products and reviews etc.

View site [here](https://easygaming.herokuapp.com/)

## **Site Goals**

### **UX Goals**

 - Users can find games, either to play or as game recommendations.

 - Users also have the ability to create, edit update and read (CRUD) reviews on products.

### **Siteowners Goals**

 - Provide a service that enabes people to easily find games over a variety of consoles.

 - Ensure the database continues to accept new data, such as: reviews and added products

 - Ensure games added to the database by siteowner's are stored in right menu

 - Ensure blog posts are relevent to the site's purpose

 ### **User Stories**

 - As a user of this site I want to find a good game from a variety of genres

 - As a user of this site I want to be abe to find games from a variety of consoles and different generations

 - As a user i want to know if my login was successful or not.

 - As a user I want a easy to use, simple site.

 - As a user I want the ability to add reviews to products

 - As a user I want the ability to edit and delete my reviews

 - As a user I want the ability to see my order history

 - As a user I want my previous information such as address stored so I don't need to keep adding it

 - As a user I want to know my payments were successfull or not


 ### **Siteowner Stories**

 - As the owner of this site, I want to create a easy to use site that serves a purpose.

 -  As the owner of this site, I want users to know their reviews have been submitted to the database

 -  As the owner of this site, I want users to come back to this site.

 - As the owner of this site, I want users to be able to have control over their reviews, so edit and delete them as well as the ability to create them. 

 - As the owner of this site I want users login details to be stored safely and securely by encrypting the password on the server.

 - As the owner of this site I want users to know their data is secure. 

 - As the owner of this site I want users to know their payment has gone through and it is a secure transaction

 - As the owner of this site I want users to have their previous information stored so they don't have to re-enter things, like their address over again. 

 - As the owner of this site, I want superusers to have the abiity to create, edit, update and read the blog posts they have made. 

 - As the owner, I want all blogposts to be relevent to the site



## **About The Site**

 - The site currently has a total of 14 pages. Some are only visible to users who are logged in (profile page for example).
 - Users who are logged in have the option to buy games, while those who aren't logged in cannot.
 - User not logged in can only browse the games. 
 - The site's purpose is to help people find second hand games they'd like to play from a variety of consoles.
 
### **Target Audience**
 - The site is primarily aimed and adults/young adults who enjoy games and want to find their next game to play.



## **Code Used**

 The site is build using:
 - *HTML* to provide the site's structure and features, for example the contact form.

 - *CSS* to add style to the site, for example the font of the typography.

 - *PYTHON* to add the backend functionality to the site, for example allowing views to be shown on the fontend, and urls to work.

 - *JQUERY* to offer interactivity to the site, for example payment information.

 ### **Frameworks**

 - *BootStrap 4* is used to help style the site, and add responsve features to the site. The code used by BootStrap is used to add some style to the site, for example the button classes, in the html templates. It is also used to make the site responsive using columns and rows, for example the <div class="col-12 col-md-6"> in the add_product.html template. 

 - *DJANGO* is a python framework, and is used in this site to help provide backend functionality. It incudes a in-built database and this is used to store games, reviews, order histories and users amongst other things in this project. 