

const hello = document.querySelector(".hello")

function changeColor() {
    var letters = '0123456789ABCDEF';
    var new_color = '#';
    for (var i = 0; i < 6; i++) {
        new_color += letters[Math.floor(Math.random() * 16)];
    }
    hello.style.color = new_color;
}


function calculate() {
    const n1 = parseFloat(document.getElementById('number1').value);
    const n2 = parseFloat(document.getElementById('number2').value);
    const operation = document.getElementById('operation').value;
    document.getElementById('calc_result').value = n1 + n2;
}