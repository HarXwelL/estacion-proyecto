from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('team', views.team, name="team"),
    path('user', views.user, name="user"),
    path('login', views.login_auth, name="login"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name="logout"),
    path('contact', views.contact, name="contact"),
    path('contact/reservation', views.reservation, name="reservation"),
    path('contact/reservation/pago', views.pago, name="pago"),
    path('registrarEstacion', views.registrarEstacion),
    path('eliminarEstacion/<nombre_estac>', views.eliminarEstacion),
    path('editarEstacion/<nombre_estac>',views.editarEstacion),
    path('edicionEstacion',views.edicionEstacion)
]