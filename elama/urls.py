"""
URL configuration for esprolama project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from elama import views

app_name = 'elama'
urlpatterns = [
    path('individual/nueva/', views.autoevaluaciones, name='autoevaluaciones'),
    path('individual/nueva/autoevaluacion_<int:autoevaluacion_id>/', views.estrategias, name='estrategias'),
    path('individual/nueva/estrategia_<int:estrategia_id>/', views.principios, name='principios'),
    path('individual/nueva/principio_<int:principio_id>/', views.descriptores, name='descriptores'),
    path('individual/nueva/descriptor_<int:descriptor_id>/', views.volcado, name='volcado'),
    #path('individual/edit/', include(''))
]
