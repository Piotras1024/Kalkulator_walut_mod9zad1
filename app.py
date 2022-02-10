from flask import Flask, render_template, redirect, request
import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0]['rates']

app = Flask(__name__)

with open('test_nbp.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    rates = writer.writerow(data[0]['rates'][0])


list_all_currency = data[0]['rates']
list_keys = list(data[0]['rates'][0].keys())

currency_py = list_keys[0]
code_py = list_keys[1]
bid_py = list_keys[2]
ask_py = list_keys[3]







@app.route('/', methods=['GET', 'POST'])
def kalkulator_walut():
    if request.method == 'GET':
        return render_template("kalkulator_walut.html")

    elif request.method == 'POST':
        how_much_cash = request.form['cash']
        currency_choosen = request.form['currency']
        for dict_waluta in list_all_currency:
            if dict_waluta[currency_py] == currency_choosen:
                currency_price = dict_waluta[ask_py]
                suma_zl = currency_price*float(how_much_cash)
                return f" Za {how_much_cash} waluty {currency_choosen} do zapłacenie będzie {suma_zl} zł, po kursie {currency_price} za 1 {currency_choosen}"

        return redirect("")











# for waluta in data[0]['rates'][waluta]



# [    print(data[0]['rates'][2]['currency'])
#     {
#         'table': 'C', 'no': '026/C/NBP/2022', 'tradingDate': '2022-02-07', 'effectiveDate': '2022-02-08', 'rates':
#         [
#             {'currency': 'dolar amerykański', 'code': 'USD', 'bid': 3.9281, 'ask': 4.0075},
#             {'currency': 'dolar australijski', 'code': 'AUD', 'bid': 2.7975, 'ask': 2.8541},
#             {'currency': 'doar kanadyjski', 'code': 'CAD', 'bid': 3.0937, 'ask': 3.1561},
#             {'currency': 'euro', 'code': 'EUR', 'bid': 4.493, 'ask': 4.5838},
#             {'currency': 'forint (Węgry)', 'code': 'HUF', 'bid': 0.012708, 'ask': 0.012964},
#             {'currency': 'frank szwajcarski', 'code': 'CHF', 'bid': 4.2541, 'ask': 4.3401},
#             {'currency': 'funt szterling', 'code': 'GBP', 'bid': 5.3146, 'ask': 5.422},
#             {'currency': 'jen (Japonia)', 'code': 'JPY', 'bid': 0.03414, 'ask': 0.03483},
#             {'currency': 'korona czeska', 'code': 'CZK', 'bid': 0.1856, 'ask': 0.1894},
#             {'currency': 'korona duńska', 'code': 'DKK', 'bid': 0.6035, 'ask': 0.6157},
#             {'currency': 'korona norweska', 'code': 'NOK', 'bid': 0.4471, 'ask': 0.4561},
#             {'currency': 'korona szwedzka', 'code': 'SEK', 'bid': 0.4303, 'ask': 0.4389},
#             {'currency': 'SDR (MFW)', 'code': 'XDR', 'bid': 5.5128, 'ask': 5.6242}
#         ]
#     }
# ]

