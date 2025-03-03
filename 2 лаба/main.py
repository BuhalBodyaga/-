import random
import json
import requests
import csv
from threading import Thread


def generate_code(input_text, language):
    # Шаблон 1: Генерация и обработка JSON-данных
    if "JSON-объект" in input_text and "отфильтровать" or "Отфильтровать" in input_text:
        if language == "Python":
            return (
                "# Генерация JSON-объекта с данными о студентах\n"
                "# Особенности Python: работа с JSON (модуль json), фильтрация данных и запись в файл\n"
                "import json\n\n"
                "# Создаем JSON-объект\n"
                "students = [\n"
                "    {'name': 'Alice', 'age': 20, 'gpa': 3.8},\n"
                "    {'name': 'Bob', 'age': 21, 'gpa': 4.2},\n"
                "    {'name': 'Charlie', 'age': 22, 'gpa': 3.5},\n"
                "    {'name': 'David', 'age': 23, 'gpa': 4.5}\n"
                "]\n\n"
                "# Фильтруем студентов с GPA > 4.0\n"
                "filtered_students = [student for student in students if student['gpa'] > 4.0]\n\n"
                "# Сохраняем результат в JSON-файл\n"
                "with open('filtered_students.json', 'w') as file:\n"
                "    json.dump(filtered_students, file, indent=4)\n\n"
                "print('Фильтрованные данные сохранены в filtered_students.json')"
            )
        elif language == "JavaScript":
            return (
                "// Генерация JSON-объекта с данными о студентах\n"
                "// Особенности JavaScript: работа с JSON (метод JSON.stringify), фильтрация данных и запись в файл (модуль fs)\n"
                "const fs = require('fs');\n\n"
                "// Создаем JSON-объект\n"
                "let students = [\n"
                "    {name: 'Alice', age: 20, gpa: 3.8},\n"
                "    {name: 'Bob', age: 21, gpa: 4.2},\n"
                "    {name: 'Charlie', age: 22, gpa: 3.5},\n"
                "    {name: 'David', age: 23, gpa: 4.5}\n"
                "];\n\n"
                "// Фильтруем студентов с GPA > 4.0\n"
                "let filteredStudents = students.filter(student => student.gpa > 4.0);\n\n"
                "// Сохраняем результат в JSON-файл\n"
                "fs.writeFileSync('filtered_students.json', JSON.stringify(filteredStudents, null, 4));\n\n"
                "console.log('Фильтрованные данные сохранены в filtered_students.json');"
            )

    # Шаблон 2: Работа с API и обработка данных
    elif "GET-запрос" in input_text and "CSV-файл" in input_text:
        if language == "Python":
            return (
                "# Выполнение GET-запроса к API и сохранение данных в CSV\n"
                "# Особенности Python: работа с HTTP-запросами (модуль requests), обработка JSON и запись в CSV\n"
                "import requests\n"
                "import csv\n\n"
                "# Выполняем GET-запрос\n"
                "response = requests.get('https://jsonplaceholder.typicode.com/users')\n"
                "users = response.json()\n\n"
                "# Извлекаем имена и email\n"
                "data = [[user['name'], user['email']] for user in users]\n\n"
                "# Сохраняем данные в CSV-файл\n"
                "with open('users.csv', 'w', newline='') as file:\n"
                "    writer = csv.writer(file)\n"
                "    writer.writerow(['Name', 'Email'])  # Заголовки\n"
                "    writer.writerows(data)  # Данные\n\n"
                "print('Данные сохранены в users.csv')"
            )
        elif language == "JavaScript":
            return (
                "// Выполнение GET-запроса к API и сохранение данных в CSV\n"
                "// Особенности JavaScript: работа с HTTP-запросами (модуль axios), обработка JSON и запись в CSV (модуль fs)\n"
                "const axios = require('axios');\n"
                "const fs = require('fs');\n\n"
                "// Выполняем GET-запрос\n"
                "axios.get('https://jsonplaceholder.typicode.com/users')\n"
                "    .then(response => {\n"
                "        let users = response.data;\n"
                "        let data = users.map(user => [user.name, user.email]);\n\n"
                "        // Сохраняем данные в CSV-файл\n"
                "        let csvContent = 'Name,Email\\n' + data.map(row => row.join(',')).join('\\n');\n"
                "        fs.writeFileSync('users.csv', csvContent);\n\n"
                "        console.log('Данные сохранены в users.csv');\n"
                "    })\n"
                "    .catch(error => {\n"
                "        console.error('Ошибка при выполнении запроса:', error);\n"
                "    });"
            )

    # Шаблон 3: Многопоточная обработка данных
    elif "многопоточная обработка" in input_text and "максимальное значение" in input_text:
        if language == "Python":
            return (
                "# Многопоточная обработка списка чисел\n"
                "# Особенности Python: многопоточность (модуль threading), разделение списка и поиск максимума\n"
                "import random\n"
                "from threading import Thread\n\n"
                "# Создаем список из 100 случайных чисел\n"
                "numbers = [random.randint(1, 1000) for _ in range(100)]\n\n"
                "# Функция для поиска максимума в части списка\n"
                "def find_max(sub_list, result, index):\n"
                "    result[index] = max(sub_list)\n\n"
                "# Делим список на 4 части\n"
                "chunk_size = len(numbers) // 4\n"
                "chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]\n\n"
                "# Создаем потоки\n"
                "results = [None] * 4\n"
                "threads = [Thread(target=find_max, args=(chunks[i], results, i)) for i in range(4)]\n\n"
                "# Запускаем потоки\n"
                "for thread in threads:\n"
                "    thread.start()\n\n"
                "# Ожидаем завершения потоков\n"
                "for thread in threads:\n"
                "    thread.join()\n\n"
                "# Объединяем результаты\n"
                "final_max = max(results)\n"
                "print('Максимальное значение:', final_max)"
            )
        elif language == "JavaScript":
            return (
                "// Многопоточная обработка списка чисел\n"
                "// Особенности JavaScript: многопоточность (Worker Threads), разделение списка и поиск максимума\n"
                "const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');\n\n"
                "if (isMainThread) {\n"
                "    // Создаем список из 100 случайных чисел\n"
                "    let numbers = Array.from({length: 100}, () => Math.floor(Math.random() * 1000));\n\n"
                "    // Делим список на 4 части\n"
                "    let chunkSize = Math.ceil(numbers.length / 4);\n"
                "    let chunks = [];\n"
                "    for (let i = 0; i < numbers.length; i += chunkSize) {\n"
                "        chunks.push(numbers.slice(i, i + chunkSize));\n"
                "    }\n\n"
                "    // Создаем потоки\n"
                "    let results = [];\n"
                "    chunks.forEach((chunk, index) => {\n"
                "        const worker = new Worker(__filename, { workerData: chunk });\n"
                "        worker.on('message', (msg) => {\n"
                "            results[index] = msg;\n"
                "            if (results.length === 4) {\n"
                "                let finalMax = Math.max(...results);\n"
                "                console.log('Максимальное значение:', finalMax);\n"
                "            }\n"
                "        });\n"
                "    });\n"
                "} else {\n"
                "    // Логика для каждого потока\n"
                "    let max = Math.max(...workerData);\n"
                "    parentPort.postMessage(max);\n"
                "}"
            )

    # Если шаблон не распознан
    else:
        return "Шаблон не распознан."
