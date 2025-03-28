function toggleMenu() {
  const menu = document.querySelector(".menu");
  const menu_mobile = document.querySelector(".menu-mobile");
  menu.classList.toggle("active");
  menu_mobile.classList.toggle("active");
}

function closeMenu() {
  const menu = document.querySelector(".menu");
  const menu_mobile = document.querySelector(".menu-mobile");
  menu.classList.remove("active");
  menu_mobile.classList.remove("active");
}
document.addEventListener("click", function (event) {
  const menu = document.querySelector(".menu");
  const hamburger = document.querySelector(".hamburger");

  if (!menu.contains(event.target) && !hamburger.contains(event.target)) {
    menu.classList.remove("active");
  }
});
