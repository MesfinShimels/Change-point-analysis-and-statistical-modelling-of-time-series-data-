import pymc3 as pm
import numpy as np

def build_bayesian_model(prices):
    """Build a Bayesian model to analyze price changes."""
    with pm.Model() as model:
        # Priors
        alpha = pm.Normal('alpha', mu=0, sigma=10)
        beta = pm.Normal('beta', mu=0, sigma=10)
        sigma = pm.HalfNormal('sigma', sigma=1)
        
        # Likelihood
        mu = alpha + beta * prices
        likelihood = pm.Normal('likelihood', mu=mu, sigma=sigma, observed=prices)
        
        # Inference
        trace = pm.sample(1000, return_inferencedata=False)
    return trace

















    