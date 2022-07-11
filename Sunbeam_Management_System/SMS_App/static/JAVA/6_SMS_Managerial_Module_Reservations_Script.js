function delete_customer(element){
    var current_row = element.parentNode.parentNode.rowIndex;
    var form = document.getElementById('customer_num');
    var form2 = document.getElementById('type');
    var cell = document.getElementById('reserved_table').rows[parseInt(current_row)].cells[0].innerHTML;
    
    form2.value = 'DELETE'
    form.value = cell
    document.form.submit()    
}

function update_customer(element){
    var current_row = element.parentNode.parentNode.rowIndex;
    var form = document.getElementById('customer_num');
    var form2 = document.getElementById('type');
    var cell = document.getElementById('reserved_table').rows[parseInt(current_row)].cells[0].innerHTML;
    
    form2.value = 'UPDATE'
    form.value = cell
    document.form.submit()    
}