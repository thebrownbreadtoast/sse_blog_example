from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .pocketbase import create_job, get_job
from .utils import fetch_slow_api, HOST_ADDR


app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")


templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "host": HOST_ADDR})


@app.get("/start-job", response_class=RedirectResponse, status_code=302)
async def start_job(request: Request, background_tasks: BackgroundTasks):
    job_obj = create_job()

    if job_obj.get("id"):
        background_tasks.add_task(fetch_slow_api, job_obj["id"])

    return f"http://{HOST_ADDR}:8000/track-job/{job_obj['id']}"


@app.get("/track-job/{job_id}", response_class=HTMLResponse)
async def track_job(job_id, request: Request, background_tasks: BackgroundTasks):
    job_obj = get_job(job_id)

    return templates.TemplateResponse("job-tracker.html", {"request": request, "host": HOST_ADDR, **job_obj})
