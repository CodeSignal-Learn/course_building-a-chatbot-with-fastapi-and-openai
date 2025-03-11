from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from controllers.chat_controller import ChatController
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Add session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key="your_secret_key_here"
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Create controller instance
chat_controller = ChatController()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Ensure user has a session
    chat_controller.ensure_user_session(request.session)
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/api/create_chat")
async def create_chat(request: Request):
    return chat_controller.create_chat(request.session)

@app.post("/api/send_message")
async def send_message(request: Request):
    data = await request.json()
    return chat_controller.send_message(request.session, data)

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)