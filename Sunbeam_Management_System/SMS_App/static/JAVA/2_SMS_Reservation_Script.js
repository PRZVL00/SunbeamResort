// confirm button function
function verify() {
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
   
    var random_code = Math.floor(100000 + Math.random() * 900000);
    document.getElementById("random_code").value = random_code;

    //--------------------------------------------------------------------------------------------------------------------------------------//
    if (room == 'AMETHYST'){
        total_price = (2000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'SAPPHIRE'){
        total_price = (2500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'MONTANA'){
        total_price = (3000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'AQUAMARINE'){
        total_price = (3500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'TURQUIOSE'){
        total_price = (4000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'PACIFIC'){
        total_price = (4500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'TROPICAL'){
        total_price = (5000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'HARBOR'){
        total_price = (5500 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'SAILOR'){
        total_price = (6000 * Difference_In_Days) + act_price + misc_fee
    } else if (room == 'ATLANTIS'){
        total_price = (10000 * Difference_In_Days) + act_price + misc_fee}

    //--------------------------------------------------------------------------------------------------------------------------------------//

    
    if (fname == '' || lname == '' || cidate == '' || codate == '' || cellnum == '' || email == '') {
        alert('Fill Up the Form');
    }else if (cellnum.charAt(0) != 0 || cellnum.charAt(1) != 9) {
        alert('Invalid Phone Number');
    }  else if (Difference_In_Days_Today < 0) {
        alert('Invalid Check In Date');
    } else if (Difference_In_Days < 1) {
        alert('Invalid Check Out Date');
    } else if (Difference_In_Days > 14) {
        alert('The limit for staying is 14 days.');
    } else {
        document.getElementById('total_days').value = Difference_In_Days;
        document.getElementById('price').value = total_price;
        document.getElementById('status').value = 'TENTATIVE';
        document.form.submit();
    }
}

// Cancel button Fucntion
function cancel_input() {
    window.location.assign('homepage')
}

//functions for buttons for choosing rooms
function room1() {
    document.getElementById("rooms").selectedIndex = "0"
}

function room2() {
    document.getElementById("rooms").selectedIndex = "1"
}

function room3() {
    document.getElementById("rooms").selectedIndex = "2"
}

function room4() {
    document.getElementById("rooms").selectedIndex = "3"
}

function room5() {
    document.getElementById("rooms").selectedIndex = "4"
}

function room6() {
    document.getElementById("rooms").selectedIndex = "5"
}

function room7() {
    document.getElementById("rooms").selectedIndex = "6"
}

function room8() {
    document.getElementById("rooms").selectedIndex = "7"
}

function room9() {
    document.getElementById("rooms").selectedIndex = "8"
}

function room10() {
    document.getElementById("rooms").selectedIndex = "9"
}