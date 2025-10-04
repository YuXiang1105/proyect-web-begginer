const menu = document.getElementById("menu_container");
const sidebar = document.getElementById("sidebar");

menu.addEventListener('click', () => {
    sidebar.classList.toggle("sidebar--visible");
});
