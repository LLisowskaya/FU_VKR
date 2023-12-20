from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

'''from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task, Employee, TaskAssignment, EmployeeConfirmation
from .permissions import CanViewAllTables


class TaskDetailView(APIView):
    permission_classes = [CanViewAllTables]

    def get(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            serialized_task_data = {
                'title': task.title,
                'deadline': task.deadline,
                'status': task.status,
                'difficulty': task.difficulty,
                'department': task.department.name if task.department else None,
                'employee': f"{task.employee.surname} {task.employee.name}" if task.employee else None,
                'notifications_sent': task.notifications_sent,
            }
            return Response(serialized_task_data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Задача не найдена'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeDetailView(APIView):
    permission_classes = [CanViewAllTables]

    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(pk=employee_id)
            serialized_employee_data = {
                'surname': employee.surname,
                'name': employee.name,
                'patronymic': employee.patronymic,
                'position': employee.position,
                'salary': str(employee.salary),
                'login': employee.login,
                'email': employee.email,
                'password': employee.password,  # Не рекомендуется возвращать пароль в реальном приложении
                'department': employee.department.name if employee.department else None,
                'rating': employee.rating,
                'max_tasks_limit': employee.max_tasks_limit,
                'is_blocked': employee.is_blocked,
            }
            return Response(serialized_employee_data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'error': 'Сотрудник не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskAssignmentDetailView(APIView):
    permission_classes = [CanViewAllTables]

    def get(self, request, task_assignment_id):
        try:
            task_assignment = TaskAssignment.objects.get(pk=task_assignment_id)
            serialized_task_assignment_data = {
                'task': task_assignment.task.title if task_assignment.task else None,
                'employee': f"{task_assignment.employee.surname} {task_assignment.employee.name}" if task_assignment.employee else None,
                'is_completed': task_assignment.is_completed,
            }
            return Response(serialized_task_assignment_data, status=status.HTTP_200_OK)
        except TaskAssignment.DoesNotExist:
            return Response({'error': 'Назначение задачи не найдено'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeConfirmationDetailView(APIView):
    permission_classes = [CanViewAllTables]

    def get(self, request, employee_confirmation_id):
        try:
            employee_confirmation = EmployeeConfirmation.objects.get(pk=employee_confirmation_id)
            serialized_employee_confirmation_data = {
                'employee': f"{employee_confirmation.employee.surname} {employee_confirmation.employee.name}" if employee_confirmation.employee else None,
                'is_confirmed': employee_confirmation.is_confirmed,
            }
            return Response(serialized_employee_confirmation_data, status=status.HTTP_200_OK)
        except EmployeeConfirmation.DoesNotExist:
            return Response({'error': 'Подтверждение сотрудника не найдено'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
'''
