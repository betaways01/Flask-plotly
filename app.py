
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import pandas as pd
import xlrd
import openpyxl


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart1')
def chart1():
    df = pd.read_excel('INRP_GHG-2020-2_CLEANED.xlsm',
                       sheet_name='GHG Emissions GES 2004-2020')

    fig = px.bar(df, x='Reporting Company Trade Name / Nom commercial de la société déclarante',
                 y="Total Emissions (tonnes CO2e) / Émissions totales (tonnes éq. CO2)",
                 color="Facility Name / Nom de l'installation", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "CHART 1"
    description = """
    A chart of Company trade name, Total emissions, by Facility name.
    """
    return render_template('base.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart2')
def chart2():
    df = pd.read_excel('INRP_GHG-2020-2_CLEANED.xlsm',
                       sheet_name='GHG Emissions GES 2004-2020')

    fig = px.bar(df, x="English Facility NAICS Code Description / Description du code SCIAN de l'installation en anglais",
                 y="Total Emissions (tonnes CO2e) / Émissions totales (tonnes éq. CO2)",
                 color="Reporting Company Trade Name / Nom commercial de la société déclarante",
                 barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "CHART 2"
    description = """
    A chart of English Facility, Total Emission, by Company Trade name
    """
    return render_template('base.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart3')
def chart3():
    df = pd.read_excel('INRP_GHG-2020-2_CLEANED.xlsm',
                       sheet_name='GHG Emissions GES 2004-2020')

    fig = px.bar(df, x="Facility Name / Nom de l'installation",
                 y="Reference Year / Année de référence",
                 color="English Facility NAICS Code Description / Description du code SCIAN de l'installation en anglais",
                 barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "CHART 3"
    description = """
    A chart of Facility Name, Year (2020), and English Facility.
    """
    return render_template('base.html', graphJSON=graphJSON, header=header, description=description)
