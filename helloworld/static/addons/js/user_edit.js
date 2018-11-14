$(document).ready(function () {

});

function validateUser() {
        var name = $('#inputName').val();
        var email = $('#inputEmail').val();
        var adress = $('#inputAdress').val();
        var phone = $('#inputPhone').val();

        if(name == "" || email == "" || adress == "") {
            alert("Por favor ingresa todos los campos");
            return false;
        } else if (phone.length != 9){
            alert("Ingresa un numero de teléfono valido sin código de area")
            return false;
        } else
            return true;

        
}

function validateCard() {
    var name = $('#cardName').val();
    var number = $('#cardNumber').val();
    var password = $('#cardPass').val();
    var month = $('#cardMonth').val();
    var year = $('#cardYear').val();
    if(name == "" || number == "" || password == "" || month == "" || year == "") {
        alert("Por favor ingresa todos los campos");
        return false;
    } else if (password.length != 3){
        alert("Ingrese una clave válida");
        return false;
    } else if (number.length != 19) {
        alert("Por favor ingresa un número de tarjeta válida");
        return false;
    } else
        return true;

    
}

