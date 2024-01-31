# Chibi URL
Chibi URL is a user-friendly and efficient URL Shortener service that simplifies the process of transforming long and complex URLs into shorter and more manageable links. With its robust technology stack including Django, Python, HTML, CSS, JavaScript, Bootstrap, and SQLite, Chibi URL offers a reliable and feature-rich solution.

## Visit the application
- [Chibi URL](https://chibiurl.azurewebsites.net/)

## Screenshots -- 
### Home View
![image](https://github.com/EGhost98/Chibi_URL/assets/76267623/c66332f5-b481-41ab-82fb-f35a86d2ea9e)

### MY URL's View
![image](https://github.com/EGhost98/Chibi_URL/assets/76267623/75d424d8-852e-4bf5-9d39-64095c7748cb)

### Login and Register View
![image](https://github.com/EGhost98/Chibi_URL/assets/76267623/eeb71e90-96b7-4e8e-960a-6da7ba83b7e7)
&nbsp;&nbsp;&nbsp;&nbsp;
![image](https://github.com/EGhost98/Chibi_URL/assets/76267623/03e4977a-5691-40c1-8376-dd35f883df09)

## How to Run the Project
To run the project, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd Chibi_URL`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the application: `python manage.py runserver`
5. Access the application in your web browser at: `http://localhost:8000`

Note: Make sure you have Python and Django installed on your system before running the project.
The application runs on the local development server when the script is executed directly.

## Tech Stack Used
Chibi URL is built using the following technologies:

- Python: A powerful programming language used for backend development.
- Django: Django is a high-level Python web framework for the rapid development of secure and scalable web applications.
- Bootstrap 5: A popular CSS framework for building responsive and stylish web interfaces.
- CSS: Cascading Style Sheets for customizing the application's appearance.
- SQLite: A lightweight and embedded database storing User Authentication data, URL, and Analytics (i.e., Times Clicked).
- JavaScript: JavaScript (JS) is a high-level programming language that enables dynamic and interactive behavior on web pages. Used to make a copy to clipboard button.
- Azure: Used for the deployment of the website.

## Project Structure
The project contains the following main files and directories:
- `backend/`:
  - `core/`: Contains the core files and configurations of the Django application.
    - `urls.py`: Defines the URL patterns and routes for the application, mapping them to the corresponding views and apps specific urls.py files.
    - `settings.py`: Configures the Django application settings, including database connection, installed apps, middleware, static files, templates, and other project-specific configurations.
  - `static/`: Directory containing static files such as CSS, JavaScript, and images.
  - `tinyurl/`: The main Django application directory.
    - `views.py`: Contains the view functions or class-based views that handle the requests and define the application's behavior. (Described Below)
    - `models.py`: Defines the database models using Django's ORM (Object-Relational Mapping).
    - `forms.py`: Contains the forms used in the application for data input and validation.
    - `utils.py`: Contains utility functions for generating random short URLs.
    - `admin.py`: Configures the Django admin interface for the URL Shortener application. Registers the Shortener model and customizes the admin site's appearance.
    - `urls.py`: Contains the URL patterns for mapping the views to the corresponding URLs.(Described Below)
    - `templates/tinyurl/`: Directory containing HTML templates for rendering the main Web pages (about.html, base.html, delete.html, home.html, myurls.html, and custom error pages)
  - `users/`: The user Authentication application directory.
    - `views.py`: Contains the view functions or class-based views that handle the requests and define the application's behavior. (Login and Register)
    - `urls.py`: Contains the URL patterns for mapping the views to the corresponding URLs. (Login, Logout and Register)
    - `templates/users/`: Directory containing HTML templates for rendering the login and register Web Pages.
  - `manage.py`: This is a command-line utility in Django for managing various aspects of the project, such as running development servers, managing database migrations, and executing administrative tasks.
- `README.md`: The project's readme file containing information about the application and instructions for running it.
- `requirements.txt`: Text file listing the Python dependencies required for the project.

## Models
The `Shortener` model in the `models.py` file represents a URL item in the Chibi URL application. It has the following fields:

- `user_name`: A foreign key relationship with the Django `User` model, representing the user who associated the URL.
- `created`: A DateTimeField that automatically records the date and time when the shortener was created.
- `times_followed`: A PositiveIntegerField that stores the number of times the short URL has been followed or clicked.
- `long_url`: A URLField that stores the original long URL.
- `short_url`: A CharField that stores the shortened URL generated for the long URL. It is unique and blank.
- `url_index`: A CharField that allows indexing a URL with a custom name. It is optional and can be left blank.

The `Shortener` model also includes a `Meta` class for defining the ordering of records based on the creation date and Indexes for Faster search Queries.

## Bootstrap and Enhanced UI
The Chibi URL application utilizes Bootstrap 5, a CSS framework, to enhance the user interface and provide a responsive and visually appealing design. The Bootstrap components, such as cards, forms, and navigation, are used to create a modern and user-friendly experience. The website is responsive and can work seamlessly on any device, ensuring a consistent and optimal user experience.

## JavaScript Copy to Clipboard Button
The application includes JavaScript functionality to implement a copy-to-clipboard button. This feature allows users to easily copy the shortened URL to their clipboard with a single click, making it convenient to share the shortened links.

## Flash Messages for Form Errors and Successful Login
Flash messages are used in the Chibi URL application to display form validation errors and successful user login notifications. When a form submission fails due to validation errors, the corresponding error messages are displayed to the user. Similarly, upon successful user login, a flash message is shown to indicate a successful login.


## Key Takeaways
- Building a URL shortener using Django and Python.
- Creating views and mapping them to URL patterns.
- Using Django's ORM to define and work with database models.
- Implementing user authentication and session management.
- Working with HTML templates and static files.
- Styling the application using Bootstrap and CSS.
- Implementing form validation and data processing.
- Handling redirects and custom error pages.
  

## References
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [SQLite Documentation](https://www.sqlite.org/index.html)
- [W3Schools](https://www.w3schools.com/)
- [Django User Authentication in 5 Minutes ](https://medium.com/swlh/django-user-authentication-in-5-minutes-4db08c5c459a)
- [ChatGPT by OpenAI](https://openai.com/)

