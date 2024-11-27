from django.db import models
from django.contrib.auth.models import AbstractUser

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(help_text="Comma-separated list of permissions")

    def __str__(self):
        return self.name

# Permission Model
class Permission(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(help_text="Description of the permission")

    def __str__(self):
        return self.name

class RolePermissions(models.Model):
    role = models.ForeignKey(Role, related_name='permissions', on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, related_name='roles', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.role.name} - {self.permission.name}'


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def has_permission(self, permission_name):
        if self.role:
            return self.role.permissions.filter(permission__name=permission_name).exists()
        return False  
