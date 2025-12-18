# flask_api (rebuilt)

This is a minimal Flask application for the BI forecasting project. It provides:

- Login/logout (Flask-Login + SQLite)
- Dashboard (`/dashboard`) that shows forecast results if `data/processed/lstm_forecast_results.csv` exists
- BI page (`/bi`) built with Bokeh from `data/processed/daily_features.csv`
- Predict endpoint (`/predict`) that lazily loads the model and scaler in `models/` (optional, requires TensorFlow)

Quick start (PowerShell):

```powershell
python -m pip install -r .\requirements.txt
cd flask_api
python create_user.py   # creates admin/admin123
python app.py
```

Open http://127.0.0.1:5000/login and login with `admin` / `admin123` (or create your own user).

Notes:
- TensorFlow is optional. If you want to use `/predict`, install TensorFlow and ensure `models/lstm_units_sold_model.keras` and `models/minmax_scaler.pkl` exist.
- `app.secret_key` reads `FLASK_SECRET` env var if set.
