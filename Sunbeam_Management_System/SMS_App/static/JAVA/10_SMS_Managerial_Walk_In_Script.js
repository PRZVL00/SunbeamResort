function reg_walkin(){
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;

    var room = document.getElementById('rooms').value;
    var cellnum = document.getElementById('cellnum').value;
    var cidate = document.getElementById('cidate').value;
    var codate = document.getElementById('codate').value;
    var act1 = document.getElementById('act1');
    var act2 = document.getElementById('act2x');
    var act3 = document.getElementById('act3');
    var act4 = document.getElementById('act4');
    var guest =  document.getElementById('numguest').value;
    let act_price = 0;
    const misc_fee = 1000;
    let total_price = 0;

    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    var check_today = yyyy + '-' + mm + '-' + dd;
 

    var today = mm + '/' + dd + '/' + yyyy;

    var date1 = new Date(cidate);
    var date2 = new Date(codate);
    var date_today = new Date(today);
    var Difference_In_Time_Today = date1.getTime() - date_today.getTime();
    var Difference_In_Days_Today = Difference_In_Time_Today / (1000 * 3600 * 24);
    var Difference_In_Time = date2.getTime() - date1.getTime();
    var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);

    //--------------------------------------------------------------------------------------------------------------------------------------//  
    // Set 15
    if (act1.checked && act2.checked && act3.checked && act4.checked){
        document.getElementById('activity').value = 'Activity Set 15';
        act_price = 2000 * guest

    // Set 7
    } else if (act2.checked && act3.checked && act4.checked){
        document.getElementById('activity').value = 'Activity Set 7';
        act_price = 1500 * guest

     // Set 11
    } else if (act1.checked && act3.checked && act4.checked){
        document.getElementById('activity').value = 'Activity Set 11';
        act_price = 1500 * guest

    // Set 13
    } else if (act1.checked && act2.checked && act4.checked){
        document.getElementById('activity').value = 'Activity Set 13';
        act_price = 1500 * guest
    
    // Set 14
    } else if (act1.checked && act2.checked && act3.checked){
        document.getElementById('activity').value = 'Activity Set 14';
        act_price = 1500 * guest
    
    // Set 9
    } else if (act1.checked && act4.checked){
        document.getElementById('activity').value = 'Activity Set 9';
        act_price = 1000 * guest
    
    // Set 10
    } else if (act1.checked && act3.checked){
        document.getElementById('activity').value = 'Activity Set 10';
        act_price = 1000 * guest

    // Set 12
    } else if (act1.checked && act2.checked){
        document.getElementById('activity').value = 'Activity Set 12';
        act_price = 1000 * guest
    
     // Set 3
    } else if (act3.checked && act4.checked){
        document.getElementById('activity').value = 'Activity Set 3';
        act_price = 1000 * guest

    // Set 5
    } else if (act2.checked && act4.checked){
        document.getElementById('activity').value = 'Activity Set 5';
        act_price = 1000 * guest
    
    // Set 6
    } else if (act2.checked && act3.checked){
        document.getElementById('activity').value = 'Activity Set 6';
        act_price = 1000 * guest

    // Set 1
    }else if (act4.checked){
        document.getElementById('activity').value = 'Activity Set 1';
        act_price = 500 * guest
    
    // Set 2
    } else if (act3.checked){
        document.getElementById('activity').value = 'Activity Set 2';
        act_price = 500 * guest
    
    // Set 4
    } else if (act2.checked){
        document.getElementById('activity').value = 'Activity Set 4';
        act_price = 500 * guest
        
    // Set 8
    } else if (act1.checked){
        document.getElementById('activity').value = 'Activity Set 8';
        act_price = 500 * guest
    // Set 15
    } else{
        act_price = 0
    }
    //--------------------------------------------------------------------------------------------------------------------------------------//

    //--------------------------------------------------------------------------------------------------------------------------------------//
    if (room == 'AMETHYST'){
        org_price = 2000
        total_price = (2000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'SAPPHIRE'){
        org_price = 2500
        total_price = (2500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'MONTANA'){
        org_price = 3000
        total_price = (3000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'AQUAMARINE'){
        org_price = 3500
        total_price = (3500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'TURQUIOSE'){
        org_price = 4000
        total_price = (4000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'PACIFIC'){
        org_price = 4500
        total_price = (4500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'TROPICAL'){
        org_price = 5000
        total_price = (5000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'HARBOR'){
        org_price = 5500
        total_price = (5500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'SAILOR'){
        org_price = 6000
        total_price = (6000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'ATLANTIS'){
        org_price = 10000
        total_price = (10000 * Difference_In_Days) + act_price + misc_fee}

    //--------------------------------------------------------------------------------------------------------------------------------------//


    if (fname == '' || lname == '' || cidate == '' || codate == '' || cellnum == '' || email == '') {
        alert('Fill Up the Form')
    } else if (cellnum.charAt(0) != 0 || cellnum.charAt(1) != 9) {
        alert('Invalid Phone Number');
    } else if (cidate != check_today) {
        alert('Invalid Check In Date');
    } else if (Difference_In_Days_Today < 0) {
        alert('Invalid Check In Date');
    } else if (Difference_In_Days < 1) {
        alert('Invalid Check Out Date');
    } else if (Difference_In_Days > 14) {
        alert('The limit for staying is 14 days.');
    } else {
        document.getElementById('total_days').value = Difference_In_Days;
        document.getElementById('price').value = total_price;
        document.getElementById('status').value = 'BOOKED';
        
        document.getElementById('stay_in_price').innerHTML =  'PHP '+ org_price + '.00 ' + ' * ' + Difference_In_Days + ' Day/s'
        document.getElementById('acti').innerHTML =  'PHP '+ act_price + '.00 ' + ' * ' + guest + ' Person/s'
        document.getElementById('ttl').innerHTML =  'PHP '+ total_price + '.00 ' 
        modal.style.display = "block";
    }
}

function cancel_bill(){
    modal.style.display = 'none';
}

function checkin_bill(){
    document.form.submit();
}

function cancel(){
    window.location.assign('walk_ins')
}