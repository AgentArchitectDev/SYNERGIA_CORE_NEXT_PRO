from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

BASE = "projects"


@app.get("/page/{project}/{page}")

def get_page(project, page):

    path = f"{BASE}/{project}/pages/{page}.json"

    if not os.path.exists(path):

        return {
            "slug": page,
            "title": page,
            "blocks": []
        }

    with open(path) as f:

        return json.load(f)


@app.post("/page/save")

async def save_page(data: dict):

    project = data["project"]

    page = data["page"]

    os.makedirs(
        f"{BASE}/{project}/pages",
        exist_ok=True
    )

    with open(
        f"{BASE}/{project}/pages/{page['slug']}.json",
        "w"
    ) as f:

        json.dump(page, f, indent=4)

    return {
        "status": "saved"
    }
