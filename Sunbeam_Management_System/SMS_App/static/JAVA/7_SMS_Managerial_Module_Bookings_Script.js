function update_customer(element){
    var current_row = element.parentNode.parentNode.rowIndex;
    var form = document.getElementById('customer_num');
    var cell = document.getElementById('booked_table').rows[parseInt(current_row)].cells[0].innerHTML;
    form.value = cell
    document.form.submit()    
}