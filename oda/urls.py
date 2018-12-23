from django.urls import path,re_path
from . import views
from django.conf.urls import url

app_name='oda'
urlpatterns = [
    #path('brand/<int:brand_id>/', views.brand_data, name='brand_data'),
    path('user/driver/',views.driver_data,name='driver_data'),
    path('user/',views.login_user,name='login'),
    path('user/heatmap/',views.Posdata_brand,name='brand_posdata'),
    path('driver/heatmap/<int:driver_id>/',views.Posdata_driver,name='driver_posdata'),
    path('',views.Home,name='home')
]