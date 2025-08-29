import pandas as pd
from utils import get_data, basic_analysis, plot_price_trend, analyze_volatility, \
                   analyze_moving_averages, predict_prices, analyze_correlation_and_volume, \
                   analyze_distribution_and_runs_test, analyze_returns

def main():
    file_path = '../data/sample_stock_data.csv'
    df = get_data(file_path)

    if df is None:
        return

    while True:
        print("\n--- FinancialDataAnalyzer ---")
        print("Selectează o opțiune pentru analiză:")
        print("1. Analiza de bază (informații și statistici)")
        print("2. Vizualizare trend prețuri")
        print("3. Analiza volatilității")
        print("4. Analiza mediilor mobile")
        print("5. Predicție prețuri (regresie liniară)")
        print("6. Analiza corelației și a volumului")
        print("7. Analiza distribuției și Runs Test")
        print("8. Analiza randamentelor")
        print("9. Ieșire")

        choice = input("Introdu numărul opțiunii (1-9): ")
        print("-" * 20)

        if choice == '1':
            basic_analysis(df)
        elif choice == '2':
            plot_price_trend(df)
        elif choice == '3':
            analyze_volatility(df)
        elif choice == '4':
            analyze_moving_averages(df)
        elif choice == '5':
            predict_prices(df)
        elif choice == '6':
            analyze_correlation_and_volume(df)
        elif choice == '7':
            analyze_distribution_and_runs_test(df)
        elif choice == '8':
            analyze_returns(df)
        elif choice == '9':
            print("Programul a fost închis.")
            break
        else:
            print("Opțiune invalidă. Te rog să alegi un număr de la 1 la 9.")

if __name__ == "__main__":
    main()