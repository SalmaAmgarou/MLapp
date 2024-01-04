import pandas as pd
import numpy as np
from scipy.stats import zscore, iqr
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


def handle_missing_values(data):
    # Loop through columns
    for column in data.columns:
        # Check data type of column
        if data[column].dtype == 'object':
            # For categorical columns, fill missing values with mode
            data[column].fillna(data[column].mode()[0], inplace=True)
        else:
            # For numerical columns, fill missing values with mean
            data[column].fillna(data[column].mean(), inplace=True)
    return data



class OutlierHandlingError(Exception):
    pass
class OutlierHandlingError(Exception):
    pass

def handle_outliers(data, method='zscore', threshold=3.0, action='remove'):
    try:
        if not isinstance(data, pd.DataFrame):
            raise OutlierHandlingError("Input should be a pandas DataFrame")

        outliers_dict = {}  # Dictionary to store outliers for each column

        for col in data.columns:
            if np.issubdtype(data[col].dtype, np.number):  # For numerical columns
                if method == 'zscore':
                    data[col + '_zscore'] = zscore(data[col])
                    outliers = data[np.abs(data[col + '_zscore']) > threshold]
                    if action == 'remove':
                        data = data[np.abs(data[col + '_zscore']) <= threshold]
                elif method == 'iqr':
                    q1 = data[col].quantile(0.25)
                    q3 = data[col].quantile(0.75)
                    iqr_val = q3 - q1
                    lower_bound = q1 - 1.5 * iqr_val
                    upper_bound = q3 + 1.5 * iqr_val
                    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
                    if action == 'remove':
                        data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
                else:
                    raise OutlierHandlingError("Unsupported outlier detection method")

                outliers_dict[col] = outliers  # Store outliers for each column

        return data, outliers_dict

    except OutlierHandlingError as e:
        print(f"Error in handling outliers: {e}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


    def handle_duplicates(data, method='remove'):
        try:
            if method == 'remove':
                # Remove duplicate rows
                data.drop_duplicates(inplace=True)
            elif method == 'keep_first':
                # Keep only the first occurrence of duplicates
                data.drop_duplicates(keep='first', inplace=True)
            elif method == 'keep_last':
                # Keep only the last occurrence of duplicates
                data.drop_duplicates(keep='last', inplace=True)
            elif method == 'highlight':
                # Add a flag column to highlight duplicates
                data['is_duplicate'] = data.duplicated()
            else:
                raise ValueError("Unsupported method for handling duplicates")

            return data

        except ValueError as e:
            print(f"Error in handling duplicates: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class CategoricalEncodingError(Exception):
    pass

def encode_categorical(data, strategy='one-hot'):
    try:
        if not isinstance(data, pd.DataFrame):
            raise CategoricalEncodingError("Input should be a pandas DataFrame")

        categorical_cols = [col for col in data.columns if data[col].dtype == 'object']

        if strategy == 'one-hot':
            encoder = OneHotEncoder(sparse=False, drop='first')
            encoded_data = pd.DataFrame(encoder.fit_transform(data[categorical_cols]))
            encoded_data.columns = encoder.get_feature_names(categorical_cols)
            data = pd.concat([data, encoded_data], axis=1)
            data.drop(categorical_cols, axis=1, inplace=True)
        elif strategy == 'label':
            label_encoder = LabelEncoder()
            for col in categorical_cols:
                data[col] = label_encoder.fit_transform(data[col])
        else:
            raise CategoricalEncodingError("Unsupported encoding strategy")

        return data

    except CategoricalEncodingError as e:
        print(f"Error in categorical encoding: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
class BinarizationError(Exception):
    pass

def binarize_data(data, threshold=0.0):
    try:
        if not isinstance(data, pd.DataFrame):
            raise BinarizationError("Input should be a pandas DataFrame")

        for col in data.columns:
            if np.issubdtype(data[col].dtype, np.number):
                data[col] = (data[col] > threshold).astype(int)
            else:
                raise BinarizationError(f"Column '{col}' is not numerical")

        return data

    except BinarizationError as e:
        print(f"Error in binarizing data: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


