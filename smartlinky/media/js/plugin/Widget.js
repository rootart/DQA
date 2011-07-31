

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
    this.$widget = $('<div>').css(style.widget).hide();
    // Userlinks section
    var userlinks_container = $('<ul>').css(style.user_links).appendTo(this.$widget);
    $('<li>').css(style.userlinks_title).text('USER LINKS').appendTo(userlinks_container);
    $('<li>').css(style.add_button).text('ADD +').click($.proxy(this, 'addLink')).appendTo(userlinks_container);
    this.$userlinks = $('<ul>').css(style.userlinks_list).droppable({
        accept: '.smartlinky-irrelevant'
    });
    $('<li>').css(style.list_item).append(this.$userlinks).appendTo(userlinks_container);
    $('<li>').css(style.user_links_more).text('SHOW MORE').hide().appendTo(userlinks_container);

    // Q&A links section
    var qalinks_container = $('<ul>').css(style.user_links).appendTo(this.$widget);

    $('<li>').css(style.qalinks_title).text("EXTERNAL Q&A's").appendTo(qalinks_container);
    this.$qalinks = $('<ul>').css(style.qalinks_list);
    $('<li>').css(style.list_item).append(this.$qalinks).appendTo(qalinks_container);
    $('<li>').css(style.external_links_more).text('SHOW MORE').appendTo(qalinks_container);

    // Irrelevant links section
    this.$irrelevantlinks = $('<ul>').droppable({
        accept: '.smartlinky-relevant',
        over: function(e, ui) {
        }
    });

    // Add small smartlinky logo
    $('<a>')
        .attr({
            href: 'http://smartlinky.com',
            target: '_blank'
        })
        .css(style.logo_small)
        .appendTo(this.$widget);

    this.$button.after(this.$widget);
};

Widget.prototype.loadLinks = function() {
    // Load Users Links
    $.ajax({
        url: '{{api-url}}' + 'users_links',
        data: {
            url: window.location.href,
            section_id: this.section.id
        },
        dataType: 'json',
        success: $.proxy(this, 'handleUserLinksData')
    });
    // Load Q&A Links
    $.ajax({
        url: '{{api-url}}' + 'qa_links',
        data: {
            url: window.location.href,
            section_id: this.section.id,
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
    var $wrapper = $('<li>');


    //Link
    var $link = $('<a>')
        .css(style.link)
        .attr('href', linkData.url)
        .text(linkData.title);
    $wrapper.append($link);

    if (linkData.id) {
        $wrapper.css(style.user_links_element);
        // Up votes counter
        var $up_votes = $('<span>')
            .css(style.star)
            .data('link-id', linkData.id)
            .text('(' + linkData.up_votes + ')')
            .click(function(e){
                e.preventDefault();
                var star = this;
                $.post("{{api-url}}vote_up", {'id': $(this).data('link-id')}, function(){
                    $(star).remove();
                });
            });
        //    .text(linkData.up_votes);
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
        $wrapper.css(style.qalinks_element);
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

Widget.prototype.toggle = function(e) {
    if (e) {
        e.preventDefault();
    }
    this.$widget.toggle(); 
    if (this.$widget.is(':visible')) {
        this.$button.css(style.button_active);
    } else {
        this.$button.css(style.button);
    }
}

Widget.prototype.addLink = function(e) {
    if (e) {
        e.preventDefault();
    }
    if (this.$addWidget) {
        return false;
    }

    this.$addWidget = $('<div>').css({
        padding: '8px',
		background: '#fbf2a4',
		marginLeft: '4px',
		marginBottom: '25px'
    });

    this.$form = $('<form>').submit($.proxy(this, 'handleNewLinkSubmit'));
    this.$form.append($('<input>').attr({
            type: 'text',
            name: 'url',
            value: 'http://'
        }).css({}));
    this.$form.prepend($('<label>').text('Add URL:'));
    this.$form.append($('<input>').attr({
        type: 'submit',
        name: 'submit',
        value: 'Submit'
    }).css(
		style.add_button).css( 
		'margin-top', '0px'
	));

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
