import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    args = ''
    help = 'Combines and generates smartlinky js plugin'

    def handle(self, *args, **options):
        
        if settings.DEBUG:
            root = settings.MEDIA_ROOT
        else:
            root = settings.STATIC_ROOT

        configs = []
        for key, value in settings.PLUGIN_CONFIG.items():
            configs.append(['{{%s}}' % key, value])

        self.stdout.write('Configuration: %s \n\n' % configs)


        plugincontent = '(function(){'
        self.stdout.write('Generate plugin..\n')
        for filename in settings.PLUGIN_FILES:
            filepath = os.path.join(root, *filename)
            self.stdout.write('%s, ' % filepath)
            f = open(filepath, 'r')
            filecontent = f.read()

            # Replace configuration patterns
            for config in configs:
                filecontent = filecontent.replace(*config)

            plugincontent += filecontent
            f.close()
        plugincontent += '})();'

        plugin_filepath = os.path.join(root, settings.PLUGIN_FILENAME)
        self.stdout.write('\nPlugin filepath: %s\n' % plugin_filepath)
        pluginfile = open(plugin_filepath, 'w')
        pluginfile.write(plugincontent)
        pluginfile.close()
                    
        
