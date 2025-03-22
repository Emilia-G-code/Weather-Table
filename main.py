import sqlite3
import requests

connection = sqlite3.connect("Weather.sl3")

cur = connection.cursor()

print(connection)
print(cur)
connection.close()


connection = sqlite3.connect("weather_data.sl3")
cur = connection.cursor()
cur.execute("CREATE TABLE students (date_time TEXT temperature TEXT")")
# подтверждаем
connection.commit()
connection.close()


response = requests.get("https://www.accuweather.com/en/az/baku/27103/daily-weather-forecast/27103")

print(response.text, "\n\n")

date_and_time = []

response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem1 in response_parse:
    if (parse_elem1.isdigit(3)):
      for parse_elem2 in parse_elem1.split("</span>"):
            if (parse_elem2.startswith("/") and parse_elem2[1].isdigit()):
                date_and_time.append(parse_elem1 and parse_elem2)

temperature_values = []

response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem1 in response_parse:
    if (parse_elem1.startswith("C)"))
            temperature_values.append(parse_elem1 and parse_elem2)

"""добавление элементов в таблицу"""
connection = sqlite3.connect("CPS_22134_DB.sl3")
cur = connection.cursor()
# выполняем скрипт позволяющий добавить элемент в таблицу
cur.execute("INSERT INTO weather_data (date_time) VALUES (date_and_time);")
cur.execute("INSERT INTO weather_data (temperature) VALUES (temperature_values);")
# подтверждаем
connection.commit()
connection.close()
