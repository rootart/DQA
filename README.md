Smartlinky
==========

We all love well written docs. But it's not an easy task to produce such. How about letting people collaborate on this? 

Project structure
-----------------
 * smartlinky/ - web project
   * apps/ - django applications
   * docs/ - documentation
   * media/ - media files
 * smartlinky_extension/ - extension for Google Chrome


Deploy on Gondor.io
-------------------

You can easily deploy it to Gondor.io service. 

0. go to web project root

1. Set up your Gondor.io environment (you can find more information on Gondor.io help pages https://gondor.io/support/)

2. Run deployment script:

    gondor deploy primary master


3. Run generateplugin management script:

    gondor run primary generateplugin



Deploy on localhost
-------------------
0. go to web project root

1. Install requirements:

    pip install requirements.pip


2. Synchronize database:

    python ./manage.py syncdb
    

3. Run your server:

    python ./manage.py runserver

4. Run generateplugin management script:

    python ./manage.py generateplugin


Generate plugin
---------------

We use only one javascript file for our browser extension and embeddable script. We created a managemant command to generate this file. This file can be embedded on every documentation.

Therefore it's important to generate this file after the deployment.

The generation process uses 3 settings variables:

 * PLUGIN_FILES: The file paths, that are compiled to one file
 * PLUGIN_FILENAME: Filename of generated/compiled file
 * PLUGIN_CONFIG: Configuration for javascript code

The settings for the production environment can be found in settings.py.
