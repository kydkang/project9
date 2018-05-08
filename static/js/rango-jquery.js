$(document).ready(function () {
    $("#about-btn").click(function (event) {
        alert("You clicked the button using JQuery!");
    });

    $("p").hover(function () {
        $(this).css('color', 'red');
        },
        function () {
            $(this).css('color', 'blue');
    });
});

$('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/rango/suggest/', {suggestion: query}, function(data){
        $('#cats').html(data);
    });
})
