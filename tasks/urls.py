from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit-profile'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Team URLs
    path('teams/', views.TeamListView.as_view(), name='team-list'),
    path('teams/create/', views.TeamCreateView.as_view(), name='team-create'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    
    # Project URLs
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    
    # Task URLs
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    
    # Task Assignment URLs
    path('tasks/<int:pk>/assign/', views.assign_task, name='assign-task'),
    path('assignments/<int:pk>/complete/', views.complete_assignment, name='complete-assignment'),
    
    # Comment URLs
    path('tasks/<int:task_pk>/comment/', views.add_comment, name='add-comment'),
]
