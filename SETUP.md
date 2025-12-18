# Flask BI Forecasting App - Setup & Usage Guide

## ✅ Status: WORKING

The Flask app is now fully functional with login, dashboard with forecast plots, and BI page with business analytics visualizations.

---

## Quick Start

### 1. Install Dependencies

```powershell
cd c:\Users\fendi\Documents\UTS_BI\TA\bi_forecasting
python -m pip install -r .\flask_api\requirements.txt
```

### 2. Create Admin User (One-time)

```powershell
python .\flask_api\create_user.py
```

Output:
```
User 'admin' created successfully
```

### 3. Run the App

```powershell
python .\flask_api\app.py
```

Expected output:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### 4. Open in Browser

- **Login Page**: http://127.0.0.1:5000/login
  - Username: `admin`
  - Password: `admin123`
- **Dashboard**: http://127.0.0.1:5000/dashboard (after login)
  - Shows forecast plot from `data/processed/lstm_forecast_results.csv`
- **BI Page**: http://127.0.0.1:5000/bi (after login)
  - Shows time-series and scatter plots from `data/processed/daily_features.csv`

---

## App Structure

```
flask_api/
├── app.py                    ← MAIN app (routes, models, auth, Bokeh)
├── create_user.py           ← Create admin user helper
├── smoke_test.py            ← Test script
├── requirements.txt         ← Dependencies
└── templates/
    ├── base.html            ← Bootstrap layout & navbar
    ├── login.html           ← Login form
    ├── dashboard.html       ← Forecast plot
    └── bi.html              ← BI analytics plots
```

---

## API Routes

| Method | Route | Auth | Purpose |
|--------|-------|------|---------|
| GET | `/` | No | Redirect to login or dashboard |
| GET | `/login` | No | Display login form |
| POST | `/login` | No | Submit login credentials |
| GET | `/dashboard` | Yes | Display forecast plot (Bokeh) |
| GET | `/bi` | Yes | Display BI plots (Bokeh) |
| GET | `/logout` | Yes | Logout and redirect to login |
| POST | `/predict` | Yes | ML prediction endpoint (lazy-loads TensorFlow) |

---

## Data Sources

- **Dashboard**: `data/processed/lstm_forecast_results.csv`
  - Columns expected: `Date`, `Actual Units Sold`, `Predicted Units Sold`
  
- **BI Page**: `data/processed/daily_features.csv`
  - Columns used: `Date`, `Units Sold`, `Price`

---

## Dependencies

Core:
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Bokeh
- Pandas
- Werkzeug

Optional (for `/predict` endpoint):
- TensorFlow
- joblib

---

## Troubleshooting

### Port Already in Use
If you get "Address already in use", kill the process:
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Database Errors
Delete `users.db` and recreate:
```powershell
Remove-Item .\users.db
python .\flask_api\create_user.py
```

### Login Not Working
- Verify user exists: check `users.db` file size > 0 bytes
- Recreate user: `python .\flask_api\create_user.py`

---

## Notes

- **Security**: Change `SECRET_KEY` in production (set via `SECRET_KEY` env var)
- **Database**: SQLite at project root (`users.db`)
- **TensorFlow**: Optional; only required for `/predict` endpoint
- **Templates**: Use Bootstrap 5 CDN, no local assets needed

---

## Useful Commands

```powershell
# Check if port 5000 is open
Test-NetConnection -ComputerName localhost -Port 5000

# Test login endpoint
python -c "import requests; r = requests.post('http://127.0.0.1:5000/login', data={'username': 'admin', 'password': 'admin123'}); print(r.status_code)"

# Check database
cd . && dir users.db
```

---

**Last Updated**: December 17, 2025
