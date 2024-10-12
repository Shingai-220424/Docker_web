function check_input(){
    let height = document.getElementById('height_id');
    let weight = document.getElementById('weight_id');
    if (height.value == "" || weight.value == ""){
        alert('身長または体重が入力されていません');
        return false;
    }
    return true;
}
