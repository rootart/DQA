
(function($){$(function(){
    var parser = new Parser();
    parser.parse();
    //Initialize
    $.ajax({
        url: '%%api-url%%',
        data: {
            url: window.location.href,
            sections: parser.sections
        },
        crossDomain: true,
        success: function(){
        } 
    });
});})($);
