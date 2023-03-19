class Dog:
    """Простая модель собаки"""
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.n = name
        self.a = age

    def sit(self):
        """Собака садиться по команде"""
        print(f"{self.n} is now sitting")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.n} rolled over!")


new_dog = Dog('bus', 5)

new_dog.sit()
