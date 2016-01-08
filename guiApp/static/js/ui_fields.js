// define the screen and the outputs that need to be updated
// the first part of the object is the unique css class of the output. 

var ScreenManager = function (_screen, data_logic) {
    if (!_screen){
        console.log("Screen not defined")
        return false;
    }

    //jquery screen objs
    var screens = {};

    //turn updating on or off 
    updating = true;

    this.get_screens_as_obj = function (_outputs) {
        sOutputs = {};
        if (_outputs) {
            Object.keys(_outputs).forEach(function(key,index) {
                // key: the name of the object key
                // index: the ordinal position of the key within the object 
                
                var cScreen = _outputs[key],
                    totOutputs = cScreen.length;
                
                sOutputs[key] = [];
                
                for (var i = 0; i < totOutputs; i++) {
                    $output = $("."+cScreen[i]);
                    sOutputs[key][cScreen[i]] = $output;
                }
            });
        }
        return sOutputs
    }

    function update(){
        (function updateloop (i) {          
            setTimeout(function () { 

                console.log("updating...")
                var data = data_logic();

                Object.keys(screens).forEach(function(key,index) {
                    var cScreen = screens[key],
                        totOutputs = cScreen.length;

                    Object.keys(cScreen).forEach(function(key2,index2) {
                        var cOutput = cScreen[key2],
                            label = null;

                        $(cOutput).each(function () {
                            var $cOutput_widget = $(this),
                                cValue = data[key][key2];

                            if( $cOutput_widget.hasClass('progress-bar') ) {
                                $cOutput_widget.width(cValue)
                            } else if ( $cOutput_widget.hasClass('label_output') ) {
                                $cOutput_widget.text(cValue)
                            } else if ( $cOutput_widget.hasClass('info_panel') ) {
                                if (cValue == true)
                                    $cOutput_widget.show()
                                else
                                    $cOutput_widget.hide()
                                //console.log("Didn't find any type css class")
                            } else {
                                console.log("Didn't find any type css class")
                                return
                            }
                            //console.log(label + data[key][key2])
                        });
                    });
                });   

                if (updating) updateloop(i);
            }, 500)
        })(updating, data_logic); 
    }

    this.initialise = function () {
        console.log("Initialise screens")
        screens = this.get_screens_as_obj(_screen);
    };
    
    this.initialise();

    return {'update':update}
};

/*
stop
start
move
get_status
get_position
get_speed*/