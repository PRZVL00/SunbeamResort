function validateForm() {
    var fname = document.getElementById("i_fname").value;
    var lname = document.getElementById("i_lname").value;
    var cnum = document.getElementById("i_cnum").value;
    var email = document.getElementById("i_email").value;
    var pword = document.getElementById("i_pword").value;
    var pword2 = document.getElementById("i_pword2").value;
    var code = document.getElementById("i_code").value;

    var confirmationofemail = email.length - 10
    var endofemail = email.length + 1

    if(fname.length == 0 || lname.length == 0 || cnum.length == 0 || email.length == 0 ||
        pword.length == 0 || pword2.length == 0 || code.length == 0) {
        alert('Incomplete/Invalid Form. Please Fill Up the Form');
    
    }else if (email.substring(confirmationofemail, endofemail) != '@gmail.com') {
        alert('Invalid Email Format');
    
    }else if (pword.length < 8){
        alert('Invalid Pasword Format. It must contain atleast 8 characters.');
    
    }else if (pword2 != pword){
        alert('Invalid Confirm Pasword. Password and Confirm Password must be the same.');
    
    }else if (code != '0000'){
        alert('Invalid Code');
    
    }else {
        if (confirm("Are you sure you want to proceed?") == true) {
            document.getElementById('i_fname').value = '';
            document.getElementById('i_lname').value = '';
            document.getElementById('i_cnum').value = '';
            document.getElementById('i_email').value = '';
            document.getElementById('i_pword').value = '';
            document.getElementById('i_pword2').value = '';
            document.getElementById('i_code').value = '';
            window.open("home.html");
        } else {
            pass;
        }
    }
}

function number(evt)
{
    var ch = String.fromCharCode(evt.which);
    if(!(/[a-zA-Z]/.test(ch)))
    {
        evt.Default();
    }
    else
    {
        alert("Only numbers are allowed")
    }
    
    var ch = String.fromCharCode(evt.which);
    if(!(/[0-9]/.test(ch)))
    {
        evt.preventDefault();
    }    
}

function letter(evt)
{
    var ch = String.fromCharCode(evt.which);
    if(!(/[a-zA-Z]/.test(ch)))
    {
        evt.preventDefault();
    }
    var ch = String.fromCharCode(evt.which);
    if(!(/[0-9]/.test(ch)))
    {
        evt.Default();
    }    
    else
    {
        alert("Only characters are allowed")
    }
}


