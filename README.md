<h3>Это бот для создания постов с Inline кнопками и URl в них</h3>

!Бот тестировался на Python 3.12!

Для начала, нам нужно создать среду окружения:

*linux*
```bash
python3 -m venv .venv
./.venv/Scripts.activate
```
*Windows*
```powershell
python -m venv .venv
./.venv/Scripts.activate
```

После создания среды окружения , скачиваем зависимости:

*linux*
```bash
pip3 install -r req.txt
```
*Windows*
```powershell
pip install -r req.txt
```
Заходим в файл .env и меняем значение TOKEN= на свой токен бота.

Когда все зависимости установлены , можно запускать бота. Для того чтобы изменять сообщения других администраторов - выдайте ему права администратора с отправлением и изменением сообщений.
```text

.button:
{
    "button":[
        {"https://example.com/":"text1"},
        {"https://example.com/":"Любой текст №1"},
        {"https://example.com/":"Любой текст №2" , "https://example.com/":"Любой текст №3""},
        {"https://example.com/":"text2"}
    ]
}:Любой ваш текст (без двоеточий после этого)
```
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
