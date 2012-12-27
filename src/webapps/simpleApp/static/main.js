require(["jquery", "handlebars", "text!template.html"], function($, handlebars, template) {
    $.getJSON('showmetime', function(day){
        var html = handlebars.compile(template)({day:day});
        $('.main-body').html(html);
    });
});
