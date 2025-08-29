# Financial Data Analyzer

Un instrument de analiză și vizualizare a datelor financiare pentru a explora și a înțelege comportamentul piețelor pe baza datelor istorice ale prețurilor acțiunilor, dezvoltat în Python. Acest program oferă o interfață de linie de comandă (CLI) pentru a rula diverse analize pe date de prețuri de acțiuni, incluzând trenduri, volatilitate, medii mobile, predicții și randamente.

## Caracteristici Principale

* **Analiză de bază**: Vizualizare rapidă a statisticilor descriptive și a informațiilor despre date.
* **Grafice interactive**: Generează grafice pentru a vizualiza trendurile prețurilor, volatilitatea și volumele de tranzacționare.
* **Analiza Mediilor Mobile**: Calculează și vizualizează mediile mobile simple (SMA) pe 5 și 20 de zile.
* **Predicție simplă**: Folosește un model de regresie liniară pentru a prezice prețurile viitoare.
* **Analiză statistică**: Include un Runs Test pentru a evalua randomness-ul datelor și o histogramă pentru distribuția prețurilor.
* **Analiza Randamentelor**: Calculează și vizualizează randamentele zilnice și randamentul cumulativ total.
* **Corelație Preț-Volum**: Măsoară corelația dintre prețul acțiunilor și volumul de tranzacționare.

## Cum Funcționează

Proiectul este structurat în două componente principale:
* `utils.py`: Conține toate funcțiile logice de analiză a datelor. Fiecare tip de analiză (volatilitate, medii mobile, etc.) este încapsulat într-o funcție separată.
* `main.py`: Conține interfața de linie de comandă (CLI) care permite utilizatorului să selecteze analiza dorită dintr-un meniu.