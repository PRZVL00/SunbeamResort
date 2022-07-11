function submitFeedback() {
    if (document.getElementById('comment').value == "") {
        alert('Please provide your feedback');
    }
    else if (document.getElementById('comment').value.length < 20) {
        alert('Feedback is too short! Please type more htan 20 characters.');
    }
    else {
        alert(document.getElementById('comment').value)
        document.forms.submit()
    }
}
