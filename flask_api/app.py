from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, login_required, current_user, login_user, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

# =====================
# INIT APP & DB
# =====================
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(BASE_DIR, 'users.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =====================
# USER MODEL
# =====================
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

# =====================
# LOGIN MANAGER
# =====================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =====================
# LOGIN ROUTE
# =====================
@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid username or password")
    
    return render_template("login.html")

# =====================
# LOGOUT ROUTE
# =====================
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# =====================
# DASHBOARD (Main Dashboard - Bokeh from CSV)
# =====================
@app.route("/dashboard")
@login_required
def dashboard():
    """Main dashboard displaying interactive Bokeh plots from CSV"""
    csv_path = os.path.join(BASE_DIR, "data", "processed", "daily_features.csv")
    forecast_csv_path = os.path.join(BASE_DIR, "data", "processed", "lstm_forecast_results.csv")
    
    script = ""
    div_forecast = None
    div1 = div2 = div3 = div4 = "<p>No data available</p>"
    plots_list = []
    
    # Try to load forecast data if available
    if os.path.exists(forecast_csv_path):
        try:
            df_forecast = pd.read_csv(forecast_csv_path, parse_dates=["Date"])
            
            if "Date" in df_forecast.columns and "Actual Units Sold" in df_forecast.columns and "Predicted Units Sold" in df_forecast.columns:
                p_forecast = figure(
                    title="📈 Sales Forecast (LSTM Model)",
                    x_axis_type="datetime",
                    width=1200,
                    height=450,
                    toolbar_location="right",
                    tools="pan,wheel_zoom,box_zoom,reset,save"
                )
                p_forecast.line(df_forecast["Date"], df_forecast["Actual Units Sold"], legend_label="Actual", line_width=2.5, color="steelblue")
                p_forecast.line(df_forecast["Date"], df_forecast["Predicted Units Sold"], legend_label="Predicted", line_width=2.5, color="coral")
                p_forecast.legend.location = "top_left"
                p_forecast.legend.click_policy = "hide"
                plots_list.append(p_forecast)
        except Exception as e:
            div_forecast = f"<p style='color:red;'>Error loading forecast: {str(e)}</p>"
    
    # Load main data from daily_features
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path, parse_dates=["Date"])
            
            # Plot 1: Time series of Units Sold
            if "Date" in df.columns and "Units Sold" in df.columns:
                p1 = figure(
                    title="📊 Units Sold Over Time",
                    x_axis_type="datetime",
                    width=1200,
                    height=450,
                    toolbar_location="right",
                    tools="pan,wheel_zoom,box_zoom,reset,save"
                )
                p1.line(df["Date"], df["Units Sold"], line_width=2.5, color="navy")
                p1.circle(df["Date"], df["Units Sold"], size=4, color="navy", alpha=0.5)
                plots_list.append(p1)
            
            # Plot 2: Category Performance
            if "Category" in df.columns and "Units Sold" in df.columns:
                category_stats = df.groupby("Category")["Units Sold"].mean().sort_values(ascending=False)
                
                p2 = figure(
                    x_range=list(category_stats.index),
                    title="🏷️ Category Performance",
                    width=580,
                    height=400,
                    x_axis_label="Category",
                    y_axis_label="Avg Units Sold",
                    toolbar_location="right",
                    tools="pan,wheel_zoom,reset,save"
                )
                p2.vbar(x=list(category_stats.index), top=category_stats.values, width=0.6, color="green", alpha=0.8)
                plots_list.append(p2)
            
            # Plot 3: Region Performance
            if "Region" in df.columns and "Units Sold" in df.columns:
                region_stats = df.groupby("Region")["Units Sold"].mean().sort_values(ascending=False)
                
                p3 = figure(
                    x_range=list(region_stats.index),
                    title="🗺️ Region Performance",
                    width=580,
                    height=400,
                    x_axis_label="Region",
                    y_axis_label="Avg Units Sold",
                    toolbar_location="right",
                    tools="pan,wheel_zoom,reset,save"
                )
                p3.vbar(x=list(region_stats.index), top=region_stats.values, width=0.6, color="coral", alpha=0.8)
                plots_list.append(p3)
            
            # Plot 4: Price vs Units Sold scatter
            if "Price" in df.columns and "Units Sold" in df.columns:
                p4 = figure(
                    title="💰 Price vs Units Sold",
                    width=580,
                    height=400,
                    x_axis_label="Price",
                    y_axis_label="Units Sold",
                    toolbar_location="right",
                    tools="pan,wheel_zoom,box_zoom,reset,save"
                )
                p4.circle(df["Price"], df["Units Sold"], size=6, color="purple", alpha=0.6)
                plots_list.append(p4)
            
            if plots_list:
                script, divs = components(tuple(plots_list))
                if len(divs) >= 1:
                    div1 = divs[0]  # Time series
                if len(divs) >= 2:
                    div2 = divs[1]  # Category
                if len(divs) >= 3:
                    div3 = divs[2]  # Region
                if len(divs) >= 4:
                    div4 = divs[3]  # Price scatter
        except Exception as e:
            div1 = f"<p style='color:red;'>Error loading data: {str(e)}</p>"
    
    return render_template("dashboard.html", script=script, div_forecast=div_forecast, div1=div1, div2=div2, div3=div3, div4=div4, username=current_user.username)


