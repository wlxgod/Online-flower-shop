$(document).ready(function (){
    $("#postDiv").hide()
    $('#join').click(function (){
        if($("#postDiv").is(':visible')){
            $("#postDiv").hide()
            $('#join').css('background','')
        }
        else{
            $("#postDiv").show()
            $('#join').css('background','aqua')
        }
    })
});