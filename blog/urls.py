from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.blog, name='blog'),
    # con esto puedo pasar categoria_id como parametro, puedo castear la entrada a int
    path('categoria/<int:categoria_id>/', views.blog_categoria, name='blog_categoria')
    
]
