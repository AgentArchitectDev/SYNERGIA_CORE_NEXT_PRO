const API = "http://127.0.0.1:8000"

async function cargar() {

    const t = await fetch(API + "/templates")
    const templates = (await t.json()).templates

    const c = await fetch(API + "/clientes")
    const clientes = (await c.json()).clientes

    const templateSelect = document.getElementById("template")
    const clienteSelect = document.getElementById("cliente")

    templateSelect.innerHTML = templates.map(x => `<option>${x}</option>`).join("")
    clienteSelect.innerHTML = clientes.map(x => `<option>${x}</option>`).join("")
}

async function generar() {

    const template = document.getElementById("template").value

    const data = {
        brand_name: document.getElementById("brand_name").value,
        hero_title: document.getElementById("hero_title").value,
        hero_subtitle: document.getElementById("hero_subtitle").value
    }

    const res = await fetch(API + "/generate_cms", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            template: template,
            data: data
        })
    })

    const json = await res.json()

    if (json.status === "ok") {

        document.getElementById("status").innerText = "✔ Generado"

        document.getElementById("preview").src =
            `${API}/03_OUTPUT/${json.result.output_dir}/index.html?t=${Date.now()}`

    } else {
        document.getElementById("status").innerText = "❌ Error"
        console.log(json)
    }
}

cargar()
