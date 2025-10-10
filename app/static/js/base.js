const menu = document.getElementById("menu_container");
const sidebar = document.getElementById("sidebar");

menu.addEventListener('click', () => {
    sidebar.classList.toggle("sidebar--visible");
});


const get_top = document.getElementById("go_top")

get_top.addEventListener('click', () => {
    window.scrollTo({top: 0, behavior : "smooth"
    })


})