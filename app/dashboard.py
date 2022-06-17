import warnings
import pandas as pd
import streamlit as st

from numpy import ceil
from utils import get_database

from app.plots import AppCharts
from app.tables import AppTables

st.set_page_config(page_title="|  Fraud Transactions Dashboard", page_icon="💰", layout="wide")
warnings.filterwarnings('ignore')


def get_data():
    df = get_database()
    return df

def css_template():
    html = """
    <style>
        p {color: #428df5; }
        ::selection { color: #b950ff; }
        h1 {color: #7033ff; text-align: center; }
        h2 {color: #9d73ff}
        h3 {text-align: center;}
    </style>
    """
    st.markdown( html, unsafe_allow_html=True )
    return None

def change_datatypes(df):
    df = df.rename(columns={"isFraud": "isFraudProba"})
    
    column_list = ['step','amount','isFraudProba','oldbalanceOrg','newbalanceOrig',
                   'oldbalanceDest','newbalanceDest','isFlaggedFraud']
    dtypes_list = ['int32','float64','float16','float64','float64',
                   'float64','float64','int32']

    for c in zip(column_list, dtypes_list):
        df[c[0]] = df[c[0]].astype(c[1])

    return df

def feature_engineering(df):
    df['day'] = ceil(df.step / 24).astype('int32')

    df = df.drop(columns=['step'], axis=1)

    return df

def streamlit_app_header():
    st.image('img/fraud_logo_2.png')
    st.header("Please, Select Visualization Type")
    show_type = st.selectbox("", options=['Tables', 'Plots'])
    st.write(' ')
    st.write('___')

    return show_type

if __name__ == "__main__":
    at = AppTables()
    ac = AppCharts()

    css_template()

    df = get_data()
    df = change_datatypes(df)
    df = feature_engineering(df)

    show_type = streamlit_app_header()

    if show_type == 'Tables':
        df = at.table_filters(df)

        at.show_dataset_tables(df)

    else:
        ac.historical_plots(df)

        ac.plot_histograms(df)