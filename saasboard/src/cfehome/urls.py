"""
URL configuration for cfehome project.

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
from django.contrib import admin
from django.urls import path, include
from landing import views as landing_views
from subscriptions import views as subs_views

urlpatterns = [
    path("", landing_views.landing_dashboard_page_view, name='home'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', landing_views.landing_dashboard_page_view, name='dashboard'),
    path("pricing/", subs_views.subscription_price_view, name='pricing'),
    path("pricing/<str:interval>/", subs_views.subscription_price_view, name='pricing_interval'),
    path('accounts/billing/', subs_views.user_subscription_view, name='user_subscription'),
    path('accounts/billing/cancel', subs_views.user_subscription_cancel_view, name='user_subscription_cancel'),
]
