from django.shortcuts import render
from rest_framework import viewsets
from .models import userProfile, Role, UserRoleMapping, Permission, RolePermissions
from .serializers import (
    userProfileSerializer,
    RoleSerializer,
    UserRoleMappingSerializer,
    PermissionSerializer,
    RolePermissionsSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = userProfile.objects.all()
    serializer_class = UserProfileSerializer

    # GET /users/<id>/roles/
    @action(detail=True, methods=["get"])
    def roles(self, request, pk=None):
        user = self.get_object()
        mappings = UserRoleMapping.objects.filter(user=user)
        serializer = UserRoleMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    # POST /users/<id>/assign-role/
    @action(detail=True, methods=["post"])
    def assign_role(self, request, pk=None):
        user = self.get_object()
        role_id = request.data.get("role_id")

        if not role_id:
            return Response({"error": "role_id is required"}, status=400)

        role = get_object_or_404(Role, role_id=role_id)

        mapping, created = UserRoleMapping.objects.get_or_create(user=user, role=role)

        if not created:
            return Response({"message": "Role already assigned"}, status=200)

        return Response(
            {"message": f"Role '{role.role_name}' assigned to {user.username}"},
            status=201
        )

    # POST /users/<id>/remove-role/
    @action(detail=True, methods=["post"])
    def remove_role(self, request, pk=None):
        user = self.get_object()
        role_id = request.data.get("role_id")

        mapping = UserRoleMapping.objects.filter(user=user, role_id=role_id).first()

        if not mapping:
            return Response({"error": "This role is not assigned"}, status=404)

        mapping.delete()

        return Response({"message": "Role removed successfully"}, status=200)


#Role ViewSet
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    # GET /roles/<id>/permissions/
    @action(detail=True, methods=["get"])
    def permissions(self, request, pk=None):
        role = self.get_object()
        perms = RolePermissions.objects.filter(role=role)
        serializer = RolePermissionsSerializer(perms, many=True)
        return Response(serializer.data)

    # POST /roles/<id>/assign-permission/
    @action(detail=True, methods=["post"])
    def assign_permission(self, request, pk=None):
        role = self.get_object()
        permission_id = request.data.get("permission_id")

        if not permission_id:
            return Response({"error": "permission_id is required"}, status=400)

        permission = get_object_or_404(Permission, permission_id=permission_id)

        mapping, created = RolePermissions.objects.get_or_create(
            role=role, permission=permission
        )

        if not created:
            return Response({"message": "Permission already assigned"}, status=200)

        return Response(
            {"message": f"Permission '{permission.permission_name}' assigned to role '{role.role_name}'"},
            status=201
        )

    # POST /roles/<id>/remove-permission/
    @action(detail=True, methods=["post"])
    def remove_permission(self, request, pk=None):
        role = self.get_object()
        permission_id = request.data.get("permission_id")

        mapping = RolePermissions.objects.filter(
            role=role, permission_id=permission_id
        ).first()

        if not mapping:
            return Response({"error": "Permission is not assigned"}, status=404)

        mapping.delete()

        return Response({"message": "Permission removed successfully"}, status=200)


#permission ViewSet

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


#RolePermissions ViewSet
class RolePermissionsViewSet(viewsets.ModelViewSet):
    queryset = RolePermissions.objects.all()
    serializer_class = RolePermissionsSerializer


#rolemapping ViewSet
class UserRoleMappingViewSet(viewsets.ModelViewSet):
    queryset = UserRoleMapping.objects.all()
    serializer_class = UserRoleMappingSerializer
