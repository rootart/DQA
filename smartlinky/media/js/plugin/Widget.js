

var Widget = function($button, $section) {
    this.$button = $button;
    this.$section = $section;

    this.$widget = null;
    this.$userlinks = null;
    this.$qalinks = null;
    this.$irrelevantlinks = null;

    this.render();
    $.ajax({
        url: '{{api-url}}' + 'user_links',
        data: {
            url: window.location.href,
            id: $section.attr('id')
        },
        dataType: 'json',
        success: $.proxy(this, 'handleUserLinksData')
    });
    $.ajax({
        url: '{{api-url}}' + 'qa_links',
        data: {
            url: window.location.href,
            id: $section.attr('id')
        },
        dataType: 'json',
        success: $.proxy(this, 'handleQALinksData')
    });
};

Widget.prototype.handleUserLinksData = function(data) {
    
};

Widget.prototype.handleQALinksData = function(data) {
    
};

Widget.prototype.render = function() {
    this.$widget = $('<div>').css({
        position: 'absolute',
        width: '220px',
        display: 'none',
        background: '#fff',
        color: '#000',
        'z-index': 100,
        border: '1px solid #000'
    });
    this.$userlinks = $('<div>').css({}).text('loading...');
    this.$qalinks = $('<div>').css({}).text('loading...');
    this.$irrelevantlinks = $('<div>').css({}).text('loading...');

    this.$widget.append(this.$userlinks);
    this.$widget.append(this.$qalinks);
    this.$widget.append(this.$irrelevantlinks);

    this.$button.before(this.$widget);
};

Widget.prototype.open = function() {
    this.$widget.show();
};

Widget.prototype.close = function() {
    this.$widget.hide(); 
};
