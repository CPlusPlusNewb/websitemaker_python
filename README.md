websitemaker_python

A lightweight Python-based local web server and static site utility for quickly serving and iterating on HTML content without external frameworks.

Built to stay simple: standard library only, terminal-driven, and easy to extend.


OVERVIEW

websitemaker_python provides a small set of utilities for:

- Running a local HTTP server
- Serving and regenerating static files
- Managing a configurable webroot
- Persisting last-used settings between runs

No frameworks, no magic — just Python.


REQUIREMENTS

- Python 3.8 or newer
- Standard library only
- Cross-platform (Windows, macOS, Linux)


INSTALLATION

Clone the repository:

git clone https://github.com/CPlusPlusNewb/websitemaker_python.git
cd websitemaker_python

Optional (recommended for isolation):

python -m venv venv
source venv/bin/activate   (macOS / Linux)
venv\Scripts\activate      (Windows)

No dependencies to install.


USAGE

Start the server:

python websitemaker.py

This will:
- Start a local HTTP server
- Serve files from the configured webroot
- Watch for file changes and refresh automatically
- Restore the last-used settings from disk

Access the server in your browser:

http://localhost:8000

(Port may vary based on configuration.)


PROJECT STRUCTURE

websitemaker_python/
│
├── websitemaker.py        Main entry point / orchestration
├── server.py              HTTP server implementation
├── terminal_ui.py         CLI interaction
├── makeanindex.py         Index generation
├── assets.py              Asset utilities
├── settings.py            Configuration handling
├── last_settings.txt      Persisted runtime settings
└── README.txt


CONFIGURATION

Runtime configuration is persisted using a plain text file (last_settings.txt) to avoid external state or formats.

This allows the application to restore the previous webroot and options on startup.


DESIGN PHILOSOPHY

- Standard library over dependencies
- Explicit over implicit behavior
- Local-first development workflow
- Easy to read, easy to modify

This project is intended to be hacked on.


CONTRIBUTING

Pull requests and issues are welcome.

Keep changes focused, readable, and consistent with the existing style.


LICENSE

MIT License.


AUTHOR

CPlusPlusNewb
https://github.com/CPlusPlusNewb
