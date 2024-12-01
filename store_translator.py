import re
import tkinter as tk
from tkinter import messagebox

def main():
    # Путь к файлу русской локализации в магазине
    # Можно открыть через "ПКМ по игре в библиотеке" >> "Управление" >> "Просмотреть локальные файлы"
    # Далее по пути "Deadlock\game\citadel\resource\localization\citadel_gc"
    file_path = 'citadel_gc_russian.txt'

    # Читаем содержимое файла
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()

    # Словарь переводов
    translations = {
        "Базовый магазин": "Basic Magazine",
        "Собиратель патронов" : "Ammo Scavenger",
        "Спешная стрельба" : "Rapid Rounds",
        "Скоростной магазин" : "High-Velocity Mag",
        "Ударная кража здоровья" : "Melee Lifesteal",
        "Тесла-пули" : "Tesla Bullets",
        "Символ безмолвия" : "Silence Glyph",
        "Глушитель" : "Silencer",
        "Замедляющие пули" : "Slowing Bullets",
        "Ограничитель" : "Inhibitor",
        "Аура охотника" : "Hunter's Aura",
        "Героическая аура" : "Heroic Aura",
        "Камень переноса" : "Warp Stone",
        "Терзающий пульс" : "Torment Pulse",
        "Мистический импульс" : "Mystic Burst",
        "Улучшенный импульс" : "Improved Burst",
        "Мистический отзвук" : "Mystic Reverb",
        "Токсичные пули" : "Toxic Bullets",
        "Спиритическое переполнение" : "Spiritual Overflow",
        "Рикошет" : "Ricochet",
        "Ближняя дистанция" : "Close Quarters",
        "Дальняя дистанция" : "Long Range",
        "Мистический выстрел" : "Mystic Shot",
        "Живительный выстрел" : "Restorative Shot",
        "Стрельба в упор" : "Point Blank",
        "Усилитель выстрелов в голову" : "Headshot Booster",
        "Прицельная стрельба" : "Sharpshooter",
        "Охотник за головами" : "Headhunter",
        "Головокружитель" : "Spellslinger Headshots",
        "Калечащий выстрел в голову" : "Crippling Headshot",
        "Берсерк" : "Berserker",
        "Ярость" : "Frenzy",
        "Душегубные пули" : "Soul Shredder Bullets",
        "Чудовищные патроны" : "Monster Rounds",
        "Разрывная оборона" : "Hollow Point Ward",
        "Первозданная эмблема" : "Pristine Emblem",
        "Стеклянная пушка" : "Glass Cannon",
        "Порыв вампиризма" : "Vampiric Burst",
        "Вытягивающие пули" : "Siphon Bullets",
        "Витальный удар" : "Lifestrike",
        "Шквальный огонь" : "Burst Fire",
        "Быстрый стрелок" : "Swift Striker",
        "Титанический магазин" : "Titanic Magazine",
        "Усиливающий магазин" : "Intensifying Magazine",
        "Растущая стойкость" : "Escalating Resilience",
        "Удачный выстрел" : "Lucky Shot",
        "Незримый покров" : "Veil Walker",
        "Призыв ракет" : "Conjure Missiles",
        "Добавочный спиритизм" : "Extra Spirit",
        "Улучшенный спиритизм" : "Improved Spirit",
        "Безграничный спиритизм" : "Boundless Spirit",
        "Спиритическая стойкость" : "Enduring Spirit",
        "Добавочное восстановление" : "Extra Regen",
        "Спиритическая кража здоровья" : "Spirit Lifesteal",
        "Мистическая уязвимость" : "Mystic Vulnerability",
        "Гроза целителей" : "Healbane",
        "Мистическое замедление" : "Mystic Slow",
        "Растущее воздействие" : "Escalating Exposure",
        "Мистический охват" : "Mystic Reach",
        "Улучшенный охват" : "Improved Reach",
        "Улучшенная перезарядка умений" : "Improved Cooldown", 
        "Превосходная перезарядка умений" : "Superior Cooldown",
        "Добавочные заряды" : "Extra Charge",
        "Спешные заряды" : "Rapid Recharge",
        "Алхимический огонь" : "Alchemical Fire",
        "Проворная поступь" : "Fleetfoot",
        "Кинетический рывок" : "Kinetic Dash",
        "Мистический порыв" : "Arcane Surge",
        "Активная перезарядка" : "Active Reload",
        "Замедляющие чары" : "Slowing Hex",
        "Плеть увядания" : "Withering Whip",
        "Развоплощение" : "Ethereal Shift",
        "Спасательный луч" : "Rescue Beam",
        "Обновитель" : "Refresher",
        "Холодный фронт" : "Cold Front",
        "Нокдаун" : "Knockdown",
        "Проклятие" : "Curse",
        "Стрелковый недуг" : "Bullet Resist Shredder",
        "Осколок эха" : "Echo Shard",
        "Увеличитель длительности" : "Duration Extender",
        "Превосходная длительность" : "Superior Duration",
        "Доспех прорицателя" : "Diviner's Kevlar",
        "Воодушевитель" : "Infuser",
        "Спиритический удар" : "Spirit Strike",
        "Похищение спиритизма" : "Spirit Snatch",
        "Удар с зарядом" : "Melee Charge",
        "Прилив мощи" : "Surge of Power",
        "Подавитель" : "Suppressor",
        "Ртутная перезарядка" : "Quicksilver Reload",
        "Ковёр-самолёт" : "Magic Carpet",
        "Заколдованные кастеты" : "Hex-Sealed Knuckles",
        "Пулевая кража здоровья" : "Bullet Lifesteal",
        "Обряд лечения" : "Healing Rite",
        "Божественный барьер" : "Divine Barrier",
        "Живительный медальон" : "Restorative Locket",
        "Пулевая броня" : "Bullet Armor",
        "Улучшенная пулевая броня" : "Improved Bullet Armor",
        "Усилитель лечения" : "Healing Booster",
        "Добавочное здоровье" : "Extra Health",
        "Уменьшитель эффектов" : "Debuff Reducer",
        "Устранитель эффектов" : "Debuff Remover",
        "Разложение" : "Decay",
        "Спиритическая броня" : "Spirit Armor",
        "Улучшенная спиритическая броня" : "Improved Spirit Armor",
        "Выдержка" : "Fortitude",
        "Кровопийца" : "Leech",
        "Перерождение" : "Rebirth",
        "Фантомный удар" : "Phantom Strike",
        "Перерождение души" : "Soul Rebirth",
        "Обратный огонь" : "Return Fire",
        "Металлическая кожа" : "Metal Skin",
        "Боевой барьер" : "Combat Barrier",
        "Барьер заклинателя" : "Enchanter's Barrier",
        "Неудержимость" : "Unstoppable",
        "Колосс" : "Colossus",
        "Беговые ботинки" : "Sprint Boots",
        "Превосходная выносливость" : "Superior Stamina",
        "Добавочная выносливость" : "Extra Stamina",
        "Скоростная стойкость" : "Enduring Speed",
        "Вспышка исцеления" : "Healing Nova",
        "Сплетение теней" : "Shadow Weave",
        "Грациозный скачок" : "Majestic Leap",
        "Барьерная реакция" : "Reactive Barrier",
        "Шестилистный заслон" : "Hexafoil Ward",
        "Лечение покровителя" : "Patron's Healing",
    }

    # Словарь строк
    updated_lines = []
    # Регулярное выражение разделяет строку на ключ("upgrade_clip_size"), пропускает пробелы, захватывает ру название предмета
    pattern = r'"(.+?)"\s+"([\u0400-\u04FF\s\-]+)"'

    for line in lines:
        # Ищем строки с русским текстом
        match = re.search(pattern, line)
        if match:
            key, value = match.groups()
            if value in translations:
                # Добавляем перевод через "/"
                translate_value = f'{value}/{translations[value]}'
                line = line.replace(f'"{value}"', f'"{translate_value}"')
        updated_lines.append(line)

    # Сохраняем изменения в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

    # Вывод в терминал о выполнении работы для тех, кто хочет запускать через .py файл
    print("finish")

    # Окно с сообщением о завершении работы программы
    root = tk.Tk()
    root.withdraw() 
    messagebox.showinfo("Завершено", "Игрунчик, мы тебе всё сделали, теперь запускай катку!") 

if __name__ == "__main__":
    main()