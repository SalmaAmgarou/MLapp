import streamlit as st
import pandas as pd
from io import StringIO, BytesIO
import json

class Sidebar:
    def __init__(self):
        self.uploaded_file = None
        self.dataframe = None
        self.target_class = None
        self.confirm_target_class = False








    def process_file(self):
        self.uploaded_file = st.sidebar.file_uploader("Choose a file")
        if self.uploaded_file is not None:
            if self.uploaded_file.name.endswith('.csv'):
                # CSV file
                self.dataframe = pd.read_csv(self.uploaded_file)
                self.select_target_class()
            elif self.uploaded_file.name.endswith('.json'):
                # JSON file
                string_data = self.uploaded_file.getvalue().decode("utf-8")
                data = json.loads(string_data)
                self.dataframe = pd.DataFrame(data)
                self.select_target_class()
            elif self.uploaded_file.name.endswith(('.xls', '.xlsx')):
                # Excel file
                bytes_data = self.uploaded_file.getvalue()
                self.dataframe = pd.read_excel(BytesIO(bytes_data))
                self.select_target_class()
            st.write(self.dataframe)
        return self.dataframe

    def select_target_class(self):
        st.sidebar.subheader('Select Target Class')
        target_col_options = self.dataframe.columns.tolist()
        target_col_options.insert(0, "None")

        self.target_class = st.sidebar.selectbox(
            "Choose the target class column:",
            target_col_options
        )

        st.sidebar.markdown(
            """
            <style>
            .stButton > button {
                display: block;
                margin: auto;
                width: 45%;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        confirm_button = st.sidebar.button("Confirm")

        if confirm_button:
            if self.target_class == "None":
                st.sidebar.warning("Please select a target class!")
            else:
                self.confirm_target_class = True

    def get_target_class(self):
        return self.target_class

    def handle_missing_values(self):
        st.sidebar.subheader('Handling Missing Values')
        missing_values_option = st.sidebar.selectbox(
            "Choose an option:",
            ("None",
             "Deletion",
             "Imputation")
        )
        return missing_values_option

    def feature_scaling(self):
        st.sidebar.subheader('Feature Scaling')
        feature_scaling_option = st.sidebar.selectbox(
            "Choose an option:",
            ("None",
             "Normalization",
             "Standardization"
             )
        )
        return feature_scaling_option

    def encode_categorical_variables(self):
        st.sidebar.subheader('Encoding Categorical Variables')
        categorical_encoding_option = st.sidebar.selectbox(
            "Choose an option:",
            ("None",
             "One-Hot Encoding",
             "Label Encoding")
        )
        return categorical_encoding_option

    def handling_outliers(self):
        st.sidebar.subheader('Handling Outliers')
        handling_outliers = st.sidebar.selectbox(
            "Choose an option:",
            ("None",
             "Z-score",
             "IQR")
        )
        return handling_outliers

    def delete_columns(self):
        st.sidebar.subheader('Delete Columns')
        columns_to_delete = st.sidebar.multiselect(
            "Select columns to delete:",
            self.dataframe.columns.tolist()
        )

        if st.sidebar.button("Delete Columns"):
            self.dataframe.drop(columns=columns_to_delete, inplace=True)
            return True  # Signal that columns were deleted
