let burger = document.getElementById("burger");
let name = document.getElementById("name");
let phone = document.getElementById("phone");
document.getElementById("order-action").onclick = function () {
    let hasError = false;

    [burger, name, phone].forEach(item => {
       if (!item.value) {
           item.parentElement.style.background = "red";
           hasError = true
       } else {
           item.parentElement.style.background = "";
       }
    });

    if (!hasError) {
        alert(name.value + ", ваш заказ (" + burger.value + ") принят!");
        [burger, name, phone].forEach(item => {
            item.value = "";
        });
    }
}