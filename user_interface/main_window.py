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
        if file_processor.delete_columns():  # Check if columns were deleted
        # Clear the old table and display the updated DataFrame
            st.text("Updated Data Overview:")
            st.write(dataframe.head())

        display_data_information(dataframe)
        display_missing_values(dataframe)
        display_descriptive_statistics(dataframe)




    if file_processor.confirm_target_class:
        st.sidebar.subheader('Selected Target Class:')
        st.sidebar.write(file_processor.target_class)

        handle_missing_values = file_processor.handle_missing_values()

        if handle_missing_values == "Imputation":
            # Perform missing value imputation
            pass
        elif handle_missing_values == "Deletion":
            # Perform missing value deletion
            pass
        else:
            # No action for "None" selected for missing value handling
            pass

        categorical_encoding_option = file_processor.encode_categorical_variables()

        if categorical_encoding_option == "One-Hot Encoding":
            # Perform one-hot encoding
            pass
        elif categorical_encoding_option == "Label Encoding":
            # Perform label encoding
            pass
        else:
            # No action for "None" selected for categorical encoding
            pass

        handling_outliers = file_processor.handling_outliers()

        if handling_outliers == "Z-score":
            # Perform Z-score outlier handling
            pass
        elif handling_outliers == "IQR":
            # Perform IQR outlier handling
            pass
        else:
            # No action for "None" selected for outlier handling
            pass

        feature_scaling = file_processor.feature_scaling()

        if feature_scaling == "Normalization":
            # Perform normalization
            pass
        elif feature_scaling == "Standardization":
            # Perform standardization
            pass
        else:
            # No action for "None" selected for feature scaling
            pass



if __name__ == "__main__":
    main()

