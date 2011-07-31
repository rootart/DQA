/**
 * Style.js
 *
 * Style of the plugin.
 */

var cleaner = {
    border: 0,
    background: 'transparent',
    color: '#fff',
    margin: 0,
    padding: 0
};

var style = {
    'wrapper': {
	width: '314px',
	position: 'absolute',
	fontFamily: 'Arial, "Helvetica", sans-serif',
	fontSize: '11px'
    },
    'button': {
	'float':'left',
	background: 'url("{{media-url}}imgs/icon_widget.png") no-repeat',
	height: '34px',
	width: '16px',
	paddingLeft: '26px',
	color: '#fff',
	margin: '10px'
    },
    'list': {
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
    'container': {
	background: '#f3f3f3',
	border: '1px solid #bebebe',
	'-webkit-box-shadow': '0px 0px 5px 0px #4a4a4a',
	'-moz-box-shadow': '0px 0px 5px 0px #4a4a4a',
	boxShadow: '0px 0px 5px 0px #4a4a4a', 
	padding: '10px',
	paddingBottom: '20px'
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
	background: '#85d1e9',
	border: '1px solid #46b0d1'
    },
    'user_links_element': {
	borderBottom: '1px solid #46b0d1'
    },
//    'user_links_more':
//    'title_user':
    'add_button': {
	color: '#fff',
	background: '#d94545',
	padding: '2px 5px'   
    },
//    'star':
    'link': {
	textDecoration: 'none',
	color: '#404646'        
    },
    'external_links': {
	background: '#e3e3e3',
	border: '1px solid #b0b3b3'        
    },
    'external_links_more': {
	color: '#404646'        
    }
//    'trash':
//    'logo_small':

        
};

for (var key in style) {
    if (style.hasOwnProperty(key)) {
        style[key] = $.extend(cleaner, style[key]);
    }
}
