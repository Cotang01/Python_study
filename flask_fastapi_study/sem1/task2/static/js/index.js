

const hello = document.querySelector(".hello")

function changeColor() {
    var letters = '0123456789ABCDEF';
    var new_color = '#';
    for (var i = 0; i < 6; i++) {
        new_color += letters[Math.floor(Math.random() * 16)];
    }
    hello.style.color = new_color;
}
