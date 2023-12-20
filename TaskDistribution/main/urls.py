from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('employee/<int:employee_id>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('task-assignment/<int:task_assignment_id>/', views.TaskAssignmentDetailView.as_view(), name='task-assignment-detail'),
    path('employee-confirmation/<int:employee_confirmation_id>/', views.EmployeeConfirmationDetailView.as_view(), name='employee-confirmation-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)'''