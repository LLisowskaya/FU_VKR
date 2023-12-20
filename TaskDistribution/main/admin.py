from django.contrib import admin
from .models import Employee, Task, TaskAssignment, EmployeeRating, Issue, Department, EmployeeConfirmation, Notes, \
    TaskCompletionRequest
import openpyxl
from django.http import HttpResponse


class TaskCompletionRequestAdmin(admin.ModelAdmin):
    list_display = ('task', 'employee', 'is_approved', 'comment')
    list_filter = ('is_approved',)
    search_fields = ('task__title', 'employee__surname', 'employee__name')


class ExportAdminMixin:
    def export_data(self, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active

        header = [field.verbose_name for field in self.model._meta.fields]
        ws.append(header)

        for obj in queryset:
            row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
            ws.append(row)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={self.model.__name__}_export.xlsx'
        wb.save(response)

        return response

    export_data.short_description = "Экспорт данных"


@admin.register(Task, Employee, TaskAssignment, EmployeeRating, Issue, Department, EmployeeConfirmation, Notes, TaskCompletionRequest)
class EmployeeAdmin(admin.ModelAdmin, ExportAdminMixin):
    actions = ['export_data']



'''admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task)
admin.site.register(TaskAssignment)
admin.site.register(EmployeeRating)
admin.site.register(Issue)
admin.site.register(Department)
admin.site.register(EmployeeConfirmation)
admin.site.register(Notes)'''







'''class BaseAdminMixin:
    def has_view_permission(self, request, obj=None):
        raise NotImplementedError("Subclasses must implement this method.")

    def has_change_permission(self, request, obj=None):
        return self.has_view_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return self.has_view_permission(request, obj)

    def has_add_permission(self, request):
        return self.has_view_permission(request)


class SonuserAdminMixin(BaseAdminMixin):
    def has_view_permission(self, request, obj=None):
        return request.user.username == 'sonuser'

    def has_change_permission(self, request, obj=None):
        return self.has_view_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return self.has_view_permission(request, obj)

    def has_add_permission(self, request):
        return self.has_view_permission(request)


class TeamLeaderAdminMixin(BaseAdminMixin):
    def has_view_permission(self, request, obj=None):
        return request.user.username == 'teamleader'

    def has_change_permission(self, request, obj=None):
        return self.has_view_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return self.has_view_permission(request, obj)

    def has_add_permission(self, request):
        return self.has_view_permission(request)


class SonuserTaskAdmin(SonuserAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'deadline', 'status', 'difficulty', 'department', 'employee', 'notifications_sent']


class SonuserTaskAssignmentAdmin(SonuserAdminMixin, admin.ModelAdmin):
    list_display = ['task', 'employee', 'is_completed']


class TeamLeaderTaskAdmin(TeamLeaderAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'deadline', 'status', 'difficulty', 'department', 'employee', 'notifications_sent']


class TeamLeaderTaskAssignmentAdmin(TeamLeaderAdminMixin, admin.ModelAdmin):
    list_display = ['task', 'employee', 'is_completed']


class SonuserEmployeeAdmin(SonuserAdminMixin, admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'position', 'salary', 'login', 'email', 'password', 'department',
                    'rating', 'max_tasks_limit', 'is_blocked']


class SonuserEmployeeConfirmationAdmin(SonuserAdminMixin, admin.ModelAdmin):
    list_display = ['employee', 'is_confirmed']


app_models = apps.get_models()

for model in app_models:
    if model.__name__ == 'Task':
        admin_class = SonuserTaskAdmin if request.user.username == 'sonuser' else TeamLeaderTaskAdmin
    elif model.__name__ == 'Employee':
        admin_class = SonuserEmployeeAdmin if request.user.username == 'sonuser' else admin.ModelAdmin
    elif model.__name__ == 'TaskAssignment':
        admin_class = SonuserTaskAssignmentAdmin if request.user.username == 'sonuser' else admin.ModelAdmin
    elif model.__name__ == 'EmployeeConfirmation':
        admin_class = SonuserEmployeeConfirmationAdmin if request.user.username == 'sonuser' else admin.ModelAdmin
    else:
        admin_class = admin.ModelAdmin  # Другие модели обрабатываются базовым классом

    admin.site.register(model, admin_class)'''

