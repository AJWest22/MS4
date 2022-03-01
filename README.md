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

6. [The DataBase](#the-database)

7. [AWS](#aws)

8. [Crispy Forms](#crispy-forms)

9. [Code Features](#code-features)

10. [JSON Files](#json-files)

11. [Bugs](#bugs)

12. [Features to be Added](#features-to-be-added)

13. [Testing](#testing)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Validation](#python-validation)
    4. [Browser Compatibility](#browser-compatibility)
    5. [Devices Tested On](#devices-tested-on)

14. [Deployment](#deployment)

15. [Credits](#credits)
     1. [Icons](#icons)
     2. [Imagery](#imagery)
     3. [JQuery Framework](#jquery-framework)
     4. [Crispy Forms](#crispy-forms)



## **Overview**
 - This site was created for MS4 submission for Code Institute.
 - The site's name is Easy Gaming.
 - The source code can be found on GitHub
 - The site is deployed using Heroku

 - The purpose of this site is to help people find games they might like to play over a selection of consoles, from the 7th and 8th generations of game consoles.


 - There is currently one account made at the moment:

     **Username**: easygaming_admin **Password**: E45yG4m1ng

This account is the main admin account of the site, and has also been used to test site functionality, for example: to check order history, add products and reviews etc. All address, payment and order history and data on this account is FAKE. 

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


 ### **Files Made**

 - There were 13 HTML files made in this project, 56 python files, 2 JavaScript files, 2 CSS files, a Procfile for Heroku deployment and a requirements.txt file. 

 - Most can be viewed on GitHUb, however an env.py file was created, to connect variables together in the setting.py file in the main app, which contains sensitve information, and has not been pushed to GitHub.

 - The HTML files are stored in the templates folder, as they form the basis of the site, and it helps structure and organise 
   the code. 

 - The static folders contains the JavaScript and CSS files, and is used to help structure the code files, and keep things orderly.

 - The app.py file provides the backend code that handles the data of the site. It is used for submitting data to the database and pulling information from the database. 

 - urls.py contains urls for the site

 - views.py contains the views for the site, which are then add to the urls.py so the views can be reflected onto the frontend of the site

 - forms.py contains form data and deals with the backend of the forms, pushing them to the database

 - The env.py file that was created contains information regarding the database and has not been pushed to GitHub.

 ### **Apps Made**

 - There are currently 10 apps made for this project. Each app, except the main app, contains a templates folder with at least one html file inside. 

 - The main app is called EasyGaming and contains the main settings.py file, the env.py file, and the standard asgi.py, wsgi.py, and __init__.py files. It contains no html files.

 - A checkout app was made so users had the ability to buy games, this contains a forms.py file to handle the backend information of the sites forms, and the standard py files that ar added by default to a django app. It contains 2 html files, one for the checkout page, and one for a complete checkout page, that is only displayed if the payment is successfull. A static css file is used to style this app.

 - A basket app is used to add items from the store too. This app contains the standard django files, and a contexts.py file to track whats in the basket. It contains one html file, that is used to display either a message saying there are no itmes in the basket, and a button encouraging users to keep shopping, or the users items that they have added to the basket.

 - The home app contains the standard apps for django and a html file in the templates folder that is used to display the home page for the store.

 - Media app is used to store images for the site. All images are stored in AWS

 - The products app contains information on the products, and gives superusers the ability to add, edit and delete products from the database. The app contains the standard py files for a django app, as well a fixtures file which contains the products and categories of the store, and 4 html files for displaying products, and giving details on each product when clicked on, and for adding and editing a product.

 - The profiles app contains information on users profiles, and their details such as address and order history. It contains 1 html file used to create the base of a profile page, the standard apps found in a django application, and a forms.py file used my a user to update their profile page. A static css file is used to style it.

 - The reviews app is used to add reviews to the site, this app is in development. A static css file is used to style this app.


## **The Design**

The site was designed to have a more relaxed feel to it, and easy to use. The site uses simpe coloring, fonts and imagery to create and achieve this effect.


### **Typography**

The site uses the font Lato to create a relaxed feel and a modern look for the site. It is used on the paragraph text.

The Oswald font is used as the Header font, and is used with some letter-spacing to create a bold look, which is attention grabbing, while maintaining the modern look of the site.


### **Colors**

The site uses a black and white coloring to ceate the modern look. The cdesign style comes from CI's Boutique Ado project. Originaly I was going to add some custom CSS, but ran out of time to add some.

### **Images** 

The homepage image of the ps4 controller on this site comes from pixabay. Its used to create a striking, eye catching effect, while setting out immediately the purpose of the site, (a videogame site). A PS5 controller image wasn't available, but would have been preferred as it would have made the site look and feel more modern. 

The video game images are screenshots of the games on Amazon, then cropped so that only the game is shown. The images are of the official covers of the games. 

The images are stored on AWS, except the homepage image which couldn't be added for some reason. 


## **The DataBase**

The DataBase is a in-built function of DJango, and has been structured so there is a section for: categories, products, users, orders etc. 

<details><summary>The layout of the DataBase:</summary>
  <img src="/media/database.png">
</details>

<details><summary>Example of how the products are stored in the Database:</summary>
  <img src="/media/database1.png">
</details>

<details><summary>How orders are stored in the DataBase:</summary>
  <img src="/media/database2.png">
</details>



## **AWS***

The images of this site are stored on AWS, hwever the homepage image wasn't accepted for some reason, hence why it isn't showing on the deployed site, but can be seen on the un-deployed site [here](https://8000-pink-swift-q4x485ok.ws-eu29.gitpod.io/)

An Image of the homepage as seen on the un-deployed site can be seen below:

<details><summary>Homepage on un-deployed site:</summary>
  <img src="/media/homepage.png">
</details>

In contrast this is the homepage on the deployed site:

<details><summary>Homepage on deployed site:</summary>
  <img src="/media/homepage-deployed.png">
</details>

The images that are stored on AWS are the videogame images that are used to advertise the products of the store. An example of one of those images stored on AWS can be seen below.

<details><summary>Example of image stored on AWS:</summary>
  <img src="/media/ac.jpg">
</details>


## **Code Features**

There are several code features used to give the site functionality, these include: a navbar, forms, and dropdown menus.
### **NavBar**

- Is used to offer a way of navigating the site. 

- Is a global element, as it appears on all pages.

- Uses if statements to hide certain pages from users that aren't logged in. For example the add review page is hidden from uses that aren't logged into the site. 

### **Forms**

- There are several forms on this site: A login form, a signup form, editing and updating a product, and a      profile form.

  - The Login Form:

      <details><summary>Login Form:</summary>
        <img src="/media/login-form.png">
      </details>

     - Appears on the login page.

     - Contains fields called: Username and Password.

     - Has a login button to log the user in, the information provided is then checked in the database, if it checks out, the user will log in successfully, if it doesn't the user will not be logged in.

     - The home button uses hover effect to add a bit of flash to the site.

     - Has a remember me option for returning users so they don't have to re-enter their login details.

     - All fields are required.


  - The Registration Form:

      <details><summary>Signup Form:</summary>
        <img src="/media/signup-form.png">
      </details>

     - Appears on the register page.

     - Contains fields: email address, email address confirmation, username, password, and password confirmation.
 
     - Has a link at the top asking if a user already has an account, if they already do, they can click there and be re-directed to the login page, where they will be asked to provide ther account details.

     - Has a sign up button that submits their data to the database, where it will be added.

     - All fields are required.


  - Checkout Form:

    <details><summary>Checkout Form:</summary>
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

      <details><summary>Profile Form:</summary>
        <img src="/media/profile-form.png">
      </details>

      - Contains information on the user's delivery address

      - Can only be accessed when a user has logged into their account

      - All fields are required


  - Edit Products Form

      <details><summary>Edit Product Form:</summary>
        <img src="/media/edit-product.png">
      </details>

      - Contains current information on that product

      - Can only be accessed when a superuser has logged into their account

      - All fields are required

      - The superuser has the ability to edit and change the image of the game

      - Contains a dropdown menu of the consoles to change the category if required

      - Gives superusers the ability to change the price and rating of the game using arrow buttons


  - Add Products Form

      <details><summary>Edit Product Form:</summary>
        <img src="/media/add-product.png">
      </details>   

    - Can only be accessed by a superuser logged in

    - Is used to add a new product to the store

    - Contains a dropdown menu to select the console whee the product wil be added to

    - Wii is the default

    - All fields are required


### **Dropdown Menus**

 Dropdown menus are used around the site to increase site functionalit, and make it easier for users and siteowners to perform actions. 

 - Navbar dopdowns 

   - Are found in the navbar menu of the site

   - Are used to present the categories in a user-friendly way

   - Make it easier for users to navigate the different categories of the site

  
  - Form dropdowns

    - Found in the add product and edit product forms

    - Make it easier to select the right category when adding or editing a product

    - Wii is set to default (not sure why this is)

    
## JSON Files

The JSON Files are used to store information on the products and their categories. Information on the products in the JSONS Files includes: SKU number, product name, a description of the item, a price tag, the categoy where it is to be store (each number represents a game console category), a rating, and an image. 

  Example:

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


## **Bugs**

There are several bugs to mention:

  1. When updating on GitPod and then pushing to GitHub, sometimes the code added wouldn't be in GitHub, and another push was needed to update it, this is why sometimes there are commits saying something has been added/removed but there is no visible adding or removing of anything, until the next commit. 

  2. When making the reviews model, a piece of code was added that enabled the user to add a review, however there was a bug where it said "view not found", however the view was in the code, and was written correctly. It was impacting the site to the point where when a user logged in, they weren't on the homepage of the site, and couldn't access their account page, they just got the error "view not found", and weren't able to access the site logged in. Due to this impact on the UX, the decision was taken to remove this piece of code, and is one of the reasons why you cannot add a review to the site.

  3. For some reason the default of every dropdown menu when adding or editing a product is "Wii" a placeholder text saying: "category" or "console" would have been preferred. Placeholder text was added, but wasn't showing on the site for some reason.


## **Features to be Added**

This project has several features I would like to add: A blog model which would allow superusers to make blogposts on new products coming to the store (such as games or consoles), trends in the gaming industry, new games to be released, etc. I would aso like to finish the review model so that users can add and edit, and delete reviews on products. Due to time constraints and not enough tutor support, working models weren't possible to be added in time.


## **Testing**

### HTML Validation
   - The code was validated using NU HTML Validator and displayed some errors about the default html5 document layout, and a few missing attributes.

      <details><summary>HTML Validation</summary>
        <img src="/media/html-validatior1.png">
      </details>

      <details><summary>HTML Validation</summary>
        <img src="/media/html-validator2.png">
      </details>

      <details><summary>HTML Validation</summary>
        <img src="/media/html-validator3.png">
      </details>
  

### CSS Validation
  - The code was tested using The W3C Jigsaw CSS Validation Service and encountered 4 errors:

  <details><summary>Css Validation</summary>
      <img src="/media/css-validator.jpg">
    </details>
  

### Python Validation

- The code was validated using PEP8 online check, and had several errors to do with whitespace, however when i have debugged these, I have encountered more errors. For example in the PEP8 validator it asks for a new line at the end of file, when I add one in, I get an error saying trailing whitespace, and I'm unsure why this is. For some reason I cannot upload a media file in here of the code, as I get an error saying media type unrecognised, which is unusual as its saved as a jpg format same as css.


### Browser Compatibility

- This site has been tested on the following browsers, and appears to be working well:
  FireFox
  Safari
  Microsoft Edge


#### Devices Tested On

- This site has been tested on: laptop 15", iPad 8th gen, iPhone SE (2016) and iPhone SE (2020).


## Deployment
  - This site was deployed using Heroku using the following steps:

    - Create a proc.file in your files, and connect to the app.py file.

    - Create a requirements.txt file.

    - Create an account on heroku.com

    - Create a new application and give it a name. NOTE: This name must be new, and one not already in use.

    - In the application dashboard, go to the deploy section and connect your application to your chosen GitHub repo, by      selecting your repo's name.

    - Select the branch to enable automatic deploys, (as was done with this project). Alternatively you can set it to deploy manually.

    - Set key/value pairs for the following keys:IP, PORT, SECRET_KEY

    - Return to your dashboard and click deploy.

    - Once deployed, click open app.


## Credits

### Icons

  - All icons can be found here: [here](https://fontawesome.com/)

### Imagery

 - The homepage image can be found on [Pixabay](https://pixabay.com/) [here](https://pixabay.com/photos/game-console-sony-video-games-6603120/)


### JQuery Framework

- Jquery is used for the form submitting, and can be found at the bottom of most of the templates folder to submit the Crispy Forms used. Example Checkout.html.


### Crispy Forms