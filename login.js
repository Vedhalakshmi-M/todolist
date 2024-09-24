var form=document.querySelector('#form')
var username=document.querySelector('#username')
var email=document.querySelector('#email')
var password=document.querySelector('#password')
var cpassword=document.querySelector('#cpassword')

form.addEventListener('submit',(e)=>{
    if(!validateInputs()){
        e.preventDefault();
    }
})
function validateInputs(){
    var usernameVal=username.value.trim();
    var emailVal=email.value.trim();
    var passwordVal=password.value.trim();
    var cpasswordVal=cpassword.value.trim();
    let success=true

    if(usernameVal===''){
        success=false;
        setError(username,'Username is required')
    }
    else{
        setSuccess(username)
    }
    if(emailVal===''){
        success=false;
        setError(email,'Email is required')

    }
    else if(!validateEmail(emailVal)){
        success=false;
        setError(email,'Please enter valid email')
    }
    else{
        setSuccess(email)
    }
    if(passwordVal===''){
        success=false;
        setError(password,'Password is required')
    }
    else if(passwordVal.length<8){
        setError(password,'Password must be atleast 8 characters')

    }
    else{
        setSuccess(password)
    }
    if(cpasswordVal===''){
        setError(cpassword,'Confirm password is required')

    }
    else if(cpasswordVal!==passwordVal){
        success=false;
        setError(cpassword,'Password does not match')
    }
    else{
        setSuccess(cpassword)
    }
    return success
}
function setError(element,message){
    var inputGroup=element.parentElement;
    var errorElement=inputGroup.querySelector('.error')
    errorElement.innerText=message;
    inputGroup.classList.add('error')
    inputGroup.classList.remove('success')
}
function setSuccess(element){
    var inputGroup=element.parentElement;
    var errorElement=inputGroup.querySelector('.error')
    errorElement.innerText='';
    inputGroup.classList.add('success')
    inputGroup.classList.remove('error')
}
function generatePassword() {
    var randomChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*";
    var passwordLength = 12; // You can adjust the length
    var password = "";

    for (var i = 0; i < passwordLength; i++) {
        var randomIndex = Math.floor(Math.random() * randomChars.length);
        password += randomChars[randomIndex];
    }

    return password;
}

document.querySelector('.random a').addEventListener('click', function(e) {
    e.preventDefault();
    var newPassword = generatePassword();
    alert("Generated Password: " + newPassword);
    document.querySelector('#password').value = newPassword;
    document.querySelector('#cpassword').value = newPassword;
});

    

    
