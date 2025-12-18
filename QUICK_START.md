# Quick Start Guide - BI Forecasting Dashboard

## 🚀 Start the Application (30 seconds)

### Option 1: PowerShell (Windows)
```powershell
cd C:\Users\fendi\Documents\UTS_BI\TA\bi_forecasting\bi_app
python app.py
```

### Option 2: Command Line (Windows)
```cmd
cd C:\Users\fendi\Documents\UTS_BI\TA\bi_forecasting\bi_app
python app.py
```

### Option 3: Any Location (Use Full Path)
```bash
python C:\Users\fendi\Documents\UTS_BI\TA\bi_forecasting\bi_app\app.py
```

---

## ✅ What You Should See

```
✅ Admin user created: admin / admin123
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.100.110:5000
Press CTRL+C to quit
 * Restarting with watchdog
 * Debugger is active!
 * Debugger PIN: 490-284-676
```

✅ If you see this, **the app is running successfully!**

---

## 🌐 Access the Dashboard

1. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

2. **Login Page** appears
   - Username: `admin`
   - Password: `admin123`
   - Click **"Login"**

3. **Dashboard Page** loads with 9 interactive Bokeh charts

---

## 📊 Dashboard Features

### Charts Displayed

1. **4 Time Series Charts** (Full Width)
   - Units Sold Over Time
   - Price Trend
   - Inventory Level
   - Demand

2. **4 Scatter Plots** (2-Column Grid)
   - Price vs Units Sold
   - Inventory vs Orders
   - Discount vs Sales
   - Promotion vs Sales

3. **1 LSTM Forecast Chart** (Full Width)
   - Actual vs Predicted Units Sold

### Interactive Features (All Charts)
- **Hover**: Point mouse over chart to see values
- **Pan**: Click & drag to move around
- **Zoom**: Scroll mouse wheel to zoom in/out
- **Box Zoom**: Click & drag box to zoom to area
- **Reset**: Click reset icon to return to original view
- **Save**: Click save icon to download as PNG

---

## 🔑 Login Credentials

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin123` |

**Note**: These are default credentials. Change in production!

---

## 📁 File Locations

| File | Location | Purpose |
|------|----------|---------|
| Flask App | `bi_app/app.py` | Main application entry point |
| Routes | `bi_app/routes.py` | Dashboard & Bokeh charts |
| Models | `bi_app/models.py` | User database model |
| Database | `bi_app/users.db` | SQLite auth database |
| Templates | `bi_app/templates/` | HTML pages (login, dashboard) |
| Data | `data/processed/` | CSV data used by charts |
| Notebook | `notebooks/complete_workflow.ipynb` | Data pipeline (Jupyter) |

---

## 🛑 Stop the Application

Press **CTRL+C** in the terminal where the app is running

```
Press CTRL+C to quit
Keyboard interrupt
```

---

## 🔧 Requirements Already Installed

All dependencies are pre-installed in `bi_app/requirements.txt`:
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- Flask-Login 0.6.3
- Bokeh 3.3.1
- Pandas 2.1.3
- NumPy 1.26.2
- Scikit-learn
- Werkzeug (password hashing)

If you need to reinstall:
```bash
cd bi_app
pip install -r requirements.txt
```

---

## ❓ Troubleshooting

### "Can't open file 'app.py'"
- Make sure you're in the right directory
- Use the full path: `python C:\Users\fendi\...\bi_app\app.py`

### "Port 5000 already in use"
- Another app is using port 5000
- Change port in `bi_app/app.py` line 51: `port=5001`
- Or: Kill the process using port 5000

### "Module not found: pandas/bokeh/flask"
- Reinstall dependencies: `pip install -r bi_app/requirements.txt`

### Charts not appearing
- Check CSV files exist:
  - `data/processed/daily_features.csv`
  - `data/processed/lstm_forecast_results.csv`
- Press F12 in browser to check console errors

### Login not working
- Default credentials are: `admin` / `admin123`
- Database file: `bi_app/users.db`
- Try deleting and restarting (will recreate user)

---

## 📚 What's Inside?

### Complete Workflow
```
Raw Data (sales_data.csv)
    ↓
Jupyter Notebook (Data Processing)
    ↓
Processed Data (daily_features.csv)
    ↓
LSTM Model Training
    ↓
Forecast Results (lstm_forecast_results.csv)
    ↓
Flask App (Authentication)
    ↓
Bokeh Chart Generation
    ↓
Dashboard (9 Interactive Charts)
```

### Key Technologies
- **Backend**: Flask (Python web framework)
- **Database**: SQLite + SQLAlchemy ORM
- **Auth**: Flask-Login (secure sessions)
- **Visualization**: Bokeh (interactive JavaScript charts)
- **Data**: Pandas (CSV processing)
- **ML**: TensorFlow/Keras (LSTM forecasting)

---

## 🎓 Learning Path

1. **See it run** ← You are here
2. **Explore the data**: Open `notebooks/complete_workflow.ipynb`
3. **Understand the code**: Read `bi_app/routes.py` (Bokeh chart generation)
4. **Modify charts**: Edit chart dimensions, colors, data in `routes.py`
5. **Deploy**: Use Gunicorn + Nginx for production

---

## 📞 Next Steps

### To Add New Charts
1. Edit `notebooks/complete_workflow.ipynb` to add new data processing
2. Add Bokeh chart code in `bi_app/routes.py` function `generate_bokeh_charts()`
3. Add HTML container in `bi_app/templates/dashboard.html`

### To Change Login Credentials
1. Delete `bi_app/users.db`
2. Modify `bi_app/app.py` lines 42-46 to set new credentials
3. Restart app

### To Deploy to Production
1. Set `debug=False` in `bi_app/app.py`
2. Use Gunicorn: `gunicorn bi_app.app:app`
3. Configure Nginx as reverse proxy
4. Enable HTTPS with SSL certificate

---

## ✨ Features

✅ User authentication with secure password hashing
✅ 9 interactive Bokeh charts
✅ Real-time data from CSV files
✅ LSTM sales forecasting
✅ Responsive Bootstrap design
✅ One-click logout
✅ Mobile-friendly dashboard

---

**Ready to go!** Open http://127.0.0.1:5000 in your browser 🎉
