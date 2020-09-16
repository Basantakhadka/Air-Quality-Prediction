"""airprediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from  .import views


app_name="main"

urlpatterns = [
	path('', views.homepage, name ='home-page'),
	path('about',views.about, name ='about-us'),
	path('past_data', views.past_data, name='past-data'),
    path('predict',views.predict,name='predict-data'),
    path('predictaqi',views.predictaqi,name='predict-aqi'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('download',views.download,name='download')
]
