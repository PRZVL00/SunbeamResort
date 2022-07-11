function update_item(){
    var quantity = document.getElementById('Item_Quantity');

    if (quantity.value == 0){
        alert('Quantity must be atleast 1.')
    } else if (quantity.value > 99){
        alert('Maximum quantity is 99.')
    } else{
        document.form.submit()
    }
}