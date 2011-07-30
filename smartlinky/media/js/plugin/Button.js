

var Button = function(section_id, count) {
    this.$section = $('#' + section_id);
    this.count = count ? count : null;
    this.widget = null;
    this.$button = null;
    this.render(); 
};

Button.prototype.render = function() {
    var $wrapper = $('<div>').css({
        position: 'relative',
        height: '0px'
    });
    this.$button = $('<div>').css({
        position: 'absolute',
        background: '#000',
        color: '#fff',
        padding: '8px',

    });
    if (this.count) {
        this.$button.text(this.count);
    } else {
        this.$button.text(0);
    }
    $wrapper.append(this.$button);
    $wrapper.prependTo(this.$section);

    this.$button.click($.proxy(this, 'clickHandler'));
};

Button.prototype.clickHandler = function(e) {
    e.preventDefault();
    if (!this.widget) {
        this.widget = new Widget(this.$button, this.$section);
    }

    this.widget.open();
};
