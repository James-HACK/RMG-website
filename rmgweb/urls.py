from django.conf.urls.defaults import *
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('rmgweb',
    # Example:
    # (r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # The RMG website homepage
    (r'^$', 'main.views.index'),
    
    # User account management
    (r'^login$', 'main.views.login'),
    (r'^logout$', 'main.views.logout'),
    (r'^profile$', 'main.views.editProfile'),

    (r'^user/(?P<username>\w+)$', 'main.views.viewProfile'),

)

# When developing in Django we generally don't have a web server available to
# serve static media; this code enables serving of static media by Django
# DO NOT USE in a production environment!
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.PROJECT_PATH, 'media'),
             'show_indexes': True, }
        ),
    )
