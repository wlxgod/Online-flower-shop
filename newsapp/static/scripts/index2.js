function RemoveBasket(id){
$.post('/RemoveBasket',
        {id:id}).done(function (response){
            var message = response['message']
            $("#fuck"+response['id']).remove()
            $("#length").text(response['length'])
            $("#total").text(response['total'])

    }).fail(function (){
        alert('Wrong!!!')
    })
}