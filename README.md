# masterthesis
# Recent Determinants of Real Estate Prices in USA, UK and France

This repository is a part of my master's thesis named Recent Determinants of Real Estate Prices in the USA, UK, and France. It contains the Python code used to gather and process the data required for the study.

Structure
The repository consists of two separate python files:

common.py - Contains custom functions for data collection using the Estated API.
main.py - The main script which utilizes the functions defined in common.py to gather real estate data for the USA, UK, and France.
Code Explanation
The code is divided into four main parts: preparation, execution, and optional graph visualization for each country (UK, France, and USA).

Preparation
Preparation involves reading necessary information such as the API keys and data fields to be used from Excel sheets. It also defines the API URLs and host names for each country.

The API_keys.xlsx file should contain your Estated API keys, and elements.xlsx should contain the parameters used for querying the Estated API for each country.

Execution
Execution uses the dataframe_generation function from common.py to send requests to the Estated API and store the responses in a DataFrame. It repeats this for each parameter in elements.xlsx.

It also handles errors and quotas from the API. If it encounters a 429 error (too many requests), it will switch to another API key (if available). If all quotas are exhausted, it prints an error message with the querystring that caused the quota to be exceeded.

After data collection, unnecessary columns are dropped to reduce the DataFrame's size. The cleaned data is then saved in a CSV file with the country name and the current date.

Optional Graph Visualization
The code also includes a section (commented out by default) for creating a graphical representation of the obtained data for the USA and the UK. This uses Plotly Express to create a scatter map plot of property locations.

Usage
To use this code, you will need to install the required Python libraries. You can do this with pip:

bash
Copy code
pip install pandas numpy openpyxl requests
Then, run the main.py script:

bash
Copy code
python main.py
Note
Please make sure that your API_keys.xlsx and elements.xlsx files are in the correct format and location.

This code does not perform any data cleaning beyond dropping specified unnecessary columns. You may need to further preprocess the data before using it for analysis.

