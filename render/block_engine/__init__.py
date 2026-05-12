import os
import json
from datetime import datetime


# =========================================================
# TEMPLATE RENDER
# =========================================================

def render_template_block(
    block
):

    block_type = block.get(
        "type",
        ""
    )

    template_name = block.get(
        "template",
        "modern_dark"
    )

    data = block.get(
        "data",
        {}
    )

    template_path = os.path.join(

        "render",
        "templates",
        block_type,
        f"{template_name}.html"
    )

    # =====================================================
    # TEMPLATE NO EXISTE
    # =====================================================

    if not os.path.exists(
        template_path
    ):

        return f"""
        <section style='padding:40px;background:#111;color:red;font-family:Arial'>
            TEMPLATE NOT FOUND:
            {template_path}
        </section>
        """

    # =====================================================
    # LEER TEMPLATE
    # =====================================================

    with open(
        template_path,
        "r",
        encoding="utf-8"
    ) as f:

        html = f.read()

    # =====================================================
    # REEMPLAZAR VARIABLES
    # =====================================================

    for key, value in data.items():

        html = html.replace(
            "{{" + key + "}}",
            str(value)
        )

    return html


# =========================================================
# GENERAR HTML BASE
# =========================================================

def build_html(
    blocks
):

    html = """
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>SYNERGIA SITE</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
background:#050505;
color:white;
font-family:Arial;
overflow-x:hidden;
}

</style>

</head>

<body>
"""

    # =====================================================
    # RENDER BLOCKS
    # =====================================================

    for block in blocks:

        html += render_template_block(
            block
        )

    html += """

</body>
</html>
"""

    return html


# =========================================================
# ENGINE
# =========================================================

class BlockEngine:


    # =====================================================
    # BUILD SIMPLE
    # =====================================================

    def build(
        self,
        project_name
    ):

        project_dir = os.path.join(
            "projects",
            project_name
        )

        page_file = os.path.join(
            project_dir,
            "page.json"
        )

        if not os.path.exists(
            page_file
        ):

            return {
                "status": "error",
                "detail": "No existe page.json"
            }

        with open(
            page_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        blocks = data.get(
            "blocks",
            []
        )

        html = build_html(
            blocks
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        output_dir = os.path.join(

            "storage",
            "output",
            f"{project_name}_{timestamp}"
        )

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        output_file = os.path.join(
            output_dir,
            "index.html"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)

        return {

            "status": "ok",

            "output_dir": output_dir,

            "file": output_file
        }


    # =====================================================
    # BUILD MULTI PAGE SITE
    # =====================================================

    def build_site(
        self,
        project_name
    ):

        project_dir = os.path.join(
            "projects",
            project_name
        )

        pages_dir = os.path.join(
            project_dir,
            "pages"
        )

        if not os.path.exists(
            pages_dir
        ):

            return {
                "status": "error",
                "detail": "No existe pages/"
            }

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        output_dir = os.path.join(

            "storage",
            "output",

            f"{project_name}_site_{timestamp}"
        )

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        generated_pages = []

        # =================================================
        # RECORRER PAGES
        # =================================================

        for filename in os.listdir(
            pages_dir
        ):

            if not filename.endswith(
                ".json"
            ):
                continue

            page_path = os.path.join(
                pages_dir,
                filename
            )

            with open(
                page_path,
                "r",
                encoding="utf-8"
            ) as f:

                page = json.load(f)

            blocks = page.get(
                "blocks",
                []
            )

            html = build_html(
                blocks
            )

            slug = filename.replace(
                ".json",
                ""
            )

            if slug == "home":

                html_name = "index.html"

            else:

                html_name = f"{slug}.html"

            output_file = os.path.join(
                output_dir,
                html_name
            )

            with open(
                output_file,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(html)

            generated_pages.append(
                html_name
            )

        return {

            "status": "ok",

            "mode": "multi_page_site",

            "project": project_name,

            "pages_generated": generated_pages,

            "output_dir": output_dir
        }


# =========================================================
# INSTANCE
# =========================================================

engine = BlockEngine()
