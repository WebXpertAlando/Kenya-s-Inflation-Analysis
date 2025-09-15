import pandas as pd 
from statsmodels.tsa.arima.model import ARIMA 



def arima_forecast(df):
    # Ensure 'Year' is datetime or index (optional)
    df = df.copy()

    # Set 'Year' as index if needed
    if 'Year' in df.columns:
        df['Year'] = pd.to_datetime(df['Year'], format='%Y')
        df.set_index('Year', inplace=True)

    # Ensure Inflation Rate is numeric
    df['Inflation Rate'] = pd.to_numeric(df['Inflation Rate'], errors='coerce')

    # Drop rows with NaNs
    df = df.dropna(subset=['Inflation Rate'])

    # Fit ARIMA model
    model = ARIMA(df['Inflation Rate'], order=(1, 1, 1))
    results = model.fit()

    # Forecast next 5 years
    forecast = results.forecast(steps=5)

    forecast_years = pd.date_range(df.index[-1], periods=6, freq='Y')[1:]  # exclude last known
    forecast_df = pd.DataFrame({'Year': forecast_years.year, 'Forecast': forecast.values})

    return forecast_df