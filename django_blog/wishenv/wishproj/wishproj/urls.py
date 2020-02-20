"""wishlistproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wishapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),

    path('home/',views.home ,name='home'),
    path('wishlist/',views.wish_list ,name='wishlist'),
    path('list/<int:list_id>/detail/',views.list_detail ,name='list-detail'),
    path('list/<int:list_id>/item/',views.item_create ,name='item-detail'),
    path('itemlist/<int:item_id>',views.items_wish ,name='item-list'),
    path('list/create/',views.list_create ,name='list-create'),
    path('list/<int:list_id>/update/',views.list_update ,name='list-update'),
    path('list/<int:list_id>/delete/',views.list_delete ,name='list-delete'),
    path('list/<int:list_id>/item/create/',views.item_create ,name='item-create'),


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
