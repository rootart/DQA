

var Widget = function(section, $button, $section) {
    this.$button = $button;
    this.section = section;
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
            id: $section.attr('id'),
            page_title: document.title,
            section_title: this.section.title

        },
        dataType: 'json',
        success: $.proxy(this, 'handleQALinksData')
    });
};

Widget.prototype.handleUserLinksData = function(data) {
    this.$userlinks.empty();
    this.$irrelevantlinks.empty();
    if (data.links.length) {
        for (var i = 0; i < data.links.length; i++) {
            var $wrapper = $('<div>').css({});

            //Link
            var $link = $('<a>')
                .css({})
                .attr('href', data.links[i].url)
                .text(data.links[i].title);

            // Up votes counter
            var $up_votes = $('<span>')
                .css({})
                .text(data.links[i].up_votes);

            $wrapper.append($link);
            $wrapper.append($up_votes);
            if (data.links[i].is_relevant) {
                this.$userlinks.append($wrapper);
            } else {
                this.$irrelevantlinks.append($wrapper);
            }
        }
    }    
};

Widget.prototype.handleQALinksData = function(data) {
    this.$qalinks.empty();
    if (data.links.length) {
        for (var i = 0; i < data.links.length; i++) {
            var $link = $('<a>').attr('href', data.links[i].url).text(data.links[i].title);

            this.$qalinks.append($link);
        }
    }    
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