# =====================
# BI PAGE (Bokeh plots from daily_features)
# =====================
@app.route("/bi")
@login_required
def bi():
    csv_path = os.path.join(BASE_DIR, "data", "processed", "daily_features.csv")
    
    script = ""
    div1 = "<p>No data available</p>"
    div2 = "<p>No data available</p>"
    
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path, parse_dates=["Date"])
            
            # Plot 1: Time series of Units Sold
            if "Date" in df.columns and "Units Sold" in df.columns:
                p1 = figure(
                    title="Units Sold Over Time",
                    x_axis_type="datetime",
                    width=900,
                    height=400
                )
                p1.line(df["Date"], df["Units Sold"], line_width=2, color="navy")
                p1.circle(df["Date"], df["Units Sold"], size=3, color="navy", alpha=0.6)
            else:
                p1 = figure(title="Units Sold Over Time", width=900, height=400)
                p1.text([0], [0], text=["Missing Date or Units Sold columns"])
            
            # Plot 2: Price vs Units Sold scatter
            if "Price" in df.columns and "Units Sold" in df.columns:
                p2 = figure(
                    title="Price vs Units Sold",
                    width=450,
                    height=350,
                    x_axis_label="Price",
                    y_axis_label="Units Sold"
                )
                p2.circle(df["Price"], df["Units Sold"], size=6, color="orange", alpha=0.6)
            else:
                p2 = figure(title="Price vs Units Sold", width=450, height=350)
                p2.text([0], [0], text=["Missing Price or Units Sold columns"])
            
            script, (div1, div2) = components((p1, p2))
        except Exception as e:
            div1 = f"<p>Error: {str(e)}</p>"
    
    return render_template("bi.html", script=script, div1=div1, div2=div2, username=current_user.username)

