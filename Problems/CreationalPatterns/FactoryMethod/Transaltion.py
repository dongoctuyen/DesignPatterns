from Core.CreationalPatterns.FactoryMethod import Creator, Product


class EuropeLanguage(Creator):
    def __init__(self):
        self.language = {
            'French': French(),
            'Spanish': Spanish()
        }

    def factory_method(self, language: str):
        return self.language.get(language)


class AsiaLanguage(Creator):
    def __init__(self):
        self.language = {
            'Vietnam': Vietnam()
        }

    def factory_method(self, language: str):
        return self.language.get(language)


class French(Product):
    def __init__(self):
        self.translations = {"car": "voiture",
                             "bike": "bicyclette",
                             "cycle": "cyclette"}

    def operation(self, message):
        return self.translations.get(message)


class Spanish(Product):
    def __init__(self):
        self.translations = {"car": "coche",
                             "bike": "bicicleta",
                             "cycle": "ciclo"}

    def operation(self, message):
        return self.translations.get(message)


class Vietnam(Product):
    def __init__(self):
        self.translations = {"car": "ô tô",
                             "bike": "xe đạp",
                             "cycle": "vòng tròn"}

    def operation(self, message):
        return self.translations.get(message)


def factory(c):
    continent = {
        "asia": AsiaLanguage(),
        "europe": EuropeLanguage()
    }
    return continent.get(c)


if __name__ == '__main__':
    asia = factory('asia')
    europe = factory('europe')
    v = asia.factory_method(language='Vietnam')
    s = europe.factory_method(language='Spanish')

    message = ["car", "bike", "cycle"]
    for msg in message:
        print(v.operation(message=msg))
        print(s.operation(message=msg))
