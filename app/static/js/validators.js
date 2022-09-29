function validatepass(pass) {
    // var pass=document.getElementById('Password');
    if (pass.value.length < 8) {
        pass.classList.add("is-invalid")
        pass.classList.remove("is-valid")
        return false
    }
    else {
        pass.classList.remove("is-invalid")
        pass.classList.add("is-valid")
        return true
    }
}
function validatephone(phone) {
    const rePhone = /^(0?9)\d{9}$/g;
    // var phone=document.getElementById('phone');

    if (!rePhone.test(phone.value)) {
        phone.classList.add("is-invalid")
        return false
    }
    else {
        phone.classList.remove("is-invalid")
        return true
    }
}

function confirmpass() {
    var pass = document.getElementById('Password');
    var cpass = document.getElementById('ConfirmPassword');
    var valid = pass.classList.contains("is-valid")
    if (cpass.value != pass.value || !valid) {
        cpass.classList.add("is-invalid")
        cpass.classList.remove("is-valid")
        return false
    }
    else {
        cpass.classList.remove("is-invalid")
        cpass.classList.add("is-valid")
        return true
    }
}