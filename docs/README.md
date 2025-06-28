# Data Engineering Assessment

Welcome!  
This exercise evaluates your core **data-engineering** skills:

| Competency | Focus                                                         |
| ---------- | ------------------------------------------------------------- |
| SQL        | relational modelling, normalisation, DDL/DML scripting        |
| Python ETL | data ingestion, cleaning, transformation, & loading (ELT/ETL) |

---

## 0 Prerequisites & Setup

> **Allowed technologies**

- **Python ≥ 3.8** – all ETL / data-processing code
- **MySQL 8** – the target relational database
- **Lightweight helper libraries only** (e.g. `pandas`, `mysql-connector-python`).  
  List every dependency in **`requirements.txt`** and justify anything unusual.
- **No ORMs / auto-migration tools** – write plain SQL by hand.

---

## 1 Clone the skeleton repo

```
git clone https://github.com/100x-Home-LLC/data_engineer_assessment.git
```

✏️ Note: Rename the repo after cloning and add your full name.

**Start the MySQL database in Docker:**

```
docker-compose -f docker-compose.initial.yml up --build -d
```

- Database is available on `localhost:3306`
- Credentials/configuration are in the Docker Compose file
- **Do not change** database name or credentials

For MySQL Docker image reference:
[MySQL Docker Hub](https://hub.docker.com/_/mysql)

---

### Problem

- You are provided with a raw JSON file containing property records is located in data/
- Each row relates to a property. Each row mixes many unrelated attributes (property details, HOA data, rehab estimates, valuations, etc.).
- There are multiple Columns related to this property.
- The database is not normalized and lacks relational structure.
- Use the supplied Field Config.xlsx (in data/) to understand business semantics.

### Task

- **Normalize the data:**

  - Develop a Python ETL script to read, clean, transform, and load data into your normalized MySQL tables.
  - Refer the field config document for the relation of business logic
  - Use primary keys and foreign keys to properly capture relationships

- **Deliverable:**
  - Write necessary python and sql scripts
  - Place your scripts in `sql/` and `scripts/`
  - The scripts should take the initial json to your final, normalized schema when executed
  - Clearly document how to run your script, dependencies, and how it integrates with your database.

**Tech Stack:**

- Python (include a `requirements.txt`)
  Use **MySQL** and SQL for all database work
- You may use any CLI or GUI for development, but the final changes must be submitted as python/ SQL scripts
- **Do not** use ORM migrations—write all SQL by hand

---

## Submission Guidelines

- Edit the section to the bottom of this README with your solutions and instructions for each section at the bottom.
- Place all scripts/code in their respective folders (`sql/`, `scripts/`, etc.)
- Ensure all steps are fully **reproducible** using your documentation
- Create a new private repo and invite the reviewer https://github.com/mantreshjain

---

**Good luck! We look forward to your submission.**

## Solutions and Instructions (Filed by Candidate)

**Document your database design and solution here:**

- I have taken starschema as the database design. The main table is taken as **property** , all other tables have property_id which is foreign key referencing the property    table.
- Other tables are :
    - **Valuation**
    - **Taxes**
    - **Rehab**
    - **Hoa**
    - **Leads**
- Give clear instructions on how to run and test your script
    - Step_1 : Fork and clone the repo so as to get your own copy.
    - Step_2 : Delete the cleanData.csv for seeing actual flow.(scripta > cleanData.csv). If not deleted also it will work.
    - Step_3 : Execute the sql script.(sql > sql_scripts.sql). Copy the scripts and paste it in SQL Query editor in Workbench and execute it.
    - Step_4 : Open the cloned project in VS code.
    - Step_5 : Now in terminal install required dependencies if do not have(pandas,mysql-connector-python) with 'pip install pandas' command
    - Step_6 : Now in terminal go inside scripts folder(cd .\scripts\) execute data_ET.py file(python data_ET.py). This will load and transform the data and create a new                   clean csv(ie cleanData.csv)
    - Step_7 : Now execute dataLoad.py(python dataLoad.py). This loads the data into respective tables.
   
**Document your ETL logic here:**

- Outline your approach and design
      Read the data > create a cleaning config to specify the type and default value > If any null or empty values add default values according to the type > create a clean
      csv file(Creating a new file is not necessary with same dataframe we can proceed if required) 
      In data Load > Open the db connection > make sure connection is valid > make sure the tables are created > run the load script 
- Provide instructions and code snippets for running the ETL
    - Step 1 : Create required tables in any databse using the sql create script in sql > sql_scripts.
    - Step 2 : Install required dependencies.
    - Step 3 : Run  data_ET.py file(python data_ET.py) then run dataLoad.py(python dataLoad.py)
- List any requirements
    `pandas`, `mysql-connector-python` 
