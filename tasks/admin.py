from django.contrib import admin
from .models import Team, Project, Task, TaskAssignment, Comment


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'member_count', 'created_at')
    list_filter = ('created_at', 'owner')
    search_fields = ('name', 'description')
    filter_horizontal = ('members',)

    def member_count(self, obj):
        return obj.members.count()
    member_count.short_description = 'Members'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'owner', 'progress', 'created_at')
    list_filter = ('team', 'owner', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

    def progress(self, obj):
        return f"{obj.get_progress()}%"
    progress.short_description = 'Progress'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'due_date', 'is_overdue_status')
    list_filter = ('status', 'priority', 'project', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'project', 'created_by')
        }),
        ('Task Details', {
            'fields': ('status', 'priority', 'due_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def is_overdue_status(self, obj):
        return "⚠️ Overdue" if obj.is_overdue() else "On Time"
    is_overdue_status.short_description = 'Status'


@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ('task', 'assigned_to', 'assigned_by', 'is_completed', 'assigned_at')
    list_filter = ('is_completed', 'assigned_at')
    search_fields = ('task__title', 'assigned_to__username')
    readonly_fields = ('assigned_at', 'completed_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('task__title', 'author__username', 'content')
    readonly_fields = ('created_at', 'updated_at')
