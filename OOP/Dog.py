class Dog():
    """Простая модель собаки"""

    def __int__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садиться по команде"""
        print(f"{self.name} is now sitting")

