(function(){
var app = angular.module('Questions', ['ionic'])
var questions = [];

app.config(function($stateProvider, $urlRouterProvider ){
	
	$stateProvider.state('questionsList' , {
		url:'/list',
		templateUrl:'templates/list.html'
	});
	
	$stateProvider.state('sigleQuestions' , {
		url:'/question/:questionId',
		templateUrl:'templates/question.html'
	});
	
	$urlRouterProvider.otherwise('/list');
});

var questionsMap = {};

function getQuestionList($http){
	
	$http.get('http://df6b5946.ngrok.io/rest_api/read').success(function(response){
		angular.forEach(response.questions, function(question){
		questionsMap[question.question_id] = question;
		console.log(questionsMap);
		});
	});
	console.log("Qm"+questionsMap);
	return questionsMap;

}

function getQuestion(questionId){

	return questionsMap[questionId];
}
 
app.controller('questionsListCtrl',function($http, $scope){
			
	$scope.questions = getQuestionList($http);
	
});
 
app.controller('questionCtrl',function($scope , $state){
	
	$scope.question=getQuestion($state.params.questionId);
	
});
 


app.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if(window.cordova && window.cordova.plugins.Keyboard) {       
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);
     }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
});
}());