#__author__ = 'Dragan Vidakovic'
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from restaurant import views


app_name = 'restaurant'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^about/$', views.about,name='about'),
    url(r'^contact/$', views.contact,name='contact'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^password-reset/$',
         auth_views.PasswordResetView.as_view(
             template_name='restaurant/password_reset.html'
         ),
         name='password_reset'),
    url(r'^password-reset/done/$',
         auth_views.PasswordResetView.as_view(
             template_name='restaurant/password_reset_done.html'
        , email_template_name = 'restaurant/password_reset_email.html'),
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='restaurant/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
   
    url(r'^password-reset-complete/$',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='restaurant/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    url(r'^activation/(?P<user_id>[0-9]+)/$', views.activation, name='activation'),
    url(r'^manager/(?P<manager_id>[0-9]+)/$', views.manager, name='manager'),
    url(r'^profiling/(?P<manager_id>[0-9]+)/$', views.profiling, name='profiling'),
    url(r'^updating/(?P<manager_id>[0-9]+)/$', views.updating, name='updating'),
    url(r'^menu/(?P<restaurant_id>[0-9]+)/(?P<manager_id>[0-9]+)/$', views.menu, name='menu'),
    url(r'^tables/(?P<restaurant_id>[0-9]+)/(?P<manager_id>[0-9]+)/$', views.tables, name='tables'),
    url(r'^setup/(?P<restaurant_id>[0-9]+)/(?P<manager_id>[0-9]+)/$', views.setup, name='setup'),
    url(r'^remove/(?P<item_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/(?P<manager_id>[0-9]+)/$', views.remove, name='remove'),
    url(r'^edit/(?P<item_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/(?P<manager_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^saveedition/(?P<item_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/(?P<manager_id>[0-9]+)/$', views.saveedition, name='saveedition'),
    url(r'^insert/(?P<restaurant_id>[0-9]+)/(?P<manager_id>[0-9]+)/$', views.insert, name='insert'),
    url(r'^guest/(?P<guest_id>[0-9]+)/$', views.guest, name='guest'),
    url(r'^rate/(?P<guest_id>[0-9]+)/(?P<visit_id>[0-9]+)/$', views.rate, name='rate'),
    url(r'^rating/(?P<guest_id>[0-9]+)/(?P<visit_id>[0-9]+)/$', views.rating, name='rating'),
    url(r'^friends/(?P<guest_id>[0-9]+)/$', views.friends, name='friends'),
    url(r'^search/(?P<guest_id>[0-9]+)/$', views.search, name='search'),
    url(r'^connect/(?P<guest_id>[0-9]+)/(?P<connection_id>[0-9]+)/$', views.connect, name='connect'),
    url(r'^disconnect/(?P<guest_id>[0-9]+)/(?P<friend_id>[0-9]+)/$', views.disconnect, name='disconnect'),
    url(r'^profile/(?P<guest_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^update/(?P<guest_id>[0-9]+)/$', views.update, name='update'),
    url(r'^myreservations/(?P<guest_id>[0-9]+)/$', views.myreservations, name='myreservations'),
    url(r'^searching/(?P<guest_id>[0-9]+)/$', views.searching, name='searching'),
    url(r'^restaurantlist/(?P<guest_id>[0-9]+)/$', views.restaurantlist, name='restaurantlist'),
    url(r'^restaurantmenu/(?P<guest_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/$', views.restaurantmenu, name='restaurantmenu'),
    url(r'^reservationtime/(?P<guest_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/$', views.reservationtime, name='reservationtime'),
    url(r'^makereservation/(?P<guest_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/$', views.makereservation, name='makereservation'),
    url(r'^reservetables/(?P<guest_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/(?P<reservation_id>[0-9]+)/$', views.reservetables, name='reservetables'),
    url(r'^invitefriends/(?P<guest_id>[0-9]+)/(?P<restaurant_id>[0-9]+)/(?P<reservation_id>[0-9]+)/$', views.invitefriends, name='invitefriends'),
    url(r'^showinvitation/(?P<guest_id>[0-9]+)/(?P<reservation_id>[0-9]+)/(?P<visit_id>[0-9]+)/$', views.showinvitation, name='showinvitation'),
    url(r'^acceptinvitation/(?P<guest_id>[0-9]+)/(?P<reservation_id>[0-9]+)/(?P<visit_id>[0-9]+)/$', views.acceptinvitation, name='acceptinvitation'),

]