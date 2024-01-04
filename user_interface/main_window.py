import streamlit as st
from Sidebar import Sidebar
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def display_data_information(dataframe):
    st.subheader("Data Information")
    st.write("Number of Rows:", dataframe.shape[0])
    st.write("Number of Columns:", dataframe.shape[1])
    st.write("Column Names:", dataframe.columns.tolist())
    st.write("Data Types:", dataframe.dtypes)

def display_missing_values(dataframe):
    st.subheader("Missing Values")
    missing_values = dataframe.isnull().sum()
    st.write(missing_values)

def display_descriptive_statistics(dataframe):
    st.subheader("Descriptive Statistics")
    st.write(dataframe.describe())








def main():
    file_processor = Sidebar()
    dataframe = file_processor.process_file()

    if dataframe is not None:
        display_data_information(dataframe)
        display_missing_values(dataframe)
        display_descriptive_statistics(dataframe)

    if file_processor.confirm_target_class:
        st.sidebar.subheader('Selected Target Class:')
        st.sidebar.write(file_processor.target_class)
        handle_missing_values = file_processor.handle_missing_values()
        feature_scaling = file_processor.feature_scaling()
        categorical_encoding_option = file_processor.encode_categorical_variables()
        handling_outliers = file_processor.handling_outliers()

        # Show data information

if __name__ == "__main__":
    main()

