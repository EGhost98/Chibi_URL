# Chibi URL
A URL shortener web application

## Visit the application 
- https://chibiurl.azurewebsites.net/

## Description
Chibi URL is a user-friendly and efficient URL Shortener service that simplifies the process of transforming long and complex URLs into shorter and more manageable links. With its robust technology stack including Django, Python, HTML, CSS, JavaScript, Bootstrap, and SQLite, Chibi URL offers a reliable and feature-rich solution.

## How to Run the Project
To run the project, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd Chibi_URL`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the application: `python manage.py runserver'
5. Access the application in your web browser at: `http://localhost:8000`

Note: Make sure you have Python and Django installed on your system before running the project.

## Tech Stack Used
ChibiURL is built using the following technologies:

- Python: A powerful programming language used for backend development.
- Django: Django is a high-level Python web framework for the rapid development of secure and scalable web applications.
- Bootstrap 5: A popular CSS framework for building responsive and stylish web interfaces.
- CSS: Cascading Style Sheets for customizing the application's appearance.
- SQLite: A lightweight and embedded database storing User Authentication data, URL and Analytics(i.e, Times Clicked)
- JavaScript: JavaScript (JS) is a high-level programming language that enables dynamic and interactive behavior on web pages. Used to Make a copy to clipboard Button.
- Azure: Used for the deployment of the website 

## The Working
- The application uses SQLite as the database to store URL data and user information.
- It utilizes the Flask framework, along with other packages like hashids for generating short aliases, Flask-Login for user authentication, and Werkzeug for password hashing.
- The application consists of several routes:
  - `/`: The main route where authenticated users can shorten URLs. It handles both GET and POST requests. When a POST request is received, it checks if the URL is already present in the database and updates it if necessary. If it's a new URL, it generates a short URL and saves it in the database.
  - `/register`: Handles user registration. It saves the username and hashed password in the database.
  - `/login`:  Handles user login. It compares the provided username and password with the stored values in the database, and if they match, logs the user in.
  - `/logout`: Logs out the currently authenticated user.
  - `/<alias>`: Redirects the user to the original URL associated with the provided alias.
  - `/stats`: Displays the statistics for the URLs created by the currently authenticated user.
  - `/search`: Allows users to search for URLs based on notes, original URLs, or aliases which the shorten before.
  - `/about`: Displays information about the application and its author.

- The application utilizes templates (index.html, register.html, login.html, stats.html, search.html, about.html) to render HTML pages with dynamic content.
- User authentication is handled using the User class, which extends the UserMixin class from Flask-Login. It provides methods for loading users from the database and managing user sessions.
- Flash messages are used to display notifications and error messages to the user.
- The application runs on the local development server when the script is executed directly.

## Key Takeaways
- Building a URL shortener using Python and Flask.
- Working with SQLite database for storing URL and user data.
- User authentication and session management using Flask-Login.
- Using Bootstrap and CSS for styling the web interface.
- Handling form submissions and data validation.
- Implementing search functionality to filter URLs based on keywords.

## References
- https://flask.palletsprojects.com/en/2.3.x/
- https://getbootstrap.com/docs/5.0/getting-started/introduction/
- https://www.sqlite.org/index.html
- https://www.w3schools.com/
- https://www.youtube.com/@CodeWithHarry
- https://chozinthet20602.medium.com/authentication-with-flask-login-5d504af3f517
