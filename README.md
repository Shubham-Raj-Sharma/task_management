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

### Task Features
- `Title` and `Description`: Clear task identification
- `Status`: To Do, In Progress, or Completed
- `Priority`: Low, Medium, High, or Urgent
- `Due Date`: Track task deadlines with overdue warnings (📅 **Interactive Date/Time Picker**)
- `Assignments`: Assign tasks to multiple team members
- `Comments`: Collaborative communication on tasks
- `Timestamps`: Track creation and modification times

### User Features
- Secure user authentication
- Team-based access control
- Task filtering by status, priority, and project
- Personal dashboard showing overview of tasks and projects
- Overdue task tracking
- Member profiles and statistics
- Password change functionality

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

## 🎨 Templates & UI

All templates extend from `base.html` which includes:
- Navigation header with user authentication status
- Responsive CSS styling (mobile-friendly)
- Status and priority badges with color coding
- Progress bars for project tracking
- Form components with validation
- Message alerts for user feedback

### 📅 Date & Time Picker
The task creation and update forms include an interactive date/time picker powered by **Flatpickr**:
- Click on the "Due Date" field to open the calendar picker
- Select date and time with an intuitive interface
- Minimum date is set to today (no backdating tasks)
- Time increment set to 15 minutes for convenient scheduling
- Supports both keyboard and mouse input
- Format: `YYYY-MM-DD HH:mm` (24-hour time)

**How to use:**
1. Navigate to [Create Task](http://127.0.0.1:8000/tasks/tasks/create/)
2. Fill in the task details
3. Click the "Due Date" field 
4. Select date from the calendar
5. Adjust time using the time picker
6. Click outside to confirm selection

Templates use Django template language with:
- Template inheritance
- Template tags and filters
- Form rendering with custom widgets
- CSRF protection
- JavaScript integration for enhanced UX

## 🔐 Security Features

- CSRF token protection on all forms
- User authentication required for all views
- Team-based access control
- Secure password handling
- Admin panel access control

## 💻 Views Overview

### Class-Based Views (CBV)
- `TeamListView`: List user's teams
- `TeamDetailView`: Display team details
- `TeamCreateView`: Create new team
- `ProjectListView`: List user's projects
- `ProjectDetailView`: Display project details
- `ProjectCreateView`: Create new project
- `ProjectUpdateView`: Update project
- `TaskListView`: List user's tasks with filtering
- `TaskDetailView`: Display task details
- `TaskCreateView`: Create new task
- `TaskUpdateView`: Update task
- `TaskDeleteView`: Delete task

### Function-Based Views (FBV)
- `dashboard()`: User overview dashboard
- `assign_task()`: Assign task to member
- `complete_assignment()`: Mark assignment complete
- `add_comment()`: Add comment to task

### Authentication Views
- `CustomLoginView`: User login with authentication
- `CustomLogoutView`: User logout with messages
- `RegisterView`: New user registration with password validation
- `UserProfileView`: Display user information and statistics
- `EditProfileView`: Edit profile information (first name, last name, email)
- `ChangePasswordView`: Secure password change functionality

## 🔐 Authentication System

The application includes a complete authentication system with the following features:

### Registration & Account Creation
- User registration with Django's built-in `UserCreationForm`
- Password strength validation (minimum 8 characters, not common passwords)
- Password confirmation
- Secure account creation

### Login & Authentication
- Secure login with username and password
- "Remember me" functionality (browser session management)
- Login required decorators on all task-related views
- Automatic redirection to login for unauthorized access

### User Profiles
- View account information (username, email, full name, registration date)
- **Edit profile information** (first name, last name, email address)
- Track user statistics (teams, projects, tasks assigned, tasks created)
- Email validation to prevent duplicates
- Secure password change functionality

### Security Features
- CSRF token protection on all forms
- Password hashing with Django's authentication system
- Session-based authentication
- Login URL setting: `LOGIN_URL = 'login'`
- Automatic redirect to dashboard after login
- Secure logout with session clearing

### Password Management
- Change password view with old password verification
- Password validation rules enforcement
- Secure password storage

## 🎓 Learning Outcomes

This project covers intermediate Django concepts:

1. **Models**
   - ForeignKey relationships
   - ManyToMany relationships
   - Model methods and properties
   - Meta options

2. **Views**
   - Class-based views (CRUD operations)
   - Function-based views
   - Mixins (LoginRequiredMixin)
   - QuerySet filtering and optimization

3. **Templates**
   - Template inheritance
   - Template tags and filters
   - Form rendering
   - Static file handling

4. **Forms**
   - ModelForm creation
   - Form validation
   - Dynamic form fields

5. **Admin Interface**
   - Custom admin displays
   - Admin filters and search
   - Inline editing

6. **Authentication & Authorization**
   - User authentication
   - Permission-based access control
   - Team-based authorization

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

## 🐛 Troubleshooting

### Migrations Failed
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Database Reset
```bash
# Remove db.sqlite3 and migrations (except __init__.py)
python manage.py migrate
```

## 📝 License

This is an educational project for learning intermediate Django development.

## 🤝 Contributing

This is a learning project. Suggestions for improvements are welcome!

---

**Happy Task Managing! 🎉**
