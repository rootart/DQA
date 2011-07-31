

var Widget = function(section, $button, $section) {
    this.$button = $button;
    this.section = section;
    this.$section = $section;

    this.$widget = null;
    this.$userlinks = null;
    this.$qalinks = null;
    this.$irrelevantlinks = null;

    this.render();
    this.loadLinks();
};

/* {@ Init methods */
Widget.prototype.render = function() {
    // Widget box
    this.$widget = $('<div>').css(style.widget);
    // Userlinks section
    var userlinks_container = $('<ul>').css(style.user_links).appendTo(this.$widget);
    $('<li>').css(style.userlinks_title).text('USER LINKS').appendTo(userlinks_container);
    $('<li>').css(style.add_button).text('ADD +').click($.proxy(this, 'addLink')).appendTo(userlinks_container);
    
    this.$userlinks = $('<ul>').css(style.userlinks_list).droppable({
        accept: '.smartlinky-irrelevant'
    });
    
    $('<li>').append(this.$userlinks).appendTo(userlinks_container);

    $('<li>').css(style.user_links_more).text('ADD +').appendTo(userlinks_container);

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

    this.$button.after(this.$widget);
};

Widget.prototype.loadLinks = function() {
    // Load Users Links
    $.ajax({
        url: '{{api-url}}' + 'users_links',
        data: {
            url: window.location.href,
            section_id: $section.attr('id')
        },
        dataType: 'json',
        success: $.proxy(this, 'handleUserLinksData')
    });
    // Load Q&A Links
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
/* Init methods @} */


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


/**
 * Open widget
 */
Widget.prototype.open = function(e) {
    if (e) {
        e.preventDefault();
    }
    this.$widget.show();
};

/**
 * Close widget
 */
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
