const button = document.getElementById("navigation")
const navbar = document.getElementById("navbar")
let current_index = 0

button.onclick = function() {
    
    // console.log(navbar.getElementsByTagName('a'))

    let current_item = navbar.getElementsByTagName('a')[current_index];

    if (current_index == 4) {
        current_index = 0 
    }

    else {
        current_index += 1
    }
    // console.log(navbar.getElementsByTagName('a')[0])

    console.log(current_index)

    let next_item = navbar.getElementsByTagName('a')[current_index];

    console.log(current_item);
    console.log(next_item);

    current_item.style.display = "none";
    next_item.style.display = "initial";
}
