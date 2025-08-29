import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression


def runs_test(series):

    if len(series) < 2:
        return 1
    runs = 1
    for i in range(1, len(series)):
        if series[i] != series[i - 1]:
            runs += 1
    return runs


def get_data(file_path):
    """
    Încarcă datele, le curăță și le returnează.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Eroare: Fișierul nu a fost găsit la calea specificată: {file_path}")
        return None

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Daily_Return'] = df['Price'].pct_change()
    df.dropna(inplace=True)
    return df


def basic_analysis(df):
    """
    Afișează informații de bază despre date.
    """
    print("\nDatele încărcate sunt:")
    print(df.head())
    print("\nInformații despre date:")
    print(df.info())
    print("\nStatistici de bază:")
    print(df.describe())


def plot_price_trend(df):
    """
    Creează un grafic cu trendul prețurilor.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Price'], label='Preț', color='blue')
    plt.title('Trendul Prețurilor în Timp')
    plt.xlabel('Dată')
    plt.ylabel('Preț')
    plt.legend()
    plt.grid(True)
    plt.show()


def analyze_volatility(df):
    """
    Calculează și vizualizează volatilitatea.
    """
    volatility = np.std(df['Daily_Return']) * np.sqrt(252)
    print(f"\nVolatilitatea anualizată a prețurilor este: {volatility:.4f}")

    df['Volatility'] = df['Daily_Return'].abs()
    plt.figure(figsize=(12, 6))
    plt.bar(df.index, df['Volatility'], color='purple', alpha=0.7)
    plt.title('Volatilitatea Zilnică (Deviația Absolută)')
    plt.xlabel('Dată')
    plt.ylabel('Volatilitate')
    plt.grid(True, axis='y', linestyle='--')
    plt.show()

    print("\n--- Analiza Volatilității ---")
    print(f"Volatilitatea maximă zilnică: {df['Volatility'].max():.4f}")
    print(f"Volatilitatea minimă zilnică: {df['Volatility'].min():.4f}")
    print(f"Media volatilității zilnice: {df['Volatility'].mean():.4f}")


def analyze_moving_averages(df):
    """
    Calculează și vizualizează mediile mobile.
    """
    df['SMA_5'] = df['Price'].rolling(window=5).mean()
    df['SMA_20'] = df['Price'].rolling(window=20).mean()

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Price'], label='Preț', color='blue')
    plt.plot(df.index, df['SMA_5'], label='Media Mobilă (5 zile)', color='orange', linestyle='--')
    plt.plot(df.index, df['SMA_20'], label='Media Mobilă (20 zile)', color='red', linestyle='--')
    plt.title('Prețul și Mediile Mobile')
    plt.xlabel('Dată')
    plt.ylabel('Preț')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\n--- Analiza Mediilor Mobile ---")
    print("Ultimele valori ale mediilor mobile:")
    print(df[['SMA_5', 'SMA_20']].tail())


def predict_prices(df):
    """
    Realizează o predicție simplă de preț.
    """
    df_pred = df.copy()
    X = np.array(range(len(df_pred))).reshape(-1, 1)
    y = df_pred['Price'].values
    model = LinearRegression()
    model.fit(X, y)

    future_days = np.array(range(len(df_pred), len(df_pred) + 5)).reshape(-1, 1)
    predicted_prices = model.predict(future_days)

    print("\nPredicțiile prețurilor pentru următoarele 5 zile:")
    for i, price in enumerate(predicted_prices, 1):
        print(f"Ziua {i}: {price:.2f}")

    plt.figure(figsize=(10, 6))
    plt.plot(df_pred.index, df_pred['Price'], label='Prețuri reale', color='blue')
    future_dates = pd.date_range(start=df_pred.index[-1], periods=6, freq='B')[1:]
    plt.plot(future_dates, predicted_prices,
             label='Predicții', color='red', linestyle='--')
    plt.title('Trendul Prețurilor și Predicții')
    plt.xlabel('Dată')
    plt.ylabel('Preț')
    plt.legend()
    plt.grid(True)
    plt.show()


def analyze_correlation_and_volume(df):
    """
    Analizează corelația preț-volum și vizualizează volumul.
    """
    print("\n--- Analiza Corelației ---")
    if 'Volume' in df.columns and len(df) > 1:
        prices = df['Price']
        volumes = df['Volume']
        correlation_coefficient, p_value = pearsonr(prices, volumes)

        print(f"Coeficient de corelație Pearson între Preț și Volum: {correlation_coefficient:.2f}")
        print(f"Valoarea p: {p_value:.4f}")

        if p_value < 0.05:
            if abs(correlation_coefficient) > 0.5:
                print("Există o corelație semnificativă și puternică între preț și volum.")
            else:
                print("Există o corelație semnificativă, dar slabă între preț și volum.")
        else:
            print("Nu există o corelație semnificativă statistic între preț și volum.")
    else:
        print("Coloana 'Volume' nu există sau datele sunt insuficiente pentru analiză.")

    plt.figure(figsize=(10, 6))
    plt.bar(df.index, df['Volume'], color='green', alpha=0.6, label='Volum de Tranzacționare')
    plt.title('Volumul de Tranzacționare în Timp')
    plt.xlabel('Dată')
    plt.ylabel('Volum')
    plt.legend()
    plt.grid(True, axis='y', linestyle='--')
    plt.show()

    print("\n--- Analiza Volumului ---")
    print(f"Volumul total de tranzacționare: {df['Volume'].sum():.2f}")
    print(f"Volumul mediu zilnic: {df['Volume'].mean():.2f}")
    print(f"Ziua cu cel mai mare volum: {df['Volume'].idxmax().strftime('%Y-%m-%d')} ({df['Volume'].max():.2f})")


def analyze_distribution_and_runs_test(df):
    """
    Analizează distribuția prețurilor și efectuează un Runs Test.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribuția Frecvenței Prețurilor')
    plt.xlabel('Preț')
    plt.ylabel('Frecvență')
    plt.grid(axis='y', linestyle='--')
    plt.show()

    price_changes = np.sign(df['Daily_Return'].dropna())
    price_changes = price_changes[price_changes != 0]

    if len(price_changes) > 1:
        num_runs = runs_test(price_changes)
        print("\n--- Analiza Distribuției și Runs Test ---")
        print(f"Numărul de serii de preț: {num_runs}")
    else:
        print("\nDate insuficiente pentru a efectua Runs Test.")


def analyze_returns(df):
    """
    Vizualizează randamentele zilnice și calculează randamentul cumulativ.
    """
    daily_returns = df['Daily_Return'].dropna()

    # Vizualizare randamente zilnice
    plt.figure(figsize=(12, 6))
    colors = ['green' if x > 0 else 'red' for x in daily_returns]
    plt.bar(daily_returns.index, daily_returns, color=colors, alpha=0.7)
    plt.title('Randamentele Zilnice')
    plt.xlabel('Dată')
    plt.ylabel('Randament (%)')
    plt.grid(True, axis='y', linestyle='--')
    plt.show()

    # Calcul și vizualizare randament cumulativ
    cumulative_returns = (1 + daily_returns).cumprod()

    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_returns.index, cumulative_returns, color='blue', label='Randament Cumulativ')
    plt.title('Randamentul Cumulativ')
    plt.xlabel('Dată')
    plt.ylabel('Randament')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\n--- Analiza Randamentelor ---")
    print(f"Randamentul total: {(cumulative_returns.iloc[-1] - 1) * 100:.2f}%")
    print(f"Randamentul mediu zilnic: {daily_returns.mean() * 100:.2f}%")