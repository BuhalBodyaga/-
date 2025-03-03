# Пример использования
from main import generate_code
import requests

input_text = "Создать JSON-объект с данными о студентах (имя, возраст, средний балл). Отфильтровать студентов с баллом выше 4.0 и сохранить их в отдельный JSON-файл."
language = "Python"
print(generate_code(input_text, language))

print("\n")

input_text = "Создать JSON-объект с данными о студентах (имя, возраст, средний балл). Отфильтровать студентов с баллом выше 4.0 и сохранить их в отдельный JSON-файл."
language = "JavaScript"
print(generate_code(input_text, language))

print("\n")

input_text = "Сделать GET-запрос к API (https://jsonplaceholder.typicode.com/users), получить данные о пользователях, извлечь их имена и email, и сохранить в CSV-файл."
language = "Python"
print(generate_code(input_text, language))

print("\n")

input_text = "Сделать GET-запрос к API (https://jsonplaceholder.typicode.com/users), получить данные о пользователях, извлечь их имена и email, и сохранить в CSV-файл."
language = "JavaScript"
print(generate_code(input_text, language))

print("\n")

input_text = "Создать список из 100 случайных чисел, должна использоваться многопоточная обработка. Разделить его на 4 части и обработать каждую часть в отдельном потоке, чтобы найти максимальное значение в каждой части. Затем объединить результаты."
language = "Python"
print(generate_code(input_text, language))

print("\n")

input_text = "Создать список из 100 случайных чисел, должна использоваться многопоточная обработка. Разделить его на 4 части и обработать каждую часть в отдельном потоке, чтобы найти максимальное значение в каждой части. Затем объединить результаты."
language = "JavaScript"
print(generate_code(input_text, language))