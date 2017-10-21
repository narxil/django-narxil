from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'narxil.views.bookmark_user',
        name='narxil_bookmark_user'),
    url(r'^$', 'narxil.views.bookmark_list', name='narxil_bookmark_list'),
]
