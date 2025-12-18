# Repo-specific instructions for AI coding agents

Goal: a minimal Flask-based BI app for forecasting with login, a dashboard and a Bokeh-based BI page.

Quick architecture
- `flask_api/` — main Flask application. Key files:
  - `app.py` — application entrypoint, routes: `/login`, `/logout`, `/dashboard`, `/bi`, `/predict`.
  - `auth.py` — small register_auth_routes(app) function that adds login/logout.
  - `models.py` — SQLAlchemy `db` and `User` model.
  - `create_user.py` — create admin user helper.
  - `requirements.txt` — pinned development dependencies. Note: TensorFlow is optional and may be commented.
  - `templates/` — `base.html`, `login.html`, `dashboard.html`, `bi.html` (Bootstrap-based).

Data & ML artifacts
- `data/processed/` contains CSVs used by the BI pages:
  - `daily_features.csv` — source for BI visualizations (columns: Date, Units Sold, Price, ...)
  - `lstm_forecast_results.csv` — used on the main dashboard if present (expects `Date`, `Actual Units Sold`, `Predicted Units Sold`).
- `models/` contains model artifacts (`lstm_units_sold_model.keras`, `minmax_scaler.pkl`). The app lazy-loads the model only on `/predict` to avoid heavy startup.

Developer workflows (commands)
- Install dependencies for the Flask API (from project root):
  - python -m pip install -r flask_api/requirements.txt
- Create default admin user:
  - python flask_api/create_user.py
- Run app (development):
  - python flask_api/app.py

Conventions and patterns
- Keep heavy ML imports lazy: do not import TensorFlow at module import time. Import inside `/predict` when necessary.
- Prefer defensive CSV handling: check for file existence and expected columns; render a friendly message instead of crashing.
- Templates are minimal and use Bootstrap CDN. If integrating AdminLTE (folder: `static/flask-adminlte-master`), adapt `base.html` to include its CSS/JS and template blocks.

Integration points
- DB: `users.db` at repo root; `flask_api/app.py` uses `SQLALCHEMY_DATABASE_URI` pointing to that SQLite file.
- Model files: `models/lstm_units_sold_model.keras`, `models/minmax_scaler.pkl` used only by `/predict`.

Notes for AI edits
- When changing `app.py`, keep model imports lazy to avoid dev-env crashes.
- When adding templates, ensure `{{ script | safe }}` and `{{ div | safe }}` are injected into `head`/`content` blocks appropriately.
- If adding new endpoints, register auth routes via `register_auth_routes(app)` or follow current `auth.py` pattern.

When in doubt, run the app locally and test these pages:
- /login, /dashboard, /bi, /predict (POST with {"sequence": [[...]]})

If you make a structural change (move files, rename modules), update `flask_api/README.md` accordingly.
