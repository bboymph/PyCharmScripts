(function() {
  var app = angular.module('myapp2', []);
 app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{');
    $interpolateProvider.endSymbol('}');
});

  app.controller('StoreController', function($scope, $http){
    $scope.users = [];
    $scope.hide = false;
    $scope.isShow = false;
      $scope.id = "";
      $scope.nome = "";
      $scope.email = "";
    $http.get('rest/rest/get_all_users').
        success(function(result){
            $scope.users = result;
        });

    $scope.func = function(){
        $scope.hide = !$scope.hide;
    }

    $scope.remover = function(user, index){
        $scope.users.splice(index, 1);
        $http.post('rest/rest/remove_user', {'nome':user.nome});
    };

   $scope.atualizar = function(usuario){
       usuario.isShow = false;
       $http.post('rest/rest/edit_user', {
         'id': usuario.id,
         'nome': usuario.nome,
         'email': usuario.email

       });
   }

  });

})();