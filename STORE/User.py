class User:
    def __init__(self, id ,email, password):
        self.__id = id
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__id

    def set_name(self, id):
        self.__id = id

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password