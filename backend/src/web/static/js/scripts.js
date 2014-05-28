var setActive = function() {
    url= window.location.href.split('/');
    if (url[3] === "cadastro"){
        var el = document.getElementById("cadastrar");
    }else{
        var el = document.getElementById(url[3]);
    }
    el.className = el.className + "active";
};


window.onload = function(){
    setActive();
};

function logar() {
    var msg;
    $('.required').each(function() {
       if ($(this).val() == '') {
           msg = msg + $(this).prev().text() + '\n';
       }
    });
    if (msg != undefined) {

    }
}

myapp= angular.module("myapp",[]);
myapp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{');
    $interpolateProvider.endSymbol('}');
});
myapp.controller("mainController", function($scope, $http, $timeout){

});