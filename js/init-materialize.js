document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems);
});


document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
});


document.querySelectorAll('.collapsible-header').forEach(item => {
    item.addEventListener('click', event => {
        let arrow = item.getElementsByTagName("i")

        if (arrow[0].innerText == "keyboard_arrow_down") {
            return arrow[0].innerText = "keyboard_arrow_up"
        } else if (arrow[0].innerText == "keyboard_arrow_up") {
            return arrow[0].innerText = "keyboard_arrow_down"
        }
    })
})