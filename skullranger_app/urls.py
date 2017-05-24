from django.conf.urls import url

from skullranger_app import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^login$',views.login_view,name='login'),
    url(r'^logout$',views.logout_view,name='logout'),
    url(r'^signup$',views.signup,name='signup'),
]
