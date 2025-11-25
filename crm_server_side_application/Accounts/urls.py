from django.urls import path, include
from rest_framework.routers import DefaultRouter
from serializers import userProfileSerializer, RoleSerializer, PermissionSerializer, UserRoleMappingSerializer, RolePermissionsSerializer
from .models import userProfile, Role, Permission, UserRoleMapping, RolePermissions


from .views import (
    UserViewSet, RoleViewSet, PermissionViewSet,
    UserRoleMappingViewSet, RolePermissionsViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'user-role-mappings', UserRoleMappingViewSet)
router.register(r'role-permissions', RolePermissionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
