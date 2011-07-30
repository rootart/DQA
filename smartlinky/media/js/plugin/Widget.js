

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
            var $wrapper = $('<div>')
                .css({});


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
                $wrapper.addClass('smartlinky-relevant').draggable({
                    revert: "invalid"
                });
            } else {
                this.$irrelevantlinks.append($wrapper);
                $wrapper.addClass('smartlinky-irrelevant').draggable({
                    revert: "invalid"
                });
            }
        }
    }    
};

Widget.prototype.handleQALinksData = function(data) {
    this.$qalinks.empty();
    if (data.links.length) {
        for (var i = 0; i < data.links.length; i++) {
            var $wrapper = $('<div>').css({});
            var $link = $('<a>').attr('href', data.links[i].url).text(data.links[i].title);
            $wrapper.append($link);

            this.$qalinks.append($wrapper);
        }
    }    
};


Widget.prototype.render = function() {
    // Widget box
    this.$widget = $('<div>').css({
        position: 'absolute',
        width: '220px',
        left: '30px',
        display: 'none',
        background: '#fff',
        color: '#000',
        'z-index': 100,
        border: '1px solid #000'
    });
    // Userlinks section
    this.$userlinks = $('<div>').css({
        padding: '3px',
        border: '1px dotted #00f'
    }).text('loading...').droppable({
        accept: '.smartlinky-irrelevant'
    });
    // Q&A section
    this.$qalinks = $('<div>').css({
        padding: '3px',
        border: '1px dotted #00f'
    }).text('loading...');
    // Irrelevant links section
    this.$irrelevantlinks = $('<div>').css({
        padding: '3px',
        border: '1px dotted #00f'
    }).text('loading...').droppable({
        accept: '.smartlinky-relevant',
        over: function(e, ui) {
        }
    });

    // Close button
    this.$widget.append($('<span>').css({
        width: '13px',
        height: '13px',
        background: '#000',
        color: '#f00',
        float: 'right'
    }).click($.proxy(this, 'close')).text('x'));

    // Add button
    this.$widget.append($('<span>').css({
        width: '33px',
        height: '13px',
        margin: '0px 2px',
        background: '#000',
        color: '#0f0',
        float: 'right'
    }).click($.proxy(this, 'addLink')).text('add'));

    this.$widget.append(this.$userlinks);
    this.$widget.append(this.$qalinks);
    this.$widget.append(this.$irrelevantlinks);

    this.$button.before(this.$widget);
};

Widget.prototype.open = function(e) {
    if (e) {
        e.preventDefault();
    }
    this.$widget.show();
};

Widget.prototype.close = function(e) {
    if (e) {
        e.preventDefault();
    }
    this.$widget.hide(); 
};

Widget.prototype.addLink = function(e) {
    if (e) {
        e.preventDefault();
    }
    if (this.$addWidget) {
        return false;
    }

    this.$addWidget = $('<div>').css({
        padding: '3px',
        border: '1px dotted #00f'
    });

    this.$addWidget.append($('<form>').append($('<input>').attr({
        type: 'text',
        name: 'url'
    }).css({}))).submit($.proxy(this, 'handleNewLinkSubmit'));

    this.$addWidget.prepend($('<label>').text('Add URL:'));
    this.$addWidget.append($('<input>').attr({
        type: 'submit',
        name: 'submit',
        value: 'Submit'
    }));
    
    this.$addWidget.prependTo(this.$widget);
    
};

Widget.prototype.handleNewLinkSubmit = function(e) {
    e.preventDefault();


};
