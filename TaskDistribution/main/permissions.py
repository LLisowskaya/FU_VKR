'''from rest_framework import permissions

class CanViewTask(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('view_task')

class CanViewEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('view_employee')

class CanViewTaskAssignment(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('view_taskassignment')

class CanViewEmployeeConfirmation(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('view_employeeconfirmation')'''
