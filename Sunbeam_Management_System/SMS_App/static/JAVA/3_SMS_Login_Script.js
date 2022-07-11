function validate() {
    document.forms.submit();
    }

function cancel() {
    document.getElementById('username').value = "";
    document.getElementById('password').value = "";
    window.location.assign('home')
}