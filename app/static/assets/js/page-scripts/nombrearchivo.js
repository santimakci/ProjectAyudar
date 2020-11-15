
function nombrearchivo(file) {
    var fileName = file.files[0].name
    $("#nombrearchivo").css("visibility", "").text(fileName)
}
