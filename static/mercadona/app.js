let bouton = document.getElementById("bouton")
const printUser =  () => {
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value
    for (i = 0; i < listUser.length; i++){
        if(username == listUser[i].username && password == listUser[i].password){
            bouton.innerHTML = "Bienvenue " + username
            return
        }
        else{
            if(i+1 == listUser.length){
                bouton.innerHTML = "OH LE NUL"
                bouton.style.backgroundColor = "red"
            }
        }
    }
}

bouton.addEventListener("click", printUser)