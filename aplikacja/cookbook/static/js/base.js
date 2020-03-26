$(".body_img img").each(function(){
    $(this).addClass("img-fluid")
})

$("form input[type=submit]").each(function(){
    $(this).addClass("btn btn-primary")
})

$(".crispy_forms_file button, input[type=file]").each(function(){
    $(this).addClass("btn btn-secondary disabled")
})

$('input').attr('autocomplete','off');
