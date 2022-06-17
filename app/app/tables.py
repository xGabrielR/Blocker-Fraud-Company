import streamlit as st
from numpy import mean, median, std, unique
from pandas import DataFrame, merge, concat, IndexSlice

class AppTables(object):

    def get_numerical_description(self, df):
        num_att = df.select_dtypes(exclude=['object'])
        d1 = DataFrame(num_att.apply(mean)).T
        d2 = DataFrame(num_att.apply(median)).T
        c1 = DataFrame(num_att.apply(std)).T
        c2 = DataFrame(num_att.apply(min)).T
        c3 = DataFrame(num_att.apply(max)).T

        num_descp = concat([c2, c3, d1, d2, c1]).T
        num_descp.columns = ['min', 'max', 'mean', 'median', 'std']

        return num_descp

    def get_type_description(self, df):
        aux1 = df[['type', 'amount']].groupby('type').median().reset_index()
        aux2 = df[['type', 'oldbalanceOrg']].groupby('type').median().reset_index()
        aux3 = df[['type', 'newbalanceOrig']].groupby('type').median().reset_index()

        m1 = merge(aux1, aux2, on='type', how='inner')
        cat_descp = merge(m1, aux3, on='type', how='inner').set_index('type')
        cat_descp['Type'] = 'Median / Type'
        cat_descp = cat_descp.set_index('Type', append=True).unstack('Type')

        return cat_descp

    def descriptive_statistical(self, df):
        m = self.get_numerical_description(df)
        c = self.get_type_description(df)

        return {'num_att':m,'cat_att':c}

    def filtred_dataset(self, df, radio_fraud, list_filters: list):
        if not df.empty:

            for k in list_filters:
                if k == []: df = df.iloc[:, :]
                else: df = df.loc[df['type'].isin(list_filters[0]), :]

            if radio_fraud == "All Dataset":
                df = df.copy()

            elif radio_fraud == "Fraud Detected":
                df = df.loc[df["isFraudProba"] > 0]

            elif radio_fraud == "No Fraud Detected":
                df = df.loc[df["isFraudProba"] <= 0]

            if df.empty:
                return "Please, check the filter OR this user / payment do not match with is Fraud Filter"

        else:
            return 'Dataset is Empty!'

        return df

    def table_filters(self, df):
            st.sidebar.title("Geral Table Filters")
            st.sidebar.write('___')
            pay_type_filter = st.sidebar.multiselect("Payment Transaction Type", options=unique(df['type'].tolist()))
            name_org_filter = st.sidebar.multiselect("Name of Transaction Orig", options=unique(df['nameOrig'].tolist()))
            name_des_filter = st.sidebar.multiselect("Name of Transaction Dest", options=unique(df['nameDest'].tolist()))
            is_fraud_filter = st.sidebar.radio("Is Fraud Dataset Filter ?", options=["All Dataset", "Fraud Detected", "No Fraud Detected"], )

            df = self.filtred_dataset(df, is_fraud_filter, 
                                [pay_type_filter, name_org_filter, name_des_filter])

            return df

    def show_dataset_tables(self, df):
        if type(df).__name__ == "DataFrame":

            st.title("Data Overview")
            st.header("🔎 M.L Fraud Detection Dataset")
            st.dataframe(df.sort_values(by="isFraudProba", ascending=False)#.style
                        .style.format(precision=1, thousands=',')
                        .highlight_max(color='#4a0000', subset=IndexSlice[:, "isFraudProba"]))

            c1, c2 = st.columns((2))
            c1.header("Descriptive Statistical")
            c1.dataframe(self.descriptive_statistical(df)['num_att']#.style
                        .style.format(precision=1, thousands=',')
                        .highlight_max(color="#160e3d", 
                                        subset=IndexSlice[:, ["max", "mean", "median"]]))

            c2.header("Transaction Type Overview")
            c2.dataframe(self.descriptive_statistical(df)['cat_att']#.style
                        .style.format(precision=2, thousands=',')
                        .highlight_max(color='#160e3d'))

        else:
            st.title(df)