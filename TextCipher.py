import pyAesCrypt

# Создание текстового файла Data.txt
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Привет, я документ для теста кода.\n")

# Ввод пароля для шифрования
# password = input('Введите пароль для шифрования или расшифрования файла: ')

# Шифрование файла
# pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

# Расшифрование файла
# pyAesCrypt.decryptFile('data.txt.aes', 'output.txt', password)


