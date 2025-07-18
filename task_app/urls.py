# task_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler403
from task_app import views as app_views

handler403 = app_views.custom_403_view

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),                        # Home Page for Dept. Managers
    path('assigned_to_me/', views.assigned_to_me, name='assigned_to_me'),  # Tickets assigned to the user
    path('assigned_by_me/', views.assigned_by_me, name='assigned_by_me'),  # Tickets assigned by the user
    path('user_profile/', views.user_profile, name='user_profile'),        # User Profile page
    path('reassign/<str:task_id>/', views.reassign_task, name='reassign_task'),
    # Existing paths
    path('create/', views.create_task, name='create_task'),
    path('edit/<str:task_id>/', views.edit_task, name='edit_task'),
    path('detail/<str:task_id>/', views.task_detail, name='task_detail'),
    path('update_status/<str:task_id>/', views.update_task_status, name='update_task_status'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('system_logs/', views.view_system_logs, name='view_system_logs'),
    path('activity/', views.activity, name='activity'),     # Activity page for Task Management System Managers
    path('metrics/', views.metrics, name='metrics'),
    path('metrics/download/', views.download_metrics, name='download_metrics'),
    path('download_activity_log/', views.download_activity_log, name='download_activity_log'),  # New URL for download
    path('reassign_within_department/<str:task_id>/', views.reassign_within_department, name='reassign_within_department'),
    path('test_deadline_reminders/', views.send_deadline_reminders, name='test_deadline_reminders'),
    path('test_overdue_notifications/', views.notify_overdue_tasks, name='test_overdue_notifications'),
    path('task/<str:task_id>/note/', views.task_note_page, name='task_note_page'),
    path('metrics/<str:department>/', views.department_metrics, name='department_metrics'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('users/', views.general_manage_users, name='general_manage_users'),

]
