# {{ _project_name }}

Welcome to **{{ _project_name }}**, a fully modular, Copier-ready Python boilerplate optimized for **UV** dependency management. This template is designed for:

- Python libraries/packages
- Backend applications
- Data science pipelines
- Quick project scaffolding with automated folder creation

---

## Features

- **UV-managed Python project** (Python {{ _python_version }})
- **Copier-ready** for dynamic project, package, and folder naming
- Modular folder structure:
  - `src/{{ _package_name }}/backend` (optional, can be renamed via Copier)
  - `src/{{ _package_name }}/{{ _data_science_folder }}` (optional, can be renamed via Copier)
  - `shared/src/shared/utils` with fully tested `text.py` and `numeric.py`
- Docker-ready (`docker/Dockerfile` & `docker/docker-compose.yml`)
- Centralized configuration and logging
- Environment variable management (`.env` & `.env.sample`)
- Unit tests (`tests/`)
- Documentation for UV setup and GitHub tricks (`docs/`)

---

## Quick Start

### 1. Generate a new project

```bash
pip install copier
copier copy ./ms_python_boilerplate_template ./my_new_project
```

**Copier** will ask for:
- `_project_name` – display/repo name (can contain spaces or hyphens)
- `_package_name` – Python importable package (auto-derived from `_project_name`, must be snake_case and valid for pip)
- `_backend_folder` – optional backend module name
- `_data_science_folder` – optional DS module name
- `_python_version` – default 3.13

---

### 2. Setup environment with UV

```bash
uv venv
uv pip install -r requirements.txt
```

UV will manage virtual environments, dependency isolation, and scripts.

---

### 3. Run your application

```bash
uv run python -m {{ _package_name }}.main
```

---

## Project Structure

Below is the complete project layout with inline comments for guidance:

```bash
{{ _project_name }}/
├─ docs/                        # Documentation for developers
│  ├─ uv_setup_and_usage_guide.md  # UV installation & usage guide
│  └─ github_tricks.md              # GitHub workflow tips
├─ copier.yaml                   # Copier template configuration
├─ README.md                     # Project instructions & guides (this file)
├─ pyproject.toml                # UV build & dependency configuration
├─ docker/                       # Docker setup
│  ├─ Dockerfile
│  └─ docker-compose.yml
├─ .env                          # Environment variables
├─ .gitignore                    # Git-ignored files
├─ config/                       # Centralized configuration
│  ├─ config.py                  # Paths & env variables
│  ├─ logger.py                  # Centralized logger
│  └─ credentials/               # Sensitive files (gitignored)
├─ data/                         # Data storage
│  ├─ raw/                       # Raw data (copier auto-creates)
│  └─ processed/                 # Processed data
├─ shared/                       # Shared utilities
│  └─ src/shared/utils/
│     ├─ __init__.py
│     ├─ text.py                 # String/text utilities
│     └─ numeric.py              # Numeric/statistical utilities
├─ src/                          # Main source code
│  ├─ __init__.py
│  ├─ main.py                    # Entry point
│  ├─ {{ _backend_folder }}/     # Optional backend module
│  │  ├─ __init__.py
│  │  ├─ api.py
│  │  ├─ routes.py
│  │  ├─ db.py
│  │  └─ services.py
│  ├─ {{ _data_science_folder }}/ # Optional data science module
│  │  ├─ __init__.py
│  │  ├─ pipelines.py            # ETL / preprocessing scripts
│  │  ├─ models.py               # ML / DS models
│  │  ├─ notebooks/              # Jupyter notebooks
│  │  └─ reports/                # Reports / outputs
│  └─ utils/                     # Project-specific helpers
│     ├─ __init__.py
│     └─ helpers.py
├─ tests/                        # Unit tests
│  ├─ __init__.py
│  ├─ test_text.py               # Tests for text utilities
│  └─ test_numeric.py            # Tests for numeric utilities
└─ requirements.txt              # Development dependencies (ruff, pytest, etc.)
```

---

## Environment Configuration

- `.env` – environment variables for development
- `.env.sample` – template to copy for new projects
- **Centralized logger** (`config/logger.py`) respects `.env` for `LOG_ENABLED=True/False`

---

## Documentation

- **UV Setup & Usage**: [docs/uv_setup_and_usage_guide.md](docs/uv_setup_and_usage_guide.md)
- **GitHub Tricks**: [docs/github_tricks.md](docs/github_tricks.md)

---

## Credits

- Author: **Mohit Shrestha** (`contact@mohitshrestha.com.np`)
- Default boilerplate name: **ms_python_boilerplate_template**
- Fully modular, UV-compatible, and Copier-ready

---

## Contributing

1. Fork the repository
2. Use Copier to generate your own project
3. Submit PRs for enhancements, fixes, or new utilities
4. Ensure tests pass (`pytest`) before merging

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
