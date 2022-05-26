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

4. [Development of Site](#development-of-site)
      1. [Development Bugs](#development-bugs)
      2. [HTML Development](#html-development)
      3. [CSS Development](#css-development)
      4. [Python Development](#python-development)
      5. [JQUERY Development](#jquery-development)
      6. [CRUD Development](#crud-development)

5. [Code Used](#code-used)
    1. [Frameworks](#frameworks)
    2. [Files Made](#files-made)
    3. [Apps Made](#apps-made)

6. [Design](#design)
    1. [Typography](#typography)
    2. [Colors](#colors)
    3. [Images](#images)

7. [The DataBase](#the-database)

8. [AWS](#aws)

9. [Crispy Forms](#crispy-forms)

10. [Code Features](#code-features)

11. [JSON Files](#json-files)

12. [Bugs](#bugs)

13. [Features to be Added](#features-to-be-added)

14. [Testing](#testing)
    1. [User Story Testing](#user-story-testing)
    2. [Superuser Story Testing](#superuser-story-testing)
    3. [HTML Validation](#html-validation)
    4. [CSS Validation](#css-validation)
    5. [Python Validation](#python-validation)
    6. [Browser Compatibility](#browser-compatibility)
    7. [Devices Tested On](#devices-tested-on)

15. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [Stripe](#stripe)
    3. [AWS Deployment](#aws-deployment)

16. [Credits](#credits)
     1. [Icons](#icons)
     2. [Imagery](#imagery)
     3. [JQuery Framework](#jquery-framework)
     4. [Crispy Forms](#crispy-forms)



## **Overview**
 - This site was created for MS4 submission for Code Institute.
 - The site's name is Easy Gaming.
 - The source code can be found on GitHub
 - The site is deployed using Heroku

 - The purpose of this site is to help people find games they might like to play over a selection of consoles, from the 7th and 8th generations of game consoles. Customers can also leave reviews and read blog posts on: trends in the gaming industry, upcoming games and consoles, and reviews on games and consoles.

 - There was one **general** user account made to test the create an account functionality.
      **Username**: CEKI

 - There is currently one superuser account made at the moment:

     **Username**: easygaming_admin

This account is the main admin account of the site, and has also been used to test site functionality, for example: to check order history, add products and reviews etc. All address, payment and order history and data on this account is **FAKE**. 

View site [here](https://easygaming.herokuapp.com/)



## **Site Goals**


### **UX Goals**

 - Users can find games, either to play or as game recommendations.

 - Users also have the ability to create, edit update and read (CRUD) reviews on products.

 - Users can read blog posts on games, gaming trends, and consoles.

 - Site admin have CRUD functionality on products, so they can add, edit and delete site products, which regular users can't.

 - Site admin also have CRUD functionality on blog posts.


### **Siteowners Goals**

 - Provide a service that enabes people to easily find games over a variety of consoles.

 - Ensure the database continues to accept new data, such as: reviews and added products

 - Ensure games added to the database by siteowner's are stored in right menu

 - Ensure blog posts are relevent to the site's purpose

 - Ensure reviews and blog posts contain appropriate language

 
 ### **User Stories**

 - As a user of this site I want to find a good game from a variety of genres

 - As a user of this site I want to be abe to find games from a variety of consoles and different generations

 - As a user I want to know if my login was successful or not.

 - As a user I want a easy to use, simple site.

 - As a user I want the ability to add reviews to products

 - As a user I want the ability to edit and delete my reviews

 - As a user I want the ability to see my order history

 - As a user I want my previous information such as address stored so I don't need to keep adding it

 - As a user I want to know my payments were successfull or not

 - As a user I want the ability to read blog posts


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

 - As the owner of this site, I want the ability to create, edit and delete blogs.

 - As the owner of this site, I want the ability to delete reviews if I find them inappropriate



## **About The Site**

 - The site currently has a total of 31 pages. This includes all account pages, so pages for signing in/out, password reset, and verification pages. Some pages are only visible to users who are logged in (profile page for example).

 - Users who are logged in have the option to buy games, and leave a review of a product, while those who aren't logged in cannot.

 - Users not logged in can only browse the games. 

 - The site's purpose is to help people find second hand games they'd like to play from a variety of consoles.
 

### **Target Audience**
 - The site is primarily aimed and adults/young adults who enjoy games and want to find a new game to play.



## **Development of Site**

The following is a brief overview of the development of the site, including the development of the code used, and bugs solved. Any bugs that have been solved have been recorded in the [bugs](#bugs) section of this README. This overview is divided into 5 sections: [Development Bugs](#development-bugs) [HTML Development](#html-development), [CSS Development](#css-development), [Python Development](#python-development), [JQUERY Development](#jquery-development).


### Development Bugs

During development there were several bugs were mentioning and how they were fixed:

1. An image didn't load on the deployed site, but did load on the development site. This was amended by renaming it in the gitpod terminal and then re-uploading it in the databse, and then re-deploying the site.

2. There was a bug in which any user could edit and delete any review, including other user's and superuser's. This was corrected by changing the code from: 

```
{% if request.user.is_authenticated %}
```

to:

```
{% if review.user == request.user or request.user.is_superuser %}
```

3. The third major bug was to do with making payments on the site: The webhook keys weren't matching from the deployed site on Heroku with the environment variables in GitPod settings.

4. The fourth bug to be fixed during development, was that any user could buy something from the store, regardless if they had an account or not, this was ammended by wrapping the secure checkout button in an if statement, and removing it and replacing it with a message asking the user to login first.


### HTML Development

The HTML files form the base structure of the site. A base.html template is used to contain the navbars for computer and mobile, and other sections that needed to appear on all pages. There are several base.html files, used for elements that need to appear on all pages. There is a  base.html in the allauth folder, forms the base of the allauth forms for signing up, logging in/out and handing email verificatons and changing email addresses. A 3rd base.html is used to create the format for any toast messages that appear on the site when a user triggers them.

Within each app, HTML files are used to structure the app, and create the skeleton of it. Example of these include the profile.html file, where despite the app not having any CRUD functionality, the html file is used to structure the app, and display a user's profile information onto the site. For apps with CRUD functionality, there are files for adding, editing and deleting products, reviews, and blogs. These files structure those respective apps, while holding the right Crispy Form and displaying it for the user to fill in and submit.


### CSS Development

To hold the CSS of the site static folders are used to hold the css files. The base.css files hold the css for the site. Each app, except the basket app, has a static folder, and by extension, a base.css file. The base.css file in the indivicual apps holds osme of the unique styling needed for each app. Unless the style is a universal style in which case, it can be found in the main base.css file, in the static folder, in the main files directory.

To develop the styling and design of the site, CSS Bootstrap classes are used around the site to develop it, and style elements of the site. Common CSS BootStrap classes used include: ``` font-weight-bold ```, to make the text and header text bold where required. 

``` mx-auto ``` is used to make elements fully extend across the screen. Examples include ``` <hr> ``` and the clickable icon at the foot of the 'All Products' page.

I also created some custom classes for this classes, to style some text elements, examples include the: ```koulen-font``` class, and the ```Roboto Font``` class. These can be found around the site.


### Python Development

Most of the Python used for this site is written using DJANGO, a fullstack framework that also includes server development. DJANGO handles the building, verification (using the CSRF token) and submitting of forms, using forms.py, the urls for the site in urls.py, and is responsible for displaying the CRUD functionality onto the front end of the site using views in the views.py file. Models.py holds the data for that app, and contains things like form fields. Each app has these same files, some have the additional forms.py file, which is used to make the forms, and Crispy Forms is used to style the form and make it mobile friendly.

DJANGO was a bit of a challenge to get to grips with in terms of memorising the individual steps needed to get an app working, for example remembering to add the newly created app to the main settings.py file in the main app, and the url in the main urls.py file. 


### JQUERY Development

JQUERY is used for making dropdown menus, sorting products, and for the spainner that shows up when a user makes a payment on the site. The JQUERY is imported by CDN from JQUEY.com, BootStrap JQUERY and from Stripe. 


### CRUD Development

This site has several apps and some installations that use CRUD functionality. Some of the apps and installations only display CRUD functionality for users who have an account and are logged in, all the apps and installations that use CRUD are accessible for superusers/site owners. The apps that use CRUD are: 

  - **AllAuth** AllAuth is responsible for the ability for users to create, login and log out of their accounts. It is available for all users who have and don't have an account and superusers.

  - **Profile App** the profile app gives users the ability to update and change things within their profile, such as their address. This is available to only users who have an account and superusers

  - **Basket App** The basket app gives users the ability to update, remove, and read items in their basket. The CRUD functionality is available to anyone using the site, regardless if they have an account or not, however anyone who clicks on the basket and has nothing in it, is requested to continue shopping, and then returned to the products page.

  - **Checkout App** Uses CRUD as it gives users to update/delete their address information. The checkout App is only accessible to users with an account, and superusers.

  - **Blog App** The Blog app only offers CRUD functionality to both users and superusrs, but the extend of the CRUD functionality depends on the type of account being used. General users who either have an account, or don't have an account are only able to read the blog posts and cannot edit or delete them. Superusers, however, can Create, Read, Update, and Delete blog posts as they see fit.

  - **Reviews App** The Reviews App offers full CRUD functionality to both users with accounts and superusers. Both these groups can create, read, update, and delete their reviews, while users who don't have accounts can only read them.

  - **Products App** The products app, like the blog app, only offers full CRUD ability to superusers. This means, that while users who have/don't have accounts can look at the products, they cannot edit or delete the products, only superusers can do that.

  

## **Code Used**

 The site is build using:
 - *HTML* to provide the site's structure and features, for example the contact form.

 - *CSS* to add style to the site, for example the font of the typography, and the site's *official* scolor scheme.

 - *PYTHON* to add the backend functionality to the site, for example allowing views to be shown on the fontend, and urls to work.

 - *JQUERY* to offer interactivity to the site, for example payment information.

 ### **Frameworks**

 - *BootStrap 4* is used to help style the site, and add responsve features to the site. The code used by BootStrap is used to add some style to the site, for example the button classes, in the html templates. It is also used to make the site responsive using columns and rows, for example the <div class="col-12 col-md-6"> in the add_product.html template. 

 - *DJANGO* is a python framework, and is used in this site to help provide backend functionality. It incudes a in-built database and this is used to store games, reviews, order histories and users amongst other things in this project. 


 ### **Files Made**

 - There were 36 HTML files made in this project, 87 python files, 2 JavaScript files, 4 CSS files, a Procfile for Heroku deployment and a requirements.txt file. 

 - Most can be viewed on GitHUb, however an env.py file was created, to connect variables together in the setting.py file in the main app, which contains sensitve information, and has not been pushed to GitHub.

 - The **HTML files** are stored in the templates folder of each app, as they form the basis of each page on the site, and it helps structure and organise the code used. 

 - The **static folders** contains the JavaScript and CSS files. Generally the apps CSS and/or JS are placed in static files of each app, which are used to help oragnise and style each app, unless it is a common styling in which case the apps are styled using the base.css file. An example of this would be, the post:hover class, which is used to enlarge a blog post on the blog page, this feature isn't reflected in any of the other apps, so is contained in the blog app's personal css file in the static folder.

 - The **app.py** file provides the backend code that handles the data of the site. It is used for submitting data to the database and pulling information from the database. 

 - **urls.py** contains urls for the site. Each app has at least one of these as they contain the urls needed for the apps, example: path('<int:post_id>', views.post_details, name='post_details'), is used so when a user clicks on a blog post, it gets the id of a blog post, and then gets the view called post_details and displays it on the post_details page.

 - **views.py** contains the views for the site, which are then add to the urls.py so the views can be reflected onto the frontend of the site. Each app has a views.py file. For apps with CRUD functionality, the views.py file contains views for adding, editing or deleting or displaying the contents of the apps.

 - **forms.py** contains form data and deals with the backend of the forms, and pushing them to the database. Most of the apps on the site have a forms.py page, bar the basket app. The form.py file contains the form's structure and fields and some styling of the form fields coloring.

 - The **env.py** file that was created contains security information regarding the database, deployment, and payment information, so has not been pushed to GitHub. It contains the variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, DEBUG, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS, which provide site functionality for AWS, Stripe Payments, and email verification.

 - To better illustrate the contents of the env.py file, a **env_sample.py** file has been created which contains the variables needed for this project, but NOT the values of these variables.

 - A .gitignore file was created, and contains the env.py file amongst other files, that have not been pushed to GitHub.


 ### **Apps Made**

 - There are currently 8 apps made for this project. Each app, except the main app, contains a templates folder with at least one html file inside. 

 - The main app is called EasyGaming and contains the main settings.py file, the env.py file, and the standard asgi.py, wsgi.py, and __init__.py files. It contains no html files.

 - A checkout app was made so users had the ability to buy games, this contains a forms.py file to handle the backend information of the sites forms, and the standard py files that ar added by default to a django app. It contains 2 html files, one for the checkout page, and one for a complete checkout page, that is only displayed if the payment is successfull. A static css file is used to style this app.

 - A basket app is used to add items from the store too. This app contains the standard django files, and a contexts.py file to track whats in the basket. It contains one html file, that is used to display either a message saying there are no itmes in the basket, and a button encouraging users to keep shopping, or the users items that they have added to the basket.

 - The home app contains the standard apps for django and a html file in the templates folder that is used to display the home page for the store.

 - Media app is used to store images for the site. All images are stored in AWS

 - The products app contains information on the products, and gives superusers the ability to add, edit and delete products from the database. The app contains the standard py files for a django app, as well a fixtures file which contains the products and categories of the store, and 4 html files for displaying products, and giving details on each product when clicked on, and for adding and editing a product.

 - The profiles app contains information on users profiles, and their details such as address and order history. It contains 1 html file used to create the base of a profile page, the standard apps found in a django application, and a forms.py file used my a user to update their profile page. A static css file is used to style it.

 - The reviews app is used to read reviews for games on the site. Users who are logged in can add, delete, edit reviews to the site. A static css file is used to style this app. A form.py file was created to create the form for making and editing reviews. A static css page is used to style this app.

 - The blog app is used so users can read blog posts relating to video games, the gaming industry, and game consoles either upcoming or older. Only site admin's have the ability to make blog posts, and by extension edit or delete them. The blog app uses s static css page to customise the blog app with some app specific features, such as the blog post enlarging on hover.

 - A newsletter app which users can sign up and receive a monthly newsletter on new games and consoles coming to the store. Only registered users with the store can access this feature. The styling of this app is inline with the overall styling fo the site, and as yet as no specific app features.



## **The Design**

The site was designed to have a more relaxed feel to it while still maintaining a aesthetic look, and ease of use. The site uses: coloring, fonts and imagery to create and achieve this effect.


### **Typography**

The site uses several fonts to style the site: Lato, Roboto, and Koulen. to create a relaxed feel and a modern look for the site. 

The Koulen font is used as the main Header font, and is used with some letter-spacing to create a bold look, which is attention grabbing, while maintaining the modern look of the site. It can be seen on the Products page header, the blog and reviews headers. Originally Oswald was used, but was then updated to Koulen to create a more aesthetic look, and it had a more "game" feel to it than Oswald.

- Lato is used to style the logo, and is also used as the main font for paragraphs of text found around the site. Example being on the log out page, the text asking a user if they want to log out, is styled using Lato. 

- Roboto is used to style the headers of blog posts and review titles, as well as the files that contain CUD elements of those apps, for example the header on the add review page. 


### **Colors**

The site uses a blue gradient as the main color scheme of the site. This adds a nice aesthetic, while creating a modern look to the site. The gradient changes as the user scrolls down the page, this creates a change in scenery and relieves a "same-y" feel from the site and stops the user feeling bored just staring at the same background all the way down the page. The blue color style is a reference to Sony's blue on Playstion 4 products. Originally I was going to use a background video with a subtle blue motion on it, to prevent boredom and make the background of the Products page more dynamic, and less plain to look at, as it has the most products and is the longest page to scroll through on the site. However I struggled to implement it, so it was removed and a blue background gradient was added to the site and this then evolved into the site's official color scheme. 

Originally I would have liked to make a different gradient for the different categories of products, so a green gradient for the Xbox games, the current blue gradient for the PlayStation games, and a white/slightly off white gradient for the Wii games. This would be in keeping with each games official colors for the respective consoles. However, again I had problems implementing this, so the blue gradient was chosen as it looked most aesthetically plasing, and evolved to become the site's official colors.


### **Images** 

The homepage image of the ps4 controller on this site comes from pixabay. Its used to create a striking, eye catching effect, while setting out immediately the purpose of the site, (a videogame site). A PS5 controller image wasn't available, but would have been preferred as it would have made the site look and feel more modern. 

The video game images are screenshots of the games on Amazon, then cropped so that only the game is shown. The images are of the official covers of the games. I DO NOT OWN THESE IMAGES. ALL RIGHTS TO THEIR RIGHTFUL OWNERS.

The images are stored on AWS. 



## **The DataBase**

The DataBase is a in-built function of DJango, and has been structured so there is a section for: categories, products, users, orders, reviews and blog posts. Examples of how these look are shown below: 

<details><summary>Click to expand image: The layout of the DataBase</summary>
  <img src="/media/database.png">
</details>

<details><summary>Click to expand image: How categories are stored in the database</summary>
  <img src="/media/database.png">
</details>

<details><summary>Click to expand image: Example of how the products are stored in the Database</summary>
  <img src="/media/categories-db.png">
</details>

<details><summary>Click to expand image: How orders are stored in the DataBase</summary>
  <img src="/media/database2.png">
</details>

<details><summary>Click to expand image: How users are stored in the DateBase</summary>
  <img src="/media/users-db.png">
</details>

<details><summary>Click to expand image: How reviews are stored in the DataBase</summary>
  <img src="/media/reviews-db.png">
</details>

<details><summary>Click to expand image: How blog posts are stored the DataBase</summary>
  <img src="/media/blog-posts-db.png">
</details>



## **AWS**

AWS is used to store the images of this site. The images that are stored on AWS are the videogame images that are used to advertise the products of the store. An example of one of those images stored on AWS can be seen below. 

<details><summary>Click to expand image: Example of image stored on AWS</summary>
  <img src="/media/ac.jpg">
</details>

However one image doesn't display on the deployed version of the site: the Xbox 360 edition of the Fifa World Cup South Africa. It can be seen on the undeployed version of the site but not the deployed, and has been uploaed to AWS.



## Crispy Forms

Crispy Forms is package that allows users to format forms using bootstrap styling. To install it type: pip3 install django-crisy-forms into your terminal. Crispy Forms is used in this project to create and style the forms and form fields. The basic template used for the forms is similar throughout the site, an example can be found on the checkout app when creating an account. Required fields on this form include asking for a user's: name, email address, phone number, country, postal code, city or town, the user's address, and phone number and card number.



## **Code Features**

There are several code features used to give the site functionality, these include: a navbar, forms, cards, and dropdown menus.


### **NavBar**

- Is used to offer a way of navigating the site. 

- Is a global element, as it appears on all pages.

- Uses if statements to hide certain pages from users that aren't logged in. For example the add review page is hidden from uses that aren't logged into the site. 


### **Forms**

- There are several forms on this site: A login form, a signup form, editing and updating a product, and a profile form, addig reviws and blog posts forms, and editing a review or blog post form, and a checkout form. All forms have a CSRF token, to ensure the data is secure and all fields are required for the forms before submitting to ensure form validation.

  - The Login Form:

      <details><summary>Click to expand image: Login Form</summary>
        <img src="/media/login-form.png">
      </details>

     - Appears on the login page.

     - Contains fields called: Username and Password.

     - Has a login button to log the user in, the information provided is then checked in the database, if it checks out, the user will log in successfully, if it doesn't the user will not be logged in.

     - The home button uses hover effect to add a bit of flash to the site.

     - Has a remember me option for returning users so they don't have to re-enter their login details.

     - All fields are required.


  - The Registration Form:

      <details><summary>Click to expand image: Signup Form</summary>
        <img src="/media/signup-form.png">
      </details>

     - Appears on the register page.

     - Contains fields: email address, email address confirmation, username, password, and password confirmation.
 
     - Has a link at the top asking if a user already has an account, if they already do, they can click there and be re-directed to the login page, where they will be asked to provide ther account details.

     - Has a sign up button that submits their data to the database, where it will be added.

     - All fields are required.


  - Checkout Form:

    <details><summary>Click to expand image: Checkout Form</summary>
      <img src="/media/checkout-form.png">
    </details>

     - Appears on the checkout page.

     - Users can submit their order to the database.

     - Users must have an account or login to use it.

     - Users must already have added something to the basket, otherwise when they click on the basket they will get a message    prompting them to add something.
 
     - Contains fields asking for a full name, an email, phone number, address, and a card number. The phone number and email are required so a user can be contacted directly. This also adds to creating a feeling of trustworthiness between the user and siteowner.

     - Offers a means of direct commnication between the siteowner and users.

     - All fields are required.

     - Icons are used to add a bit of decoration, and come from fontawesome.


  - Profile Form

      <details><summary>Click to expand image: Profile Form</summary>
        <img src="/media/profile-form.png">
      </details>

      - Contains information on the user's delivery address

      - Can only be accessed when a user has logged into their account

      - All fields are required


  - Edit Products Form

      <details><summary>Click to expand image: Edit Product Form</summary>
        <img src="/media/edit-product.png">
      </details>

      - Contains current information on that product

      - Can only be accessed when a superuser has logged into their account

      - All fields are required

      - The superuser has the ability to edit and change the image of the game

      - Contains a dropdown menu of the consoles to change the category if required

      - Gives superusers the ability to change the price and rating of the game using arrow buttons


  - Add Products Form

      <details><summary>Click to expand image: Add Product Form</summary>
        <img src="/media/add-product.png">
      </details>   

    - Can only be accessed by a superuser logged in

    - Is used to add a new product to the store

    - Contains a dropdown menu to select the console where the product will be added to and a dropdown menu asking about the quantity of the product, ie: is it just one in stock or are there more than one in stock.

    - Uses arrow buttons to adjust the rating and price of the product

    - Wii is the default

    - All fields are required
  

  - Add Reviews Form

      <details><summary>Click to expand image: Add Reviews Form</summary>
        <img src="/media/add_review-form.png">
      </details>   

    - Can only be used by a user that is logged in

    - Is used to add a new review to the store

    - Has a title field for the name of the review

    - Contains a dropdown menu to select the product the review will be about

    - Contains a field where the review can be written, the maximum amount of characters for each review is set to 500 characters.

    - All fields are required

  
  - Edit Reviews Form

      <details><summary>Click to expand image: Edit Review Form</summary>
        <img src="/media/edit-review-form.png">
      </details>   

    - Can only be accessed by a user who left that particular review

    - Is used to edit a review in the store

    - Contains a dropdown menu to select the product the review is being left on

    - The previously selected product is the default

    - Contains a field where the review can be re-written, the maximum amount of characters for each review is set to 500       characters, and the review in its original state is in the review field ready to be edited/re-written

    - All fields are required


  - Add Blog Posts Form

      <details><summary>Click to expand image: Add Blog Post</summary>
        <img src="/media/add-blog-post.PNG">
      </details>   

    - Can only be accessed by a superuser logged in

    - Is used to add a new blog post to the store

    - Contains a title field for the name of the blog post

    - Contains a post field for the main body of the post, te maximum amount of characters for a blog post is: 500,000

    - Contains an image field where an image for the blog post can be uploaded if wanted

    - All fields are required

  
  - Edit Blog Posts Form

      <details><summary>Click to expand image: Edit Blog Posts Form</summary>
        <img src="/media/edit-blog-post.PNG">
      </details>   

    - Can only be accessed by a superuser logged in

    - Is used to edit a blog post on the store

    - Contains the same fields as the add blog post form, with the original title, post and image ready to be edited/re-written

    - All fields are required

  
  - Newsletter Form

      <details><summary>Click to expand image: Newsletter Form</summary>
        <img src="/media/newsletter-form.png">
      </details>

    - Can be accessed by any user using the site, whether they have an account or not

    - Is used to sign up to the monthly newsletter on the store

    - Contains two fields, an email field, and a email confirmation field

    - All fields are required

    - Was originaly going to be for only users who had an account, before being made universally accessible


### Cards

Bootstrap cards are used to display the games on the site. The card header holds an image of the game, while the card body contains the title of the game. The card footer contains the price, and rating of the game, and the category of the game. The cards have an added hover effect that enlarges the card when its hovered over. This effect is one I created using the transform and scale css effect.


### **Dropdown Menus**

 Dropdown menus are used around the site to increase site functionality, and make it easier for users and siteowners to perform actions. 

 - Navbar dopdowns 

   - Are found in the navbar menu of the site

   - Are used to present the categories in a user-friendly way

   - Make it easier for users to navigate the different categories of the site

  
  - Form dropdowns

    - Found in the add product and edit product forms, and the add review and edit review forms

    - Make it easier to select the right category when adding or editing a product

    - Make it easier to select the right product when adding ot editing a review



## JSON Files

The JSON Files are used to store information on the products and their categories. Information on the products in the JSONS Files includes: SKU number, product name, a description of the item, a price tag, the category where it is to be store (each number represents a category), a rating, and a product image. 

  Example of how products are stored:

```json
"pk": 1,
  "model": "products.product",
  "fields": {
      "sku": "pp5001340155",
      "name": "Mario Kart Wii",
      "description": "Originally released in 2008, Mario Kart Wii has become a classic amongst racing games and Nintendo.",
      "price": 14.99,
      "category": 1,
      "rating": 4.5,
      "image": "mario-kart.jpg"
  }
```



## **Bugs**

There are a couple of bugs on this site:

1. The first is on the blog model, a superuser cannot upload an image to the blog post using the form field for images. Instead to upload an image to a blog post, they have to upload it in the database. I'm not sure why this is, and its something I want to have a play with and correct in time. I believe the issue lies in the widget 'Clearable File Input', I've also used this widget on the images for the adding a product form, and it works well there. 

2. On the deployed site, an image to the blog will not display if it is not first stored in AWS. In order to add an image to a blog post, users have to create it on the undeployed site first, add the image used to AWS, then deploy it, and it will show.


## **Features to be Added**

This site has several feature to be added, I would like to do more with the profile app to give users more personalisation of their profile. So giving them the option to have their own profile picture.

I would also like to add a star rating option to the reviews form, which can then be calculated into an average for the products. At the moment the star ratings are ones I have made up.



## **Testing**

To test the code in this project, a mixture of external code validators and the in built testing framework of Django was used. For the HTML, CSS and JavaScript, external validators were used to proof read the code and check it. The in-built Django tetsing framework was originally going to be used along with PyTest, but due to continuous difficulties using these, the decision was taken to rely on validators and auto testing.


### **User Story Testing**

 - As a user of this site I want to find a good game from a variety of genres
  
      <details><summary>Click to expand image: Displays variety of games to user</summary>
        <img src="/media/good-game-story.PNG">
      </details>   

 - As a user of this site I want to be abe to find games from a variety of consoles and different generations

      <details><summary>Click to expand image: Displays different consoles to the User</summary>
        <img src="/media/console-story.PNG">
      </details>
    
      <details><summary>Click to expand image: Shows the different generations of consoles on the store to the User, Wii is from the previous generation of game conesoles to the Xbox One.</summary>
        <img src="/media/generation-story.PNG">
      </details>

 - As a user I want to know if my login and logout was successful or not.

      <details><summary>Click to expand image: Shows a login was successful</summary>
        <img src="/media/user-login-story.PNG">
      </details>   

      <details><summary>Click to expand image: Shows a logout was successfull</summary>
        <img src="/media/logout-story.PNG">
      </details>   

 - As a user I want a easy to use, simple site.

      <details><summary>View of Site. Click to expand image:</summary>
        <img src="/media/laptop-view.png">
      </details>   

 - As a user I want the ability to add reviews to products

      <details><summary>Add review form for a user for add a review. Click to expand image:</summary>
        <img src="/media/add-review-story.PNG">
      </details>

      <details><summary>Add review success. Click to expand image:</summary>
        <img src="/media/add-review.PNG">
      </details>

 - As a user I want the ability to edit and delete my reviews

      <details><summary>Edit review form for a user for edit a review. Click to expand image:</summary>
        <img src="/media/edit-review-story.PNG">
      </details>

      <details><summary>Delete Review. Click to expand image:</summary>
        <img src="/media/delete-review-story.PNG">
      </details>  

 - As a user I want the ability to see my order history

      <details><summary>Order history on profile. Click to expand image:</summary>
        <img src="/media/profile-story.PNG">
      </details>   

 - As a user I want tthe option for my previous information such as address stored so I don't need to keep adding it

      <details><summary>Saved info in Profile. Click to expand image:</summary>
        <img src="/media/profile-story.PNG">
      </details>   

 - As a user I want to know my payments were successfull or not

      <details><summary>Toast to show successfull payment. Click to expand image:</summary>
        <img src="/media/payments-story.PNG">
      </details>   

 - As a user I want the ability to read blog posts

      <details><summary>Read Blog Story. Click to expand image:</summary>
        <img src="/media/read-blog-story.png">
      </details>   


### **SuperUser Story Testing**

  - As the owner of this site, I want to create a easy to use site that serves a purpose.

      <details><summary>View of Site. Click to expand image:</summary>
        <img src="/media/laptop-view.png">
      </details>  

  - As the owner of this site, I want users to know their reviews have been submitted to the database

      <details><summary>Add review form for a user for add a review. Click to expand image:</summary>
        <img src="/media/add-review-story.PNG">
      </details>    

  - As the owner of this site, I want users to come back to this site.

      <details><summary>View of Site. Click to expand image:</summary>
        <img src="/media/laptop-view.png">
      </details>  

  - As the owner of this site, I want users to be able to have control over their reviews, so edit and delete them as well as the ability to create them.

      <details><summary>Edit review form for a user for edit a review. Click to expand image:</summary>
        <img src="/media/edit-review-story.PNG">
      </details>

      <details><summary>Delete Review.Click to expand image:</summary>
        <img src="/media/delete-review-story.PNG">
      </details>

  - As the owner of this site I want users login details to be stored safely and securely by encrypting the password on the server.

  - As the owner of this site I want users to know their data is secure.

  - As the owner of this site I want users to know their payment has gone through and it is a secure transaction

      <details><summary>Toast to show successfull payment. Click to expand image:</summary>
        <img src="/media/payments-story.PNG">
      </details>

  - As the owner of this site I want users to have their previous information stored so they don't have to re-enter things, like their address over again.

      <details><summary>Saved info option. Click to expand image:</summary>
        <img src="/media/profile-story.PNG">
      </details>

  - As the owner of this site, I want superusers to have the abiity to create, edit, update and read the blog posts they have made.

      <details><summary>Read Blog Story. Click to expand image:</summary>
        <img src="/media/read-blog-story.png">
      </details>   


  - As the owner, I want all blogposts to be relevent to the site

      <details><summary>Relevant Blogs. Click to expand image:</summary>
        <img src="/media/read-blog-story.png">
      </details>

  - As the owner of this site, I want the ability to create, edit and delete blogs.

      <details><summary>Add Blog Post. Click to expand image:</summary>
        <img src="/media/add-blog-post.PNG">
      </details>

      <details><summary>Edit Blog Post. Click to expand image:</summary>
        <img src="/media/edit-blog-post.PNG">
      </details>

      <details><summary>Delete Blog Post Story. Click to expand image:</summary>
        <img src="/media/delete-blog-post.PNG">
      </details>

  - As the owner of this site, I want the ability to delete reviews if I find them inappropriate

      <details><summary>Delete Inappropriate Review Story. Click to expand image:</summary>
        <img src="/media/delete-review-story.PNG">
      </details>

  - - As the owner of this site, I want the ability to edit reviews if I find them inappropriate/have bad spelling

      <details><summary>Edit Inappropriate Review Story. Click to expand image:</summary>
        <img src="/media/edit-review-story.PNG">
      </details>


### HTML Validation
   - The code was validated using NU HTML Validator and displayed some errors about the default html5 document layout, and a few missing attributes.

      <details><summary>HTML Validation. Click to expand image:</summary>
        <img src="/media/html-validatior1.png">
      </details>

      <details><summary>HTML Validation. Click to expand image:</summary>
        <img src="/media/html-validator2.png">
      </details>

      <details><summary>HTML Validation. Click to expand image:</summary>
        <img src="/media/html-validator3.png">
      </details>
  

### CSS Validation
  - The code was tested using The W3C Jigsaw CSS Validation Service and encountered 4 errors:

    <details><summary>Css Validation. Click to expand image:</summary>
      <img src="/media/css-validator.jpg">
    </details>
  

### Python Validation

The Python code was tested using the build in Django testing framework. In order to properly test the code was working, the project was disconnected from the Heroku/Postgres databse so testing could be conducted. The first test was a test function, and can be seen in the below screenshot: 

<details><summary>Original Test Function. Click to expand image:</summary>
      <img src="/media/test-function.png">
</details>

This test passed successfully.


### Browser Compatibility

- This site has been tested on the following browsers and is fully functioning:
  FireFox:
  <details><summary>Click to expand image. View of the site on Firefox:</summary>
    <img src="/media/firefox-view.png">
  </details>

  Safari:
  <details><summary>Click to expand image. View of the site on Safari:</summary>
    <img src="/media/ipad-view.PNG">
  </details>

  Microsoft Edge:
  <details><summary>Click to expand image. View of the site on Edge browser:</summary>
    <img src="/media/edge-view.png">
  </details>

  Google Chrome:
  <details><summary>Click to expand image. View of the site on Chrome:</summary>
    <img src="/media/chrome-view.png">
  </details>


#### Devices Tested On

- This site has been tested on: laptop 15", iPad 8th gen, iPhone SE (2016) and iPhone SE (2020).

<details><summary>Click to expand image. Laptop 15inch View</summary>
  <img src="/media/laptop-view.png">
</details>


<details><summary>Click to expand image. iPad 8th Gen View</summary>
  <img src="/media/ipad-view.PNG">
</details>


<details><summary>Click to expand image. iPhone 2020 View</summary>
  <img src="/media/mobile-view.PNG">
</details>


<details><summary>Click to expand image. iPhone 2016 View **same photo as the 2020 model, as they look the same**</summary>
  <img src="/media/mobile-view.PNG">
</details>



## Deployment

  ### Heroku

  - This site was deployed using Heroku using the following steps:

    - Create a [Procfile](Procfile) in your files, and connect to the app.py file.

    - Create a [requirements.txt](requirements.txt) file.

    - Create an account on [heroku.com](https://www.heroku.com)

    - Create a new application and give it a name. NOTE: This name must be new, and one not already in use.

    - In the application dashboard, go to the deploy section and connect your application to your chosen GitHub repo, by      selecting your repo's name.

    - Select the branch to enable automatic deploys, (as was done with this project). Alternatively you can set it to deploy manually.

    - Return to your dashboard and click deploy.

    - Once deployed, click open app.


  ### STRIPE

  Stripe is used to handle the payments on this site, to use Stripe:

  - Create an account on [Stripe](#https://stripe.com/en-gb)

  - On your stripe dashbaord copy the Stripe public key and paste it into your checkout app view.

  - In your workspace import Stripe using the command: pip3 install stripe

  - Create an env.py file

  - In your env.py file add the variables: STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, and STRIPE_WH_SECRET

  - For the STRIPE_PUBLIC_KEY add the public key value found on your dashboard

  - For the STRIPE_SECRET_KEY, go to [Random Key Gen](#https://randomkeygen.com/) and select a password, copy and paste that into your STRIPE_SECRET_KEY variable.

  - For the STRIPE_WH_SECRET copyt the key and paste it into the variable's value

  - Go over to your Heroku app and in the Config Vars section add the above variables, ensuring they match.

  - In the settings.py file in the main app, add the same variables above.

  - On Stripe go to developers, and look for 'webhooks'

  - Select 'add end point'

  - Paste the URL of your site,, and click 'receive all events', then click 'add end point'


  ### AWS Deployment

  - Create an account at [AWS](#https://aws.amazon.com/)

  - Open the S3 application and create an S3 bucket named the same as your project/app

  - Uncheck the "Block All Public Access" setting

  - In Properties, go to 'Static Website Hosting' and click edit

  - Enable the setting and and set the index and error.html values

  - Back in permissions, click edit on 'CORS configuration and add:

      ```
        [
          {
            "AllowedHeaders":[
              "Authorisation"
            ],
            "AllowedMethods":[
              "GET"
            ],
            "AllowedOrigins":[
               "*"
            ],
            "ExposedHeaders":[]
          }
        ]
      ```
  - In Permissions click edit on the bucket policy and generate and set the below configuration:
        
      ``` 
          {
            "Version": "2012-10-17",
            "Id": "Policy1641548102148",
            "Statement": [
                {
                  "Sid": "Stmt1641548086079",
                  "Effect": "Allow",
                  "Principal": "*",
                  "Action": "s3:GetObject",
                  "Resource": "arn:aws:s3:::name-of-your-app/*"
                }
              ]
          }
      ```
  - Still in permissions, click 'edit' on the Access control list (ACL)

  - Click Read access for the Bucket ACL for Everyone(Public Access)

  - The bucket is created, the next step is to open the IAM application to set up access

  **The Bucket has now been created, the next step is the open the IAM application:**

  - Create a new user group, the same name as your project/app

  - Add the AmazonS3FullAccess Policy to the group

  - Navigate to Policies and click 'Create New policy'

  - Click 'Imprort Managed Policy

  - Select AmazonS3FullAccess, then click 'Import'

  - Go to the JSON editor and add the following:

      ```
        "Resource": [
          "arn:aws:s3:::name-of-project",
          "arn:aws:s3:::name-of-project/*"
        ]
      ```
  - Give the Policy a name, and click create Policy, then add it to the use group

  - Navigate to Users and click 'new user'

  - Add the user to your user group

  - Select 'Programmatic Access' for the access type

  - The user is now created and should have the the correct user group and policy


## Credits

My friends and family for their support, and for letting me use their devices and for their feedback on the design of the site.

My amazing mentor Tim Nelson for his feedback and support making this project


### Icons

  - All icons can be found here: [here](https://fontawesome.com/)


### Imagery

 - The homepage image can be found on [Pixabay](https://pixabay.com/) [here](https://pixabay.com/photos/game-console-sony-video-games-6603120/)

 - The noimage available image, was found on Google. I do not own this image.

 - The video game images themselves, are screenshots of the games on Amazon, then trimmed so they contain only the image of the game itself. I do not own the cover art of these games.


### JQuery Framework

- [Jquery](#https://releases.jquery.com/) is used for the form submitting, the toasts and the spinner at the bottom of the checkout page, and can eithe rbe found at the bottom of the htl files or in the static folders JS folder of the apps. Example the checkout app has JQuery att he bottom of the template, and in the static folder.


### Crispy Forms

Most forms are made using [Crispy Forms](#https://pypi.org/project/django-crispy-forms/) which is installed using: pip3 install django-crispy-forms, and then added to the installed apps in settings.py then set to BootStrap 4 to style the forms and make them mobile responsive.