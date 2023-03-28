require("./database_helper")
function Signup(){
    var name = String(document.getElementsByClassName("signup-form").getElementById("name").value);
    var email = String(document.getElementsByClassName("signup-form").getElementById("email").value);
    var pwd = String(document.getElementsByClassName("signup-form").getElementById("pwd").value);
    const db = new db_connect();
    db.connect();
    code,msg = db.signup(name,email,pwd);
    document.getElementsByClassName("signup-form").getElementById("signup_text").innerHTML = msg;
}