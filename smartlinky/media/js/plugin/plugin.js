
(function($){$(function(){
    var parser = new Parser();
    parser.parse();
    //Initialize
    $.ajax({
        url: '{{api-url}}' + 'init',
        data: {
            url: window.location.href
        },
        dataType: 'json',
        success: function(data){
            for (var key in parser.sections) {
                if (parser.sections.hasOwnProperty(key)) {
                    if (data.sections[key]) {
                        new Button(parser.sections[key], key, data.sections[key]);
                    } else {
                        new Button(parser.sections[key], key);
                    }
                }
            }
        } 
    });
});})($);
