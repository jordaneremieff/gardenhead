import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from gardenhead.resources import SpeciesResource
from gardenhead.models import Species


templates = Jinja2Templates(directory="templates")

app = Starlette(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.route("/")
async def home(request):
    q = request.query_params.get("q")
    context = {"request": request}
    if q:
        handle = SpeciesResource()
        results = await handle.search(q)
        records = [Species(record) for record in results["searchResults"]["results"]]
        context["search_query"] = q
        context["search_results"] = records
        context["record_count"] = results["searchResults"]["totalRecords"]

    return templates.TemplateResponse("index.html", context)
