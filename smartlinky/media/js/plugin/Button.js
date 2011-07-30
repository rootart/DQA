

var Button = function(section_id, count) {
    this.$section = $('#' + section_id);
    this.count = count ? count : null;
    this.render(); 
};

Button.prototype.render = function() {
    var $wrapper = $('<div>').css({
        position: 'relative',
        height: '0px'
    });
    var $button = $('<div>').css({
        position: 'absolute',
        background: '#000',
        color: '#fff',
        padding: '8px',

    });
    if (this.count) {
        $button.text(this.count);
    } else {
        $button.text(0);
    }
    $wrapper.append($button);
    $wrapper.prependTo(this.$section);
};
