
window.onload = getFocus();

function myFunction() {
    let temp = document.getElementsByClassName('sidebar');
    console.log(temp);
    temp[0].classList.toggle("sidebar__display");
}

function handleSelect(elm) {
    window.location = elm.value + ".php";
}

function getFocus() {
    alert(1)
    document.getElementById("default").focus();
}
