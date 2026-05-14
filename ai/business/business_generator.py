import os
import json
from datetime import datetime


class BusinessGenerator:
    """
    SYNERGIA BUSINESS ENGINE v1
    Genera negocios completos: CMS + branding + marketing + export
    """

    def __init__(self):
        self.output_base = "outputs/business"

    # =====================================================
    # MAIN ENTRY
    # =====================================================
    def generate(self, idea: str, mode="auto"):
        """
        mode:
        - auto (full AI)
        - assisted (human review)
        """

        analysis = self.analyze_idea(idea)
        brand = self.generate_brand(idea)
        cms = self.generate_cms(brand)
        social = self.generate_social(brand)
        marketing = self.generate_marketing(brand)

        package = {
            "idea": idea,
            "mode": mode,
            "analysis": analysis,
            "brand": brand,
            "cms": cms,
            "social": social,
            "marketing": marketing,
            "created_at": datetime.now().isoformat()
        }

        path = self.export(package)

        return package, path

    # =====================================================
    # 1. ANALYSIS ENGINE
    # =====================================================
    def analyze_idea(self, idea):
        idea = idea.lower()

        if "pizza" in idea or "comida" in idea:
            business = "food"
        elif "software" in idea or "saas" in idea:
            business = "saas"
        else:
            business = "service"

        return {
            "business_type": business,
            "complexity": "medium",
            "target": "general public"
        }

    # =====================================================
    # 2. BRAND ENGINE
    # =====================================================
    def generate_brand(self, idea):
        name = "Synergia " + idea.split(" ")[0].capitalize()

        return {
            "name": name,
            "colors": ["#ff0033", "#111111", "#ffffff"],
            "style": "modern minimal tech",
            "logo_prompt": f"modern logo for {idea}, clean, futuristic"
        }

    # =====================================================
    # 3. CMS ENGINE (BÁSICO REAL)
    # =====================================================
    def generate_cms(self, brand):

        html = f"""
        <html>
        <head>
            <title>{brand['name']}</title>
        </head>
        <body style="font-family:Arial;background:#111;color:white;">
            <h1>{brand['name']}</h1>
            <p>Bienvenido a {brand['name']} generado por SYNERGIA</p>

            <h2>Productos</h2>
            <ul>
                <li>Producto 1</li>
                <li>Producto 2</li>
                <li>Producto 3</li>
            </ul>

            <button>Comprar ahora</button>
        </body>
        </html>
        """

        return {
            "index.html": html
        }

    # =====================================================
    # 4. SOCIAL ENGINE
    # =====================================================
    def generate_social(self, brand):

        return {
            "instagram_posts": [
                f"Descubrí {brand['name']} 🚀",
                f"Nuevo concepto digital creado con IA",
                f"Automatización total de negocios"
            ],
            "hashtags": [
                "#IA", "#negocios", "#automatizacion", "#synergia"
            ],
            "reels_scripts": [
                "Transformamos una idea en negocio en segundos",
                "IA generando empresas automáticamente"
            ]
        }

    # =====================================================
    # 5. MARKETING ENGINE
    # =====================================================
    def generate_marketing(self, brand):

        return {
            "seo_keywords": [
                brand["name"].lower(),
                "negocio con ia",
                "crear web automática"
            ],
            "ads_copy": [
                f"Crea tu negocio con {brand['name']} en minutos",
                "IA que construye empresas completas"
            ]
        }

    # =====================================================
    # 6. EXPORT ENGINE
    # =====================================================
    def export(self, package):

        name = package["brand"]["name"].replace(" ", "_")
        path = os.path.join(self.output_base, name)

        os.makedirs(path, exist_ok=True)

        # save json full
        with open(os.path.join(path, "business.json"), "w") as f:
            json.dump(package, f, indent=2)

        # save cms
        cms_path = os.path.join(path, "cms")
        os.makedirs(cms_path, exist_ok=True)

        for file, content in package["cms"].items():
            with open(os.path.join(cms_path, file), "w") as f:
                f.write(content)

        # social
        with open(os.path.join(path, "social.json"), "w") as f:
            json.dump(package["social"], f, indent=2)

        return path
