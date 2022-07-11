function update_room(){
    var price = document.getElementById('Room_Price');

    if (price.value < 2000){
        alert('Price must be atleast 2000.')
    } else if (price.value > 10000){
        price('Price max is 10000.')
    } else{
        document.form.submit()
    }
}