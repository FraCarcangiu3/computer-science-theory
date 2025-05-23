from fastapi import FastAPI
from routers import books

# === LIBRARY IMPORTS FOR THE FRONTEND ===
# HTMLResponse: Class that represents an HTTP response in HTML format
from fastapi.responses import HTMLResponse
# Jinja2Templates: Template system for generating dynamic HTML pages
from fastapi.templating import Jinja2Templates
# Request: Class that represents an HTTP request sent by the client
from fastapi import Request
# StaticFiles: For serving static files (CSS, JavaScript, images)
from fastapi.staticfiles import StaticFiles

# === APPLICATION CONFIGURATION ===
# Creating the main FastAPI application instance
app = FastAPI()
# Adding the router dedicated to book management
# The 'tags' parameter is used to group routes in the documentation
app.include_router(books.router, tags=["books"])

# === FRONT-END CONFIGURATION ===
# Configuring the Jinja2 template system, specifying the directory where the HTML files are located
templates = Jinja2Templates(directory="app/templates")

# Configuration to serve static files (CSS, JavaScript)
# This allows accessing files in the "app/static" directory through the "/static" URL
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Definition of the main route (homepage)
# The @app.get decorator specifies that this function responds to GET requests
# response_class=HTMLResponse indicates that we will return an HTML page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Renders the home.html template, passing the request object as a parameter
    # (necessary for Jinja2 to correctly generate links and forms)
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

# This block is executed only when the file is run directly
# (not when it is imported from another module)
if __name__ == "__main__":
    # Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server for Python applications
    import uvicorn
    # Starts the server with the FastAPI app
    # The reload=True parameter allows automatic reloading when files are modified
    # (useful during development)
    uvicorn.run(app, reload=True)