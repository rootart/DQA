import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    args = ''
    help = 'Combines and generates smartlinky js plugin'

    def handle(self, *args, **options):
        plugincontent = '(function(){'
        self.stdout.writelines(['Generate plugin..'])
        for filename in settings.PLUGIN_FILES:
            filepath = os.path.join(settings.MEDIA_ROOT, *filename)
            self.stdout.writelines(['..%s' % filepath])
            f = open(filepath, 'r')
            plugincontent += f.read()
            f.close()
        plugincontent += '})();'

        plugin_filepath = os.path.join(settings.MEDIA_ROOT, settings.PLUGIN_FILENAME)
        self.stdout.writelines(['Plugin filepath: %s' % plugin_filepath])
        pluginfile = open(plugin_filepath, 'w')
        pluginfile.write(plugincontent)
        pluginfile.close()

                    
        
