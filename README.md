Brent Oil Prices Analysis and Dashboard
Project Title: Brent Oil Prices Analysis and Change Point Detection
Description:
This project, part of the "10 Academy: Artificial Intelligence Mastery" Week 10 Challenge, conducts change point analysis and statistical modeling on Brent oil price time series data. The primary objective is to detect significant price changes and to associate these changes with global events such as political decisions, conflicts, economic sanctions, and OPEC policy shifts. This analysis provides actionable insights for investors, analysts, and policymakers navigating the volatile energy market.

Business Objectives

Understand Global Impacts:
Analyze how major events (political, economic, regulatory) affect Brent oil prices.


Quantify Price Changes:
Measure the extent to which these events drive price fluctuations.


Inform Decision-Making:
Deliver data-driven insights to guide investment strategies, policy development, and operational planning within the energy sector.


Data Overview
Dataset: Historical Brent oil prices.
Time Period: May 20, 1987 to September 30, 2022.
Fields: 
oDate: Recorded date of the oil price (format: day-month-year, e.g., 20-May-87).
oPrice: Brent oil price in USD per barrel.

Project Tasks
1.
Defining the Data Analysis Workflow & Understanding the Model/Data
2.
oOutline steps from data collection and preprocessing to exploratory data analysis (EDA) and model evaluation.
oReview and select appropriate time series models (e.g., ARIMA, VAR, Markov-Switching ARIMA, LSTM).
oClarify model inputs, outputs, assumptions, and limitations.
3.
Time Series Analysis and Model Adaptation
4.
oApply time series analysis to the Brent oil dataset.
oExperiment with multiple models to capture various market conditions.
oIntegrate additional economic, technological, and regulatory indicators to refine analysis.
5.
Developing an Interactive Dashboard
6.
oBuild a dashboard using Flask (backend) and React (frontend) for interactive visualization.
oProvide features such as dynamic charts, filters, and date-range selection.
oVisualize historical trends, forecasting results, and correlations with key events.

Project Structure
brent-oil-analysis/
├── backend/              # Flask backend for APIs and analysis logic
│   ├── app.py            # Main application file with API endpoints
│   ├── analysis.py       # Data analysis and forecasting functions
│   ├── models.py         # Time series models (e.g., ARIMA)
│   ├── utils.py          # Utility functions (e.g., data loading)
│   ├── requirements.txt  # Python dependencies
│   └── README.md         # Backend-specific documentation
├── frontend/             # React frontend for the interactive dashboard
│   ├── package.json      # NPM package configuration
│   ├── public/           # Public assets (e.g., index.html)
│   ├── src/              # Source code (React components, services)
│   │   ├── index.js      # App entry point
│   │   ├── App.js        # Main React component
│   │   ├── components/   # UI components (Dashboard, ChartComponent, etc.)
│   │   └── services/     # API services for backend communication
│   └── README.md         # Frontend-specific documentation
├── data/                 # Data files
│   └── brent_oil_prices.csv  # Historical Brent oil prices dataset
├── notebooks/            # Jupyter notebooks for exploratory analysis
│   └── exploratory_analysis.ipynb  # EDA notebook
└── README.md             # Project overview and instructions (this file)

Setup Instructions
1. Backend Setup
1.
Navigate to the backend directory:
2.
cd backend
3.
4.
Create a virtual environment and activate it:
5.
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
6.
7.
Install dependencies:
8.
pip install -r requirements.txt
9.
10.
Run the Flask application:
11.
python app.py
12.
The API will run on http://localhost:5000.
13.
2. Frontend Setup
1.
Navigate to the frontend directory:
2.
cd frontend
3.
4.
Install dependencies:
5.
npm install
6.
7.
Start the development server:
8.
npm start
9.
The dashboard will be accessible at http://localhost:3000.
10.
3. Data Preparation
Place the brent_oil_prices.csv file in the data/ directory.
Ensure the CSV file includes at least the Date and Price columns in the specified formats.
4. Exploratory Analysis
Open the notebooks/exploratory_analysis.ipynb notebook to perform additional data exploration and prototyping.

Usage

Dashboard Exploration:
Use the React dashboard to view summary statistics and model forecasts (ARIMA) interactively.


API Endpoints:
The Flask backend provides endpoints (e.g., /api/summary and /api/forecast) that serve data for analysis and visualization.


Extensibility:
Enhance the project by integrating additional models (e.g., VAR, GARCH, LSTM) and incorporating more diverse data sources.


Future Enhancements

Advanced Models:
Implement further econometric and machine learning models for improved forecasting accuracy.


Expanded Data Sources:
Integrate economic indicators, technological advancements, and regulatory data for deeper analysis.


Enhanced Dashboard Features:
Add interactive filters, real-time updates, and detailed event analysis visualizations.


Contributing
Contributions to improve models, visualizations, or the overall functionality are welcome. Please open an issue or submit a pull request for enhancements or bug fixes.

License

Contact
For further inquiries or collaboration opportunities, please contact:
Mesfins973@gmail.com

This project was developed as part of the "10 Academy: Artificial Intelligence Mastery" program's Week 10 Challenge, aiming to deliver robust, data-driven insights into the dynamics of Brent oil prices and their relation to global events.
