import pandas as pd
from mysql.connector import MySQLConnection

# Read the Transformed CSV file into a DataFrame
df = pd.read_csv('./cleanData.csv')


# Connect to MySQL
conn = MySQLConnection(
    host='127.0.0.1',
    port=3306,
    user='db_user',
    password='6equj5_db_user',
    database='home_db'
)
print(conn)

if conn.is_connected():
    print("✅ Connected to MySQL successfully!")
else:
    print("❌ Connection failed.")
cursor = conn.cursor()

# Loop through each row
for _, row in df.iterrows():
    try:
        # 1. Insert into `property`
        cursor.execute("""
            INSERT INTO property (
                Property_Title, Address, Market, Flood, Street_Address, City, State, Zip,
                Property_Type, Highway, Train, Tax_Rate, SQFT_Basement, HTW, Pool,
                Commercial, Water, Sewage, Year_Built, SQFT_MU, SQFT_Total, Parking,
                Bed, Bath, BasementYesNo, Layout, Rent_Restricted, Neighborhood_Rating,
                Latitude, Longitude, Subdivision, School_Average
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row[col] for col in [
            'Property_Title', 'Address', 'Market', 'Flood', 'Street_Address',
            'City', 'State', 'Zip', 'Property_Type', 'Highway', 'Train', 'Tax_Rate',
            'SQFT_Basement', 'HTW', 'Pool', 'Commercial', 'Water', 'Sewage',
            'Year_Built', 'SQFT_MU', 'SQFT_Total', 'Parking', 'Bed', 'Bath',
            'BasementYesNo', 'Layout', 'Rent_Restricted', 'Neighborhood_Rating',
            'Latitude', 'Longitude', 'Subdivision', 'School_Average'
        ]))

        property_id = cursor.lastrowid

        # 2. Insert into `leads`
        cursor.execute("""
            INSERT INTO leads (
                property_id, Reviewed_Status, Most_Recent_Status, Source, Occupancy,
                Net_Yield, IRR, Selling_Reason, Seller_Retained_Broker, Final_Reviewer
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            property_id,
            row['Reviewed_Status'], row['Most_Recent_Status'], row['Source'], row['Occupancy'],
            row['Net_Yield'], row['IRR'], row['Selling_Reason'], row['Seller_Retained_Broker'],
            row['Final_Reviewer']
        ))

        # 3. Insert into `valuation`
        cursor.execute("""
            INSERT INTO valuation (
                property_id, Previous_Rent, List_Price, Zestimate, ARV,
                Expected_Rent, Rent_Zestimate, Low_FMR, High_FMR, Redfin_Value
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            property_id,
            row['Previous_Rent'], row['List_Price'], row['Zestimate'], row['ARV'],
            row['Expected_Rent'], row['Rent_Zestimate'], row['Low_FMR'],
            row['High_FMR'], row['Redfin_Value']
        ))

        # 4. Insert into `hoa`
        cursor.execute("""
            INSERT INTO hoa (property_id, HOA, HOA_Flag)
            VALUES (%s, %s, %s)
        """, (
            property_id, row['HOA'], row['HOA_Flag']
        ))

        # 5. Insert into `rehab`
        cursor.execute("""
            INSERT INTO rehab (
                property_id, Underwriting_Rehab, Rehab_Calculation, Paint,
                Flooring_Flag, Foundation_Flag, Roof_Flag, HVAC_Flag,
                Kitchen_Flag, Bathroom_Flag, Appliances_Flag, Windows_Flag,
                Landscaping_Flag, Trashout_Flag
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            property_id,
            row['Underwriting_Rehab'], row['Rehab_Calculation'], row['Paint'],
            row['Flooring_Flag'], row['Foundation_Flag'], row['Roof_Flag'],
            row['HVAC_Flag'], row['Kitchen_Flag'], row['Bathroom_Flag'],
            row['Appliances_Flag'], row['Windows_Flag'], row['Landscaping_Flag'],
            row['Trashout_Flag']
        ))

        # 6. Insert into `taxes`
        cursor.execute("""
            INSERT INTO taxes (property_id, Taxes)
            VALUES (%s, %s)
        """, (
            property_id, row['Taxes']
        ))

    except Exception as e:
        print(f"Error in row {_}: {e}")

# Final commit
conn.commit()
cursor.close()
conn.close()
print("Load completed successfully.")