let button = document.getElementById("settings-button")
let div = document.getElementById("settings-button-content")

button.onclick = function() {

    if (div.className == "settings-button-closed") {
        div.className = "settings-button-open";
    }

    else {
        div.className = "settings-button-closed";
    }
}