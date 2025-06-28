use home_db;

CREATE TABLE property (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Property_Title VARCHAR(255),
    Address VARCHAR(255),
    Street_Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Zip INT,
    Market VARCHAR(100),
    Flood BOOLEAN,
    Property_Type VARCHAR(100),
    Highway BOOLEAN,
    Train BOOLEAN,
    Tax_Rate DECIMAL(5,2),
    SQFT_Basement INT,
    HTW VARCHAR(50),
    Pool BOOLEAN,
    Commercial BOOLEAN,
    Water VARCHAR(50),
    Sewage VARCHAR(50),
    Year_Built INT,
    SQFT_MU INT,
    SQFT_Total INT,
    Parking VARCHAR(50),
    Bed INT,
    Bath INT,
    BasementYesNo BOOLEAN,
    Layout VARCHAR(100),
    Rent_Restricted BOOLEAN,
    Neighborhood_Rating INT,
    Latitude DECIMAL(9,6),
    Longitude DECIMAL(9,6),
    Subdivision VARCHAR(100),
    School_Average DECIMAL(5,2)
);

CREATE TABLE leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    Reviewed_Status VARCHAR(50),
    Most_Recent_Status VARCHAR(50),
    Source VARCHAR(100),
    Occupancy VARCHAR(50),
    Net_Yield DECIMAL(5,2),
    IRR DECIMAL(5,2),
    Selling_Reason VARCHAR(50),
    Seller_Retained_Broker BOOLEAN,
    Final_Reviewer VARCHAR(100),
    FOREIGN KEY (property_id) REFERENCES property(id)
);

CREATE TABLE valuation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    Previous_Rent INT,
    List_Price INT,
    Zestimate INT,
    ARV INT,
    Expected_Rent INT,
    Rent_Zestimate INT,
    Low_FMR INT,
    High_FMR INT,
    Redfin_Value INT,
    FOREIGN KEY (property_id) REFERENCES property(id)
);

CREATE TABLE hoa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    HOA INT,
    HOA_Flag BOOLEAN,
    FOREIGN KEY (property_id) REFERENCES property(id)
);

CREATE TABLE rehab (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    Underwriting_Rehab INT,
    Rehab_Calculation INT,
    Paint BOOLEAN,
    Flooring_Flag BOOLEAN,
    Foundation_Flag BOOLEAN,
    Roof_Flag BOOLEAN,
    HVAC_Flag BOOLEAN,
    Kitchen_Flag BOOLEAN,
    Bathroom_Flag BOOLEAN,
    Appliances_Flag BOOLEAN,
    Windows_Flag BOOLEAN,
    Landscaping_Flag BOOLEAN,
    Trashout_Flag BOOLEAN,
    FOREIGN KEY (property_id) REFERENCES property(id)
);

CREATE TABLE taxes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    Taxes INT,
    FOREIGN KEY (property_id) REFERENCES property(id)
);

