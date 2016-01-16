app.service("connectionService", ['$q', '$rootScope', function($q, $rootScope) {

	var connectionService = {},
		//host = "localhost",
		host = "192.168.72.130",
		port = "9002";
	

	// socket server
	var ws = new WebSocket("ws://"+host+":"+port);

	ws.onopen = function(){
		console.log("Server connected");
		connectionService["isConnected"] = true;
	};

	ws.onmessage = function(event){
		connectionService.response(event.data);
	};

	// main functions
	connectionService.sendCommand = function(command, args){
		if (connectionService.isConnected == true){
		
			if (command){
				ws.send(command + get_args(args));
				console.log("Command >>> " + (command||"NO COMMAND") + " " + (args||"NO ARGUMENT"));
			} else {
				console.log("No command given");
			}
		}
	}

	connectionService.response = function(data){
		data = data.replace(/[\(\)']/g, "")
		console.log("Response >>> " + data);
		connectionService["response_data"] = data
	};

	// utility functions
	function get_args(args) {
		var res = "";
		if (args) {
			if (args.length >= 1)
				res += ",";
			res += args.join(",");
		}
		return res;
	}

	return connectionService;
}]);
