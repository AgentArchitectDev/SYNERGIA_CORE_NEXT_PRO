# =========================================================
# SYNERGIA CORE NEXT PRO
# FASTAPI APPLICATION
# STAGE 6.3.15.7.6
# AI RUNTIME OBSERVABILITY API INTEGRATION
# =========================================================


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import os
import json



# =========================================================
# OBSERVABILITY ROUTER
# =========================================================


from backend.observability.routes import (
    router as observability_router
)



print(
    "[SYNERGIA FASTAPI APP LOADED]"
)



# =========================================================
# FASTAPI INSTANCE
# =========================================================


app = FastAPI(
    title="SYNERGIA CORE NEXT PRO",
    description="AI Business Operating System API",
    version="6.3.15.7.6"
)



# =========================================================
# CORS
# =========================================================


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "*"
    ],

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ]
)



# =========================================================
# OBSERVABILITY API LAYER
# =========================================================


for route in observability_router.routes:

    app.router.routes.append(
        route
    )



# =========================================================
# CMS STORAGE
# =========================================================


BASE = "projects"



# =========================================================
# GET PAGE
# =========================================================


@app.get(
    "/page/{project}/{page}"
)
def get_page(
    project,
    page
):


    path = (
        f"{BASE}/{project}/pages/{page}.json"
    )


    if not os.path.exists(path):

        return {

            "slug": page,

            "title": page,

            "blocks": []

        }



    with open(
        path,
        encoding="utf-8"
    ) as f:


        return json.load(f)




# =========================================================
# SAVE PAGE
# =========================================================


@app.post(
    "/page/save"
)
async def save_page(
    data: dict
):


    project = data["project"]

    page = data["page"]



    os.makedirs(
        f"{BASE}/{project}/pages",
        exist_ok=True
    )



    file = (
        f"{BASE}/{project}/pages/{page['slug']}.json"
    )



    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            page,
            f,
            indent=4,
            ensure_ascii=False
        )



    return {

        "status":
            "saved",

        "file":
            file

    }



# =========================================================
# ROOT HEALTH CHECK
# =========================================================


@app.get(
    "/"
)
def root():


    return {

        "system":
            "SYNERGIA CORE NEXT PRO",

        "stage":
            "6.3.15.7.6",

        "status":
            "running",

        "module":
            "AI RUNTIME OBSERVABILITY API"

    }
