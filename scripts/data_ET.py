import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('../sql/fake_data.csv')
print("Extract completed successfully.")
# Display the DataFrame
num_rows_with_nulls = df.isnull().any(axis=1).sum()

column_cleaning_config = {
    'Property_Title': {'type': 'string', 'default': 'Unknown', 'required': True},
    'Address': {'type': 'string', 'default': 'Unknown', 'required': True},
    'Reviewed_Status': {'type': 'string', 'default': 'Unknown'},
    'Most_Recent_Status': {'type': 'string', 'default': 'Unknown'},
    'Source': {'type': 'string', 'default': 'Unknown'},
    'Market': {'type': 'string', 'default': 'Unknown'},
    'Occupancy': {'type': 'string', 'default': 'Unknown'},
    'Flood': {'type': 'bool', 'default': False},
    'Street_Address': {'type': 'string', 'default': 'Unknown'},
    'City': {'type': 'string', 'default': 'Unknown'},
    'State': {'type': 'string', 'default': 'Unknown'},
    'Zip': {'type': 'int', 'default': None},
    'Property_Type': {'type': 'string', 'default': 'Unknown'},
    'Highway': {'type': 'bool', 'default': False},
    'Train': {'type': 'bool', 'default': False},
    'Tax_Rate': {'type': 'float', 'default': 0.0},
    'SQFT_Basement': {'type': 'float', 'default': 0.0},
    'HTW': {'type': 'string', 'default': 'Unknown'},
    'Pool': {'type': 'bool', 'default': False},
    'Commercial': {'type': 'bool', 'default': False},
    'Water': {'type': 'string', 'default': 'Unknown'},
    'Sewage': {'type': 'string', 'default': 'Unknown'},
    'Year_Built': {'type': 'int', 'default': None},
    'SQFT_MU': {'type': 'float', 'default': 0.0},
    'SQFT_Total': {'type': 'float', 'default': 0.0},
    'Parking': {'type': 'string', 'default': 'Unknown'},
    'Bed': {'type': 'int', 'default': None},
    'Bath': {'type': 'float', 'default': 0.0},
    'BasementYesNo': {'type': 'bool', 'default': False},
    'Layout': {'type': 'string', 'default': 'Unknown'},
    'Net_Yield': {'type': 'float', 'default': 0.0},
    'IRR': {'type': 'float', 'default': 0.0},
    'Rent_Restricted': {'type': 'bool', 'default': False},
    'Neighborhood_Rating': {'type': 'string', 'default': 'Unknown'},
    'Previous_Rent': {'type': 'float', 'default': 0.0},
    'List_Price': {'type': 'float', 'default': 0.0},
    'Zestimate': {'type': 'float', 'default': 0.0},
    'ARV': {'type': 'float', 'default': 0.0},
    'Expected_Rent': {'type': 'float', 'default': 0.0},
    'Rent_Zestimate': {'type': 'float', 'default': 0.0},
    'Low_FMR': {'type': 'float', 'default': 0.0},
    'High_FMR': {'type': 'float', 'default': 0.0},
    'HOA': {'type': 'float', 'default': 0.0},
    'Underwriting_Rehab': {'type': 'float', 'default': 0.0},
    'Rehab_Calculation': {'type': 'float', 'default': 0.0},
    'Paint': {'type': 'bool', 'default': False},
    'Flooring_Flag': {'type': 'bool', 'default': False},
    'Foundation_Flag': {'type': 'bool', 'default': False},
    'Roof_Flag': {'type': 'bool', 'default': False},
    'HVAC_Flag': {'type': 'bool', 'default': False},
    'Kitchen_Flag': {'type': 'bool', 'default': False},
    'Bathroom_Flag': {'type': 'bool', 'default': False},
    'Appliances_Flag': {'type': 'bool', 'default': False},
    'Windows_Flag': {'type': 'bool', 'default': False},
    'Landscaping_Flag': {'type': 'bool', 'default': False},
    'Trashout_Flag': {'type': 'bool', 'default': False},
    'Latitude': {'type': 'float', 'default': None},
    'Longitude': {'type': 'float', 'default': None},
    'Subdivision': {'type': 'string', 'default': 'Unknown'},
    'Taxes': {'type': 'float', 'default': 0.0},
    'Redfin_Value': {'type': 'float', 'default': 0.0},
    'Selling_Reason': {'type': 'string', 'default': 'Unknown'},
    'Seller_Retained_Broker': {'type': 'bool', 'default': False},
    'HOA_Flag': {'type': 'bool', 'default': False},
    'Final_Reviewer': {'type': 'string', 'default': 'Unknown'},
    'School_Average': {'type': 'float', 'default': 0.0}
}

# Data Cleaning Function ie Removing nulls and empty values
def clean_dataframe(df: pd.DataFrame, config: dict):
    df.replace('', pd.NA, inplace=True)

    for col, rules in config.items():
        if col not in df.columns:
            continue
        
        col_type = rules.get('type')
        default = rules.get('default')
        required = rules.get('required', False)

        # Drop rows where required column is null
        if required:
            df = df[df[col].notna()]

        # Convert and fill based on type
        if col_type == 'bool':
            df[col] = df[col].fillna(default).astype(bool)
        elif col_type == 'string':
            df[col] = df[col].fillna(default).astype(str)
        elif col_type == 'int':
            df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
            if default is not None:
                df[col] = df[col].fillna(default)
        elif col_type == 'float':
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if default is not None:
                df[col] = df[col].fillna(default)
    return df

cleaned_df = clean_dataframe(df, column_cleaning_config)
num_rows_without_nulls = cleaned_df.isnull().any(axis=1).sum()

cleaned_df.to_csv('cleanData.csv', index=False)

print(num_rows_with_nulls,num_rows_without_nulls)
print("Transform completed successfully.")



