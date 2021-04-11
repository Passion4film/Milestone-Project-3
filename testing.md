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
    - However some users encountered difficulty with logging back in as the form kept saying the username or password didnt match the pattern required. I checked the code and the pattern was identical to the register page so I couldn't see why certain users had problems.

* Fix

    - To fix this so that no one has any issues in logging in I removed the pattern requirement for the log in username and password and this resolved the issue. My reason behind this is that the user had to comply with the required pattern in order to register their account. In the logging in stage the code is designed to check that the username and password matches what they registered with - if they match they will clearly be adhering to the pattern requirement anyway. It is worth removing this potential issue for users so that they have a smoother process when they log back in to the site.  

## Jinja templating for ingredients & preparation steps

* Expected

    - The ingredients and preparation steps to be displayed neatly on the page while being easy to read.

* Testing

    - I added the jinja templating to bring the information through from Mongodb the same way as the other fields.

* Result

    - The ingredients/steps came through in one line with gaps between them rather than on one line.

* Fix

    - After reviewing help online I saw that I needed to create another jinja loop for the ingredients/steps to iterate through them all and display on separate lines.
    
    ```
    {% for ingredient in recipe.ingredients_measurements %}
        {{ ingredient }}
    {% endfor %}
    ```
    
    And the same for the preparation steps.

## Adding dynamic plus/remove buttons for ingredients/preparation steps

* Expected

    - When a user is adding more ingredients/steps to a new recipe - or adding more to an edited recipe, they should be able to click on a button and a new blank line in the form will appear - this will then be saved to the database as a nested array.

* Testing

    - Originally, with the help of my mentor, I used JavaScript to create a function that added fields when a new ingredient was required. Which I then tried to emulate for the prepartation steps.

* Result

    - The preparation steps button overwrote the ingredients field. So if you had a list of new ingredients and you pressed for another preparation step the ingredient field was replaced by a blank step instead.

* Fix

    - I found a video guide to creating dynamic input fields (credited in the code and readme) using JQuery. As I had already used JQuery for the materialize initialisation I took the information from the video and adjusted it to my needs and the buttons now work correctly. I am aware that on the edit recipe page the buttons don't delete the earlier rows - just ones created by the button. However, on the basis that its more likley to need to add or edit ingredients/steps than to remove, I have left this in. It could be a future aspect to be rectified if it proves to be an issue to any users.

## Uploading images for recipes

* Expected

    - The user can upload an image of the recipe they are adding to the site to make the site look more visual and the recipe seem more attractive to other users.

* Testing

    - I experimented with many ways of doing this, the external image sites such as Cloudinary and AWS S3 were beyond my scope and time left for this project. Furthermore Slack advice was not to spend too long on this one aspect as images cannot be saved in mongodb - but url strings could. I therefore tested out how I could get this to work instead.

* Result

    - The user can paste the image address from an online image or from a free uploading site and the site should display this image on the recipe reveal card.

* Fix

    - I found that through testing some users had difficulty with this, so I made sure the instructions are clear as I possibly can - since a file extension to indicate the file is an image is essential (jpeg, jpg, png for example). The copying and pasting of an image address is also more suited to the desktop version of the site than the mobile.

## Editing profile picture url

* Expected

    - The user (who has chosen a profile image when registering in a similar way to adding a reicpe image) is able to upload a new picture that displays on their own private profile page. 

* Testing

    - When creating the @app.route python for this to work I tried to take the same approach as I did with the recipe images and the way a recipe is edited.

* Result

    - However I couldn't get it to work as the profile had a username variable and the user_id wasnt being recognised.

* Fix

    - Once I had set the username variables in the code and enabled python to find the correct user, I had to make sure that mongo.db.users was being updated, as thats the name of the collection that the user's profile image is stored. I also had to reference the username variable on the form's action for the edit profile page. Follwoing these adjustments the page works properly and if the user pastes a proper image address (including an image file extension as mentioned earlier) then the url string stored in their user collection is updated and the new image is displayed on their profile page with a flash message to confirm.

[Return to README](README.md)