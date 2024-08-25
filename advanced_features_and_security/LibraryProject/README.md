This is a djanog project with the name Library project that is running on development server

## Permissions and Groups Setup

This application uses Django's permissions and groups system to control access to the `Book` model.

### Custom Permissions:
- `can_view`: Allows viewing of book instances.
- `can_create`: Allows creation of book instances.
- `can_edit`: Allows editing of book instances.
- `can_delete`: Allows deletion of book instances.

### User Groups:
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Have full access, including deleting books.

### Enforcement in Views:
- Views are protected using the `permission_required` decorator to ensure only users with the correct permissions can access certain actions.

