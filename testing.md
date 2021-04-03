# Manual Testing Evidence

* Checking flask is running:

<img src="static/images/screenshots/check-flask1.png" style="margin: 0;">
<img src="static/images/screenshots/check-flask2.png" style="margin: 0;">

* Checking flask is connected to MongoDB

<img src="static/images/screenshots/mongodb-connection1.png" style="margin: 0;">
<img src="static/images/screenshots/mongodb-connection2.png" style="margin: 0;">
<img src="static/images/screenshots/mongodb-connection3.png" style="margin: 0;">

* Testing base template works:

<img src="static/images/screenshots/testing-base-template1.png" style="margin: 0;">
<img src="static/images/screenshots/testing-base-template2.png" style="margin: 0;">
<img src="static/images/screenshots/testing-base-template3.png" style="margin: 0;">

* Create delete modal so the user has to verify they want to delete a recipe:

<img src="static/images/screenshots/delete-modal1.png" style="margin: 0;">
<img src="static/images/screenshots/delete-modal2.png" style="margin: 0;">

An issue encountered when setting up the delete a recipe function was that a recipe could be deleted with one click of the button, which means there was a risk that it could 
be done accidentely or the user could change their mind but have no warning.

To combat this and create some defensive progamming I included a modal, using Materialise, that will pop-up when the delete button is clicked to ask the user if they are sure 
that they want to delete. They can cancel and they go back to the page, or they can choose again to delete and the recipe will be deleted. Haveing a double-check on the user's 
intentions make it much safer and more user-friendly.

* The edit and delete buttons affected the grid size of the recipes and caused them not to sit right on the page – 
so I moved the buttons (which only appear if the created by user matches the logged in user) now they are under the card-reveal. 
So, when you click on the card to see the recipe details, then you can see the buttons at the top. Makes the recipes sit much cleaner on the page.

<img src="static/images/screenshots/edit-delete-buttons.png" style="margin: 0;">

# Bugs and issues that needed to be overcome:

## Matching the cards

* Expected

    - The game is expected to know when 2 cards match each other and to keep them turned face-up, if they do not match they are to be flipped back over for the user to try again. Used frameworks to name each card image and created code that checked the framework names to know if the cards matched or not.

* Testing

    - Tested the site by running the matchcard funtion multiple times and running a check in the console.log to ensure it was registering whether 2 cards matched or not. 

* Result

    - Cards that match remain face-up and cards that dont match are 'unflipped' so their image is hidden again and then the user can try again.

## Game timer function

* Expected

    - The game timer function triggering with the first click of the first card of the game only, and not every time a card was clicked.

* Testing

    - Tested the site by playing the game and watching the time to see what happened.

* Result

    - The time function was triggering with each first click on a card.

* Fix

    - Overcame with 'var firstClick = false' in app.js, which solved the problem and now the timer function only activates on the first card click at the beginning of the game.

## Disable cards

* Expected

    - Once two cards had been over-turned and no match found, they needed to be 'unflipped' again so the user couldnt keep 'flipping' the cards before the match function could be executed.

* Testing

    - Tested the site by quickly clicking on multiple cards when the game started and triggering them to be 'flipped'.

* Result

    - Without time to execute the match function the cards remained flipped over and therefore broke the game.

* Fix

    - A disableCards funtion was needed, which locked the board until the match function had resolved. Also needed to create a 'disableAllCards' funtion for when the game is won or lost so the user cant keep playing so they need to select to play again or a new level.

## Level 2 problems

* Expected

    - Once the code was in place for the first level, I aimed to incororate the same code for a second, harder, level. The code was expected to work the same way.

* Testing

    - Tested the site when the level 2.html was created and the new game grid/images uploaded.

* Result

    - The code didnt work and no cards were flipped and the time and score didnt update. Also as there were 8 pairs of cards instead of 6 the critera for winning the game was wrong.

* Fix

    - The 'const cards' variable wasnt triggering for the level 2 cards, to overcome this a 'cards2' was created and another event listener. 
        A level1 & level2 ID was given to each game grid and these targeted using 'getAttribute('id')' and 'levelOneMatches' and 'levelTwoMatches' variables created.

## IOS Mobile devices

* Expected

    - The site is expected to work on a mobile device exactly the same way as a desktop.

* Testing

    - Tested the site using Chome Dev Tools for responsivness and sent the deployed link to several mobile devices, some android and some iPhones of differing types.

* Result

    - The CSS wasnt loading correctly for the game on IOS software, the cards wouldnt 'flip' correctly.

* Fix

    - Solved this by running the appropriate CSS through 'Autoprefixer' (as linked to in README) and adding the webkit options to the code for IOS software.

[Return to README](README.md)