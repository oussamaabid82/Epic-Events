"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from rest_framework import routers
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import SignupViewset, UserViewset
from create_events.views import ClientViewSet, EventViewSet, ContractViewSet, EventsListViewSet


router = routers.SimpleRouter()
router.register('signup', SignupViewset, basename='signup')
router.register('userlist', UserViewset, basename='userlist')
router.register('clients', ClientViewSet, basename='clients')
router.register('contracts', ContractViewSet, basename='contracts')
router.register('eventslist', EventsListViewSet, basename='events_list')

"""
Nested router:
    -/contracts/{id}/events/{id}
"""
contract_router = routers.NestedSimpleRouter(router, r'contracts', lookup='contract')
contract_router.register(r'events', EventViewSet, basename='event_view')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include(contract_router.urls)),
]