# =====================
# INTERACTIVE ANALYTICS (from EDA notebook)
# =====================
@app.route("/analytics")
@login_required
def analytics():
    """Interactive Bokeh dashboard from business_problem_eda.ipynb analysis"""
    csv_path = os.path.join(BASE_DIR, "data", "processed", "daily_features.csv")
    
    script = ""
    div1 = div2 = div3 = div4 = "<p>No data available</p>"
    
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path, parse_dates=["Date"])
            
            # Plot 1: Distribution of Units Sold (histogram)
            if "Units Sold" in df.columns:
                hist, edges = pd.cut(df["Units Sold"], bins=30, retbins=True)
                hist_df = pd.DataFrame({"units": hist.value_counts().sort_index().values}, 
                                       index=[f"{edges[i]:.1f}-{edges[i+1]:.1f}" for i in range(len(edges)-1)])
                
                p1 = figure(
                    title="Distribution of Units Sold",
                    width=450,
                    height=350,
                    x_axis_label="Units Sold Range",
                    y_axis_label="Frequency"
                )
                p1.vbar(x=list(range(len(hist_df))), top=hist_df.values.flatten(), width=0.8, color="steelblue")
                p1.xaxis.major_label_overrides = {i: hist_df.index[i] for i in range(min(5, len(hist_df)))}
            else:
                p1 = figure(title="Distribution of Units Sold", width=450, height=350)
                p1.text([0], [0], text=["Missing Units Sold column"])
            
            # Plot 2: Category Performance (Bar chart)
            if "Category" in df.columns and "Units Sold" in df.columns:
                category_stats = df.groupby("Category")["Units Sold"].mean().sort_values(ascending=False)
                
                p2 = figure(
                    x_range=list(category_stats.index),
                    title="Average Units Sold by Category",
                    width=450,
                    height=350,
                    x_axis_label="Category",
                    y_axis_label="Avg Units Sold"
                )
                p2.vbar(x=list(category_stats.index), top=category_stats.values, width=0.6, color="green")
                p2.xaxis.major_label_orientation = 0.785  # 45 degrees
            else:
                p2 = figure(title="Category Performance", width=450, height=350)
                p2.text([0], [0], text=["Missing Category or Units Sold column"])
            
            # Plot 3: Region Performance (Bar chart)
            if "Region" in df.columns and "Units Sold" in df.columns:
                region_stats = df.groupby("Region")["Units Sold"].mean().sort_values(ascending=False)
                
                p3 = figure(
                    x_range=list(region_stats.index),
                    title="Average Units Sold by Region",
                    width=450,
                    height=350,
                    x_axis_label="Region",
                    y_axis_label="Avg Units Sold"
                )
                p3.vbar(x=list(region_stats.index), top=region_stats.values, width=0.6, color="coral")
            else:
                p3 = figure(title="Region Performance", width=450, height=350)
                p3.text([0], [0], text=["Missing Region or Units Sold column"])
            
            # Plot 4: Promotion Impact (Line chart)
            if "Promotion" in df.columns and "Units Sold" in df.columns:
                promo_stats = df.groupby("Promotion")["Units Sold"].mean().sort_index()
                
                p4 = figure(
                    title="Promotion Level Impact on Sales",
                    width=450,
                    height=350,
                    x_axis_label="Promotion Level",
                    y_axis_label="Avg Units Sold"
                )
                p4.line(list(range(len(promo_stats))), promo_stats.values, line_width=3, color="purple")
                p4.circle(list(range(len(promo_stats))), promo_stats.values, size=8, color="purple")
            else:
                p4 = figure(title="Promotion Impact", width=450, height=350)
                p4.text([0], [0], text=["Missing Promotion or Units Sold column"])
            
            script, (div1, div2, div3, div4) = components((p1, p2, p3, p4))
        except Exception as e:
            div1 = f"<p>Error loading analytics: {str(e)}</p>"
    
    return render_template("analytics.html", script=script, div1=div1, div2=div2, div3=div3, div4=div4, username=current_user.username)


# =====================
# PREDICT ENDPOINT (lazy load model)
# =====================
@app.route("/predict", methods=["POST"])
@login_required
def predict():
    try:
        import joblib
        import numpy as np
        from tensorflow.keras.models import load_model
    except ImportError:
        return jsonify({"error": "TensorFlow/joblib not installed"}), 500
    
    data = request.get_json()
    if not data or "sequence" not in data:
        return jsonify({"error": "Missing 'sequence' in JSON"}), 400
    
    model_path = os.path.join(BASE_DIR, "models", "lstm_units_sold_model.keras")
    scaler_path = os.path.join(BASE_DIR, "models", "minmax_scaler.pkl")
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        return jsonify({"error": "Model files not found"}), 500
    
    try:
        scaler = joblib.load(scaler_path)
        model = load_model(model_path)
        
        sequence = np.array(data["sequence"])
        if sequence.ndim != 2:
            return jsonify({"error": "Sequence must be 2D"}), 400
        
        scaled = scaler.transform(sequence)
        X = scaled.reshape((1, sequence.shape[0], sequence.shape[1]))
        pred_scaled = model.predict(X, verbose=0)[0][0]
        
        dummy = np.zeros((1, sequence.shape[1]))
        dummy[0, 0] = pred_scaled
        prediction = scaler.inverse_transform(dummy)[0][0]
        
        return jsonify({"prediction": float(prediction), "user": current_user.username})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =====================
# CREATE TABLES & RUN
# =====================
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=5000)

