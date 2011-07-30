var Parser = function() {
    var sections = {};
};

/**
 * Parses the document and looks for sections
 */
Parser.prototype.parse = function() {
    $('.section').each($.proxy(this, 'match'));
};

/**
 * Parses the section and gets the id and header
 */
Parser.prototype.match = function(key, section) {
    $section = $(section);
    var title = $section.find('h1, h2, h3, h4, h5').first().text();
    this.sections[$section.attr('id')] = {
        title: title,
        id: $section.attr('id'),
        order: key
    };    
};
