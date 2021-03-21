<h1 align="center"><img src="static/images/logo-img.png" style="margin: 0;" alt="image of site logo"></h1>

[View the live website here.](https://bitter-sweet-milestone-3.herokuapp.com/)

# BitterSweet


## The important things to consider were:

1. 
2. 
3. 
4. 
5. 

## User stories

- #### Site user goals
    1. As a site user, I want .
    2. As a site user, I want .
    3. As a site user, I want .

- #### Site owner goals
    1. As a site owner, I want .
    2. As a site owner, I want .
    3. As a site owner, I want .

-   ### Design
    -   #### Colour Scheme
        -   The main colours used are shades of brown, purple and white, as these complement each other nicely and are suggestive of the classic colours of Cadbury's, however as this is a site for the purpose of learning no copyright infringement is intended. 
    -   #### Typography
        -   The --- font is used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. --- is easy to read, attractive and appropriate to the aesthetic of the site. The font colour throughout is dependent on the background and the tupe of content to make it stand-out and for ease of reading against the background.
    -   #### Imagery
        -   I created the site logo using Adobe Photoshop and a stock photo located online that I edited to suit my purpose. 

## Wireframes page designs:


## Features

-   Responsive on all device sizes. For example:


## Technologies Used

### Languages Used

-   In this project I used [HTML5](https://en.wikipedia.org/wiki/HTML5), [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and [JavaScript](https://en.wikipedia.org/wiki/JavaScript). 

### Frameworks, Libraries & Programs Used

-   [Google Fonts:](https://fonts.google.com/) Google fonts were used to import the 'Satisfy' font into the style.css file which is used on all pages throughout the project.
-   [Font Awesome:](https://fontawesome.com/) Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
-   [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
-   [Git:](https://git-scm.com/) Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
-   [Responsinator:](http://www.responsinator.com/) Responsinator was used to check the site was responsive across all devices.
-   [Balsamiq:](https://balsamiq.com/) Balsamiq was used to create the wireframes during the design process.
-   [Autoprefixer CSS online](https://autoprefixer.github.io/) Autoprefixer was used to get the correct web extensions like -webkit- added to my CSS so that it worked on IOs systems.
-   [Lighthouse](https://developers.google.com/web/tools/lighthouse)
-   Chrome, Microsoft Edge & Firefox internet browsers.
-   Adobe Photoshop, for the logo.
-   I also made use of the [Materialise framework library](https://materializecss.com/getting-started.html).


## Testing

### Manual Testing documentation

[Please see the testing file](testing.md)

### Validators

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

<img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />

JSHint was used to check there were no errors in the JavaScript code, while there may be some warnings after running the JS though JSHint, they are mainly that a lot of the code is only available in ES6, but this was the code I was taught and there are no errors with the code, it works on all systems tested so I am keeping it with the ES6 version.

### Testing User Stories from User Experience (UX) Section

- #### Site user goals
    1. As a site user, I want .
        -   

    2. As a site user, I want  
        -   

    3. As a site user, I want 
        -   


- #### Site owner goals
    1. As a site owner, I want . 
        -   
    2. As a site owner, I want .
        -   
    3. As a site owner, I want 
        -   

### Further Testing

-   The Website was tested on Google Chrome, Microsoft Edge and FireFox browsers to check it loaded correctly.
-   The website was viewed on a variety of devices such as Desktop, Laptop and a variety of iPhones & Android phones to check it loaded correctly.
-   The website was tested on Responsinator to ensure responsiveness on all devices.
-   A large amount of testing was done to ensure that all pages were linking correctly. This was done by frequently moving from one page by clicking the button links for all pages on all devices.
-   A large amount of testing of the dtatbase C.R.U.D functions was completed during development. After every change the site was tested to ensure no new issues or bugs were located.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues, they reported a success on all fronts.
-   The website was tested on [Lighthouse](https://developers.google.com/web/tools/lighthouse) and achieved a high score on all issues:

    <img src="screenshots/lighthouse-desktop.jpg" style="margin: 0;">
    <img src="screenshots/lighthouse-mobile.jpg" style="margin: 0;">

    You can use the Lighthouse Tool on any webpage by right clicking on the site, then 'inspect', then the two arrow button '>>' and 'Lighthouse'. You can select to test the site as a desktop version or mobile version and then click the blue 'Generate Report' which will provide you with the results in the screenshots provided above.

## Known Bugs

An issue encountered when setting up the delete a recipe function was that a recipe could be deleted with one click of the button, which means there was a risk that it could be done accidentely or the user could change their mind but have no warning.

To combat this and create some defensive progamming I included a modal, using Materialise, that will pop-up when the delete button is clicked to ask the user if they are sure that they want to delete. They can cancel and they go back to the page, or they can choose again to delete and the recipe will be deleted. Haveing a double-check on the user's intentions make it much safer and more user-friendly.

No bugs have been located at the time of Deployment.

## Deployment to Heroku 

Before creating a Heroku application there are some files that need to be created to run the app, these are the requirements.txt file (which lists the dependencies that are needed for the app) and the Procfile (this is what Heroku looks for to know which file runs the app, and how to run it)

At Heroku.com you can 'Create a New App' and the name must be unique, and generally use dashes instead of spaces as well as lowercase letters.
Next, select the region closest to you then click 'Create App'.
For this project I chose to setup Automatic Deployment from my GitHub repository. Make sure your GitHub profile is displayed, then add your repository name then click 'Search'. Once it finds your repo, click to connect to this app.
DON'T click to Enable Automatic Deployment yet, otherwise we'll get unwanted application errors.

Since environment variables are within a hidden env.py file, Heroku won't be able to read those variables. Click on the 'Settings' tab for your app, and then click on 'Reveal Config Vars', where we can securely tell Heroku which variables are required.
Make sure not to include any "quotes" for the key, or the value.

Make sure all changes on GitHub have been added, commited and pushed to GitHub. We can now safely 'Enable Automatic Deployment', as everything should be available on our repository.
Click 'Deploy Branch'. Heroku will now receive the code from GitHub, and start building the app using the required packages. When this is completed it will state: "Your app was successfully deployed." Click "View" to launch your new app.

## Future maintainability

The images used are stored in the static/images folder for easy maintainability, 

There is clear code commenting for each section of the HTML pages, which make it easy for developers to view for future maintenence. It makes changing the code/updating the details easier for other developers.

There is also clear code commenting in the CSS & Python sections. Each section is clearly labled to ensure if any bugs or errors do occur it will be simple to see what part of the page each CSS and JavaScript section affects. This makes updating and changing the CSS and JS effects easier for other developers.

## Credits

### Content

Online tutorials:



### Media

I created the logo for the site using Adobe Photoshop.

The images used in this site were obtained from Google/images. 


All photos used are stored in the assets folder (and in their own named folders) and labled clearly.

## Acknowledgements

I received inspiration for this project from the online tutorials and example websites credited above as well as much appreciated help from my Mentor; Antonio Rodriguez.

**DISCLAIMER: This project is for educational purposes only, no materials/files are intended for any commercial use**