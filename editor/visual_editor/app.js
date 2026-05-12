const API = "http://127.0.0.1:8000";

let PAGE = {
    slug: "home",
    title: "Inicio",
    blocks: []
};

async function loadPage() {

    const response = await fetch(
        API + "/page/demo_site/home"
    );

    PAGE = await response.json();

    renderEditor();

    renderPreview();
}

function renderEditor() {

    const editor = document.getElementById("editor");

    editor.innerHTML = "";

    PAGE.blocks.forEach((block, index) => {

        const div = document.createElement("div");

        div.className = "block-item";

        div.draggable = true;

        div.dataset.index = index;

        div.innerHTML = `
            <div class="block-header">

                <strong>
                    ${block.type}
                </strong>

                <div>

                    <button onclick="moveUp(${index})">
                        ↑
                    </button>

                    <button onclick="moveDown(${index})">
                        ↓
                    </button>

                    <button onclick="removeBlock(${index})">
                        X
                    </button>

                </div>

            </div>

            <div class="visual-fields">

                ${generateFields(block, index)}

            </div>

        `;

        div.addEventListener(
            "dragstart",
            dragStart
        );

        div.addEventListener(
            "dragover",
            dragOver
        );

        div.addEventListener(
            "drop",
            dropBlock
        );

        editor.appendChild(div);
    });
}

function generateFields(block, index) {

    let html = "";

    Object.keys(block.data).forEach((key) => {

        html += `
            <label>
                ${key}
            </label>

            <input
                type="text"
                value="${block.data[key]}"
                onchange="
                    updateField(
                        ${index},
                        '${key}',
                        this.value
                    )
                "
            />
        `;
    });

    html += `

        <hr>

        <label>
            background
        </label>

        <input
            type="color"
            value="#000000"
            onchange="
                updateStyle(
                    ${index},
                    'background',
                    this.value
                )
            "
        />

        <label>
            text color
        </label>

        <input
            type="color"
            value="#ffffff"
            onchange="
                updateStyle(
                    ${index},
                    'color',
                    this.value
                )
            "
        />

        <label>
            padding
        </label>

        <input
            type="range"
            min="0"
            max="200"
            value="50"
            onchange="
                updateStyle(
                    ${index},
                    'padding',
                    this.value + 'px'
                )
            "
        />

        <label>
            margin
        </label>

        <input
            type="range"
            min="0"
            max="200"
            value="0"
            onchange="
                updateStyle(
                    ${index},
                    'margin',
                    this.value + 'px'
                )
            "
        />

        <label>
            font size
        </label>

        <input
            type="range"
            min="10"
            max="100"
            value="18"
            onchange="
                updateStyle(
                    ${index},
                    'fontSize',
                    this.value + 'px'
                )
            "
        />
    `;

    return html;
}

function updateField(
    index,
    field,
    value
) {

    PAGE.blocks[index]
        .data[field] = value;

    renderPreview();
}

function updateStyle(
    index,
    prop,
    value
) {

    if(
        !PAGE.blocks[index].style
    ) {
        PAGE.blocks[index].style = {};
    }

    PAGE.blocks[index]
        .style[prop] = value;

    renderPreview();
}

function renderPreview() {

    const preview =
        document.getElementById(
            "preview"
        );

    let html = "";

    PAGE.blocks.forEach((block) => {

        let tpl =
            BLOCKS[block.type];

        if(!tpl) return;

        Object.keys(block.data)
            .forEach((key) => {

                tpl = tpl.replaceAll(
                    "{{" + key + "}}",
                    block.data[key]
                );
            });

        let style = "";

        if(block.style) {

            Object.keys(block.style)
                .forEach((k) => {

                    style += `
                        ${k}:${block.style[k]};
                    `;
                });
        }

        tpl = `
            <div style="${style}">
                ${tpl}
            </div>
        `;

        html += tpl;
    });

    preview.srcdoc = html;
}

function addBlock(type) {

    const defaults = {

        hero: {
            title: "SYNERGIA CMS",
            subtitle:
                "Visual AI Builder",
            button: "Comenzar"
        },

        navbar: {
            logo: "SYNERGIA"
        },

        cards: {
            title: "Servicio"
        },

        footer: {
            copyright:
                "GAB 2026"
        }
    };

    PAGE.blocks.push({
        type,
        data: defaults[type]
    });

    renderEditor();

    renderPreview();
}

function removeBlock(index) {

    PAGE.blocks.splice(index, 1);

    renderEditor();

    renderPreview();
}

async function savePage() {

    await fetch(
        API + "/page/save",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                project: "demo_site",
                page: "home",
                data: PAGE
            })
        }
    );

    alert("guardado");
}

let DRAG_INDEX = null;

function dragStart(e) {

    DRAG_INDEX = Number(
        e.currentTarget.dataset.index
    );
}

function dragOver(e) {

    e.preventDefault();
}

function dropBlock(e) {

    e.preventDefault();

    const DROP_INDEX = Number(
        e.currentTarget.dataset.index
    );

    const item =
        PAGE.blocks.splice(
            DRAG_INDEX,
            1
        )[0];

    PAGE.blocks.splice(
        DROP_INDEX,
        0,
        item
    );

    renderEditor();

    renderPreview();
}

function moveUp(index) {

    if(index <= 0) return;

    [
        PAGE.blocks[index - 1],
        PAGE.blocks[index]
    ] = [
        PAGE.blocks[index],
        PAGE.blocks[index - 1]
    ];

    renderEditor();

    renderPreview();
}

function moveDown(index) {

    if(
        index >=
        PAGE.blocks.length - 1
    ) return;

    [
        PAGE.blocks[index + 1],
        PAGE.blocks[index]
    ] = [
        PAGE.blocks[index],
        PAGE.blocks[index + 1]
    ];

    renderEditor();

    renderPreview();
}

loadPage();
