''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Necessary Imports
from fastapi import FastAPI, Request, Response    # The main FastAPI import and Request/Response objects
from fastapi.responses import RedirectResponse    # Used to redirect to another route
# from pydantic import BaseModel                    # Used to define the model matching the DB Schema
from fastapi.responses import HTMLResponse        # Used for returning HTML responses (JSON is default)
from fastapi.templating import Jinja2Templates    # Used for generating HTML from templatized files
from fastapi.staticfiles import StaticFiles       # Used for making static resources available to server
import uvicorn                                    # Used for running the app directly through Python
# import dbutils as db                             # Import helper module of database functions!

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Configuration
app = FastAPI()                                     # Specify the "app" that will run the routing
views = Jinja2Templates(directory='views')          # Specify where the HTML files are located
static_files = StaticFiles(directory='public')      # Specify where the static files are located
static_pictures = StaticFiles(directory='pictures') # Specify where the picture files are located
css_files = StaticFiles(directory='css')            # Specify where the css files are located

# Mount the static directory
app.mount('/public', static_files, name='public') # Mount the static files directory to /public for javascripts
app.mount('/pictures', static_pictures, name='pictures') # Mount the static files directory to /pictures for pictures
app.mount('/css', css_files, name='css') # Mount the static files directory to /css for css style to make things pretty


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# This is the homepage --- '/' same for html
@app.get('/', response_class=HTMLResponse)
def get_home(request:Request) -> HTMLResponse:
  with open("views/homepage.html") as html:
    return HTMLResponse(content=html.read())
  
# This is the team page --- '/teams' same for html
@app.get('/teams', response_class=HTMLResponse)
def get_teams(request:Request) -> HTMLResponse:
  with open("views/teammates.html") as html:
    return HTMLResponse(content=html.read())
  
# This is the milestone and timelines --- '/milestonesAndTimelines' same for html
@app.get('/milestonesAndTimelines', response_class=HTMLResponse)
def get_milestonesAndTimelines(request:Request) -> HTMLResponse:
  with open("views/milestonesAndTimelines.html") as html:
    return HTMLResponse(content=html.read())
  
# This is the favorites page --- '/favorites' same for html
@app.get('/favorites', response_class=HTMLResponse)
def get_favorites(request: Request) -> HTMLResponse:
  with open("views/favorites.html") as html:
    return HTMLResponse(content=html.read())

# This is the schematics page --- '/schematics' same for html
@app.get('/schematics', response_class=HTMLResponse)
def get_schematics(request: Request) -> HTMLResponse:
  with open("views/schematics.html") as html:
    return HTMLResponse(content=html.read())
  
# This is the video demo page --- '/video' same for html
@app.get('/video', response_class=HTMLResponse)
def get_video(request: Request) -> HTMLResponse:
  with open("views/video.html") as html:
    return HTMLResponse(content=html.read())
  
# This is the poster page --- '/poster' same for html
@app.get('/poster', response_class=HTMLResponse)
def get_poster(request: Request) -> HTMLResponse:
  with open("views/poster.html") as html:
    return HTMLResponse(content=html.read())
  
# This is the mini projects page --- '/miniProjects' same for html
@app.get('/miniProjects', response_class=HTMLResponse)
def get_miniProjects(request: Request) -> HTMLResponse:
  with open("views/miniProjects.html") as html:
    return HTMLResponse(content=html.read())
  
# This is the resources page --- '/resources' same for html
@app.get('/resources', response_class=HTMLResponse)
def get_miniProjects(request: Request) -> HTMLResponse:
  with open("views/resources.html") as html:
    return HTMLResponse(content=html.read())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=6543)
