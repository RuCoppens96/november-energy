import pandas as pd
## Helpers
# This function generates a default gas consumption pattern for each month based on actual consumption data.
def generate_default_consumption_pattern_gas():
    """
    Generates a default gas consumption pattern for each month based on actual consulmption data.
    :return: DataFrame with default gas consumption pattern.
    """
    # Read the CSV file
    df = pd.read_csv('../data/raw/Verbruikshistoriek_gas_old.csv',  sep=';')
    
    # Filter rows based on column: 'Eenheid'
    df = df[df['Eenheid'] == "kWh"]

    # Filter DataFrame to keep only the last 12 months
    df['Month'] = pd.to_datetime(df['Month'], format='%d/%m/%Y')
    df = df.sort_values(by='Month', ascending=False).head(12)

    # Convert 'Volume' to numeric and normalize
    df['Volume'] = df['Volume'].str.replace(',', '.').astype(float)
    df['pattern'] = df['Volume'] / df['Volume'].sum()

    # Extract month number from 'Month' column
    df['month'] = df['Month'].dt.month

    # Select column: 'month'
    df = df.loc[:, ['month', 'pattern']]

    # Sort the DataFrame by month
    df = df.sort_values(by='month')

    # Add 'consumption_type' metadata
    df.attrs['consumption_type'] = 'Gas'
    return df.copy()

# This function generates a default electricity consumption pattern for each month based on actual consumption data.
# It is specifically for electricity consumption during the day.
def generate_default_consumption_pattern_electricity_day():
    """
    Generates a default eletricity during daytime consumption pattern for each month based on actual consulmption data.
    :return: DataFrame with default eletricity during daytime consumption pattern.
    """
    # Read the CSV file
    df = pd.read_csv('../data/raw/Verbruikshistoriek_elektriciteit_old.csv',  sep=';')
    
    # Filter rows based on column: 'Eenheid'
    df = df[df['Register'] == "Afname Dag"]

    # Filter DataFrame to keep only the last 12 months
    df['Month'] = pd.to_datetime(df['Month'], format='%d/%m/%Y')
    df = df.sort_values(by='Month', ascending=False).head(12)

    # Convert 'Volume' to numeric and normalize
    df['Volume'] = df['Volume'].str.replace(',', '.').astype(float)
    df['pattern'] = df['Volume'] / df['Volume'].sum()

    # Extract month number from 'Month' column
    df['month'] = df['Month'].dt.month

    # Select column: 'month'
    df = df.loc[:, ['month', 'pattern']]

    # Sort the DataFrame by month
    df = df.sort_values(by='month')

    # Add 'consumption_type' metadata
    df.attrs['consumption_type'] = 'eletricity Day'
    return df.copy()

def generate_default_consumption_pattern_electricity_night():
    """
    Generates a default eletricity during night consumption pattern for each month based on actual consulmption data.
    :return: DataFrame with default eletricity during night consumption pattern.
    """
    # Read the CSV file
    df = pd.read_csv('../data/raw/Verbruikshistoriek_elektriciteit_old.csv',  sep=';')
    
    # Filter rows based on column: 'Eenheid'
    df = df[df['Register'] == "Afname Nacht"]

    # Filter DataFrame to keep only the last 12 months
    df['Month'] = pd.to_datetime(df['Month'], format='%d/%m/%Y')
    df = df.sort_values(by='Month', ascending=False).head(12)

    # Convert 'Volume' to numeric and normalize
    df['Volume'] = df['Volume'].str.replace(',', '.').astype(float)
    df['pattern'] = df['Volume'] / df['Volume'].sum()

    # Extract month number from 'Month' column
    df['month'] = df['Month'].dt.month

    # Select column: 'month'
    df = df.loc[:, ['month', 'pattern']]

    # Sort the DataFrame by month
    df = df.sort_values(by='month')

    # Add 'consumption_type' metadata
    df.attrs['consumption_type'] = 'eletricity Night'
    return df.copy()


