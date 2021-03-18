$(document).ready(function (){
    $("#postDiv").hide()
    $(".commentDiv").hide()
    $(".comments").hide()
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
    $('.commentButton').click(function (){
        div = $(this).parent().children('.commentDiv')
        if(div.is(':visible')){
            div.hide()
            $(this).css('background','')
        }
        else{
            div.show()
            $(this).css('background','aqua')
        }
    })
    $('.view').click(function () {
        x = $(this).siblings('.comments');
        if(x.is(':visible')){
            x.hide();
        }
        else{
            x.show();
        }
    })


    $('.comment').click(function () {
        text = $(this).parent().children('.writeComment').val()
        if(text===''){
            alert("You cannot comment nothing")
        }
        else{
        }
    })

    $('#post').click(function () {
        if($('#writePost').val()==="") {
            alert("You cannot post nothing")
        }
        else{
        }
    })
    $("#like").click(checkLikeDiscussion);
    $('#dislike').click(checkDislikeDiscussion)
    $('.likePost').click(checkLikePost)
    $('.dislikePost').click(checkDislikePost)
});


function checkLikeDiscussion(){
    $.post('/like',{
        'user_id' : $('#user_id').html(),
        'discussion_id' : $('#discussion_id').html(),
        'post_id' : ''
    }).done(function (response){
        num = parseInt($('#like_number').html())
        if(response ==='1'){
            alert('You canceled a like before')
            $("#like").css('background','')
            num=num-1
            $('#like_number').html(num)
        }
        else{
            $("#like").css('background','greenyellow')
            num=num+1
            $('#like_number').html(num)
        }
    }).fail(function (){
            alert('failure')
    });
}


function checkLikePost(){
    button = $(this)
    post_id=$(this).parent().parent().children('#post_id').html()
    $.post('/like',{
        'user_id' : $('#user_id').html(),
        'discussion_id' : $('#discussion_id').html(),
        'post_id' : post_id
    }).done(function (response){
        if(response ==='1'){
            alert('You canceled a like before')
            button.css('background','')
        }
        else{
            button.css('background','greenyellow')
        }
    }).fail(function (){
            alert('failure')
    });
}


function checkDislikeDiscussion(){
    $.post('/dislike',{
        'user_id' : $('#user_id').html(),
        'discussion_id' : $('#discussion_id').html(),
        'post_id' : ''
    }).done(function (response){
        num = parseInt($('#dislike_number').html());
        if(response ==='1'){
            alert('You canceled a dislike before')
            $("#dislike").css('background','')
            num=num-1;
            $('#dislike_number').html(num)
        }
        else{
            $("#dislike").css('background','red')
            num=num+1;
            $('#dislike_number').html(num)
        }
    }).fail(function (){
            alert('failure')
    });
}


function checkDislikePost() {
    button = $(this)
    post_id = $(this).parent().parent().children('#post_id').html()
    $.post('/dislike', {
        'user_id': $('#user_id').html(),
        'discussion_id': $('#discussion_id').html(),
        'post_id': post_id
    }).done(function (response) {
        if (response === '1') {
            alert('You canceled a dislike before')
            button.css('background', '')
        } else {
            button.css('background', 'red')
        }
    }).fail(function () {
        alert('failure')
    });
}