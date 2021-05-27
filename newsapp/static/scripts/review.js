$(document).ready(function () {

    $('#makereview').click(function () {
        console.log('start review')
        var input = $('#reviewtext').val()
        var rate = $('input[name=rating]:checked').val();
        var flower_id = $('#flower_id').attr('class')
        console.log('rate: ' + rate)
        console.log('flower_id: ' + flower_id)
        $.post('/sendreview', {
            'flower_id': flower_id,
            'text': input,
            'rate': rate
        }).done(function (state) {
            console.log(state['state']);
        });
    });

    $('.btn-reply').click(function(){
        var review_id = $(this).attr("id")
        $.post('/checkidentity').done(function (result) {
            console.log('review_id: '+review_id)
            console.log('identity: '+result['identity'])
            if(result['identity']=='staff'){
                var reply = prompt('please enter your reply: ','')
                if (reply !=null && reply !=''){
                    console.log('start send reply')
                    $.post('/sendreply', {
                        'review_id': review_id,
                        'text': reply
                    }).done(function (state){
                        console.log(state['state']);
                        if(state['state']=='fail'){
                            alert('Can only reply once!')
                        }else{
                            location.reload()
                        }
                    });
                }
            }else{
                alert('Only staff can reply!')
            }
        })
    });
})