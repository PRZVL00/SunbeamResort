// confirm button function
function check_input() {
    //     var fname = document.getElementById('fname').value;
    //     var lname = document.getElementById('lname').value;
    //     var cellnum = document.getElementById('cellnum').value;
    //     var email = document.getElementById('email').value;
    //     var numguest = document.getElementById('numguest').value;
    //     var cidate = document.getElementById('cidate').value;
    //     var codate = document.getElementById('codate').value;
    
    //     var confirmationofemail = email.length - 10
    //     var endofemail = email.length + 1
    
    //     var today = new Date();
    //     var dd = String(today.getDate()).padStart(2, '0');
    //     var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    //     var yyyy = today.getFullYear();
    
    //     var today = mm + '/' + dd + '/' + yyyy;
    
    
    //     var date1 = new Date(cidate);
    //     var date2 = new Date(codate);
    //     var date_today = new Date(today);
    //     var Difference_In_Time_Today = date1.getTime() - date_today.getTime();
    //     var Difference_In_Days_Today = Difference_In_Time_Today / (1000 * 3600 * 24);
    //     var Difference_In_Time = date2.getTime() - date1.getTime();
    //     var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);
    
    //     if (fname.length == 0 || lname.length == 0 || cellnum.length == 0 || email.length == 0 ||
    //         numguest == 0 || numguest > 5) {
    //         alert('Incomplete/Invalid Form. Please Fill Up the Form');
    //     } else if (cellnum.length < 11) {
    //         alert('Invalid Phone Number');
    //     } else if (cellnum.charAt(0) != 0 || cellnum.charAt(1) != 9) {
    //         alert('Invalid Phone Number')
    //     } else if (email.substring(confirmationofemail, endofemail) != '@gmail.com') {
    //         alert('Invalid Email Format')
    //     } else if (Difference_In_Days_Today < 0) {
    //         alert('Invalid Check In Date')
    //     } else if (Difference_In_Days < 1) {
    //         alert('Invalid Check Out Date')
    //     } else {
    //         if (confirm("Are you sure you want to proceed?") == true) {
    //             document.getElementById('fname').value = '';
    //             document.getElementById('lname').value = '';
    //             document.getElementById('cellnum').value = '';
    //             document.getElementById('email').value = '';
    //             document.getElementById('numguest').value = '';
    //             document.getElementById('cidate').value = '';
    //             document.getElementById('codate').value = '';
    //             document.getElementById('rooms').value = '';
    //             document.getElementById("act1").checked = false;
    //             document.getElementById("act2").checked = false;
    //             document.getElementById("act3").checked = false;
    //             document.getElementById("act4").checked = false;
    //             document.getElementById("act5").checked = false;
    //             window.open("Billing module.html");
    //         } else {
    //             pass;
    //         }
    //     }
        window.location.assign('billing')}
    
    // Cancel button Fucntion
    function cancel_input() {
        if (confirm("Are you sure you want to Cancel?") == true) {
            document.getElementById('fname').value = '';
            document.getElementById('lname').value = '';
            document.getElementById('cellnum').value = '';
            document.getElementById('email').value = '';
            document.getElementById('numguest').value = '';
            document.getElementById('cidate').value = '';
            document.getElementById('codate').value = '';
            document.getElementById('rooms').value = '';
            document.getElementById("act1").checked = false;
            document.getElementById("act2").checked = false;
            document.getElementById("act3").checked = false;
            document.getElementById("act4").checked = false;
            document.getElementById("act5").checked = false;
            window.locate='home.html'
        }
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