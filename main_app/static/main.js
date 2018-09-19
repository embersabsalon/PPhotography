$(document).ready( function() {



$('button').on('click',function(event){
    event.preventDefault();
    var element = $(this);
    elementoget = '#likes' + element.attr("data-id");
    $.ajax({
        url : '/likepicture',
        type : 'GET',
        data: { photoid : element.attr("data-id")},
        success: function(response){
                    element.html('Like (' + response +')');
                    $(elementoget).html('Likes: ' + response);
                }
    });
});
});