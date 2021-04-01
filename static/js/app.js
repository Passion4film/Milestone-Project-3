/*
    function for adding new recipe ingredients 
*/
/* var ingredientCount = 1;
    document.getElementById('addIngredient').addEventListener('click', function(){
        let nextId = 'next'+ ingredientCount + 1;
        const labelText = 'New Ingredient'
        const removeId = 'remove'+ ingredientCount;
        ingredientCount = ingredientCount + 1;
        const newInput = '<div class="input-field col s12"> <i class="fas fa-balance-scale prefix deep-purple-text text-darken-3 text-shadow"></i> <textarea id="'+ labelText + '" name="ingredients_measurements" minlength="5" maxlength="300" class="materialize-textarea validate white-text" required></textarea> <label for="'+ labelText + '">'+ labelText + '</label><i class="fas fa-trash-alt deep-purple-text text-darken-3 text-shadow removeInput" id="'+ removeId + '"></i></div>';
        newDiv = document.createElement("div")
        newDiv.id = nextId;
        document.getElementById('extraIngredients').appendChild(newDiv);
        document.getElementById(nextId).innerHTML = newInput;

        var elems = document.querySelectorAll(".removeInput");
        [].forEach.call(elems, function(el) {
            el.addEventListener('click', function(event){
                event.target.parentElement.remove();
            });
        });
    });

/*
    function for adding new recipe preparation steps 
*/
/*var stepCount = 1;
    document.getElementById('addStep').addEventListener('click', function(){
        let nextId = 'next'+ stepCount + 1;
        const labelText = 'Next Step'
        const removeId = 'remove'+ stepCount;
        stepCount = stepCount + 1;
        const newInput = '<div class="input-field col s12"> <i class="fas fa-clipboard-list prefix deep-purple-text text-darken-3 text-shadow"></i> <textarea id="'+ labelText + '" name="preparation_steps" minlength="5" maxlength="300" class="materialize-textarea validate white-text" required></textarea> <label for="'+ labelText + '">'+ labelText + '</label><i class="fas fa-trash-alt deep-purple-text text-darken-3 text-shadow removeInput" id="'+ removeId + '"></i></div>';
        newDiv = document.createElement("div")
        newDiv.id = nextId;
        document.getElementById('extraSteps').appendChild(newDiv);
        document.getElementById(nextId).innerHTML = newInput;

        var elems = document.querySelectorAll(".removeInput");
        [].forEach.call(elems, function(el) {
            el.addEventListener('click', function(event){
                event.target.parentElement.remove();
            });
        });
    });
*/