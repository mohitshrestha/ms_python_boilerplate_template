# Project Folder Structure with Copier placeholders

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
