from django.conf.urls import url

from OGS.views import first_view, SobreNosotrosView, CafeView, BebidasCalientesView, BebidasFriasView, SnacksView, \
    ServiciosView, PromocionesView, ContactoView

urlpatterns = [
    url(r'^$', first_view, name='vending-ogs'),
    url(r'^sobrenosotros/$', SobreNosotrosView.as_view(), name='sobre-nosotros'),
    url(r'^cafe/$', CafeView.as_view(), name='cafe'),
    url(r'^productos/bebidascalientes/$', BebidasCalientesView.as_view(), name='bebidas-calientes'),
    url(r'^productos/bebidasfrias/$', BebidasFriasView.as_view(), name='bebidas-frias'),
    url(r'^productos/snacks/$', SnacksView.as_view(), name='snacks'),
    url(r'^servicios/$', ServiciosView.as_view(), name='servicios'),
    url(r'^promociones/$', PromocionesView.as_view(), name='promociones'),
    url(r'^contacto/$', ContactoView.as_view(), name='contacto'),

]
