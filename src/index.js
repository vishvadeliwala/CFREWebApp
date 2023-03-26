console.clear();

const loginBtn = document.getElementsByClassName('log-in');
const signupBtn = document.getElementById('signup');
const eyeBtn = document.getElementById('eye');

loginBtn.addEventListener("click", login);
signupBtn.addEventListener("click", signup);
eyeBtn.addEventListener("click",showpass);

function login() {
  loginBtn.innerHTML = "Login!!"
  };

function signup() {
    signupBtn.innerHTML = "Sign up"
    };
  
function showpass() {
        showpass.innerHTML = eyeBtn.value;
        };