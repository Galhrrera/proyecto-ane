// // ejecutar función en el evento click
// document.getElementById("btn-open-close").addEventListener("click", open_close_menu)

// // variables
// var menu_container = document.getElementById("menu-container")
// var btn_open_close = document.getElementById("btn-open-close")
// var body = document.getElementById("my-body")

// // evento para mostrar y ocultar menu
// function open_close_menu(){
//     alert("btn")
//     body.classList.toggle("body-moved")
//     menu_container.classList.toggle("menu-container-moved")
// }
var body = document.getElementById("my-body")
var menu_container = document.getElementById("menu-container")
window.addEventListener("resize", function(){
    if (this.window.innerWidth > 760){
        body.classList.remove("body-moved")
        menu_container.classList.remove("menu-container-moved")
    }
})