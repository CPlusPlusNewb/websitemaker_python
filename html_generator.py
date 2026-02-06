#HTML generator - creates the portfolio viewer page
import os
import json

def make_index_html(base_dir="."):    
    # scan for project folders
    folders = {}
    for f in os.listdir(base_dir):
        path = os.path.join(base_dir, f)
        if os.path.isdir(path) and not f.startswith('.'):
            files = [fi for fi in os.listdir(path) if os.path.isfile(os.path.join(path, fi))]
            folders[f] = files
    
    folders_json = json.dumps(folders)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portfolio</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  background: #0a0a0a;
  color: #fff;
  overflow-x: hidden;
}}

/* nav tabs */
.nav {{
  position: fixed;
  top: 0;
  width: 100%;
  height: 60px;
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 0 20px;
  background: rgba(0,0,0,0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255,255,255,0.1);
  z-index: 100;
  overflow-x: auto;
}}

/* rainbow line under nav */
.rainbow-line {{
  position: fixed;
  top: 60px;
  left: 0;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, 
    #ff0000, #ff7f00, #ffff00, #00ff00, 
    #0000ff, #4b0082, #9400d3, #ff0000
  );
  background-size: 200% 100%;
  animation: rainbowMove 3s linear infinite;
  z-index: 99;
}}

@keyframes rainbowMove {{
  0% {{ background-position: 0% 0%; }}
  100% {{ background-position: 200% 0%; }}
}}

.nav button {{
  background: none;
  border: none;
  color: #999;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  padding: 8px 12px;
  border-radius: 4px;
  transition: all 0.2s;
}}

