import pandas as pd
import statsmodels.api as sm
import pymc3 as pm
import numpy as np

def fit_arima_model(df, order=(1,1,1)):
    """
    Fit an ARIMA model to the Brent oil price data.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing the 'Price' column.
        order (tuple): The (p,d,q) order of the ARIMA model.
        
    Returns:
        ARIMAResults: Fitted ARIMA model results.
    """
    model = sm.tsa.ARIMA(df['Price'], order=order)
    results = model.fit()
    return results

def forecast_arima(results, steps=30):
    """
    Forecast future prices using the fitted ARIMA model.
    
    Parameters:
        results: Fitted ARIMA model results.
        steps (int): Number of steps (days) to forecast.
        
    Returns:
        pd.Series: Forecasted values.
    """
    forecast = results.forecast(steps=steps)
    return forecast

def bayesian_modeling(df):
    """
    Build and run a simple Bayesian model using PyMC3.
    This example models the oil price as a normally distributed variable.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing the 'Price' column.
        
    Returns:
        model: The PyMC3 model.
        trace: Inference trace from sampling.
    """
    price_data = df['Price'].values
    with pm.Model() as model:
        # Priors for unknown model parameters
        sigma = pm.Exponential('sigma', 1.0)
        mu = pm.Normal('mu', mu=np.mean(price_data), sigma=10)
        
        # Likelihood (sampling distribution) of observations
        likelihood = pm.Normal('likelihood', mu=mu, sigma=sigma, observed=price_data)
        
        # Sampling from the posterior
        trace = pm.sample(1000, tune=1000, return_inferencedata=True)
        
    return model, trace
