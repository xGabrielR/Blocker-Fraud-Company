import streamlit as st
from plotly import express as px

class AppCharts(object):
    
    def historical_plots(self, df):
        st.title("Charts and Distribution's")

        st.header('💸 Daily and Type Transaction Amount')
        msk = (df['isFraudProba'] > 0)
        sum_amount_per_day = df[['amount', 'day']].groupby('day').sum().reset_index()
        sum_amount_per_typ = df[['amount', 'type']].groupby('type').sum().reset_index()
        fraud_sum_amount   = df[msk][['amount', 'type']].groupby('type').sum().reset_index()

        fig = px.line(x=sum_amount_per_day.day, y=sum_amount_per_day.amount, title="<b>Amount</b> / <b>Day's</b>",
                    color_discrete_sequence=["red"], labels={"x": "<b>Day's</b>", "y": "<b>Amount</b>",})
        fig.update_layout(plot_bgcolor='#0e1117')
        st.plotly_chart(fig, use_container_width=True)

        c1, c2 = st.columns((2))

        fig = px.bar(sum_amount_per_typ, x='type', y='amount', title='<b>Total Amount</b> / <b>Type</b>', 
                    color_discrete_sequence=['#210042'])
        fig.update_layout(plot_bgcolor='#0e1117')
        c1.plotly_chart(fig, use_container_width=True)

        fig = px.bar(fraud_sum_amount, x='type', y='amount', title='<b>FRAUD Detected Total Amount</b> / <b>Type</b>', 
                    color_discrete_sequence=['#37016e'])
        fig.update_layout(plot_bgcolor='#0e1117')
        c2.plotly_chart(fig, use_container_width=True)

        return None

    def plot_histograms(self, df):
        st.header('Numerical Features Distribution')

        fig = px.histogram(df, x='amount', color='isFraudProba', opacity=.9, log_y=True, nbins=50,
                        color_discrete_sequence=['blue', 'red'], title="Amount Histogram")
        fig.update_layout(plot_bgcolor='#0e1117')
        st.plotly_chart(fig, use_container_width=True)

        c1, c2 = st.columns((2))

        fig = px.histogram(df, x='oldbalanceOrg', color='isFraudProba', opacity=.9, log_y=True, nbins=25,
                        color_discrete_sequence=['yellow', 'red'], title="Old Balance Origin Histogram")
        fig.update_layout(plot_bgcolor='#0e1117')
        c1.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df, x='newbalanceOrig', color='isFraudProba', opacity=.9, log_y=True, nbins=25,
                        color_discrete_sequence=['yellow', 'red'], title="New Balance Origin Histogram")
        fig.update_layout(plot_bgcolor='#0e1117')
        c2.plotly_chart(fig, use_container_width=True)

        c1, c2 = st.columns((2))

        fig = px.histogram(df, x='oldbalanceDest', color='isFraudProba', opacity=.9, log_y=True, nbins=25,
                        color_discrete_sequence=['yellow', 'red'], title="Old Balance Dest Histogram")
        fig.update_layout(plot_bgcolor='#0e1117')
        c1.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df, x='newbalanceDest', color='isFraudProba', opacity=.9, log_y=True, nbins=25,
                        color_discrete_sequence=['yellow', 'red'], title="New Balance Dest Histogram")
        fig.update_layout(plot_bgcolor='#0e1117')
        c2.plotly_chart(fig, use_container_width=True)

        return None