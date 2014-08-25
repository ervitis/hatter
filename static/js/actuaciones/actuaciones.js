$(function(){
    $('#tabContent a').click(function(event) {
        var $this = $(this);

        $this.tab('show');
        e.preventDefault();
    });
});
