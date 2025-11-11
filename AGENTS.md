# Agent Guidelines for matar-a-react

## Build/Lint/Test Commands

### Environment Setup
- Activate virtual environment: `source app/venv/bin/activate`
- Run commands from: `app/sheep_counter/` directory

### Testing
- Run all tests: `python manage.py test`
- Run single test: `python manage.py test counter.tests.TestClass.test_method`
- Run app tests: `python manage.py test counter`

### Linting & Code Quality
- Lint code: `ruff check app/sheep_counter/`
- Auto-fix issues: `ruff check app/sheep_counter/ --fix`
- Django checks: `python manage.py check`

### Database
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`

## Code Style Guidelines

### Python
- **Imports**: Django imports first, then third-party, then local
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Line length**: 88 characters (ruff default)
- **Formatting**: Follow PEP 8 standards
- **Linting**: Use ruff for consistency

### Django Patterns
- Use `get_object_or_404()` for model retrieval
- Follow standard Django URL patterns and view structure
- Use Django's F expressions for atomic updates
- Implement proper CSRF protection

### HTML/Templates
- Use Django template language with `{% load static %}`
- HTMX for dynamic interactions
- Inline styles for component-specific CSS
- Follow semantic HTML structure

### Error Handling
- Use Django's built-in error handling patterns
- Return appropriate HTTP status codes
- Use try/except blocks for external operations

### Security
- Always validate user input
- Use Django's CSRF protection
- Follow Django security best practices</content>
<parameter name="filePath">/home/ska/Projects/matar-a-react/AGENTS.md