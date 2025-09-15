import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import os
import streamlit as st

def generate_eda_plots(df, output_dir):
    """
    Generate EDA plots for inflation data

    Args:
    df (pd.DataFrame): Preprocessed inflation data.
    output_dir (str): Directory to save plots
    
    """
    
    # Make sure output directory exists

    os.makedirs(output_dir, exist_ok=True)

    # Convert 'Year' to datetime if not already'
    if not pd.api.types.is_datetime64_any_dtype(df['Year']):
        df['Year'] = pd.to_datetime(df['Year'], format='%')

    # Time  series Plots
    plt.figure(figsize=(12,8))
    plt.plot(df['Year'], df['Inflation Rate'], marker='o', color='#1f77b4')
    plt.title("Historical Inflation Rates (1980 - 2024)", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Inflation Rate (%)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(os.path.join(output_dir, "historical_trend.png"))
    plt.close()

    # ACF/PACF Plots

    fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(12, 8))
    plot_acf(df['Inflation Rate'], lags=10, ax=ax1, title='Autocorrelation (ACF)')
    plot_pacf(df['Inflation Rate'], lags=10, ax=ax2, method='ywm', title='Partial_Autocorrelation(PACF)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "acf_pacf.png"))
    plt.close()


    # Display eda plots

    def display_eda_plots(df):
        """
        Generate EDA plots for inflation data

    Args:
    df (pd.DataFrame): Preprocessed inflation data.
    output_dir (str): Directory to save plots
        
        """

        st.subheader("Exploratory Data Analysis(EDA)")

        # Time series Plots

        st.write("###  Historical Inflation Rates (1980 - 2024)")
        fig1, ax1 = plt.subplots(figsize=(12,8))
        ax1 = plot(df['Year'], df['Inflation Rate'], marker='o', color='#1f77b4')
        ax1.set_xlabel("Year")
        ax1.set_yblabel("Inflation Rate (%)")
        ax1.grid(True, linestyle='--', alpha=0.7)
        st.pypplot(fig1)


        # ACF /PACF Plots

        st.write("### Autocorrelation and Partial Autocorrelation")
        fig2, (ax2, ax3) =plt.subplots(2, 1, figsize=(12,8))
        plot_acf(df['Inflation Rate'], lags=10, ax=ax1, title='Autocorrelation (ACF)')
        plot_pacf(df['Inflation Rate'], lags=10, ax=ax2, method='ywm', title='Partial_Autocorrelation(PACF)')
        plt.tight_layout()
        st.pyplot(fig2)

if __name__ == "__main__":
    # for standalone script usage
    data_path = os.path.join("..", "results", "cleaned_data.csv")
    output_dir = os.path.join("..", "results", "eda_plots")
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(data_path)
    df['Year'] = pd.to_datetime(df['Year'], formate='%Y')

    generate_eda_plots(df, output_dir)
                                
