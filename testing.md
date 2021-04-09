# Manual Testing Evidence

* Checking flask is running:

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897083/check-flask1_txh6hd.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897083/check-flask2_dv5fp4.png" style="margin: 0;">


* Checking flask is connected to MongoDB


<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897083/mongodb-connection1_p5kzpz.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897083/mongodb-connection2_rvs14z.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897084/mongodb-connection3_jubupr.png" style="margin: 0;">


* Testing base template works:


<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897085/testing-base-template1_axkhe6.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897085/testing-base-template2_vyudow.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897085/testing-base-template3_nrbcsh.png" style="margin: 0;">


* Create delete modal so the user has to verify they want to delete a recipe:


<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897083/delete-modal1_aqoejc.png" style="margin: 0;">
<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897083/delete-modal2_iorhve.png" style="margin: 0;">


An issue encountered when setting up the delete a recipe function was that a recipe could be deleted with one click of the button, which means there was a risk that it could 
be done accidentely or the user could change their mind but have no warning.

To combat this and create some defensive progamming I included a modal, using Materialise, that will pop-up when the delete button is clicked to ask the user if they are sure 
that they want to delete. They can cancel and they go back to the page, or they can choose again to delete and the recipe will be deleted. Haveing a double-check on the user's 
intentions make it much safer and more user-friendly.

* The edit and delete buttons affected the grid size of the recipes and caused them not to sit right on the page – 
so I moved the buttons (which only appear if the created by user matches the logged in user) now they are under the card-reveal. 
So, when you click on the card to see the recipe details, then you can see the buttons at the top. Makes the recipes sit much cleaner on the page.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1617897084/edit-delete-buttons_jeinee.png" style="margin: 0;">

# Bugs and issues that needed to be overcome:

## Register & Login

* Expected

    - When a user tries to register their username will be checked to see if it is unique - if so their password will need to fit the requirements. To Log In to the site, a check will be made to see if the username and password matches what is stored in the database for that user.

* Testing

    -  Creating multiple users, asking friends/family to register - logging in and out multiple times and checking the database to see that the required details were captured there correctly.

* Result

    - A new user can easily register an account, their username is checked and their password is hashed for security. An existing user can easily log in and their username/password is checked and only allowed to log in if both match - should one not match the user isn't told which one failed to increase security so it is harder to force their way onto the system not knowing which field is incorrect.

## Jinja templating for ingredients & preparation steps

* Expected

    - 

* Testing

    - 

* Result

    - 

* Fix

    - 

## Adding dynamic plus/remove buttons for ingredients/preparation steps

* Expected

    - 

* Testing

    - 

* Result

    - 

* Fix

    - 

## Uploading images for recipes

* Expected

    - 

* Testing

    - 

* Result

    - 

* Fix

    - 

## Editing profile picture url

* Expected

    - 

* Testing

    - 

* Result

    - 

* Fix

    - 

[Return to README](README.md)