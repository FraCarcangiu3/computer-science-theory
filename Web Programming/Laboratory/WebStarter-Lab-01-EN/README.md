# Web Programming Laboratory - Online Library: Step by Step Guide

Welcome to the introductory Web Programming course! 📚 This comprehensive guide will teach you how to build an online library management application from scratch. The project is specifically designed for beginners who want to learn the basics of modern web development.

## Table of Contents

### Introduction
1. [Introduction and objectives](#introduction-and-objectives)
2. [Prerequisites](#prerequisites)
3. [Technologies used](#technologies-used)
4. [Project structure](#project-structure)

### Part 1: The Backend (Server)
5. [Back-end with FastAPI](#back-end-with-fastapi)
   - [Data models (Pydantic)](#data-models-appmodels)
   - [RESTful API](#api-approutersbookspy)
   - [Entry point](#entry-point-appmainpy)

### Part 2: The Frontend (Client)
6. [Front-end: HTML, CSS and JavaScript](#front-end-with-html-css-and-javascript)
   - [HTML: The structure](#html-apptemplateshomelhtml)
   - [CSS: The style](#css-appstaticcssfilecss)
   - [JavaScript: The behavior](#javascript-appstaticjsmainjs)
7. [Separation of concerns](#separation-of-concerns-a-best-practice)

### Part 3: Integration and Usage
8. [API and client-server communication](#api-and-client-server-communication)
9. [How to run the application](#how-to-run-the-application)
10. [Suggested exercises](#suggested-exercises)
11. [Common troubleshooting guide](#common-troubleshooting-guide)

## Introduction and objectives

This application is a practical example of a full-stack web application that manages a collection of books. It is designed as a teaching tool to learn the fundamental principles of web development.

### What you will learn:

- How to structure a modern web application
- How to create REST APIs with FastAPI
- How to connect a front-end to a back-end
- How to implement CRUD operations (Create, Read, Update, Delete)
- How to manage data and data validation
- How to create an interactive user interface

### Application features:

- 📝 View the list of books
- ➕ Add new books
- 🔄 Edit existing books
- 🗑️ Delete books
- ⭐ Add reviews to books (from 1 to 5 stars)
- 🔍 Sort books by rating

## Prerequisites

Before starting, make sure you have:

- **Python 3.7 or higher** installed
- **A code editor** (such as Visual Studio Code, PyCharm, or even a simple text editor)
- **Basic knowledge** of HTML, CSS and JavaScript
- **Basic familiarity** with programming concepts

Don't worry if you're not proficient in all these technologies: this guide is designed to explain each step clearly.

## Technologies used

In this project we use several technologies, divided between the server side (backend) and the client side (frontend).

### 🖥️ Back-end (server side)

- **Python**: A versatile and easy-to-learn programming language, popular for web development.
  - *Why we use it?* Python is easy to read and write, has a clear syntax and is perfect for beginners.

- **FastAPI**: A modern and fast framework for creating web APIs with Python.
  - *Why we use it?* FastAPI is easy to use, fast, and automatically includes API documentation.

- **Pydantic**: Library for data validation and model definition.
  - *Why we use it?* Pydantic ensures that data is in the correct format, reducing errors.

- **Uvicorn**: An ASGI (Asynchronous Server Gateway Interface) server for running the FastAPI application.
  - *Why we use it?* Uvicorn is fast and easy to configure to run our web application.

### 🎨 Front-end (client side)

- **HTML5**: The standard language for creating web pages.
  - *Why we use it?* HTML5 provides the basic structure for our user interface.

- **CSS3**: The language used to define the style and appearance of web pages.
  - *Why we use it?* CSS3 allows us to create an attractive and responsive user interface.

- **JavaScript**: The programming language to make web pages interactive.
  - *Why we use it?* JavaScript allows us to add interactivity and communicate with the server.

### 🔄 Application architecture

Our application follows the **client-server** architecture:
- The **server** (back-end) manages the data and provides APIs
- The **client** (front-end) displays the user interface and interacts with the user
- Communication between client and server occurs via **REST APIs**

#### What is a REST API?

REST API (Representational State Transfer) is an architecture for creating web services. Here are the key concepts:

1. **Resources**: In the API, a resource is anything we can access via a URL (in our case, the books).

2. **HTTP Methods**: We use different HTTP methods to operate on resources:
   - **GET**: To obtain data (e.g., retrieve the list of books)
   - **POST**: To create new data (e.g., add a new book)
   - **PUT**: To update existing data (e.g., modify a book)
   - **DELETE**: To delete data (e.g., remove a book)

3. **JSON Format**: Data is exchanged in JSON format (JavaScript Object Notation), a lightweight and easy-to-read format.

## Project structure

```
lab2025/
├── app/
│   ├── data/
│   │   └── books.py         # Example "database" with the books
│   ├── models/
│   │   ├── book.py          # Model for books
│   │   └── review.py        # Model for reviews
│   ├── routers/
│   │   └── books.py         # API definition
│   ├── static/              # Directory for static files
│   │   ├── css/
│   │   │   └── style.css    # Separate CSS styles
│   │   └── js/
│   │       └── main.js      # JavaScript script
│   ├── templates/
│   │   └── home.html        # User interface (HTML structure only)
│   ├── __init__.py
│   └── main.py              # Application entry point
└── README.md                # This guide
```

This structure follows a common pattern for web applications:

- **app/**: The main directory containing all the application code
  - **data/**: Contains the application data (in a real application, it might be replaced by a database)
  - **models/**: Defines the data structure used by the application
  - **routers/**: Contains the API logic and the application routes
  - **static/**: Contains static files (CSS, JavaScript, images)
    - **css/**: Contains CSS stylesheets
    - **js/**: Contains JavaScript scripts
  - **templates/**: Contains HTML files for the user interface
  - **main.py**: The application entry point that connects all components

This organization allows:
- Clearly separating the different code responsibilities
- Keeping the code clean and easy to navigate
- Facilitating maintenance and extension of the application
- Following the principle of separation of concerns (HTML for structure, CSS for style, JS for behavior)

## Back-end with FastAPI

In this section, we'll analyze how to build the "brain" of our application: the back-end. The back-end is the part of the software that runs on the server and manages the application logic, data access, and basic operations.

### Data models (app/models/)

Data models define the structure of our objects and ensure that data is valid. In Python, we use Pydantic for this purpose.

#### ✏️ Step 1: Define the Book model (app/models/book.py)
```python
from pydantic import BaseModel, Field
from typing import Annotated

class Book(BaseModel):
    id: int
    title: str
    author: str
    review: Annotated[int|None, Field(ge=1, le=5)] = None
```

This model represents a book with:
- `id`: unique numeric identifier
- `title`: book title
- `author`: book author
- `review`: optional review (from 1 to 5)

#### ✏️ Step 2: Define the Review model (app/models/review.py)
```python
from pydantic import BaseModel, Field
from typing import Annotated

class Review(BaseModel):
    review: Annotated[int | None, Field(ge=1, le=5)] = None
```

This model represents a review with a value from 1 to 5.

### Example data (app/data/books.py)

For simplicity, we use a Python dictionary as a "database" instead of a real database:

```python
from models.book import Book

books = {
    0: Book(id=0, title="book zero", author="author zero", review=1),
    1: Book(id=1, title="book one", author="author one", review=2),
    2: Book(id=2, title="book two", author="author two", review=5),
}
```

### API (app/routers/books.py)

APIs define the operations we can perform on our data. In this project, we have implemented a complete set of RESTful APIs for book management.

#### 📋 Complete guide to implemented APIs

| Operation | HTTP Method | Endpoint | Description | Usage Example |
|------------|-------------|----------|------------|-------------------|
| Get all books | GET | `/books` | Returns the list of all available books | `GET /books` |
| Get all books (sorted) | GET | `/books?sort=true` | Returns books sorted by rating | `GET /books?sort=true` |
| Get a specific book | GET | `/books/{id}` | Gets a specific book by its ID | `GET /books/1` |
| Add a new book | POST | `/books` | Creates a new book (requires book data in the request body) | `POST /books` with JSON: `{"id": 3, "title": "New book", "author": "Author"}` |
| Update a book | PUT | `/books/{id}` | Updates an existing book's data | `PUT /books/1` with JSON: `{"id": 1, "title": "Updated title", "author": "Author"}` |
| Delete a book | DELETE | `/books/{id}` | Deletes a specific book | `DELETE /books/1` |
| Delete all books | DELETE | `/books` | Deletes all books from the database | `DELETE /books` |
| Add a review | POST | `/books/{id}/review` | Adds a rating (1-5) to a specific book | `POST /books/1/review` with JSON: `{"review": 5}` |

#### Detailed API implementation

Here's how the APIs are implemented in the `books.py` file:

##### 1. Get all books

```python
@router.get("/")
def get_all_books(sort: bool = False) -> list[Book]:
    if sort:
        # Sort books by review if the sort parameter is true
        return sorted(books.values(), key=lambda book: book.review)
    
    # Otherwise, return all books without sorting
    return list(books.values())
```

This API:
- Accepts an optional `sort` parameter (default: `false`)
- If `sort=true`, sorts the books based on the review value
- Returns the list of books as a JSON array

##### 2. Get a specific book

```python
@router.get("/{id}")
def get_book_by_id(id: Annotated[int, Path(description="The ID of the book")]) -> Book:
    try:
        return books[id]
    except KeyError:
        # If the book doesn't exist, return a 404 error
        raise HTTPException(status_code=404, detail="Book not found")
```

This API:
- Requires an ID as a parameter in the URL path
- Searches for the book with the specified ID
- If the book is found, it returns it
- If the book doesn't exist, it returns a 404 error

##### 3. Add a review

```python
@router.post("/{id}/review")
def add_review(
    id: Annotated[int, Path(description="The ID of the book")],
    review: Review
):
    try:
        books[id].review = review.review
        return "Review added successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
```

This API:
- Requires an ID as a parameter in the URL path
- Accepts a Review object in the request body
- Updates the book's review with the specified ID
- Returns a success message or a 404 error if the book doesn't exist

##### 4. Add a new book

```python
@router.post("/")
def add_book(book: Book):
    if book.id in books:
        raise HTTPException(status_code=403, detail="Book ID already exists")
    books[book.id] = book
    return "Book added successfully"
```

This API:
- Accepts a Book object in the request body
- Checks if a book with the same ID already exists
- If the ID is already in use, it returns a 403 error
- Otherwise, it adds the book and returns a success message

##### 5. Update a book

```python
@router.put("/{id}")
def update_book(
    id: Annotated[int, Path(description="The ID of the book")],
    book: Book
):
    if not id in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[id] = book
    return "Book updated successfully"
```

This API:
- Requires an ID as a parameter in the URL path
- Accepts a Book object in the request body
- Checks if a book with the specified ID exists
- If the book exists, it updates it with the new data
- Otherwise, it returns a 404 error

##### 6. Delete all books

```python
@router.delete("/")
def delete_all_book():
    books.clear()
    return "All books deleted successfully"
```

This API:
- Deletes all books from the "database"
- Returns a confirmation message

##### 7. Delete a specific book

```python
@router.delete("/{id}")
def delete_book(id: Annotated[int, Path(description="The ID of the book")]):
    try:
        del books[id]
        return "Book deleted successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
```

This API:
- Requires an ID as a parameter in the URL path
- Searches for the book with the specified ID
- If the book is deleted, it returns a success message
- If the book doesn't exist, it returns a 404 error

### Entry point (app/main.py)

The file main.py is the application entry point, i.e., the file that gets executed to start the server.

#### ✏️ Step 1: Create the main.py file

```python
from fastapi import FastAPI
from routers import books
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(books.router, tags=["books"])

# Configuration to serve static files (CSS, JavaScript)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, reload=True)
```

#### 📝 Explanation of the code

This file:
1. Creates a FastAPI application
2. Integrates the book API router
3. **Configures the system to serve static files** (CSS and JavaScript)
4. Configures the Jinja2 templating system to serve the HTML page
5. Defines a route for the main page
6. Starts the server when the file is executed directly

The line `app.mount("/static", StaticFiles(directory="app/static"), name="static")` is crucial because it allows the system to serve static files from the `app/static` folder, making them accessible via the `/static` URL in the browser.

## Front-end with HTML, CSS and JavaScript

The frontend represents the part of the application that interacts directly with the user. In this section, we'll explore how to build an intuitive and reactive user interface using the three fundamental languages of the web.

### HTML (app/templates/home.html)

HTML (HyperText Markup Language) defines the structure and content of the web page.

#### ✏️ Step 1: Create the basic structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Library</title>
    
    <!-- Linking to external stylesheet -->
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Online Library</h1>
            <p class="subtitle">Library catalog management</p>
        </div>
    </header>

    <main class="container">
        <!-- Application content -->
        <!-- ... (book table, edit form, etc.) ... -->
    </main>

    <footer>
        <div class="container">
            <p>© 2025 Online Library - Project developed by Francesco Carcangiu</p>
        </div>
    </footer>

    <!-- Linking to external JavaScript file -->
    <script src="/static/js/main.js"></script>
</body>
</html>
```

#### 📝 Main elements

The HTML structure organizes the interface in:
- **Header**: Contains the application title
- **Main**: The main section that contains:
  - Table for displaying books
  - Form for adding/editing books
  - Form for adding reviews
- **Footer**: Contains copyright information

### CSS (app/static/css/style.css)

CSS (Cascading Style Sheets) defines the visual appearance of HTML elements.

#### ✏️ Step 1: Define variables and reset

```css
/* Definition of CSS variables */
:root {
    --blue-primary: #3498db;   /* Primary color for buttons and accents */
    --dark-blue: #2c3e50;        /* Secondary color for header and titles */
    --red: #e74c3c;            /* Color for dangerous actions (e.g., delete) */
    --text-color: #333;        /* Primary text color */
    --light-background: #f9f9f9;    /* Light background color of the page */
    --white: #ffffff;           /* White color for elements in foreground */
    --shadow: 0 2px 8px rgba(0, 0, 0, 0.1);  /* Shadow effect for elements */
    --border-radius: 8px;    /* Radius for rounded corners */
}

/* Reset default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

#### ✏️ Step 2: Define main styles

```css
/* Style of the body of the page */
body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--light-background);
    padding-bottom: 2rem;
}

/* Style of the header */
header {
    background-color: var(--dark-blue);
    color: var(--white);
    text-align: center;
    padding: 1.5rem 0;
    margin-bottom: 2rem;
    box-shadow: var(--shadow);
}
/* ... other styles ... */
```

#### 📝 Advantages of a separate CSS file

- **Greater readability**: the HTML code is cleaner and focused on structure
- **Maintainability**: it's easier to make changes to the appearance of the app
- **Caching**: browsers can cache the CSS file, improving performance
- **Reusability**: the same styles can be applied to multiple pages

### JavaScript (app/static/js/main.js)

JavaScript adds interactivity to the web page and communicates with the server.

#### ✏️ Step 1: Configure initial variables

```javascript
// API URLs
const API_URL = '/books';

// DOM elements
const sectionBooks = document.getElementById('section-books');
const sectionFormBook = document.getElementById('section-form-book');
const sectionFormReview = document.getElementById('section-form-review');
const bookList = document.getElementById('book-list');
// ... other variables ...

// Application state
let isModifying = false;
let currentOrder = false;
let selectedRating = 0;

// Load books on startup
document.addEventListener('DOMContentLoaded', () => {
    loadBooks();
    setEventHandlers();
});
```

#### ✏️ Step 2: Implement main functions

```javascript
// Function to load books from the server
async function loadBooks() {
    try {
        const response = await fetch(`${API_URL}?sort=${currentOrder}`);
        if (!response.ok) {
            throw new Error('Error loading books');
        }
        const books = await response.json();
        renderBooks(books);
    } catch (error) {
        showAlert(error.message, 'error');
    }
}

// ... other functions ...
```

#### 📝 Features implemented in JavaScript

1. **Data loading**: retrieves books from the server using fetch API
2. **DOM manipulation**: dynamically updates the user interface
3. **Event handling**: responds to user actions (clicks, form submissions)
4. **Server communication**: sends HTTP requests to the server
5. **Error handling**: shows alerts to the user when necessary

## Separation of concerns: A best practice

One of the best practices in web development is "separation of concerns" (Separation of Concerns, SoC). Let's explore what it is and why it's so important for your development as a programmer.

### �� What does it mean?

Separation of concerns is a design principle that consists of dividing an application into distinct parts, each responsible for a specific aspect:

1. **HTML** is responsible for structure and content 
2. **CSS** is responsible for visual appearance and style
3. **JavaScript** is responsible for behavior and interactivity

### 🌟 Advantages of this separation

#### 1. Better code organization
Each file has a clear and well-defined purpose, making it easier to navigate and understand the code.

#### 2. Improved maintainability
It's easier to make changes to one aspect (e.g., style) without affecting the others (structure or behavior).

#### 3. More efficient collaboration
Different team members can work on different parts of the application simultaneously with less conflicts.

#### 4. Code reusability
Styles and scripts can be easily reused in multiple pages.

#### 5. Better performance
Browsers can cache CSS and JavaScript files, reducing loading times for subsequent visits.

### ��️ Implementation in our project

In our project, we separated:

- **app/templates/home.html**: containing only the HTML structure of the page
- **app/static/css/style.css**: containing all style rules
- **app/static/js/main.js**: containing all logic and interactivity

To make this organization work, we configured FastAPI to serve static files with:

```python
app.mount("/static", StaticFiles(directory="app/static"), name="static")
```

And we added external file references in the HTML:

```html
<link rel="stylesheet" href="/static/css/style.css">
<script src="/static/js/main.js"></script>
```

### 📊 Comparison: Before and After

**Before**: all code (HTML, CSS, JavaScript) was in one file, making it difficult to maintain and understand.

**After**: each language has its dedicated file, making the code more organized, readable, and maintainable.

## API and client-server communication

A modern web application is composed of two parts that communicate with each other: the client (frontend) and the server (backend). Let's see how this communication works in our application.

### 🔄 Communication cycle

Here's how communication between the front-end and the back-end works:

1. **Request**: The user performs an action in the interface (e.g., clicking "Add Book")
2. **JavaScript** captures the event and prepares an HTTP request to the server
3. **Backend API** receives the request, processes it, and accesses the data
4. **Response**: The server responds with the requested data or a confirmation message
5. **UI update**: JavaScript receives the response and updates the user interface

### 📡 Examples of client-server communication

#### Example 1: Loading books

```javascript
// In the JavaScript (client)
async function loadBooks() {
    const response = await fetch('/books?sort=' + currentOrder);
    const books = await response.json();
    renderBooks(books);
}
```

```python
# In the Python (server)
@router.get("/")
def get_all_books(sort: bool = False) -> list[Book]:
    if sort:
        return sorted(books.values(), key=lambda book: book.review)
    return list(books.values())
```

#### Example 2: Adding a new book

```javascript
// In the JavaScript (client)
async function addBook(bookData) {
    const response = await fetch('/books', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bookData)
    });
    // Handling the response...
}
```

```python
# In the Python (server)
@router.post("/")
def add_book(book: Book):
    if book.id in books:
        raise HTTPException(status_code=403, detail="Book ID already exists")
    books[book.id] = book
    return "Book added successfully"
```

### 🔍 Debugging communication

When developing a web application, it's useful to know the tools for debugging client-server communication:

1. **Browser development tools** (F12): The "Network" tab shows all HTTP requests
2. **Browser console**: You can see JavaScript errors and server responses
3. **Server log**: Uvicorn shows server request and error logs

## How to run the application

This detailed guide will help you configure and run the application on your computer.

### System prerequisites

Before starting, make sure you have:

1. **Python 3.7 or higher** installed on your system.
   - To check if Python is installed and which version: `python --version` or `python3 --version`
   - If not installed, download it from [python.org](https://www.python.org/downloads/)

2. **pip** (Python package manager)
   - Generally comes with Python
   - To check: `pip --version` or `pip3 --version`

### Step 1: Clone or download the project

You have two options:

- **Option 1**: Clone the repository if you have Git installed:
  ```bash
  git clone https://github.com/tuousername/lab2025.git
  cd lab2025
  ```

- **Option 2**: Download the project as a ZIP file, extract it, and open the terminal in the extracted folder.

### Step 2: Create a virtual environment (recommended)

A virtual environment isolates project dependencies from system dependencies:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

Install required packages:

```bash
pip install fastapi uvicorn jinja2
```

Alternatively, if there's a `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
# From the project main directory
python -m app.main
```

You should see something like:

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Step 5: Open the application in the browser

Open your web browser and go to the address:
```
http://localhost:8000
```

You should see the Online Library interface with the list of books.

### Step 6: Explore the API documentation

FastAPI generates automatic interactive API documentation. You can access it by visiting:
```
http://localhost:8000/docs
```

This page allows you to:
- See all available APIs
- Read API documentation
- Test APIs directly from the browser

### Common troubleshooting

- **Port already in use error**: Another application is already using port 8000
  - Solution: Terminate the other application or modify the port in `main.py` by adding `port=8001` to `uvicorn.run()`

- **ModuleNotFoundError**: A module is not found
  - Solution: Verify that all dependencies are installed with `pip install fastapi uvicorn jinja2`
  
- **404 error when visiting a page**: The URL might be incorrect
  - Solution: Verify the URL or check server logs for any errors

- **The server starts but the interface doesn't load books**: There might be a problem with API calls
  - Solution: Open browser developer tools (F12) and check the console for any errors

## Suggested exercises

Here are some exercises to improve the application:

### 1. UI/UX improvements
   - Add a dark mode implementation by creating a separate CSS file
   - Improve mobile appearance by adding media queries to the CSS file
   - Add animations for transitions using CSS or JavaScript libraries

### 2. Modular JavaScript organization
   - Divide the `main.js` file into smaller and more specific modules (e.g., `api.js`, `ui.js`, `validation.js`)
   - Implement a more advanced state management system
   - Use JavaScript design patterns like the Module Pattern or the Revealing Module Pattern

### 3. Static file optimization
   - Implement file minification
   - Add file versioning to manage browser cache
   - Use a CSS preprocessor (like SASS or LESS) for better maintainability

### 4. Additional features
   - Add book search with dynamic result highlighting
   - Implement categories/genres for books
   - Add pagination for the book list

### 5. Style extension
   - Create a design system with CSS variables and reusable components
   - Implement different themes that the user can choose
   - Add more sophisticated hover and transition effects

### 6. Data persistence
   - Replace the in-memory "database" with SQLite
   - Add a more robust SQL database like PostgreSQL
   - Implement an ORM like SQLAlchemy

### 7. Authentication
   - Add a login system
   - Implement different roles (user, admin)
   - Limit certain operations to authenticated users

### 8. Accessibility improvements
   - Ensure the application is accessible following WCAG guidelines
   - Improve user label usage and semantic HTML structure
   - Implement keyboard navigation and screen reader support

Have fun with web programming!

---

This project was created for the Web Programming Laboratory 2025.

© 2025 - Project developed by Francesco Carcangiu
