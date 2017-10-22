from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'narxil.views.bookmark_user',
        name='narxil_bookmark_user'),

    url(r'^create/$', 'narxil.views.bookmark_create',
        name='narxil_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'narxil.views.bookmark_edit',
        name='narxil_bookmark_edit'),

    url(r'^$', 'narxil.views.bookmark_list', name='narxil_bookmark_list'),
]
