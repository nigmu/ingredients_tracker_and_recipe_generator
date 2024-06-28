"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path


from accounts.views import (
    login_view,
    logout_view,
    register_view,
)


# from articles import views

# write the above or the below

from articles.views import (
    article_search_view,
    article_create_view,
    article_detail_view,
)
from .views import home_view

# urlpatterns = [
#     path("", home_view), #index / home / root
#     path("articles/", views.article_search_view),
#     path("articles/create/", views.article_create_view),
#     path("articles/<int:id>/", views.article_detail_view),
#     path("admin/", admin.site.urls),
# ]

# above for above and below for below

urlpatterns = [
    path("", home_view), #index / home / root
    path("articles/", article_search_view),
    path("articles/create/", article_create_view),
    path("articles/<int:id>/", article_detail_view),
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),

]

