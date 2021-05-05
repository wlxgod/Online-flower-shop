$(document).ready(function (){
    $("#username").on("change",check_username);
    $("#email").on("change",check_email);
});


function check_username(){
    var chosen_username = $(this);
    var checkuser = $("#checkuser")
    checkuser.removeClass();

    $.post('/checkusername',{
        'username' : chosen_username.val()
    }).done(function (response){
        var server_response = response['text']
        var server_code = response['returnvalue']
        if(server_code == 0){
            $("#email").focus();
            checkuser.html(server_response);
            checkuser.addClass("success");
        }
        else{
            chosen_username.focus();
            checkuser.html(server_response);
            checkuser.addClass("failure");
        }
    }).fail(function (){
            checkuser.html('Server Error existing');
            checkuser.addClass("failure");
    });
}

function check_email(){
    var chosen_email = $(this);
    var checkemail = $("#checkemail")
    checkemail.removeClass();

    $.post('/checkemail',{
        'email' : chosen_email.val()
    }).done(function (response){
        var server_response = response['text']
        var server_code = response['returnvalue']
        if(server_code == 0){
            $("#password").focus();
            checkemail.html(server_response);
            checkemail.addClass("success");
        }
        else{
            chosen_email.focus();
            checkemail.html(server_response);
            checkemail.addClass("failure");
        }
    }).fail(function (){
            checkemail.html('Server Error existing');
            checkemail.addClass("failure");
    });
}