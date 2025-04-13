import pandas as pd

##### Helper functions ######
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

# Plot the default consumption pattern
def plot_default_consumption_pattern(df):
    """
    Plots the default consumption pattern.
    :param df: DataFrame with default consumption pattern.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 3))
    plt.plot(df['month'], df['pattern'], marker='o')
    plt.title('Default ' + df.attrs['consumption_type'] + ' Consumption Pattern')
    plt.xlabel('Month')
    plt.ylabel('Normalized Consumption Pattern')
    plt.xticks(df['month'])
    plt.grid()
    plt.show()


## The EnergyConsumption class is used to manage and analyze energy consumption data.
## It includes methods for generating default consumption patterns, calculating total consumption,
## and plotting consumption patterns.
class EnergyConsumption:
    def __init__(self, history, default_consumption_pattern):
        self.history = history
        self.default_consumption_pattern = default_consumption_pattern
        self.consumption = pd.DataFrame(columns=['month', 'consumption'])
        self.consumpion_total = 0
        self.consumption_pattern = pd.DataFrame(columns=['month', 'pattern'])
