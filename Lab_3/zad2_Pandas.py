# 2. Pandas
#   a. pobierz dane: https://huggingface.co/datasets/imodels/credit-card
#   b. sprawdź czy dane nie zawierają duplikatów
#   c. oblicz korelację pomiędzy wiekiem i limitem kredytu
#   d. dodaj kolumnę będącą sumą wszystkich transakcji (bill_amt_X)
#   e. znajdź 10 najstarszych klientów i narysuj tabelkę w której będą znajdować się
#       tylko kolumny: limit_bal, age, education (po nazwie), oraz nowo dodana
#       kolumna
#   f. używając matplotlib narysuj w jednym oknie (subplots) histogram limitu
#       kredytu, wieku, oraz zależność limitu kredytu od wieku



import pandas as pd
import matplotlib.pyplot as plt

# # a. Pobierz dane
# url = "https://huggingface.co/datasets/imodels/credit-card"
# data = pd.read_csv(url)

# a. Wczytaj dane z pliku CSV
file_path = "train.csv"
data = pd.read_csv(file_path)
#print(data)
#print(data[:5])


# b. Sprawdź czy dane nie zawierają duplikatów
if data.duplicated().any():
    print("Dane zawierają duplikaty")
else:
    print("Dane nie zawierają duplikatów")


# c. Oblicz korelację pomiędzy wiekiem i limitem kredytu
correlation = data['age'].corr(data['limit_bal'])
print(f"Korelacja pomiędzy wiekiem a limitem kredytu: {correlation}")


# d. Dodaj kolumnę będącą sumą wszystkich transakcji (bill_amt_X)
data['total_bill_amt'] = data.filter(like='bill_amt').sum(axis=1)


# e. Znajdź 10 najstarszych klientów i wyświetl wybrane kolumny
print("10 najstarszych klientów: ")

# oldest_clients = data.nlargest(10, 'age')[['limit_bal', 'age']]
# print(oldest_clients)

oldest_clients = data.nlargest(10, 'age')
# print(oldest_clients)
# print(oldest_clients.loc[:, ['limit_bal', 'age']])
#print(oldest_clients[['limit_bal', 'age', 'education:1', 'education:2', 'education:3', 'education:4', 'education:5', 'education:6', 'marriage:1', 'marriage:2', 'marriage:3']])
#print(oldest_clients[['limit_bal', 'age', 'education:0', 'education:1', 'education:2', 'education:3', 'total_bill_amt']])
#print(oldest_clients[['limit_bal', 'age', data.filter(like='education'), 'total_bill_amt']])  <-- nie dziala
# print(oldest_clients[['limit_bal', 'age'] + list(data.filter(regex='^edu')) + ['total_bill_amt']])
print(oldest_clients[['limit_bal', 'age'] + list(data.filter(like='education')) + ['total_bill_amt']])



# f. Narysuj histogramy i zależność

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
#       Ustawienie tytułu całego wykresu
fig.suptitle("Histogramy limitu kredytu, wieku, oraz zależność limitu kredytu od wieku\n", fontsize=16)
fig.canvas.manager.set_window_title('Histogramy')   #Tytuł okienka

# Histogram limitu kredytu
axes[0, 0].hist(data['limit_bal'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Histogram limitu kredytu')
axes[0, 0].set_xlabel('Limit kredytu')   # 1e6 = 1*10^(6)

# Histogram wieku
axes[0, 1].hist(data['age'], bins=20, color='lightcoral', edgecolor='black')
axes[0, 1].set_title('Histogram wieku')
axes[0, 1].set_xlabel('Wiek')

# Zależność limitu kredytu od wieku
axes[1, 0].scatter(data['age'], data['limit_bal'], alpha=0.5, color='orange')
axes[1, 0].set_title('Zależność limitu kredytu od wieku')
axes[1, 0].set_xlabel('Wiek')
axes[1, 0].set_ylabel('Limit kredytu')

# Ukryj puste miejsce w ostatniej komórce
axes[1, 1].axis('off')

# Dostosuj układ
plt.tight_layout()

# Wyświetl wykresy
plt.show()






