// TODO: use media url from settings
require({ baseUrl : '/media/js/' });
define(['/js/lib/pubsub.js'],
/**
 * Sets up application-wide functionality, then figures out
 * which page we're on based on the body element's data-page
 * attribute, and loads the appropriate page functionality.
 *
 * @returns {Function} Application init function
 */
function() {
  // load per-page functionality
  var bodyId = $('body').attr('id');
  if (bodyId) {
    require(['pages/'+ bodyId]);
  }
}
);
