login = 'admin'
password = 'p@$$w0rD'
login1 = input()
password1 = input()
if password == password1 and login == login1:
    print("Вы вошли в систему")
if password == password1 and login != login1:
    print("Пользователь с таким именем не зарегистрирован")
if password != password1 and login == login1:
    print("Неверный пароль")
