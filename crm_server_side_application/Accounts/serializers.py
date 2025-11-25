from rest_framework import serializers
from .models import userProfile, Role, UserRoleMapping, Permission, RolePermissions
from django.contrib.auth.hashers import make_password

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["role_id", "role_name", "description"]
        read_only_fields = ("role_id",)


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            "permission_id", "permission_name", "description", "assigned_at",
            "view_all_accounts", "create_account", "edit_account", "delete_account"
        ]
        read_only_fields = ("permission_id", "assigned_at")


class UserRoleMappingSerializer(serializers.ModelSerializer):
    # Nested representations 
    user = UserProfileSerializer(read_only=True)
    role = RoleSerializer(read_only=True)

    # Write-only IDs for POST/PUT
    user_id = serializers.IntegerField(write_only=True)
    role_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserRoleMapping
        fields = [
            "mapping_id", "user", "role", "user_id", "role_id", "assigned_at"
        ]
        read_only_fields = ("mapping_id", "assigned_at")

    def create(self, validated_data):
        user_id = validated_data.pop("user_id")
        role_id = validated_data.pop("role_id")

        # Assign by ID
        validated_data["user"] = userProfile.objects.get(user_id=user_id)
        validated_data["role"] = Role.objects.get(role_id=role_id)

        return super().create(validated_data)

class RolePermissionsSerializer(serializers.ModelSerializer):
    # Nested display (optional)
    role = RoleSerializer(read_only=True)
    permission = PermissionSerializer(read_only=True)

    # Write-only fields for assignment
    role_id = serializers.IntegerField(write_only=True)
    permission_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RolePermissions
        fields = [
            "role_permission_id", "role", "permission",
            "role_id", "permission_id"
        ]
        read_only_fields = ("role_permission_id",)

    def create(self, validated_data):
        role_id = validated_data.pop("role_id")
        permission_id = validated_data.pop("permission_id")

        validated_data["role"] = Role.objects.get(role_id=role_id)
        validated_data["permission"] = Permission.objects.get(permission_id=permission_id)

        return super().create(validated_data)

