function RemoveBasketlike(id){
$.post('/RemoveBasketlike',
        {id:id}).done(function (response){
            var message = response['message']
            $("#fuck1"+response['id']).remove()
            $("#length1").text(response['length'])

    }).fail(function (){
        alert('Wrong!!!')
    })
}