from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Team, Project, Task, TaskAssignment, Comment
from .forms import UserProfileForm


# Team Views
class TeamListView(LoginRequiredMixin, ListView):
    """Display all teams for the logged-in user."""
    model = Team
    template_name = 'tasks/team_list.html'
    context_object_name = 'teams'
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.teams.all()


class TeamDetailView(LoginRequiredMixin, DetailView):
    """Display team details and projects."""
    model = Team
    template_name = 'tasks/team_detail.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.object.projects.all()
        context['members'] = self.object.members.all()
        return context


class TeamCreateView(LoginRequiredMixin, CreateView):
    """Create a new team."""
    model = Team
    template_name = 'tasks/team_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('team-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


# Project Views
class ProjectListView(LoginRequiredMixin, ListView):
    """Display all projects for the user's teams."""
    model = Project
    template_name = 'tasks/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        user_teams = self.request.user.teams.all()
        return Project.objects.filter(team__in=user_teams)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    """Display project details with tasks and progress."""
    model = Project
    template_name = 'tasks/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['tasks'] = project.tasks.all()
        context['progress'] = project.get_progress()
        
        # Task statistics
        context['total_tasks'] = project.tasks.count()
        context['completed_tasks'] = project.tasks.filter(status='completed').count()
        context['in_progress_tasks'] = project.tasks.filter(status='in_progress').count()
        context['todo_tasks'] = project.tasks.filter(status='todo').count()
        
        # Overdue tasks
        context['overdue_tasks'] = [task for task in project.tasks.all() if task.is_overdue()]
        
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Create a new project."""
    model = Project
    template_name = 'tasks/project_form.html'
    fields = ['name', 'description', 'team']
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['team'].queryset = self.request.user.teams.all()
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing project."""
    model = Project
    template_name = 'tasks/project_form.html'
    fields = ['name', 'description']
    
    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'pk': self.object.pk})


# Task Views
class TaskListView(LoginRequiredMixin, ListView):
    """Display all tasks assigned to the user."""
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 20

    def get_queryset(self):
        queryset = Task.objects.filter(assignments__assigned_to=self.request.user).distinct()
        
        # Filter by status if provided
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by priority if provided
        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(priority=int(priority))
        
        # Filter by project if provided
        project_id = self.request.GET.get('project')
        if project_id:
            queryset = queryset.filter(project_id=int(project_id))
        
        return queryset.order_by('-priority', 'due_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_tasks_count'] = Task.objects.filter(assignments__assigned_to=self.request.user).count()
        context['overdue_tasks'] = Task.objects.filter(
            assignments__assigned_to=self.request.user,
            status__in=['todo', 'in_progress']
        ).exclude(due_date__isnull=True)
        context['projects'] = Project.objects.filter(team__members=self.request.user)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Display task details with comments and assignments."""
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['assignments'] = self.object.assignments.all()
        context['can_edit'] = self.object.created_by == self.request.user or \
                             self.request.user.teams.filter(id=self.object.project.team_id).exists()
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Create a new task."""
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'project', 'status', 'priority', 'due_date']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user_teams = self.request.user.teams.all()
        form.fields['project'].queryset = Project.objects.filter(team__in=user_teams)
        return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing task."""
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'status', 'priority', 'due_date']

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a task."""
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')


# Task Assignment Views
@login_required
def assign_task(request, pk):
    """Assign a task to a team member."""
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    team = project.team

    if request.method == 'POST':
        assigned_to_id = request.POST.get('assigned_to')
        user = get_object_or_404(User, pk=assigned_to_id)
        
        if user in team.members.all():
            TaskAssignment.objects.get_or_create(
                task=task,
                assigned_to=user,
                defaults={'assigned_by': request.user}
            )
    
    return redirect('task-detail', pk=pk)


@login_required
def complete_assignment(request, pk):
    """Mark a task assignment as complete."""
    assignment = get_object_or_404(TaskAssignment, pk=pk)
    
    if assignment.assigned_to == request.user or request.user == assignment.task.created_by:
        assignment.is_completed = True
        assignment.completed_at = datetime.now()
        assignment.save()
    
    return redirect('task-detail', pk=assignment.task.pk)


# Comment Views
@login_required
def add_comment(request, task_pk):
    """Add a comment to a task."""
    task = get_object_or_404(Task, pk=task_pk)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                task=task,
                author=request.user,
                content=content
            )
    
    return redirect('task-detail', pk=task_pk)


# Dashboard View
@login_required
def dashboard(request):
    """Display user's dashboard with overview of tasks and projects."""
    user_teams = request.user.teams.all()
    
    context = {
        'my_tasks': Task.objects.filter(assignments__assigned_to=request.user).distinct(),
        'overdue_tasks': Task.objects.filter(
            assignments__assigned_to=request.user,
            status__in=['todo', 'in_progress']
        ).exclude(due_date__isnull=True).filter(due_date__lt=datetime.now()),
        'in_progress_tasks': Task.objects.filter(
            assignments__assigned_to=request.user,
            status='in_progress'
        ),
        'my_projects': Project.objects.filter(team__in=user_teams),
        'my_teams': user_teams,
    }
    
    return render(request, 'tasks/dashboard.html', context)


# ============= AUTHENTICATION VIEWS =============

class CustomLoginView(LoginView):
    """Handle user login."""
    template_name = 'tasks/login.html'
    success_url = reverse_lazy('dashboard')
    authentication_form = AuthenticationForm

    def get_success_url(self):
        messages.success(self.request, f"Welcome back, {self.request.user.username}!")
        return super().get_success_url()


class CustomLogoutView(LogoutView):
    """Handle user logout."""
    template_name = 'tasks/logout.html'
    next_page = 'login'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully!")
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    """Handle user registration/signup."""
    form_class = UserCreationForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully! Please log in.")
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # Redirect to dashboard if user is already logged in
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, DetailView):
    """Display user profile."""
    model = User
    template_name = 'tasks/profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['my_tasks_count'] = Task.objects.filter(assignments__assigned_to=user).count()
        context['my_projects_count'] = Project.objects.filter(team__members=user).distinct().count()
        context['my_teams_count'] = user.teams.count()
        context['created_tasks_count'] = Task.objects.filter(created_by=user).count()
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    """Allow user to edit their profile information."""
    model = User
    form_class = UserProfileForm
    template_name = 'tasks/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Your profile has been updated successfully!")
        return super().form_valid(form)


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    """Handle password change."""
    template_name = 'tasks/change_password.html'
    success_url = reverse_lazy('profile')
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "Your password has been changed successfully!")
        return super().form_valid(form)
