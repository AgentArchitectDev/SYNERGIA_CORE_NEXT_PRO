export default function SynergiaDynamicEditor() {
  const blocks = [
    {
      id: 'hero',
      name: 'Hero Modern',
      category: 'hero',
      fields: [
        { id: 'title', type: 'text', label: 'Título' },
        { id: 'subtitle', type: 'textarea', label: 'Subtítulo' },
        { id: 'button', type: 'text', label: 'Botón' }
      ]
    },
    {
      id: 'navbar',
      name: 'Navbar Modern',
      category: 'navigation',
      fields: [
        { id: 'logo', type: 'text', label: 'Logo' }
      ]
    },
    {
      id: 'footer',
      name: 'Footer Minimal',
      category: 'footer',
      fields: [
        { id: 'copyright', type: 'text', label: 'Copyright' }
      ]
    }
  ]

  const [selectedBlock, setSelectedBlock] = React.useState(blocks[0])

  const [formData, setFormData] = React.useState({
    title: 'SYNERGIA CMS',
    subtitle: 'Visual AI Builder',
    button: 'Comenzar',
    logo: 'SYNERGIA',
    copyright: '2026'
  })

  const [settings, setSettings] = React.useState({
    model: 'gpt-5.5',
    apiKey: '',
    template: 'modern_dark',
    renderMode: 'automatic'
  })

  function updateField(id, value) {
    setFormData(prev => ({
      ...prev,
      [id]: value
    }))
  }

  function updateSetting(id, value) {
    setSettings(prev => ({
      ...prev,
      [id]: value
    }))
  }

  function renderInput(field) {
    if (field.type === 'textarea') {
      return (
        <textarea
          className="w-full bg-zinc-900 border border-zinc-700 rounded-xl p-3 text-white min-h-[120px]"
          value={formData[field.id] || ''}
          onChange={(e) => updateField(field.id, e.target.value)}
        />
      )
    }

    return (
      <input
        className="w-full bg-zinc-900 border border-zinc-700 rounded-xl p-3 text-white"
        value={formData[field.id] || ''}
        onChange={(e) => updateField(field.id, e.target.value)}
      />
    )
  }

  return (
    <div className="min-h-screen bg-black text-white flex">

      <aside className="w-[320px] border-r border-zinc-800 bg-zinc-950 p-5 overflow-y-auto flex flex-col gap-6">

        <div>
          <h1 className="text-2xl font-bold">⚡ SYNERGIA CORE NEXT</h1>
          <p className="text-zinc-400 text-sm mt-2">
            Dynamic Visual AI CMS
          </p>
        </div>

        <div className="space-y-3">
          <h2 className="text-sm uppercase tracking-wider text-zinc-500">
            Bloques
          </h2>

          {blocks.map(block => (
            <button
              key={block.id}
              onClick={() => setSelectedBlock(block)}
              className={`w-full text-left p-4 rounded-2xl border transition-all ${selectedBlock.id === block.id
                ? 'bg-emerald-500 text-black border-emerald-400'
                : 'bg-zinc-900 border-zinc-800 hover:bg-zinc-800'
              }`}
            >
              <div className="font-bold">{block.name}</div>
              <div className="text-xs opacity-70 mt-1">
                {block.category}
              </div>
            </button>
          ))}
        </div>

        <div className="space-y-4">
          <h2 className="text-sm uppercase tracking-wider text-zinc-500">
            Configuración IA
          </h2>

          <div>
            <label className="text-xs text-zinc-400">Modelo IA</label>
            <select
              className="w-full mt-2 bg-zinc-900 border border-zinc-700 rounded-xl p-3"
              value={settings.model}
              onChange={(e) => updateSetting('model', e.target.value)}
            >
              <option>gpt-5.5</option>
              <option>claude</option>
              <option>gemini</option>
              <option>deepseek</option>
              <option>local-llm</option>
            </select>
          </div>

          <div>
            <label className="text-xs text-zinc-400">API KEY</label>
            <input
              type="password"
              className="w-full mt-2 bg-zinc-900 border border-zinc-700 rounded-xl p-3"
              placeholder="sk-..."
              value={settings.apiKey}
              onChange={(e) => updateSetting('apiKey', e.target.value)}
            />
          </div>

          <div>
            <label className="text-xs text-zinc-400">Template Base</label>
            <select
              className="w-full mt-2 bg-zinc-900 border border-zinc-700 rounded-xl p-3"
              value={settings.template}
              onChange={(e) => updateSetting('template', e.target.value)}
            >
              <option>modern_dark</option>
              <option>corporate</option>
              <option>minimal</option>
              <option>cinematic</option>
              <option>futuristic</option>
            </select>
          </div>

          <div>
            <label className="text-xs text-zinc-400">Modo</label>
            <select
              className="w-full mt-2 bg-zinc-900 border border-zinc-700 rounded-xl p-3"
              value={settings.renderMode}
              onChange={(e) => updateSetting('renderMode', e.target.value)}
            >
              <option value="automatic">Automático IA</option>
              <option value="manual">Manual Humano</option>
              <option value="hybrid">Híbrido</option>
            </select>
          </div>
        </div>

        <div className="space-y-4">
          <h2 className="text-sm uppercase tracking-wider text-zinc-500">
            Campos Dinámicos
          </h2>

          {selectedBlock.fields.map(field => (
            <div key={field.id}>
              <label className="text-xs text-zinc-400 block mb-2">
                {field.label}
              </label>
              {renderInput(field)}
            </div>
          ))}
        </div>

        <button className="w-full bg-emerald-500 text-black font-bold p-4 rounded-2xl hover:scale-[1.01] transition-all">
          🚀 GENERAR WEB
        </button>
      </aside>

      <main className="flex-1 bg-zinc-100 p-8 overflow-auto">

        <div className="bg-white rounded-[32px] shadow-2xl overflow-hidden min-h-full">

          <div className="bg-black text-white px-8 py-6 border-b border-zinc-800 flex items-center justify-between">
            <div>
              <h2 className="text-xl font-bold">Preview Live</h2>
              <p className="text-zinc-400 text-sm">
                Render visual dinámico
              </p>
            </div>

            <div className="text-xs bg-emerald-500 text-black px-4 py-2 rounded-full font-bold">
              {settings.renderMode.toUpperCase()}
            </div>
          </div>

          <div>

            <nav className="bg-black text-white px-8 py-5 flex justify-between items-center">
              <div className="font-bold text-xl">
                {formData.logo}
              </div>

              <div className="flex gap-6 text-sm">
                <span>Inicio</span>
                <span>Servicios</span>
                <span>Contacto</span>
              </div>
            </nav>

            <section className="min-h-[70vh] bg-black text-white flex items-center justify-center text-center px-8">
              <div>
                <h1 className="text-7xl font-black leading-tight max-w-4xl mx-auto">
                  {formData.title}
                </h1>

                <p className="text-2xl text-zinc-400 mt-8 max-w-2xl mx-auto">
                  {formData.subtitle}
                </p>

                <button className="mt-10 bg-emerald-500 text-black px-8 py-4 rounded-2xl font-bold text-lg">
                  {formData.button}
                </button>
              </div>
            </section>

            <section className="grid grid-cols-3 gap-6 p-10 bg-zinc-100">
              {[1,2,3].map(card => (
                <div key={card} className="bg-white border border-zinc-200 rounded-3xl p-8 shadow-sm">
                  <div className="text-4xl mb-4">⚡</div>
                  <h3 className="text-2xl font-bold mb-3">
                    IA Service {card}
                  </h3>
                  <p className="text-zinc-600">
                    Sistema modular visual impulsado por bloques dinámicos.
                  </p>
                </div>
              ))}
            </section>

            <footer className="bg-black text-zinc-400 text-center py-8">
              © {formData.copyright} SYNERGIA CORE NEXT
            </footer>
          </div>
        </div>
      </main>
    </div>
  )
}

