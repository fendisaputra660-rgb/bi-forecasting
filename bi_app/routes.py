"""
Routes for dashboard and authentication
"""
import os
import pandas as pd
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

from models import db

# Create blueprints
dashboard_bp = Blueprint('dashboard', __name__)
auth_bp = Blueprint('auth', __name__)

# Get base path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================================
# BOKEH CHART GENERATION
# ============================================================================

def generate_bokeh_charts():
    """Generate all Bokeh charts from CSV data"""
    
    try:
        # Load data
        csv_path = os.path.join(BASE_PATH, 'data', 'processed', 'daily_features.csv')
        forecast_path = os.path.join(BASE_PATH, 'data', 'processed', 'lstm_forecast_results.csv')
        
        if not os.path.exists(csv_path):
            return {}, "", "CSV file not found"
        
        df = pd.read_csv(csv_path)
        df['Date'] = pd.to_datetime(df['Date'])
        
        plots = {}
        
        # ===== PLOT 1: Units Sold Over Time =====
        p1 = figure(
            x_axis_type="datetime",
            title="📈 Units Sold Over Time",
            width=1000,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p1.line(df['Date'], df['Units Sold'], line_width=3, color='#00d9ff', alpha=0.9)
        p1.scatter(df['Date'], df['Units Sold'], size=5, color='#00d9ff', alpha=0.6)
        
        hover1 = HoverTool(tooltips=[
            ("Date", "@x{%F}"),
            ("Units", "@y{0,0.00}")
        ], formatters={"@x": "datetime"})
        p1.add_tools(hover1)
        p1.xaxis.axis_label = "Date"
        p1.yaxis.axis_label = "Units Sold"
        p1.title.text_font_size = "14pt"
        p1.title.text_color = "#00d9ff"
        p1.xaxis.axis_label_text_color = "#9ca3af"
        p1.yaxis.axis_label_text_color = "#9ca3af"
        
        plots['plot1'] = p1
        
        # ===== PLOT 2: Price Trend =====
        p2 = figure(
            x_axis_type="datetime",
            title="💰 Price Trend",
            width=1000,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p2.line(df['Date'], df['Price'], line_width=2, color='#ff6b9d', alpha=0.9)
        p2.scatter(df['Date'], df['Price'], size=4, color='#ff6b9d', alpha=0.6)
        
        hover2 = HoverTool(tooltips=[
            ("Date", "@x{%F}"),
            ("Price", "@y{$0,0.00}")
        ], formatters={"@x": "datetime"})
        p2.add_tools(hover2)
        p2.xaxis.axis_label = "Date"
        p2.yaxis.axis_label = "Price ($)"
        p2.title.text_font_size = "14pt"
        p2.title.text_color = "#ff6b9d"
        p2.xaxis.axis_label_text_color = "#9ca3af"
        p2.yaxis.axis_label_text_color = "#9ca3af"
        
        plots['plot2'] = p2
        
        # ===== PLOT 3: Inventory Level =====
        p3 = figure(
            x_axis_type="datetime",
            title="📦 Inventory Level",
            width=1000,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p3.line(df['Date'], df['Inventory Level'], line_width=2, color='#2ecc71', alpha=0.9)
        p3.scatter(df['Date'], df['Inventory Level'], size=4, color='#2ecc71', alpha=0.6)
        
        hover3 = HoverTool(tooltips=[
            ("Date", "@x{%F}"),
            ("Inventory", "@y{0,0.00}")
        ], formatters={"@x": "datetime"})
        p3.add_tools(hover3)
        p3.xaxis.axis_label = "Date"
        p3.yaxis.axis_label = "Inventory"
        p3.title.text_font_size = "13pt"
        
        plots['plot3'] = p3
        
        # ===== PLOT 4: Demand =====
        p4 = figure(
            x_axis_type="datetime",
            title="📊 Demand",
            width=1000,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p4.line(df['Date'], df['Demand'], line_width=2, color='#f39c12', alpha=0.9)
        p4.scatter(df['Date'], df['Demand'], size=4, color='#f39c12', alpha=0.6)
        
        hover4 = HoverTool(tooltips=[
            ("Date", "@x{%F}"),
            ("Demand", "@y{0,0.00}")
        ], formatters={"@x": "datetime"})
        p4.add_tools(hover4)
        p4.xaxis.axis_label = "Date"
        p4.yaxis.axis_label = "Demand"
        p4.title.text_font_size = "14pt"
        p4.title.text_color = "#f39c12"
        p4.xaxis.axis_label_text_color = "#9ca3af"
        p4.yaxis.axis_label_text_color = "#9ca3af"
        
        plots['plot4'] = p4
        
        # ===== PLOT 5: Price vs Units (Scatter) =====
        p5 = figure(
            title="💹 Price vs Units Sold",
            width=900,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p5.scatter('Price', 'Units Sold', source=df, size=6, color='#9b59b6', alpha=0.7)
        
        hover5 = HoverTool(tooltips=[
            ("Price", "@Price{$0,0.00}"),
            ("Units", "@{Units Sold}{0,0.00}")
        ])
        p5.add_tools(hover5)
        p5.xaxis.axis_label = "Price ($)"
        p5.yaxis.axis_label = "Units Sold"
        p5.title.text_font_size = "14pt"
        p5.title.text_color = "#9b59b6"
        p5.xaxis.axis_label_text_color = "#9ca3af"
        p5.yaxis.axis_label_text_color = "#9ca3af"
        
        plots['plot5'] = p5
        
        # ===== PLOT 6: Inventory vs Orders (Scatter) =====
        p6 = figure(
            title="📦 Inventory vs Orders",
            width=900,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p6.scatter('Inventory Level', 'Units Ordered', source=df, size=6, color='#1abc9c', alpha=0.7)
        
        hover6 = HoverTool(tooltips=[
            ("Inventory", "@{Inventory Level}{0,0.00}"),
            ("Ordered", "@{Units Ordered}{0,0.00}")
        ])
        p6.add_tools(hover6)
        p6.xaxis.axis_label = "Inventory Level"
        p6.yaxis.axis_label = "Units Ordered"
        p6.title.text_font_size = "14pt"
        p6.title.text_color = "#1abc9c"
        p6.xaxis.axis_label_text_color = "#9ca3af"
        p6.yaxis.axis_label_text_color = "#9ca3af"
        
        plots['plot6'] = p6
        
        # ===== PLOT 7: Discount vs Units (Scatter) =====
        p7 = figure(
            title="🏷️  Discount Impact",
            width=900,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p7.scatter('Discount', 'Units Sold', source=df, size=6, color='#e67e22', alpha=0.7)
        
        hover7 = HoverTool(tooltips=[
            ("Discount", "@Discount{0.00}%"),
            ("Units", "@{Units Sold}{0,0.00}")
        ])
        p7.add_tools(hover7)
        p7.xaxis.axis_label = "Discount"
        p7.yaxis.axis_label = "Units Sold"
        p7.title.text_font_size = "14pt"
        p7.title.text_color = "#e67e22"
        p7.xaxis.axis_label_text_color = "#9ca3af"
        p7.yaxis.axis_label_text_color = "#9ca3af"
        
        plots['plot7'] = p7
        
        # ===== PLOT 8: Promotion vs Units (Scatter) =====
        p8 = figure(
            title="🎯 Promotion Impact",
            width=900,
            height=380,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            background_fill_color="#1a1f2e",
            border_fill_color="#2a3142"
        )
        p8.scatter('Promotion', 'Units Sold', source=df, size=6, color='#c0392b', alpha=0.7)
        
        hover8 = HoverTool(tooltips=[
            ("Promotion", "@Promotion{0.00}"),
            ("Units", "@{Units Sold}{0,0.00}")
        ])
        p8.add_tools(hover8)
        p8.xaxis.axis_label = "Promotion"
        p8.yaxis.axis_label = "Units Sold"
        p8.title.text_font_size = "14pt"
        p8.title.text_color = "#c0392b"
        p8.xaxis.axis_label_text_color = "#9ca3af"
        p8.yaxis.axis_label_text_color = "#9ca3af"
        
        plots['plot8'] = p8
        
        # ===== PLOT 9: LSTM Forecast =====
        if os.path.exists(forecast_path):
            df_forecast = pd.read_csv(forecast_path)
            df_forecast['Date'] = pd.to_datetime(df_forecast['Date'])
            
            p9 = figure(
                x_axis_type="datetime",
                title="🤖 LSTM Forecast: Actual vs Predicted",
                width=1000,
                height=380,
                tools="pan,wheel_zoom,box_zoom,reset,save",
                background_fill_color="#1a1f2e",
                border_fill_color="#2a3142"
            )
            
            # Actual
            p9.line(df_forecast['Date'], df_forecast['Actual Units Sold'], 
                   line_width=3, color='#00d9ff', legend_label='Actual', alpha=0.9)
            p9.scatter(df_forecast['Date'], df_forecast['Actual Units Sold'], 
                      size=5, color='#00d9ff', alpha=0.6)
            
            # Predicted
            p9.line(df_forecast['Date'], df_forecast['Predicted Units Sold'], 
                   line_width=3, color='#f39c12', line_dash='dashed', 
                   legend_label='Predicted', alpha=0.9)
            p9.scatter(df_forecast['Date'], df_forecast['Predicted Units Sold'], 
                      size=5, color='#f39c12', alpha=0.6)
            
            hover9 = HoverTool(tooltips=[
                ("Date", "@x{%F}"),
                ("Value", "@y{0,0.00}")
            ], formatters={"@x": "datetime"})
            p9.add_tools(hover9)
            p9.legend.location = "top_left"
            p9.legend.click_policy = "hide"
            p9.xaxis.axis_label = "Date"
            p9.yaxis.axis_label = "Units Sold"
            p9.title.text_font_size = "14pt"
            p9.title.text_color = "#00d9ff"
            p9.xaxis.axis_label_text_color = "#9ca3af"
            p9.yaxis.axis_label_text_color = "#9ca3af"
            
            plots['plot9'] = p9
        
        # Embed all plots
        plot_list = [plots[f'plot{i}'] for i in range(1, len(plots) + 1)]
        script, divs = components(tuple(plot_list))
        
        # Map divs to plot names AND FIX display:contents
        plot_divs = {}
        for i, (plot_name) in enumerate([f'plot{j}' for j in range(1, len(plots) + 1)]):
            # Remove "display: contents" from inline style to allow CSS to work
            div_html = divs[i].replace('style="display: contents;"', 'style="display: block;"')
            plot_divs[plot_name] = div_html
        
        return plot_divs, script, None
        
    except Exception as e:
        return {}, "", str(e)

# ============================================================================
# ROUTES
# ============================================================================

@dashboard_bp.route('/')
def home():
    """Home page"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    return redirect(url_for('auth.login'))

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard with Bokeh charts"""
    plot_divs, script, error = generate_bokeh_charts()
    
    if error:
        flash(f'Error loading charts: {error}', 'warning')
    
    return render_template(
        'dashboard.html',
        script=script,
        plot_divs=plot_divs,
        error=error,
        username=current_user.username
    )

# ============================================================================
# AUTHENTICATION ROUTES
# ============================================================================

@dashboard_bp.route('/bokeh-test')
def bokeh_test():
    """Test Bokeh rendering"""
    return render_template('bokeh_minimal_test.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    from models import User  # Import locally to avoid circular import
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@dashboard_bp.route('/debug-bokeh')
def debug_bokeh():
    """Debug endpoint to check Bokeh generation"""
    plot_divs, script, error = generate_bokeh_charts()
    
    debug_info = {
        'error': error,
        'script_length': len(script),
        'num_divs': len(plot_divs),
        'div_names': list(plot_divs.keys()),
        'divs': {k: v[:100] + '...' if len(v) > 100 else v for k, v in plot_divs.items()}
    }
    
    return debug_info

@auth_bp.route('/logout')
@login_required
def logout():
    """Logout"""
    logout_user()
    return redirect(url_for('auth.login'))
