/**
 * Style.js
 *
 * Style of the plugin.
 */

var cleaner = {
    border: 0,
    background: 'transparent',
    color: '#000',
    margin: 0,
    padding: 0,
    listStyle: 'none'
};

var style = {
    'list_item': {
        listStyle: 'none'
    },
    'wrapper': {
        height: '0px',
        position: 'relative'
    },
    'container': {
        position: 'absolute',
        right: '-32px',
        'top': '-16px',
        fontFamily: 'Arial, "Helvetica", sans-serif',
        fontSize: '11px'
    },
    'button': {
        'float': 'right',
        background: 'transparent url("{{media-url}}imgs/icon_widget.png") no-repeat 6px 6px',
        opacity: '0.5',
        height: '34px',
        width: '14px',
        padding: '6px 6px 6px 27px',
        color: '#fff',
        cursor: 'pointer',
        border: '0px',
        margin: '8px',
        '-moz-background-clip': 'padding',    
        '-webkit-background-clip': 'padding', 
        'background-clip': 'padding-box'
    },
    'list': {
        listStyle: 'none',
        color: '#404646',
        fontSize: '16px',
        height: '20px',
        overflow: 'hidden'
    },
    'list_element' : {
        listStyle: 'none',
        display: 'block',
        textTransform: 'none',
        marginTop: '0px'
    },
    'widget': {
        width: '300px',
        background: '#f3f3f3 ',
        margin: '0 47px 0 0',
        border: 'rgba(187, 187, 187, 0.4) 8px solid',
        padding: '10px 10px 70px',
        '-moz-background-clip': 'padding',    
        '-webkit-background-clip': 'padding', 
        'background-clip': 'padding-box'
    },
    'container_title': {
        color: '#404646',
        fontSize: '16px',
        height: '20px',
        overflow: 'hidden'
    },
    'block_list_item': {
        display: 'inline',
        textTransform: 'uppercase',
        listStyle: 'none'
    },
    'user_links': {
        paddingTop: '4px',
        marginTop: '14px',
        paddingLeft: '8px'
    },
    'user_links_element': {
    borderBottom: '1px solid #46b0d1',
        display: 'block'
    },
    'qalinks_element': {
    borderBottom: '1px solid #bebebe',
        display: 'block'
    },
    'user_links_more': {
        background: 'none repeat scroll 0 0 #46B0D1',
        'border-bottom-left-radius': '5px',
        'border-bottom-right-radius': '5px',
        fontWeight: 'bold',
        padding: '6px 10px',
        cursor: 'pointer',
        'float': 'right'
    },
    'userlinks_title': {
        'border-top-left-radius': '5px',
        'border-top-right-radius': '5px',
        'font-weight': 'bold',
        'padding': '7px 10px 3px',
        'text-transform': 'uppercase',
        'border-left': '1px solid #46B0D1',
        'border-right': '1px solid #46B0D1',
        'border-top': '1px solid #46B0D1',
        'background': 'none repeat scroll 0 0 #85D1E9',
        listStyle: 'none',
        'display': 'inline'
    },
    'userlinks_list': {
        background: '#85D1E9',
        border: '1px solid #46B0D1',
        paddingTop: '4px',
        paddingLeft: '1.2em'
    },
    'add_button': {
        color: '#fff',
        background: '#d94545',
        padding: '2px 5px',
        cursor: 'pointer',
        marginTop: '-7px',
        display: 'inline',
        'float': 'right'
    },
    'link': {
        textDecoration: 'none',
        color: '#404646'        
    },
    'qalinks_title': {
        'border-top-left-radius': '5px',
        'border-top-right-radius': '5px',
        'font-weight': 'bold',
        'padding': '7px 10px 3px',
        'text-transform': 'uppercase',
        'border-left': '1px solid #BEBEBE',
        'border-right': '1px solid #BEBEBE',
        'border-top': '1px solid #BEBEBE',
        'background': 'none repeat scroll 0 0 #E3E3E3',
        'display': 'inline' 
    },
    'qalinks_list': {
        background: '#e3e3e3',
        border: '1px solid #BEBEBE',
        paddingTop: '4px',
        paddingLeft: '1.2em'
    },
    'external_links_more': {
        background: '#B0B3B3',
        'border-bottom-left-radius': '5px',
        'border-bottom-right-radius': '5px',
        fontWeight: 'bold',
        padding: '6px 10px',
        cursor: 'pointer',
        'float': 'right',
        color: '#404646'
    },
    'logo_small': {
        'float': 'right',
        background: 'url("{{media-url}}imgs/logo_small_widget.png") no-repeat',
        width: '98px',
        height: '15px',
        clear: 'both',
        display: 'block',
        marginTop: '17px'
    },
    'star': {
        'background': 'url("{{media-url}}imgs/star.png") no-repeat scroll left bottom transparent',
        'float': 'right',
        'height': '15px',
        'overflow': 'hidden',
        paddingLeft: '15px',
        marginRight: '3px',
        'cursor': 'pointer',
        textAlign: 'right'
    }

        
};

for (var key in style) {
    if (style.hasOwnProperty(key)) {
        style[key] = $.extend({}, cleaner, style[key]);
    }
}
style.button_active = $.extend({}, style.button, {
    borderTop: 'rgba(187, 187, 187, 0.4) 8px solid',
    borderBottom: 'rgba(187, 187, 187, 0.4) 8px solid',
    borderRight: 'rgba(187, 187, 187, 0.4) 8px solid',
    margin: '0px',
    background: '#f3f3f3 url("{{media-url}}imgs/icon_widget.png") no-repeat 6px 6px',
    opacity: '1',
});
