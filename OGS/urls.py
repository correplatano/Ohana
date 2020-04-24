from django.conf.urls import url

from OGS.views import first_view, SobreNosotrosView

urlpatterns = [
    url(r'^$', first_view, name='first-view'),
    url(r'^sobrenosotros/$', SobreNosotrosView.as_view(), name='sobre-nosotros'),

]
