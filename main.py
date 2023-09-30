dict_month = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}

class Currency:
    "Информация о валюте в рублях"
    def __init__(self, FirstRate: str, SecondRate: str, rate: str, data) -> None:
        self.FirstRate, self.SecondRate, self.rate, self.data = FirstRate, SecondRate, rate, data

class Data:
    def __init__(self, data: str):
        data = data.split(".")
        self.year = data[2]
        self.month = int(data[1])
        self.day = data[0]
    def __str__(self) -> str:
        return f"{self.day} {dict_month.get(self.month)} {self.year}"

def file_operations() -> list:
    with open("test.txt") as file:
        CurrencyInformation = list()
        while True:
            FirstRate = file.readline()
            if FirstRate == "":
                break
            else:
                FirstRate = FirstRate[:-1]
            SecondRate = file.readline()[:-1]
            rate = file.readline()[:-1]
            data = file.readline()
            if data[-1] == "\n":
                data = data[:-1]

            datas = Data(data)
            CurrencyInformation.append(Currency(FirstRate, SecondRate, rate, datas))
    return CurrencyInformation
def information(CurrencyInformation: list) -> None:
    for i in CurrencyInformation:
        print(f"Курс {i.SecondRate} на {i.FirstRate} составляет {i.rate} на {i.data}")

information(file_operations())