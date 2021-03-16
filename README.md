<h1 align="center"><img src="static/images/logo-idea.png" style="margin: 0;" alt="image of site logo"></h1>

[View the live website here.](https://bitter-sweet-milestone-3.herokuapp.com/)

# BitterSweet



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