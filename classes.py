class AllPets:
    sound = ''
    name = ''
    weight = 0
    feed_pets = 'Накормить'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.feed_pets = self.feed_pets
        self.sound = self.sound


class Milk(AllPets):
    milk = 'Надоить молока'

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.milk = self.milk


class Haircut(AllPets):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.trim = 'Постричь'


class Birds(AllPets):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.eggs = 'Собрать яйца'


class Goose(Birds):
    sound = 'gagaga'


class Chicken(Birds):
    sound = 'kokoko'


class Rooster(AllPets):
    sound = 'cucareca'


class Cow(Milk):
    sound = 'mooooo'


class Ewes(Haircut):
    sound = 'beeeee'


class Goats(Milk):
    sound = 'meeeee'


class Duck(Birds):
    sound = 'crack quack'


white_goose = Goose('Белый', 5)
grey_goose = Goose('Серый', 6)
cow = Cow('Манька', 350)
goat_girl = Goats('Рога', 50)
goat_boy = Goats('Копыта', 65)
ram_lamb = Ewes('Барашек', 100)
ram_curly = Ewes('Кудрявый', 120)
duck = Duck('Кряква', 3)
chicken = Chicken('Ко-ко', 1)
rooster = Chicken('Кукареку', 1.5)

list_animals = [white_goose, grey_goose, cow, goat_girl, goat_boy, ram_lamb, ram_curly, duck, chicken, rooster]
name_and_weight_animals = {}
list_name = []
list_weight = []

for item in list_animals:
    name_and_weight_animals[item.name] = item.weight

for name_animals, weight_animals in name_and_weight_animals.items():
    list_name.append(name_animals)
    list_weight.append(weight_animals)


def max_weight_animal():
    return f'Самый большой вес у {list_name[list_weight.index(max(list_weight))]}.'


def overall_weight_animal():
    return f'Общий вес животных составляет {sum(list_weight)} кг.'


print(max_weight_animal())
print(overall_weight_animal())
