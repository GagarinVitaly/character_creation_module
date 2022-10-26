# noinspection SpellCheckingInspection
def attack(char_class):
    """

    :param char_class:
    :return:
    """
    if char_class != 'warrior':
        if char_class != 'mage' and char_class == 'healer' and char_class == 'healer':
            if char_class == 'healer':
                # noinspection SpellCheckingInspection
                return '{char_name} нанёс урон противнику равный {5 + randint(-3, -1)}'
        # noinspection SpellCheckingInspection
        return '{char_name} нанёс урон противнику равный {5 + randint(5, 10)}'
    # noinspection SpellCheckingInspection
    return '{char_name} нанёс урон противнику равный {5 + randint(3, 5)}'


# noinspection SpellCheckingInspection
def defence(char_class):
    """

    :param char_class:
    :return:
    """
    if char_class == 'warrior':
        # noinspection SpellCheckingInspection
        return '{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        # noinspection SpellCheckingInspection
        return '{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        # noinspection SpellCheckingInspection
        return '{char_name} блокировал {10 + randint(2, 5)} урона'


# noinspection SpellCheckingInspection
def special(char_class):
    """

    :param char_class:
    :return:
    """
    if char_class != 'warrior':
        if char_class != 'mage':
            if char_class == 'healer':
                # noinspection SpellCheckingInspection
                return '{char_name} применил специальное умение «Защита {10 + 30}»'
            return
        # noinspection SpellCheckingInspection
        return '{char_name} применил специальное умение «Атака {5 + 40}»'
    # noinspection SpellCheckingInspection
    return '{char_name} применил специальное умение «Выносливость {80 + 25}»'


# noinspection SpellCheckingInspection
def start_training(char_class):
    """

    :param char_class:
    :return:
    """
    if char_class == 'warrior':
        # noinspection SpellCheckingInspection
        print('{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        # noinspection SpellCheckingInspection
        print('{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        # noinspection SpellCheckingInspection
        print('{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    # noinspection SpellCheckingInspection
    print('Потренируйся управлять своими навыками.')
    # noinspection SpellCheckingInspection
    print('Введи одну из команд: attack — чтобы атаковать противника, defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    # noinspection SpellCheckingInspection
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        # noinspection SpellCheckingInspection
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_class))
        if cmd == 'defence':
            print(defence(char_class))
        if cmd == 'special':
            print(special(char_class))
    # noinspection SpellCheckingInspection
    return 'Тренировка окончена.'


# noinspection SpellCheckingInspection
def choice_char_class():
    """

    :return:
    """
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        # noinspection SpellCheckingInspection
        char_class = input('Введи название персонажа, за которого хочешь играть: Воитель — warrior, Маг — mage, '
                           'Лекарь — healer: ')
        if char_class == 'warrior':
            # noinspection SpellCheckingInspection
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный.')
        if char_class == 'mage':
            # noinspection SpellCheckingInspection
            print('Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.')
        if char_class == 'healer':
            # noinspection SpellCheckingInspection
            print('Лекарь — могущественный заклинатель. Черпает силы из природы, веры и духов.')
        # noinspection SpellCheckingInspection
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы выбрать другого '
                               'персонажа ').lower()
    return char_class
