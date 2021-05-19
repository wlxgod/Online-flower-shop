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
})