def heaviest_animal():
    return f'Самый большой вес у {list(final.list_keys)[list(final.list_values).index(max(list(final.list_values)))]}.'


def total_animal_weight():
    return f'Общий вес животных составляет {sum(list(final.list_values))} кг.'


class AllPets:
    sound = 'Издает звук'
    name = 'Имя животного'
    weight = 0
    feed = 'Кормить'
    dictionary_pets = {}  # животные и их вес
    list_keys = dictionary_pets.keys()  # список животных
    list_values = dictionary_pets.values()  # список веса каждого животного

    def __init__(self):
        self.sound = self.sound
        self.feed = 'Кормить'


class AntlersAndHooves(AllPets):
    milk = 'Доить'
    sound = 'Млеет'

    def __init__(self):
        super().__init__()
        self.milk = 'Доить'


class Voice(AllPets):
    sound = 'Блеют'

    def __init__(self):
        super().__init__()
        self.trim = 'Постричь'


class Birds(AllPets):
    sound = 'Гогочут'

    def __init__(self):
        super().__init__()
        self.eggs = 'Собрать яйца'


white_goose = Birds()
white_goose.weight = 5  # kg
white_goose.name = 'Белый'
white_goose.dictionary_pets[white_goose.name] = white_goose.weight
white_goose.__init__()
print(white_goose.__dict__)

grey_goose = Birds()
grey_goose.weight = 6  # kg
grey_goose.name = 'Серый'
grey_goose.dictionary_pets[grey_goose.name] = grey_goose.weight
grey_goose.__init__()
print(grey_goose.__dict__)

cow = AntlersAndHooves()
cow.weight = 350  # kg
cow.name = 'Манька'
cow.sound = 'Мычит'
cow.dictionary_pets[cow.name] = cow.weight
cow.__init__()
print(cow.__dict__)

goat_girl = AntlersAndHooves()
goat_girl.weight = 50  # kg
goat_girl.name = 'Рога'
goat_girl.dictionary_pets[goat_girl.name] = goat_girl.weight
goat_girl.__init__()
print(goat_girl.__dict__)

goat_boy = AntlersAndHooves()
goat_boy.weight = 65  # kg
goat_boy.name = 'Копыта'
goat_boy.dictionary_pets[goat_boy.name] = goat_boy.weight
goat_boy.__init__()
print(goat_boy.__dict__)

ram_lamb = Voice()
ram_lamb.weight = 100  # kg
ram_lamb.name = 'Барашек'
ram_lamb.dictionary_pets[ram_lamb.name] = ram_lamb.weight
ram_lamb.__init__()
print(ram_lamb.__dict__)

ram_curly = Voice()
ram_curly.weight = 120  # kg
ram_curly.name = 'Кудрявый'
ram_curly.dictionary_pets[ram_curly.name] = ram_curly.weight
ram_curly.__init__()
print(ram_curly.__dict__)

duck = Birds()
duck.weight = 3  # kg
duck.name = 'Кряква'
duck.sound = 'Крякает'
duck.dictionary_pets[duck.name] = duck.weight
duck.__init__()
print(duck.__dict__)

chicken = Birds()
chicken.weight = 1  # kg
chicken.name = 'Ко-ко'
chicken.sound = 'Кудахчет'
chicken.dictionary_pets[chicken.name] = chicken.weight
chicken.__init__()
print(chicken.__dict__)

rooster = Birds()
rooster.weight = 1.5  # kg
rooster.name = 'Кукареку'
rooster.sound = 'Кукарекает'
rooster.dictionary_pets[rooster.name] = rooster.weight
rooster.__init__()
print(rooster.__dict__)

print(AllPets.__dict__)

final = AllPets()  # итоговые результаты по весу животных
print(heaviest_animal())
print(total_animal_weight())
