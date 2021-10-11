function myFunction() {
  let temp = document.getElementsByClassName('sidebar');
  console.log(temp);
  temp[0].classList.toggle("sidebar__display");
}