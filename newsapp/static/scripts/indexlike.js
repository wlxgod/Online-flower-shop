function addLike(id,quantity,name){
$.post('/addToLike',
        {id:id,quantity:quantity,name:name}).done(function (response){
            var message = response['message']
            $("#length1").text(response['length'])
            alert(message)

    }).fail(function (){
        alert('Wrong!!!')
    })
}