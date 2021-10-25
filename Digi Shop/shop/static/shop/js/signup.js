var token=null
var loading=null

window.onload=function(){
    loading=document.getElementById('loading')
}

function validate(event) {
    var error = document.getElementById('message')
    error.hidden = false
    var message = null
    var form=event.target
    var values=form.elements
    token=values.csrfmiddlewaretoken.value;
    
    var email = values.email.value;
    var name = values.name.value;    

    message= validateform(form)
    
    if (message) {
        error.innerHTML = message
        error.hidden = false
    }
    else {
        error.innerHTML = ""
        error.hidden = true

        //email...
        sendemail(email, name, token)
    }

    event.stopPropagation();
    return false
}

function validateform(form){
    var values = form.elements;
    var name = values.name.value;
    token=values.csrfmiddlewaretoken.value;
    var message=null
    var email = values.email.value;
    var phone = values.phone.value;
    var password = values.password.value;
    var repassword = values.repassword.value;

    if (!name.trim()) {
        message = "Name is required"
    } else if (!email.trim()) {
        message = "Email is required"
    } else if (!password.trim()) {
        message = "Password is required"
    } else if (!repassword.trim()) {
        message = "Please, Enter Password again!!!"
    } else if (password.trim() != repassword.trim()) {
        message = "Password must be same!!!"
    }else if (password.length < 6 || repassword.length < 6) {
        message = "Password must be more than 6 chars!!!"
    }
    return message
}

function sendemail(email, name, token) {   
    loading.hidden=false
    $.ajax({
        method: "POST", 
        url: "/send-otp",
        data: { name: name, email: email, 'csrfmiddlewaretoken':token}
      })
        .done(function( msg ) {
          //alert( "Data Saved: " + msg );
          loading.hidden=true
          showotpinput()
        }).fail(function(err){
            loading.hidden=true
            showotpinput()
            //alert("Email Can't send")
        })    
}

function showotpinput(){
    var otpinput=document.getElementById('vcodeinput')
    var subbutton=document.getElementById('sbutton')
    var verbutton=document.getElementById('vbutton')

    otpinput.hidden=false
    subbutton.hidden=true
    subbutton.disabled=true
    verbutton.hidden=false
}

function verifyotp(){
    var codeinput=document.getElementById('code')
    var code=codeinput.value

    loading.hidden=false

    $.ajax({
        method: "POST", 
        url: "/verify",
        data: { 'code':code, 'csrfmiddlewaretoken':token}
      })
        .done(function( msg ) {
            loading.hidden=true
          submitform()          
        }).fail(function(err){
            loading.hidden=true
            alert("Code is Invalid!!!")
        })
}


function submitform(){
    try{
        var form=document.getElementById('signupform')
    var message=validateform(form)
    if(message){

    }else{
    form.submit()
    }
    }catch(err){
        console.log(err)
    }
}