import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    args = ''
    help = 'Combines and generates smartlinky js plugin'

    def handle(self, *args, **options):
        
        configs = []
        for key, value in settings.PLUGIN_CONFIG.items():
            configs.append(['{{%s}}' % key, value])

        self.stdout.write('Configuration: %s \n\n' % configs)


        plugincontent = '(function(){'
        self.stdout.write('Generate plugin..\n')
        for filename in settings.PLUGIN_FILES:
            filepath = os.path.join(settings.MEDIA_ROOT, *filename)
            self.stdout.write('%s, ' % filepath)
            f = open(filepath, 'r')
            filecontent = f.read()

            # Replace configuration patterns
            for config in configs:
                filecontent.replace(*config)

            plugincontent += filecontent
            f.close()
        plugincontent += '})();'

        plugin_filepath = os.path.join(settings.MEDIA_ROOT, settings.PLUGIN_FILENAME)
        self.stdout.write('\nPlugin filepath: %s\n' % plugin_filepath)
        pluginfile = open(plugin_filepath, 'w')
        pluginfile.write(plugincontent)
        pluginfile.close()

                    
        
