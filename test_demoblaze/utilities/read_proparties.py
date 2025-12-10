import configparser

config = configparser.RawConfigParser()
config.read('test_demoblaze/configurations/config.ini')

class ReadConfig:

    # @staticmethod
    # def get_login_page_url():
    #     url = config.get('Login_Info','login_page_url')
    #     return url

    # @staticmethod
    # def get_username():
    #     username = config.get('login info','username')
    #     return username
    #
    # @staticmethod
    # def get_password():
    #     password = config.get('login info','password')
    #     return password

    @staticmethod
    def get_invalid_login_data():
        import csv
        data = []
        with open("test_demoblaze/test_data/invalid_login_data.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data
