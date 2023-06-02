from password import Password



class PasswordCore:
    def __init__(self) -> None:
        pass


    def insert(self, password: Password):
        with open('informations.txt', 'w') as f:
            f.write(str(password))


    def selectAllPasswords(self):
        with open('informations.txt') as f:
            pwd = f.read().split('\n')[:-1]
            pwd = list(map(lambda line: line.split('|'), pwd))
            return pwd


    def selectAllUsers(self, search_user, search_pwd):
        for user, password in self.selectAllPasswords():
            if user == search_user and password == search_pwd:
                return (user, password)
            else:
                return -1