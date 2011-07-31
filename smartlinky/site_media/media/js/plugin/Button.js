

var Button = function(section, section_id, count) {
    this.section = section;
    this.$section = $('#' + section_id);
    this.count = count ? count : null;
    this.widget = null;
    this.$button = null;
    this.render(); 
};

Button.prototype.render = function() {
    var $wrapper = $('<div>').css(style.wrapper).prependTo(this.$section);
    var $container = $('<div>').css(style.container).appendTo($wrapper);
    this.$button = $('<div>').css(style.button).appendTo($container);
    if (this.count) {
        this.$button.text(this.count);
    } else {
        this.$button.text(0);
    }

    this.$button.click($.proxy(this, 'handleClick'));
};

Button.prototype.handleClick = function(e) {
    e.preventDefault();
    if (!this.widget) {
        this.widget = new Widget(this.section, this.$button, this.$section);
    }
    
    this.widget.toggle();
};
