function change_table(){
    table_obj = document.getElementById('table_id');
    
    if (table_obj.style.backgroundColor == "red"){
        table_obj.style.backgroundColor = "";
    } else {
        table_obj.style.backgroundColor = "red";
    }
}
function colorSelect(){
    table_color = document.getElementById("colorSelecter");
    table_obj = document.getElementById('table_id');

    selectedItem = table_color.value
    table_obj.style.backgroundColor = selectedItem;
}