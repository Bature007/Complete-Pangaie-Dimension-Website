from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('singlepage/<int:pk>',views.singlepage,name='singlepage'),
    path('postservice/',views.postservice,name='postservice'),
    path('registration/',views.registration,name='registration'),
    path('dashboard/',views.dashboard,name='dashboard'),
    # path('update_post/<int:og>/',views.update_post,name='update_post'),
    # path('update_post/<int:og>',views.update_post,name='update_post'),
    path('delete_post/<int:ig>',views.delete_post,name='delete_post'),
    # path('updateform/',views.updateform,name='updateform'),
    path('update/<int:ig>',views.update,name='update'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('admincontact/',views.admincontact,name='admincontact')
]
