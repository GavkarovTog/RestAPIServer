let create_buttons = document.querySelectorAll(".create_button");
let forms = document.querySelectorAll(".form");
let read_button = document.getElementById("read_button");
let tbody_data_city = document.getElementById("tbody_data_city");
let tbody_data_firm = document.getElementById("tbody_data_firm");
let tbody_data_human = document.getElementById("tbody_data_human");
let tbody_data_religion = document.getElementById("tbody_data_religion");
let tables = document.getElementsByTagName("tbody");
let cancel_buttons = document.querySelectorAll(".cancel_button");
let update_buttons = document.querySelectorAll(".update_button");
let formsUpdate = document.querySelectorAll(".block_table_update_data");
const sound = new Audio('/static/1.m4a');


for(let i = 0; i < cancel_buttons.length; i++){
    cancel_buttons[i].addEventListener("click", function(){
        this.parentNode.style.opacity = 0;
        formsUpdate[i].style.visibility = "hidden";
    });
}

read_button.addEventListener("click", () => {
    $.ajax({
        url: "readAll", 
        type: "GET", 
        success: function(response) {
            deleting_tr_in_table();
            filling_block_city(response.city);
            filling_block_firm(response.firm);
            filling_block_human(response.human);
            filling_block_religion(response.religion);
        },
        error: function(response) {
            console.log(response);
        }
    });
})

for (let i = 0; i < forms.length; i++) {
    create_buttons[i].addEventListener("click", () => {
        let formData = new FormData(forms[i]);
        let JSONData = {}
        for(const pair of formData.entries()) {
            JSONData[pair[0]] = pair[1]; 
        }
        JSONData = JSON.stringify(JSONData);
        forms[i].reset();
        creation_function(JSONData, forms[i].getAttribute("FormURL"));
        read_button.click();
    });
}

for (let i = 0; i < formsUpdate.length; i++) {
    update_buttons[i].addEventListener("click", () => {
        let formData = new FormData(formsUpdate[i]);
        let JSONData = {}
        for(const pair of formData.entries()) {
            JSONData[pair[0]] = pair[1];
        }
        JSONData["id"] = Number(formsUpdate[i].getAttribute("id_attribute"));
        JSONData = JSON.stringify(JSONData);
        forms[i].reset();
        formsUpdate[i].style.opacity = 0;
        formsUpdate[i].style.visibility = "hidden";
        update_function(JSONData, formsUpdate[i].getAttribute("FormURL"));
        read_button.click();
    });
}


function creation_function(formData, FormURL) {
    $.ajax({
        url: FormURL, 
        type: 'POST', 
        data: formData,
        success: function(response) {
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        }
    });
}

function update_function(formData, FormURL) {
    $.ajax({
        url: FormURL, 
        type: "PUT", 
        data: formData,
        success: function(response) {
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        }
    });
}

function filling_block_city(data){
    for(let i = 0; i < data.length; i++) {
        let tr = document.createElement("tr");
        let textContentForm = [];
        for(let key in data[i]){
            let td = document.createElement("td");
            td.textContent = data[i][key];
            textContentForm.push(data[i][key]);
            tr.appendChild(td);
        }
        tr.appendChild(update_delete_button("deleteCity", "updateCity", data[i].id, textContentForm));
        tbody_data_city.appendChild(tr);
    }
}

function filling_block_religion(data){
    for(let i = 0; i < data.length; i++) {
        let tr = document.createElement("tr");
        let textContentForm = [];
        for(let key in data[i]){
            let td = document.createElement("td");
            td.textContent = data[i][key]; 
            textContentForm.push(data[i][key]);
            tr.appendChild(td);
        }
        tr.appendChild(update_delete_button("deleteReligion", "updateReligion", data[i].id, textContentForm));
        tbody_data_religion.appendChild(tr);
    }
}

function filling_block_human(data){
    for(let i = 0; i < data.length; i++) {
        let tr = document.createElement("tr");
        let textContentForm = [];
        for(let key in data[i]){
            let td = document.createElement("td");
            td.textContent = data[i][key];
            textContentForm.push(data[i][key]);
            tr.appendChild(td);
        }
        tr.appendChild(update_delete_button("deleteHuman", "updateHuman", data[i].id, textContentForm));
        tbody_data_human.appendChild(tr);
    }
}

function filling_block_firm(data){
    for(let i = 0; i < data.length; i++) {
        let tr = document.createElement("tr");
        let textContentForm = [];
        for(let key in data[i]){
            let td = document.createElement("td");
            td.textContent = data[i][key]; 
            textContentForm.push(data[i][key]);
            tr.appendChild(td);
        }
        tr.appendChild(update_delete_button("deleteFirm", "updateFirm", data[i].id, textContentForm));
        tbody_data_firm.appendChild(tr);
    }
}

function deleting_tr_in_table(){
    for(let i = 0; i < tables.length; i++){
        let rows = tables[i].getElementsByTagName("tr");
        let rows_length = rows.length;
        for(let j = 0; j < rows_length; j++){
            tables[i].removeChild(rows[rows_length - j - 1]);
        }
    }
}

function update_delete_button(delete_attribute, update_attribute, id_attribute, textContentForm){
    let td = document.createElement("td");
    let button_update = document.createElement("button");
    let button_delete = document.createElement("button");

    button_delete.classList.add("button_delete");

    button_delete.setAttribute("delete_attribute", delete_attribute);
    button_delete.setAttribute("id_attribute", id_attribute);

    button_delete.addEventListener("click", function(){
        sound.play();
        $.ajax({
            url: delete_attribute, 
            type: "DELETE",
            data: JSON.stringify({"id": id_attribute}),
            success: function(response) {
                console.log(response);
                read_button.click();
            },
            error: function(response) {
                console.log(response);
            }
        });
    });

    button_update.classList.add("button_update");
    button_update.addEventListener("click", function(){
        for(let i = 0; i < formsUpdate.length; i++){
            if(formsUpdate[i].getAttribute("formURL") === update_attribute){
                let inputs = formsUpdate[i].getElementsByTagName("input");
                for(let i = 0, counter = 1; i < inputs.length; i++, counter++){
                    inputs[i].value = textContentForm[counter];
                }
                formsUpdate[i].style.opacity = 1;
                formsUpdate[i].style.visibility = "visible";

                formsUpdate[i].setAttribute("id_attribute", id_attribute)
            }
        }
    });

    button_update.setAttribute("update_attribute", update_attribute);
    button_update.setAttribute("id_attribute", id_attribute);

    button_delete.textContent = "Удалить";
    button_update.textContent = "Изменить";
    td.appendChild(button_update);
    td.appendChild(button_delete);
    return td;
}