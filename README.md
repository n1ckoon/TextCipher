# Шифрование и расшифрование файлов с помощью `pyAesCrypt`

## Описание
Код демонстрирует использование библиотеки `pyAesCrypt` для шифрования и расшифрования файлов.

## Установка
Установите библиотеку:
```bash
pip install pyAesCrypt
```

## Использование
1. **Шифрование**  
   Раскомментируйте:
   ```python
   password = input('Введите пароль: ')
   pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)
   ```
   Запустите код. Создаётся файл `data.txt.aes`.

2. **Расшифрование**  
   Раскомментируйте:
   ```python
   password = input('Введите пароль: ')
   pyAesCrypt.decryptFile('data.txt.aes', 'output.txt', password)
   ```
   Запустите код. Создаётся файл `output.txt`.

## Требования
- Python 3.6+
- Библиотека `pyAesCrypt`

---

