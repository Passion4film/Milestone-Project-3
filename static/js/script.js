/*
    jQuery for MaterializeCSS initialization
*/
$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();

/*
    jQuery for Materialize Select Validation - from Task Manager Project in Code Institute
*/
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

/*
    jQuery for adding/removing ingredients and preparation steps
    code inspired by youtube video: https://www.youtube.com/watch?v=7LpZYOyVDK0 - made by Knowledge Thrusters
*/

function addIngredient(){
    $('#first_ingredient .new_ingredient').clone().find('input').val('').end()
        .appendTo('#moreIngredients');
};

function editIngredient(){
    $('#first_ingredient .hidden').clone().removeClass('hidden').find('input').val('').end()
        .appendTo('#moreIngredients');
};

function removeIngredient(){
    $('#moreIngredients .new_ingredient').last().remove();
};

function addStep(){
    $('#extraSteps .new_step').clone().find('input').val('').end()
        .appendTo('#moreSteps');
};

function editStep(){
    $('#extraSteps .hidden').clone().removeClass('hidden').find('input').val('').end()
        .appendTo('#moreSteps');
};

function removeStep(){
    $('#moreSteps .new_step').last().remove();
};