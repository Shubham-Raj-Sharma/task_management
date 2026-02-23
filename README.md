# Task Management/Todo App - Intermediate Django Project

A comprehensive team-based task management and collaboration application built with Django. This project demonstrates intermediate Django concepts including models, views, templates, user authentication, and team collaboration features.

## 🎯 Features

### Authentication & User Management
- **User Registration**: Create new accounts with secure password validation
- **Login/Logout**: Secure authentication system
- **User Profiles**: View account information and user statistics
- **Password Management**: Change password functionality
- **Team-based Access Control**: Secure access to teams and projects

### Core Features
- **Team Management**: Create teams and manage team members
- **Projects**: Multiple projects per team with progress tracking
- **Task Management**: Create, assign, and track tasks with priorities and due dates
- **Task Assignment**: Assign tasks to team members with completion tracking
- **Comments**: Real-time collaboration through task comments
- **Progress Tracking**: Visual progress indicators for projects and overall team productivity

## Getting Started

### Prerequisites
- Python 3.8+
- Django 6.0+

### Installation

1. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main app: `http://localhost:8000/tasks/`
   - Admin panel: `http://localhost:8000/admin/`

## 📋 URL Routes

### Authentication Routes
- `/tasks/login/` - Login page
- `/tasks/register/` - User registration/signup
- `/tasks/logout/` - Logout (redirects to login)
- `/tasks/profile/` - User profile and statistics
- `/tasks/profile/edit/` - Edit profile information (first name, last name, email)
- `/tasks/change-password/` - Change password

### Dashboard & Main Routes
- `/tasks/` - Main dashboard
- `/tasks/teams/` - Teams list
- `/tasks/projects/` - Projects list
- `/tasks/tasks/` - My tasks

### Team Routes
- `/tasks/teams/` - List all teams
- `/tasks/teams/create/` - Create new team
- `/tasks/teams/<id>/` - Team details

### Project Routes
- `/tasks/projects/` - List all projects
- `/tasks/projects/create/` - Create new project
- `/tasks/projects/<id>/` - Project details
- `/tasks/projects/<id>/update/` - Update project

### Task Routes
- `/tasks/tasks/` - List all tasks
- `/tasks/tasks/create/` - Create new task
- `/tasks/tasks/<id>/` - Task details
- `/tasks/tasks/<id>/update/` - Update task
- `/tasks/tasks/<id>/delete/` - Delete task
- `/tasks/tasks/<id>/assign/` - Assign task
- `/tasks/assignments/<id>/complete/` - Mark assignment complete

### Comment Routes
- `/tasks/tasks/<id>/comment/` - Add comment to task



## � Tech Stack

### Backend
- **Django 6.0.2** - Web framework
- **Python 3.8+** - Programming language
- **SQLite** - Database (default)

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling with responsive design
- **JavaScript (Vanilla)** - Client-side interactivity
- **Flatpickr 4.6.13** - Date/Time picker library via CDN

### Form Handling
- Django's built-in forms
- ModelForms for database-backed forms
- Custom authentication forms (UserCreationForm, AuthenticationForm, PasswordChangeForm)

### External Libraries (via CDN)
- **Flatpickr** (https://flatpickr.js.org/) - Lightweight date/time picker
  - No dependencies
  - Lightweight (~6KB gzipped)
  - Supports date, time, and datetime selection
  - Mobile-friendly interface

## �🚀 Future Enhancements

### Phase 2 - Advanced Features
1. **Real-time Notifications**
   - Task assignment notifications
   - Comment notifications
   - Due date reminders
   - Channels integration for WebSocket support

2. **Advanced Collaboration**
   - File attachments on tasks
   - Task templates
   - Recurring tasks
   - Task history/audit log

3. **Reporting & Analytics**
   - Team productivity reports
   - Task completion metrics
   - Member performance tracking
   - Dashboard widgets

4. **Team Management**
   - Role-based access (Admin, Member, Observer)
   - Team invitations via email
   - Member management interface
   - Activity feed

5. **API Development**
   - REST API with Django REST Framework
   - Mobile app integration
   - Third-party integrations

6. **UI/UX Improvements**
   - Drag-and-drop task board (Kanban)
   - Calendar view for due dates
   - Gantt chart for project timeline
   - Export reports (PDF, Excel)

7. **Performance Optimization**
   - Caching with Redis
   - Database query optimization
   - Pagination for large datasets
   - Celery for async tasks

## 🔧 Common Operations

### Create a Team
1. Navigate to Teams → Create New Team
2. Enter team name and description
3. Click "Create Team"

### Create a Project
1. Go to Projects → Create New Project
2. Select team, enter name and description
3. Click "Create Project"

### Create a Task
1. Click "Create Task"
2. Fill in title, description, project, status, and priority
3. Optionally set due date
4. Click "Create Task"

### Assign a Task
1. Open task details
2. Select team member from dropdown
3. Click "Assign"

### Track Progress
1. View project details to see overall progress
2. Check dashboard for task overview
3. Filter tasks by status to track work

## 📊 Example Data Setup

After running migrations, you can:
1. Create a superuser account
2. Log in to admin panel (`/admin/`)
3. Create sample teams and projects
4. Invite team members
5. Create tasks for testing

## 📝 License

This is an educational project for learning intermediate Django development.

## 🤝 Contributing

This is a learning project. Suggestions for improvements are welcome!

---

**Happy Task Managing! 🎉**
