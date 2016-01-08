// define the screen and the outputs that need to be updated
// the first part of the object is the unique css class of the output. 

var ScreenManager = $(function () {
    // separate outputs by screens/pages
    var _outputs =  { 
                        'dashboard':[
                        'output_tube_pressure',
                        'output_pod_temperature',
                        'output_pod_pressure',
                        'output_speed',
                        'output_position',
                        'output_distance'
                        ]
                    };

    self.screens = (function () {
        sOutputs = {};
        Object.keys(_outputs).forEach(function(key,index) {
            // key: the name of the object key
            // index: the ordinal position of the key within the object 
            
            var cScreen = _outputs[key],
                totOutputs = cScreen.length;
            
            sOutputs[key] = [];
            
            for (var i = 0; i < totOutputs; i++) {
                $output = $("."+cScreen[i]).first();
                sOutputs[key].push($output);
            }
        });
        return sOutputs
    })()
    return {'screens':self.screens}
});

/*
stop
start
move
get_status
get_position
get_speed*/