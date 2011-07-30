

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
            section_id: $section.attr('id')
        },
        dataType: 'json',
        success: $.proxy(this, 'handleUserLinksData')
    });
    $.ajax({
        url: '{{api-url}}' + 'qa_links',
        data: {
            url: window.location.href,
            section_id: $section.attr('id'),
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
            this.insertLink(data.links[i]);
        }
    }    
};

Widget.prototype.insertLink = function(linkData) {
    var $wrapper = $('<div>')
        .css({});


    //Link
    var $link = $('<a>')
        .css({})
        .attr('href', linkData.url)
        .text(linkData.title);
    $wrapper.append($link);

    if (linkData.id) {
        // Up votes counter
        var $up_votes = $('<span>')
            .css({})
            .text(linkData.up_votes);
        $wrapper.append($up_votes);

        if (linkData.is_relevant) {
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
    } else {
        this.$qalinks.append($wrapper);
    }
}

Widget.prototype.handleQALinksData = function(data) {
    this.$qalinks.empty();
    if (data.links.length) {
        for (var i = 0; i < data.links.length; i++) {
            this.insertLink(data.links[i]); 
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

    this.$form = $('<form>').submit($.proxy(this, 'handleNewLinkSubmit'));
    this.$form.append($('<input>').attr({
            type: 'text',
            name: 'url'
        }).css({}));
    this.$form.prepend($('<label>').text('Add URL:'));
    this.$form.append($('<input>').attr({
        type: 'submit',
        name: 'submit',
        value: 'Submit'
    }));

    this.$addWidget.append(this.$form);
    this.$addWidget.prependTo(this.$widget);
};

Widget.prototype.handleNewLinkSubmit = function(e) {
    e.preventDefault();
    $.ajax({
        url: '{{api-url}}' + 'add_link',
        type: 'POST',
        dataType: 'json',
        data: {
            page_title: document.title,
            url: window.location.href,
            section_id: this.section.id,
            section_title: this.section.title,
            link_url: this.$addWidget.find('input[name="url"]').val(),
        },
        success: $.proxy(this, 'handleAddLinkSuccess')
    });
};

Widget.prototype.handleAddLinkSuccess = function(data) {
    this.insertLink(data);
}
