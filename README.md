Smartlinky
==========

We all love well written docs. But it's not an easy task to produce such. How about letting people collaborate on this? 


Deploy on Gondor.io
-------------------

You can easily deploy it to Gondor.io service. 

1.  Set up your Gondor.io environment (you can find more information on Gondor.io help pages https://gondor.io/support/)
2.  Run deployment script:
    gondor deploy primary master
3.  Run generateplugin management script:
    gondor run primary generateplugin



Deploy on localhost
-------------------

1.  Install requirements:
    pip install requirements.pip
2.  Synchronize database:
    python ./manage.py syncdb
3.  Run your server:
    python ./manage.py runserver