## The EnergyConsumption class is used to manage and analyze energy consumption data.
## It includes methods for generating default consumption patterns, calculating total consumption,
## and plotting consumption patterns.
class EnergyConsumption:
    def __init__(self, input_data_file = '../data/input/consumption.xlsx'):
        self.inputs = {
            'defaults': pd.read_excel(input_data_file, sheet_name='defaults'),
            'gas': pd.read_excel(input_data_file, sheet_name='digital_gas'),
            'electricity': pd.read_excel(input_data_file, sheet_name='digital_electricity')
        }

        self.default_VREG = self.VREG_API_defaults()

        self.default_consumption_pattern = {
            'Gas': generate_default_consumption_pattern_gas(),
            'Day': generate_default_consumption_pattern_electricity_day(),
            'Night': generate_default_consumption_pattern_electricity_night()
        }

        self.actual_consumption = {
            'Gas': self.get_actual_consumption_data('Gas'),
            'Day': self.get_actual_consumption_data('Day'),
            'Night': self.get_actual_consumption_data('Night')
        }



    # Get default yearly energy consumption via VREG API
    def VREG_API(self, personas, heatpump, car, hassolar, battery, solarpanels):
        """
        Retrieves default yearly energy consumption data from VREG API.
        :return: json with default yearly energy consumption data.
        """
        import requests

        # Prepare url and parameters
        url = 'https://vtest.vreg.be/Calculation/GetEstimates'
        params = {
            'electricity': 'true',
            'gas': 'true',
            'night': 'true',
            'digital': 'true',
            'persons': personas,
            'hassolar': hassolar,
            'heatpump': heatpump,
            'car': car,
            'battery': battery,
            'solarpanels': solarpanels
        }

        req = requests.models.PreparedRequest()
        req.prepare_url(url, params)
        url = req.url

        # Get response from API
        response = requests.get(url, headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

        if response.status_code == 200:
            data = response.json()
            return {key: data[key] for key in ['Day', 'Night', 'Gas']}
        else:
            raise Exception(f"Error fetching data: {response.status_code} - {response.text}")
    
    # Get default yearly energy consumption via VREG API based on 'defaults' sheet in input data file
    def VREG_API_defaults(self):
        """
        Retrieves default yearly energy consumption data from VREG API based on 'defaults' sheet in input data file.
        :return: dictonary with default yearly energy consumption data.
        """
        # Get parameters from defaults sheet
        personas = self.inputs['defaults'].iloc[0, 1]
        heatpump = self.inputs['defaults'].iloc[1, 1]
        car = self.inputs['defaults'].iloc[2, 1]
        hassolar = self.inputs['defaults'].iloc[3, 1]
        battery = self.inputs['defaults'].iloc[4, 1]
        solarpanels = self.inputs['defaults'].iloc[5, 1]

        return self.VREG_API(personas, heatpump, car, hassolar, battery, solarpanels)
    
  
    # Plot the default consumption pattern
    def plot_default_consumption_pattern(self, consumption_type):
        """
        Plots the default consumption pattern.
        :param df: DataFrame with default consumption pattern.
        """
        import matplotlib.pyplot as plt

        df = self.default_consumption_pattern[consumption_type]
        if df.empty:
            print(f"No data available for {consumption_type}.")
            return
        plt.figure(figsize=(6, 3))
        plt.plot(df['month'], df['pattern'], marker='o')
        plt.title('Default ' + df.attrs['consumption_type'] + ' Consumption Pattern')
        plt.xlabel('Month')
        plt.ylabel('Normalized Consumption Pattern')
        plt.xticks(df['month'])
        plt.grid()
        plt.show()
    
    # Plot the actual consumption data
    def plot_actual_consumption_data(self, consumption_type):
        """
        Plots the actual consumption data.
        :param df: DataFrame with actual consumption data.
        """
        import matplotlib.pyplot as plt

        df = self.actual_consumption[consumption_type]
        if df.empty:
            print(f"No data available for {consumption_type}.")
            return
        plt.figure(figsize=(6, 3))
        plt.plot(df['month'], df['Volume'], marker='o')
        plt.title('Actual ' + df.attrs['consumption_type'] + ' Consumption Data')
        plt.xlabel('Month')
        plt.ylabel('Consumption Volume')
        plt.xticks(df['month'], rotation=45)
        plt.grid()
        plt.show()

    # Get actual consumption data
    def get_actual_consumption_data(self, consumption_type):
        """
        Retrieves actual consumption data from the input data file.
        :param consumption_type: Type of consumption (Gas, Day, Night).
        :return: DataFrame with actual consumption data.
        """
        if consumption_type == 'Gas':
            df = self.inputs['gas']
            df = df[df['Eenheid'] == "kWh"]
            df = df[df['Validatiestatus'] == 'Uitgelezen']
            df.attrs['consumption_type'] = 'gas'
        elif consumption_type == 'Day':
            df = self.inputs['electricity'][self.inputs['electricity']['Register'] == "Afname Dag"]
            df = df[df['Validatiestatus'] == 'Uitgelezen']
            df.attrs['consumption_type'] = 'electricity Day'
        elif consumption_type == 'Night':
            df = self.inputs['electricity'][self.inputs['electricity']['Register'] == "Afname Nacht"]
            df = df[df['Validatiestatus'] == 'Uitgelezen']
            df.attrs['consumption_type'] = 'electricity Night'
        else:
            raise ValueError(f"Invalid consumption type: {consumption_type}")
        
        df['month'] = df['Van (datum)']
        df = df.loc[:, ['month', 'Volume']]
        return df.copy()
    
    # Get actual consumption data by consumption type for the last 12 months
    def get_actual_consumption_data_last_12_months_by_consumption_type(self, consumption_type):
        """
        Retrieves actual consumption data for the last 12 months.
        :param consumption_type: Type of consumption (Gas, Day, Night).
        :return: DataFrame with actual consumption data for the last 12 months.
        """
        df = self.get_actual_consumption_data(consumption_type)
        df['month'] = pd.to_datetime(df['month'], format='%d/%m/%Y')
        df = df.sort_values(by='month', ascending=False).head(12)
        return df['Volume'].sum()
    
    # Get actual consumption data for the last 12 months
    def get_actual_consumption_data_last_12_months(self):
        """
        Retrieves actual consumption data for the last 12 months.
        :return: DataFrame with actual consumption data for the last 12 months.
        """
        gas = self.get_actual_consumption_data_last_12_months_by_consumption_type('Gas')
        day = self.get_actual_consumption_data_last_12_months_by_consumption_type('Day')
        night = self.get_actual_consumption_data_last_12_months_by_consumption_type('Night')
        return {'Gas': gas, 'Day': day, 'Night': night}