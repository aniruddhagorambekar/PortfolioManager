"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PortFolioManager import app
from datetime import date


'''
Temp code to be moved to Library
'''
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import Configurator as cf
from dateutil.relativedelta import relativedelta
from calendar import isleap

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/summary')
def summary():
    """Renders the contact page."""
    df = pd.read_excel('Data.xlsx', sheetname='FDSummary')
    df['Current_Value'] = df.apply (lambda row: CurrentValue (row),axis=1)
    summaryDic = df.T.to_dict().values()
    return render_template(
        'summary.html',
        title='Summary',
        year=datetime.now().year,
        Entries=summaryDic
    )

@app.route('/settings')
def settings():
    config = cf.Configurator()
    settings = config.BuildUIData()
    
    """Renders the about page."""
    return render_template(
        'settings.html',
        title='Settings',
        year=datetime.now().year,
        settings = settings,
        message='Update Settings Required for Application.'
    )

def CurrentValue(row):
    Principal = row['Principal_Amount']
    ROI = row['ROI']
    today  = date.today()
    print "Today's Date:", today 
    start_date = datetime.strptime(str(row['Start_Date']), '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(str(today), '%Y-%m-%d')
    print "Start Date:", start_date
    diffyears = end_date.year - start_date.year
    difference  = end_date - start_date.replace(end_date.year)
    days_in_year = isleap(end_date.year) and 366 or 365
    difference_in_years = round((diffyears + (difference.days + difference.seconds/86400.0)/days_in_year), 2)
    print difference_in_years
    final = round((Principal * (((1 + (ROI/(100.0 * 4))) ** (4*difference_in_years)))), 2)
    return final

