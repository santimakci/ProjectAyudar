var width = $(window).width();
if(width < 992){
    $('#admin').removeClass("dropdown").css("display","none");
    $('#perfil').css("display","");
    $('#logout').css("display","");
}
$(window).resize(function(){
console.log('resize called');
var width = $(window).width();
if(width < 992){
    $('#admin').removeClass("dropdown").css("display","none");
    $('#perfil').css("display","");
    $('#logout').css("display","");
}   
else{
    $('#admin').addClass("dropdown").css("display", "");
    $('#perfil').css("display","none");
    $('#logout').css("display","none");
}
})