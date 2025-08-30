# Financial Data Analyzer  

## The first challenge: Data Exploration  
The project begins with analyzing and exploring **historical stock price data**. To make this process smooth, the tool provides a **command-line interface (CLI)** that allows quick access to different types of financial analyses. This ensures flexibility and keeps the program lightweight, while still offering a wide range of functionalities.  

## The second challenge: Visualization  
Understanding markets requires more than raw numbers. To address this, the analyzer generates **interactive charts** for price trends, trading volume, and volatility. It also supports **moving average analysis**, with calculations for both 5-day and 20-day simple moving averages (SMA), helping to identify patterns and market signals.  

## The third challenge: Predictions and Statistics  
Stock data can be unpredictable, so statistical methods are essential. The project integrates a **linear regression model** to provide simple price forecasts, along with statistical tools such as the **Runs Test** for randomness evaluation and **histograms** for price distribution. Additionally, the analyzer computes **daily returns** and **cumulative returns**, offering insights into profitability over time.  

## The final challenge: Correlation Analysis  
Market behavior is influenced by many factors, one of them being **trading volume**. The analyzer measures the **correlation between price and volume**, helping to uncover relationships that may not be visible at first glance.  

## Results  
To keep the project organized and adaptable, the implementation is divided into two main components:  

- **`utils.py`** → Contains all core data analysis functions (volatility, moving averages, predictions, etc.), each encapsulated in a separate function.  
- **`main.py`** → Hosts the CLI, which guides the user through a menu of available analyses and generates results on demand.  