.nav button:hover {{ color: #fff; background: rgba(255,255,255,0.05); }}
.nav button.active {{ color: #fff; background: rgba(168,85,247,0.2); }}

/* main content */
.container {{
  margin-top: 61px;
  padding: 30px 20px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}}

.section {{
  display: none;
}}

.section.active {{
  display: block;
  animation: fadeIn 0.3s;
}}

@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(10px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

.file-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px;
  margin-top: 20px;
}}

.file-item {{
  padding: 16px;
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 14px;
  word-break: break-word;
  display: flex;
  align-items: center;
  gap: 10px;
}}

.file-item:hover {{
  background: #252525;
  border-color: #a855f7;
  transform: translateY(-2px);
}}

.file-icon {{
  font-size: 20px;
  flex-shrink: 0;
}}

/* file viewer modal */
.modal {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.95);
  z-index: 200;
  overflow: auto;
  padding: 20px;
  display: none;
  align-items: flex-start;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}}

.modal.show {{
  display: flex;
  opacity: 1;
}}

.modal-content {{
  background: #111;
  border-radius: 12px;
  padding: 24px;
  max-width: 90vw;
  max-height: 90vh;
  overflow: auto;
  position: relative;
  transform: scale(0.9) translateY(20px);
  opacity: 0;
  transition: transform 0.3s ease, opacity 0.3s ease;
}}

.modal.show .modal-content {{
  transform: scale(1) translateY(0);
  opacity: 1;
}}

.modal-content.code {{ width: 60vw; }}
.modal-content.preview {{ width: 80vw; background: #fff; }}
.modal-content.image {{ width: 70vw; }}

.modal-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid #333;
}}

.modal-header h3 {{
  color: #fff;
  font-size: 18px;
}}

.modal-buttons {{
  display: flex;
  gap: 8px;
}}

.btn {{
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}}

.btn-primary {{
  background: #a855f7;
  color: white;
}}

.btn-primary:hover {{ background: #9333ea; }}

.btn-secondary {{
  background: #333;
  color: white;
}}

.btn-secondary:hover {{ background: #444; }}

.file-display {{
  margin-top: 12px;
}}

.file-display pre {{
  background: #0a0a0a;
  padding: 16px;
  border-radius: 6px;
  overflow-x: auto;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  line-height: 1.6;
  color: #e0e0e0;
}}

.file-display iframe {{
  width: 100%;
  height: 70vh;
  border: none;
  border-radius: 6px;
}}

.file-display img {{
  max-width: 100%;
  max-height: 70vh;
  border-radius: 6px;
  object-fit: contain;
}}

/* scrollbar */
::-webkit-scrollbar {{ width: 10px; }}
::-webkit-scrollbar-track {{ background: #0a0a0a; }}
::-webkit-scrollbar-thumb {{ 
  background: linear-gradient(180deg, #a855f7, #c084fc);
  border-radius: 10px;
}}
::-webkit-scrollbar-thumb:hover {{ background: #9333ea; }}
</style>
</head>
<body>

<nav class="nav" id="nav"></nav>
<div class="rainbow-line"></div>

<div class="container" id="content"></div>

<div class="modal" id="modal">
  <div class="modal-content" id="modalContent">
    <div class="modal-header">
      <h3 id="fileName"></h3>
      <div class="modal-buttons" id="modalButtons"></div>
    </div>
    <div class="file-display" id="fileDisplay"></div>
  </div>
</div>

<script>
const folders = {folders_json};
let currentTab = Object.keys(folders)[0];
let currentFile = null;
let viewMode = 'code';

function renderNav() {{
  const nav = document.getElementById('nav');
  nav.innerHTML = Object.keys(folders).map(tab => 
    `<button class="${{tab === currentTab ? 'active' : ''}}" 
             onclick="switchTab('${{tab}}')">${{tab}}</button>`
  ).join('');
}}

function renderContent() {{
  const content = document.getElementById('content');
  content.innerHTML = Object.keys(folders).map(tab => `
    <div class="section ${{tab === currentTab ? 'active' : ''}}" data-tab="${{tab}}">
      <h2 style="margin-bottom: 16px; color: #a855f7;">${{tab}}</h2>
      <div class="file-grid">
        ${{folders[tab].map(file => {{
          const icon = getFileIcon(file);
          return `<div class="file-item" onclick="openFile('${{tab}}', '${{file}}')">
            <span class="file-icon">${{icon}}</span>
            <span>${{file}}</span>
          </div>`;
        }}).join('')}}
      </div>
    </div>
  `).join('');
}}

function getFileIcon(file) {{
  const ext = file.split('.').pop().toLowerCase();
  const imgExts = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'svg'];
  
  if (imgExts.includes(ext)) {{
    return '🖼️';
  }} else {{
    return '📄';
  }}
}}

function switchTab(tab) {{
  currentTab = tab;
  document.querySelectorAll('.nav button').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
  document.querySelector(`[data-tab="${{tab}}"]`).classList.add('active');
}}

async function openFile(folder, file) {{
  currentFile = {{ folder, file }};
  viewMode = 'code';
  
  const ext = file.split('.').pop().toLowerCase();
  const imgExts = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'svg'];
  const previewExts = ['html', 'htm'];
  
  document.getElementById('fileName').textContent = file;
  
  if (imgExts.includes(ext)) {{
    showImage(folder, file);
  }} else {{
    const content = await loadFile(folder, file);
    showCode(content, previewExts.includes(ext) ? folder + '/' + file : null);
  }}
  
  const modal = document.getElementById('modal');
  modal.style.display = 'flex';
  
  setTimeout(() => {{
    modal.classList.add('show');
  }}, 10);
}}

async function loadFile(folder, file) {{
  try {{
    const res = await fetch(`./${{folder}}/${{file}}`);
    return await res.text();
  }} catch {{
    return '// Error loading file';
  }}
}}

function showCode(content, previewUrl = null) {{
  const modalContent = document.getElementById('modalContent');
  modalContent.className = 'modal-content code';
  
  const display = document.getElementById('fileDisplay');
  display.innerHTML = `<pre>${{escapeHtml(content)}}</pre>`;
  
  const buttons = document.getElementById('modalButtons');
  buttons.innerHTML = `
    ${{previewUrl ? `<button class="btn btn-secondary" onclick="togglePreview('${{previewUrl}}')">Preview</button>` : ''}}
    <button class="btn btn-primary" onclick="closeModal()">Close</button>
  `;
}}

function showImage(folder, file) {{
  const modalContent = document.getElementById('modalContent');
  modalContent.className = 'modal-content image';
  
  const display = document.getElementById('fileDisplay');
  display.innerHTML = `<img src="./${{folder}}/${{file}}" alt="${{file}}">`;
  
  const buttons = document.getElementById('modalButtons');
  buttons.innerHTML = `<button class="btn btn-primary" onclick="closeModal()">Close</button>`;
}}

function togglePreview(url) {{
  const modalContent = document.getElementById('modalContent');
  const display = document.getElementById('fileDisplay');
  
  if (viewMode === 'code') {{
    viewMode = 'preview';
    modalContent.className = 'modal-content preview';
    display.innerHTML = `<iframe src="./${{url}}"></iframe>`;
    document.querySelector('#modalButtons button').textContent = 'View Code';
  }} else {{
    viewMode = 'code';
    openFile(currentFile.folder, currentFile.file);
  }}
}}

function closeModal() {{
  const modal = document.getElementById('modal');
  const content = modal.querySelector('.modal-content');
  
  modal.classList.remove('show');
  
  setTimeout(() => {{
    modal.style.display = 'none';
  }}, 300);
}}

function escapeHtml(text) {{
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}}

document.getElementById('modal').addEventListener('click', (e) => {{
  if (e.target.id === 'modal') closeModal();
}});

renderNav();
renderContent();
</script>

</body>
</html>"""
    
    with open(os.path.join(base_dir, "index.html"), "w", encoding='utf-8') as f:
        f.write(html)
