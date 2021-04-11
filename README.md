<h1 align="center"><img src="static/images/logo-img.png" style="margin: 0;" alt="image of site logo"></h1>

[View the live website here.](https://bitter-sweet-milestone-3.herokuapp.com/)

## Table of Contents

- [Overview](#BitterSweet-Overview)
- [Things to consider](#Things-to-consider)
- [UX](#UX)  
    - [User Stories](#User-stories)
    - [Design](#Design)
    - [Wireframes](#Wireframes-page-designs)
    - [MongoDB](#MongoDB-data-schema-design)
- [Features](#Features)
- [Future Features](#Future-Features)
- [Error Handling](#Error-Handling)
- [Technologies Used](#Technologies-Used)
    - [Languages](#Languages-Used)
    - [Frameworks](#Frameworks,Libraries-&-Programs-Used)
- [Testing](#Testing)
    - [Testing User Stories](#Testing-User-Stories)
    - [Further Testing](#Further-Testing)
    - [Bugs](#Known-Bugs)
- [Deployment](#Deployment)
- [Future Maintainability](#Future-maintainability)
- [Credits](#Credits)
    - [Content](#Content)
    - [Media](#Media)
- [Acknowledgements](#Acknowledgements)

# BitterSweet Overview

This website is a chocolate themed recipe sharing site. Anybody can create an account and share their chocolate inspired recipes. 

Any user can view all recipes on the site, however only a registered user can add/edit/delete their own recipes. To compliment these chocolate recipes
BitterSweet©, which is a new chocolate company, would like to promote their products to be used to create these chocolate dishes. 

## Things to consider

1. Working with MongoDB as the non-relational database to store the recipes and user information.
2. Using Flask as a framework.
3. The C.R.U.D functionality - the users must be able to Create, Read, Update and Delete their own recipes - but not anyone else's for security.
4. A search function to locate recipes by name or ingredients.
5. The data displayed must be user friendly and visually appealing.

# UX

## User stories

- #### Site user goals
    1. As a site user, I want to be able to register for the site and navigate it easily, then to be able to log in and out when I wish.
    2. As a site user, I want to be able to view the recipes already on the site, but also to add and display my own.
    3. As a site user, I want to be able to edit and/or delete my recipes when I want to.

- #### Site owner goals
    1. As a site owner, I want to promote the company BitterSweet© and to suggest the users try these new chocolate products in the recipes.
    2. As a site owner, I want the users to be able to create an account and navigate the site easily, as well as create/edit/delete their recipes as much as they choose to.
    3. As a site owner, I want the users to be able to search through the chocolate recipes on the site for keywords or ingredients.

-   ### Design
    -   #### Colour Scheme
        -   The main colours used are shades of brown, purple and white, as these complement each other nicely and are suggestive of the classic colours of Cadbury's, however 
        as this is a site for the purpose of learning no copyright infringement is intended. 
    -   #### Typography
        -   The Satisfy font is used for the navbar and page titles, as it resembles the font used in the logo. Baloo Tammudu 2 is also used for the paragraphs with information, as this makes them easier to read. Sans Serif is the fallback font in case for any reason the font isn't being imported into the site correctly. These fonts are attractive and appropriate to the aesthetic of the site. The font colour throughout is dependent on the background and the type of content to make it stand-out and for ease of reading against the background.
    -   #### Imagery
        -   I created the site logo using Adobe Photoshop and a stock photo located online that I edited to suit my purpose. 
        -   I created the vegan chocolate wrapper design and the other chocolate wrapper design on the index page using Adobe Photoshop and stock photos located online. 
        This site is for educational purposes only and no copyright infringement is intended - just an example of product placement for my fictional chocolate company.
        -   The imagery used for the recipes is dependent on the content uploaded by the user. I was unable to create a system where the user uploads their own photo 
        directly to the site, however, they can upload to a free hosting platform that I have linked to in my new recipe form, they just need to paste the image url to the 
        site and it will display with the recipe details.
        -   I created a favicon icon for the browser tab - a smaller version of the logo image with the initials 'B & S' 
        <img src="https://res.cloudinary.com/passion4film/image/upload/v1617897186/bs-favicon-small_xtrf2b.png" style="margin: 0;">

## Wireframes page designs

**Home page:**

<img src="static/images/wireframes/home_page.png" style="margin: 0;">

**Register Page:**

<img src="static/images/wireframes/register.png" style="margin: 0;">

**Log In Page:**

<img src="static/images/wireframes/login.png" style="margin: 0;">

**Profile Page:**

<img src="static/images/wireframes/profile.png" style="margin: 0;">

**All Recipes Page:**

<img src="static/images/wireframes/all_recipes.png" style="margin: 0;">

**Add / Edit Recipes Page:**

<img src="static/images/wireframes/add_edit_recipes.png" style="margin: 0;">

**Categories Page - only for the Admin:**

<img src="static/images/wireframes/categories-for_admin.png" style="margin: 0;">

## MongoDB data schema design

MongoDB is a non-relational database, the database stores 'collections' instead of tables.

*"MongoDB is an open-source document database built on a horizontal scale-out architecture. Founded in 2007, MongoDB has a worldwide following in the developer community.
Instead of storing data in tables of rows or columns like SQL databases, each row in a MongoDB database is a document described in JSON, a formatting language."*

*"Document databases are extremely flexible, allowing variations in the structure of documents and allowing storage of documents that are partially complete. One document 
can have others embedded in it. Fields in a document play the role of columns in a SQL database, and like columns, they can be indexed to increase search performance."*

*   The document data model is a powerful way to store and retrieve data.

*   MongoDB has a great user experience for developers who can install MongoDB and start writing code immediately.

*   MongoDB can be used everywhere by anyone.

Check out more about why to use MongoDB [here](https://www.mongodb.com/why-use-mongodb)

### The BitterSweet© MongoDB collection design:

<img src="static/images/mongodb-schema.png" style="margin: 0;">

The Categories list contains just the object id and category_name

The Users list contains an Object id, the username, password (that has been securely hashed) & the profile_img which is the string of the url - it gets drawn back to the site via Python and displays as an image on the profile page.

The Recipes list contains:
- Object id
- category_name - which has to match an option from the categories list
- recipe_name - a string created by the user
- ingredients_measurements - which is an array with the ingredients nested inside, therefore they are displayed to the site on individual lines for easier viewing.
- preparation_steps - the same as above - an array with the steps nested inside and they also show individually - but I have the jinja index loop with them so they display as a numbered list of steps needed to create the recipe.
- time - the bake time and temp stored as a string
- is_vegan - this is a check-box and the default is "off" - the user can change to "on" by sliding the check-box to indicate the recipe is suitable for Vegans.
- recipe_img - is the string of the url the user submitted for the recipe image.
- created_by - this is the username from the Users list. I am aware that the Object id of the user would be more secure, but I wasn't able to make this amendment in time. As the user doesnt have the ability to change their username there is no risk of it being changed and therefore not matching this section and causing the user to be unable to edit their own recipes anymore.

## Features

-   Responsive on all device sizes. For example:

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897085/responsive1_rmhkgi.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897085/responsive2_fuvfd8.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897085/responsive3_n1evys.png" style="margin: 0;">

### Home Page
-    The first page the users come to is a home page - which explains the site and gives the site owners their opportunity to promote their chocolate products, while tying in with the
purpose of the site - as a chocolate recipe sharing site.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897082/home_xvl8t9.png" style="margin: 0;">

### Register & Log In Pages
-   Users are able to 'Register' or 'Log In' when first entering the site, these pages are clear, self-explanatory and easy to navigate. The users are limited to what pages they can see and have no ability to share or edit their own recipes without registering and logging in. 
-   For the Register page - there is code to check that the username doesnt already exist and there are rules for an acceptable password (5-15 characters A-Za-z0-9) alphanumperic only. The password, if conforming with the requirements, is hashed using werkzeug.security - a feature of Flask - so it is stored securely in the database and cannot be viewed by anyone.
-   For the Log In page - there is code to check that the username and password (with a check password hash from Flask) matches the database and then the log in is successful. If the username and/or password doesn't match a generic message is displayed. This is for security so the user isn't told which entry failed so if they are not genuine they cannot try to hack the system.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897084/register_dpyqlf.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897082/login_ocvojr.png" style="margin: 0;">

### Profile Page
-   As soon as the user successfully registers or logs in, they are re-directed to their own personalised 'Profile' page - where the image url they uploaded as part of their registration is loaded on the screen with a welcome message. They also have the ability to edit their profile picture to any url they choose.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897084/profile_gclwde.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897084/edit-profile_prxaot.png" style="margin: 0;">

### Recipes Page
-  The 'Recipes' page contains all recipes added by users of the site. All recipes are visable, whether a user is registered/logged in or not.
The recipes consist of Materialise 'Card Reveal' containers - that feature an image of the dish in question, which can be clicked on to reveal the recipe instructions.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897082/card-reveal1_oxcx4j.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617975624/card-reveal2_jd3gl4.png" style="margin: 0;">

-   If you are the user who created the recipe, you are then given the options to edit the recipe - which takes you to this page:

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897084/edit-recipe_ahsuox.png" style="margin: 0;">

-   Or to delete the recipe, which has defensive programming to double check you want to delete something for safety measures.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897083/delete_kiavf2.png" style="margin: 0;">

### New Recipe Page
-   The 'New Recipe' Page allows a registered/logged in user to add a recipe to the site. The form they have to fill in is clear and easy to follow. A url for the image must be included The instructions for this is made clear on the page.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897081/add-recipe_bfbfht.png" style="margin: 0;">

### Log Out
-   The 'Log Out' option is available as soon as a user logs in - by clicking on this the user's session cookies are removed from the site and they are re-directed to the log in page, and must log back in to add, edit or delete any recipes.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897082/logout_yodkkm.png" style="margin: 0;">

### Future Features
-   I wanted the user to be able to upload any files from their own computer/mobile to the site for the recipe image or profile picture. I tried to do this using Cloudinary and AWS S3 - but was unable to get the code to work in time. After seeing advice on Slack that for this project a url image upload is just as acceptable I went down this route instead. But if I was to improve this in the future I would like to get either Cloudinary or AWS S3 to work.

-   I would like in the future to enable the users to 'like' their favourite recipes, which could be saved to their profile page so they have easy access to the recipes they like.

-   I would like to set-up a system where the user can re-set their password should they forget it - an email could be sent with a link to take them to a page to re-set their password. The registration would require an email input and their email stored in the database for this to work.

## Error Handling

I created custom error pages so that if the user encounters a page that doesn't exist/deleted/forbidden etc, the stlye of the error page will match the rest of the site. This makes the site more professional.

- 404 Not Found
- 403 Forbidden
- 410 Gone
- 500 Internal Server Error

I reviewed the documentation on [Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/) in order to achieve this.

404 error page example

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897082/404-page_rki2vg.png" style="margin: 0;">

## Technologies Used

### Languages Used

In this project I used:
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JQuery](https://jquery.com/) 
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Jinja](https://pypi.org/project/Jinja2/) 

### Frameworks, Libraries & Programs Used

-   [Flask](https://flask.palletsprojects.com/en/1.1.x/) Flask is the framework used in developing the site.
-   [MongoDB](https://www.mongodb.com/cloud/atlas) MongoDB is the database where all the data for the site is stored and organised.
-   [PyMongo](https://docs.mongodb.com/drivers/pymongo/) PyMongo is the tool used to communicate between Python and MongoDB.
-   [Heroku](https://www.heroku.com/home) Heroku is where the site is deployed.
-   [Google Fonts:](https://fonts.google.com/) Google fonts were used to import the 'Satisfy' font into the style.css file which is used on all pages throughout the project.
-   [Font Awesome:](https://fontawesome.com/) Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
-   [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
-   [Git:](https://git-scm.com/) Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
-   [Responsinator:](http://www.responsinator.com/) Responsinator was used to check the site was responsive across all devices.
-   [Am I Responsive](http://ami.responsivedesign.is/) Am I Responsive was used to demonstrate the site was responsive in the attached screenshots.
-   [Balsamiq:](https://balsamiq.com/) Balsamiq was used to create the wireframes during the design process.
-   [Lighthouse](https://developers.google.com/web/tools/lighthouse)
-   Chrome, Microsoft Edge & Firefox internet browsers.
-   Adobe Photoshop.
-   I also made use of the [Materialise framework library](https://materializecss.com/getting-started.html).

## Testing

### Manual Testing documentation

[Please see the testing file](testing.md)

### Validators

I used the following services to validate every page of the project to ensure there were no syntax errors:

-   [W3C Markup Validator](https://validator.w3.org/) Using this validator shows some errors on every page due to the jinja code, however it's important to check all pages for non jinja errors also. There is no way I have found to get the validator to accept the jinja coding.
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
-   [JSHint](https://jshint.com/)

<img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />

### Testing User Stories

- #### Site user goals
    1. As a site user, I want to be able to register for the site and navigate it easily, then to be able to log in and out when I wish.
        -   Upon entering the site there is a clear welcome explanation about the site and it's purpose. There are also clear navigational 
        buttons throughout the site that are clear to understand and enable the site to be easy to navigate. The option to register, log in and log out 
        are clear and easy to do, as per earlier screenshots.

    2. As a site user, I want to be able to view the recipes already on the site, but also to add and display my own.
        -   The Recipe page clearly displays the recipes added to the site in a functional and visually appealing way.
        Once logged in the option to add your own recipe is clear and the form to be completed is straightforward and easy to understand & use.

    3. As a site user, I want to be able to edit and/or delete my recipes when I want to.
        -   If a recipe was created by the user, they have the options (after clicking on the card reveal) to:
            *   edit the recipe - which takes them to a form similar to the add a recipe form, where they can change any aspect of the recipe or cancel and go back to the previous page.
            *   delete the recipe - which has a modal to double check that they wish to delete it for security purposes, a user cannot accidently delete their recipe.

- #### Site owner goals
    1. As a site owner, I want to promote the company BitterSweet© and to suggest the users try these new chocolate products in the recipes. 
        -   The home page contains a promotion of the BitterSweet© chocolate brand as well as info on the hostory of chococlate and images showing the range of products 
        BitterSweet© has to offer - this page also informs the user that this chococlate is available in supermarkets (this is just for educational purposes and BitterSweet© isnt a real brand - no copyright infringement)

    2. As a site owner, I want the users to be able to create an acocunt and navigate the site easily, as well as create/edit/delete their recipes as much as they choose to.
        -   As shown in the features screenshots, a registered/logged in user can utilise all aspects of the C.R.U.D funtionality. They can Create their own recipes, they can Read all the 
        recipes already on the site, they can Update their own recipes and they can Delete their own recipes, easily and effectively.

    3. As a site owner, I want the users to be able to search through the chocolate recipes on the site for keywords or ingredients.
        -   The search bar that is prominent on the Recipes page is designed to identify recipes based on the name or ingredients listed in the recipes.
            <img src="https://res.cloudinary.com/passion4film/image/upload/v1617897085/search_apgpqu.png" style="margin: 0;">

        -    If a match is located the recipe(s) in question are displayed, if a match isnt found a message shows clearly.
        
        <img src="https://res.cloudinary.com/passion4film/image/upload/v1617897084/no-results_qqr6wv.png" style="margin: 0;">

        -   The reset button removes the search results and restores the page to displaying all recipes again.


### Further Testing

-   The Website was tested on Google Chrome, Microsoft Edge and FireFox browsers to check it loaded correctly.
-   The website was viewed on a variety of devices such as Desktop, Laptop and a variety of iPhones & Android phones to check it loaded correctly.
-   The website was tested on Responsinator to ensure responsiveness on all devices.
-   A large amount of testing was done to ensure that all pages were linking correctly. This was done by frequently moving from one page by clicking the button links for 
all pages on all devices.
-   A large amount of testing of the database C.R.U.D functions was completed during development. After every change the site was tested to ensure no new issues or bugs were located.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues, they reported a success on all fronts.
-   The website was tested on [Lighthouse](https://developers.google.com/web/tools/lighthouse) and achieved a high score on all issues:

    <img src="https://res.cloudinary.com/passion4film/image/upload/v1617897082/lighthouse_rg2gow.png" style="margin: 0;">

    You can use the Lighthouse Tool on any webpage by right clicking on the site, then 'inspect', then the two arrow button '>>' and 'Lighthouse'. You can select to test the site 
    as a desktop version or mobile version and then click the blue 'Generate Report' which will provide you with the results in the screenshot provided above.

## Known Bugs

No bugs have been located at the time of Deployment.

## Deployment

### GitHub Pages

To deploy to GitHub Pages you can using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Passion4film/Milestone-Project-3/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com/Passion4film/Milestone-Project-2) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Passion4film/Milestone-Project-3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Passion4film/Milestone-Project-3)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Passion4film/Milestone-Project-3
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/Passion4film/Milestone-Project-3
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Deployment to Heroku 

This site was deployed to Heroku. if you have an account login [here](https://id.heroku.com/login)

Before creating a Heroku application there are some files that need to be created to run the app:

* requirements.txt file (which lists the dependencies that are needed for the app) 
* Procfile (this is what Heroku looks for to know which file runs the app, and how to run it)

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

At Heroku.com you can choose to 'Create a New App' - the name must be unique, in lowercase letters and use dashes instead of spaces.

* Next, select the region closest (doesn't have to be exact - I chose Europe) to you then click 'Create App'.
* For this project I chose to setup 'Automatic Deployment' from my GitHub repository. 
* Make sure your GitHub profile is displayed, then add your repository name then click 'Search'. Once it finds your repo, click to connect to this app.
* DON'T click to Enable Automatic Deployment yet, otherwise you'll get unwanted application errors.

Since environment variables are within a hidden env.py file, Heroku won't be able to read those variables. Click on the 'Settings' tab for your app, and then click on 
'Reveal Config Vars', where we can securely tell Heroku which variables are required. Must match the details in the env.py file you have to create in github.

Make sure not to include any "quotes" for the key, or the value.

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|PORT|`5000`|
|SECRET_KEY|`<app secret key>`|
|MONGO_URI|mongodb+srv://root:r00tUser26@myfirstcluster.nsq0m.mongodb.net/bitter_sweet?retryWrites=true&w=majority
|MONGO_DBNAME|`bitter_sweet`|

* Make sure all changes on GitHub have been added, commited and pushed to GitHub. 
* We can now safely 'Enable Automatic Deployment', as everything should be available on our repository.
* Click 'Deploy Branch'. Heroku will now receive the code from GitHub, and start building the app using the required packages. 
* When this is completed it will state: "Your app was successfully deployed." 
* Click "View" to launch your new app.

## Future maintainability

The images used are stored in the static/images folder for easy maintainability, 

There is clear code commenting for each section of the HTML pages, which make it easy for developers to view for future maintenence. It makes changing the code/updating the 
details easier for other developers.

There is also clear code commenting in the CSS, Python & JQuery sections. Each section is clearly labled to ensure if any bugs or errors do occur it will be simple to see what part of the page each section affects. This makes updating and changing the code easier for other developers.

## Credits

### Content

Online tutorials:

* jQuery for adding/removing ingredients and preparation steps code inspired by youtube video [made by Knowledge Thrusters](https://www.youtube.com/watch?v=7LpZYOyVDK0)

Recipes:

* The recipes added by myself were from my family collection, or taken from [BBC Food](https://www.bbc.co.uk/food).

### Media

I created the logo, flavicon, 404 error and mock-designs for chocolate bars for the site using Adobe Photoshop.

The images used to create the photoshopped designs were obtained from Google/images. 

[Vegan Chocolate Bars](https://cdn-a.william-reed.com/var/wrbm_gb_food_pharma/storage/images/publications/food-beverage-nutrition/confectionerynews.com/article/2019/11/18/mars-launches-its-vegan-galaxy-chocolate-bars-in-uk/10376785-1-eng-GB/Mars-launches-its-vegan-Galaxy-chocolate-bars-in-UK_wrbm_large.jpg)

[Blank Chocolate Bar](https://d2qpatdq99d39w.cloudfront.net/wp-content/uploads/2019/09/05111656/Cadbury-Wordless-Bar.jpg)

[White, Milk & Dark Chocolate](https://blog.skipscandies.com/wp-content/uploads/2019/05/white-Dark-and-Milk-chocolates.jpg?fit=1024%2C536&ssl=1)

[Chocolate Piece](https://www.lindt.co.uk/media/wysiwyg/lindt-hello-chocolate-326x425.jpg)

[Chocolate Splash](https://i.pinimg.com/originals/2d/4a/f7/2d4af70854f6326ad642fe637da449f0.jpg)

I also used the [Fairtrade](https://www.balasport.co.uk/wp-content/uploads/2019/04/FM_RGB-2.png) Logo on my site.

The users are able to upload a url of their recipe - I have directed them to a licence-free site for stock images 
[Pixabay](https://pixabay.com/), or they can upload their own at [IMGBB](https://imgbb.com/)

All images used in the web design and not uploaded by users are stored in the static folder under images (in their own named folders) and labled clearly.

[Materialise framework library](https://materializecss.com/getting-started.html).

## Acknowledgements

I received inspiration for this project from the Task Manager mini-project as part of the Code Institute course, example websites, Slack message boards as well as 
much appreciated help from my Mentor; Antonio Rodriguez.

**DISCLAIMER: This project is for educational purposes only, no materials/files are intended for any commercial use**

[Contents](#Table-of-Contents)