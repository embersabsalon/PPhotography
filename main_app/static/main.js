$(document).ready( function() {



$('#likes').on('click',function(event){
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url : '/likepicture',
        type : 'GET',
        data: { photoid : element.attr("data-id")},
        success: function(response){
                    element.html(' ' + response);
                }
    });
});
});