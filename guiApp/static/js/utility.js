// credits: sigurd
// http://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }


 function doAjax(callback, command, arguments_){
    $.ajax({
        type: "POST",
        url: '/' + command,
        error: function (request, error) {
            console.log("AJAX ERROR:error");
            console.log(request);
        },
        data: {"args[]":arguments_},
        dataType: 'text json',
        success: callback,
        failure: failureFunc,
        timeout: 3000,
        async: false
    });

    // Use this function to do stuff if not successful. For example show validation messages?
    function failureFunc(data, textStatus, jqXHR) {
        console.log("AJAX FAILURE")
        console.log(data)
    }

 }