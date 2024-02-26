### Welcome to the Book Sharing Platform! 
This web application allows users to share their books with others, create wishlists of books they want to acquire, and facilitate the exchange of books among users. The platform is built using Django, a high-level Python web framework, and Django REST Framework for building RESTful APIs.

### Table of Contents
- Introduction
- Features
- Project Structure
- Setup
- API Endpoints
- Permissions
- Filters
- Authentication
- Deployment

### Introduction
Book Sharing Platform aims to promote the sharing economy concept by providing a platform where users can share their books with others. Whether you're looking to declutter your bookshelf, discover new reads, or simply share your favorite books with like-minded individuals, this platform has you covered.

### Features
- User Registration and Authentication: Users can register for an account with a unique username, email, and password. Token-based authentication ensures secure access to the platform's features.
- Role-based Access Control: The platform supports different user roles, including administrators, owners, and regular users. Each role has specific permissions, such as managing books, wishlists, and user accounts.
- Book Listing and Management: Users can list their books on the platform, providing details such as title, author, genre, and condition. They can also manage their listings, update book information, and mark books as available or unavailable for exchange.
- Wishlist Creation and Management: Users can create wishlists of books they want to acquire. They can add books to their wishlists, submit requests for specific books, and track the status of their requests.
- Search and Filtering: The platform offers advanced search and filtering capabilities, allowing users to find books based on various criteria, such as title, author, genre, and condition.
- Secure Transactions: All interactions on the platform, including user authentication, data exchange, and transaction processing, are conducted over secure HTTPS connections to protect user privacy and sensitive information.
- Customizable Profiles: Users can customize their profiles with personal information, preferences, and profile pictures. They can also view other users' profiles to discover shared interests and book recommendations.

### Project Structure
The project follows a typical Django project structure, with the following main components:
- books/: Django app containing models, serializers, views, and permissions related to books and wishlists.
- filters.py: Custom filters for filtering book objects based on different criteria.
- permissions.py: Custom permission classes defining access control rules for API endpoints.
- backends.py: Custom authentication backend for authenticating users against the custom user model.
- serializers.py: Serializers for converting model instances to JSON representations and vice versa.
- views.py: Viewsets and API views for handling HTTP requests and responses.
- urls.py: URL patterns for routing requests to the appropriate views.
- settings.py: Django settings including database configuration, installed apps, and authentication settings.
- manage.py: Django's command-line utility for administrative tasks.
- requirements.txt: List of Python dependencies required for the project.
- README.md: This file, providing an overview of the project and instructions for setup and usage.

### Setup
To set up the project locally, follow these steps:
- Clone the repository: git clone <repository-url>
- Navigate to the project directory: cd <project-folder>
- Install dependencies: pip install -r requirements.txt
- Apply migrations: python manage.py migrate
- Create a superuser: python manage.py createsuperuser
- Run the development server: python manage.py runserver
- Access the admin interface at http://localhost:8000/admin to add books, users, etc.

### API Endpoints
The API endpoints exposed by the application include:

- /api/books/: CRUD operations for managing books.
- /api/wishlists/: CRUD operations for managing wishlists.
- /api/registration/: User registration endpoint.
- /api/login/: User login endpoint.
- /api/logout/: User logout endpoint.
Refer to the API documentation or viewsets in views.py for more details on available endpoints and their usage.

### Permissions
Custom permission classes are defined in permissions.py to control access to different parts of the system. Permissions are based on user roles and ownership of resources such as books and wishlists.

### Filters
Custom filters are implemented in filters.py to enable search and filtering of book objects based on various criteria such as author, genre, and condition.

### Authentication
Token-based authentication is implemented using Django REST Framework's token authentication mechanism. Users can obtain a token by logging in and use it to authenticate subsequent requests to protected endpoints.

### Deployment
For deployment, make sure to configure the appropriate settings for your production environment, including database settings, security settings, and environment variables. Consider using a platform-as-a-service (PaaS) provider such as Heroku or AWS Elastic Beanstalk for easy deployment and scalability.

Feel free to explore and modify the script according to your needs. This project was created by Mariam Kalmakhelidze, Luka Megrelishvili and Sandro Tsulaia.

