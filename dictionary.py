#  Создай словарь с именем, возрастом и городом. 
# Добавь туда поле "email" и выведи все пары "ключ: значение"
# построчно.

biografy={"name":"Jango","age":18,"city":"Dushanbe"}
biografy["email"]="jangoemail@.com"
for key,value in biografy.items():
    print(key,"-",value)