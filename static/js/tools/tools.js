$(function(){
    $('#toolTabs a').click(function(event) {
        event.preventDefault();

        $(this).tab('show');
    });
});
