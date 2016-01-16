app.controller("podStatsCtrl", ["$scope", '$timeout', "connectionService", 
	function($scope, $timeout, connectionService) {
		
		$scope.value = 0;
		$scope.stats = null;

		// polling that gives us realtime data display
		var poll = function() {
			$timeout(function() {
				$scope.value++;
				get_stats();
				poll();
			}, 500);
		};     
		
		// button functions
		$scope.power_on  = function() {
	    	connectionService.sendCommand("power_on");
	    };
	    $scope.power_off  = function() {
	    	connectionService.sendCommand("power_off");
	    };
	    $scope.set_speed  = function(speed) {
	    	connectionService.sendCommand("set_speed", [speed]);
	    };
	    $scope.stop  = function() {
	    	connectionService.sendCommand("stop");
	    };

	    // helper functions
   		var get_stats = function(){
			connectionService.sendCommand("stats");
			$scope.stats = angular.fromJson(connectionService["response_data"]);
		}

	    // function calls
	    poll();
}]);