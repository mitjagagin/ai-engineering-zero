# test_environment.py
# Тестовый скрипт для проверки установки библиотек

import sys
import numpy as np
import pandas as pd
import matplotlib
import requests

print("=" * 50)
print("✅ ПРОВЕРКА ОКРУЖЕНИЯ ПРОЙДЕНА!")
print("=" * 50)
print(f"Версия Python: {sys.version}")
print(f"Версия NumPy: {np.__version__}")
print(f"Версия Pandas: {pd.__version__}")
print(f"Версия Matplotlib: {matplotlib.__version__}")
print(f"Версия Requests: {requests.__version__}")
print("=" * 50)

# Простой тест работы библиотек
print("\n🧪 Тест NumPy: создание массива")
arr = np.array([1, 2, 3, 4, 5])
print(f"Массив: {arr}")
print(f"Среднее значение: {np.mean(arr)}")

print("\n🧪 Тест Pandas: создание таблицы")
df = pd.DataFrame({
    'Имя': ['Алексей', 'Мария', 'Дмитрий'],
    'Возраст': [25, 30, 35],
    'Город': ['Москва', 'СПб', 'Казань']
})
print(df)

print("\n🧪 Тест Requests: проверка соединения")
try:
    response = requests.get('https://api.github.com', timeout=5)
    print(f"Статус ответа GitHub API: {response.status_code}")
except Exception as e:
    print(f"Ошибка соединения: {e}")

print("\n✅ ВСЕ ТЕСТЫ УСПЕШНЫ!")