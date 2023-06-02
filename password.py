class Password:
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password


    def __str__(self) -> str:
        return f'{self.user}|{self.password}\n'