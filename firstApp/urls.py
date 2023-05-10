from django.urls import path,include
from . import views


urlpatterns = [
  path('', views.home, name="home"),
  path('tool',views.tool, name='tool'),
  path('signup', views.SignUp.as_view(), name="signup"),
  path('login', views.login_view, name="login"),
  path('logout', views.logout_view, name="logout"),
  path('add_rail', views.add_rail, name="add_rail")
]