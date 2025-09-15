import re
import random
import tkinter as tk
from tkinter import scrolledtext

# Милые звуки
cute_noises_general = [
    " nya~", " уву~", " ^w^", " *blushes*", " *wagwag*", " :3",
    " *трется об тебя*", " *заглядывает в глаза*", " *бьет хвостиком*", " *пританцовывает*",
    " *смотрит с улыбочкой*", " *засыпает у тебя на коленях*", " *восторженно прыгнул*",
    " *улыбается до ушей*"
]
cute_noises_dog = [
    " гав~", " тяф~", " woof~", " *прыгает лапками*", " *ляп по носу*", " *гавкает с любовью*", 
    " *виляет хвостиком*", " *обнюхивает*", " *танцует лапками*", " *бежит с тобой*",
    " *приходит в восторг от тебя*"
]
cute_noises_cat = [
    " мяу~", " мурр~", " *трется*", " *мурлычет*", " *царапает игриво*", " *мяукает в ладошку*",
    " *потягивается*", " *пухнет хвостик*", " *глядит своими большими глазами*",
    " *мурчит с любовью*"
]

# Расширенная база милых слов
uwu_words = {
    # Русский
    'волк': 'уольчек', 'волки': 'уольчата', 'собака': 'собачка~', 'пёс': 'пёсик~',
    'псы': 'пёсики~', 'щенок': 'щеночек~', 'обортень': 'обортенёк~',
    'ужас': 'увужас~', 'страх': 'сътьрах~', 'тебя': 'тебячка~', 'привет': 'привветик~',
    'пока': 'покасики~', 'ночь': 'ночуня~', 'люблю': 'лювввблю~', 'сон': 'спаточки~',
    'еда': 'нямка~', 'друг': 'друуугик~', 'обниму': 'обнимашки~', 'пушистик': 'пушуня~',
    'грусть': 'грууустнявка~', 'мир': 'мирочка~', 'война': 'бубумка~', 'дерево': 'деревце~',
    'трава': 'травочка~', 'кот': 'котик~', 'кошка': 'кошечка~', 'котята': 'котятки~',
    'мяу': 'мяуня~', 'мур': 'мурр~', 'спать': 'спатоньки~', 'игра': 'игрулечка~', 
    'свинья': 'свинюшка~', 'помощь': 'помощечка~', 'собака': 'собачуля~', 'молоко': 'молочко~',
    'ежик': 'ежик~', 'папа': 'папочка~', 'мама': 'мамочка~', 'солнце': 'солнышко~',
    'песок': 'песочек~', 'вода': 'водичка~', 'дети': 'детишечки~', 'слон': 'слоник~',
    'вишня': 'вишеночка~', 'сирень': 'сиренечка~', 'цветы': 'цветочки~',
    
    # English
    'wolf': 'wuffie~', 'wolves': 'wuffies~', 'dog': 'doggo~', 'puppy': 'puppo~',
    'werewolf': 'werewuff~', 'friend': 'fwend~', 'scary': 'scawwy~',
    'love': 'wuv~', 'you': 'yuu~', 'cat': 'kitteh~', 'kitten': 'kittie~',
    'night': 'nitey~', 'food': 'noms~', 'sleep': 'sweepies~',
    'cute': 'cutie~', 'hug': 'snuggie~', 'kiss': 'smoochie~', 'puppy': 'puppie~',
    'fox': 'foxxie~', 'rabbit': 'wabbit~', 'turtle': 'turtly~', 'rat': 'rattie~',
    'elephant': 'elephawnt~', 'sun': 'sunny~', 'sand': 'sandy~', 'water': 'wattery~',
    'flower': 'flowie~', 'berries': 'berwies~', 'cherry': 'cherrie~', 'rain': 'rainy~',
    'bunny': 'bunbun~', 'moon': 'moonie~', 'stars': 'starry~', 'heart': 'hearty~'
}

# Ключевые слова для шумов
canine_keywords = ['волк', 'волки', 'собака', 'пёс', 'псы', 'щенок', 'обортень', 'wolf', 'dog', 'puppy', 'werewolf']
feline_keywords = ['кот', 'кошка', 'котята', 'cat', 'kitten']
other_keywords = ['свинья', 'свинюшка', 'помощь', 'помощечка', 'молоко', 'молочко', 'фокс', 'лиса', 'ракун', 'слон']

# UWU функция
def uwu_translate(text):
    original_text = text.lower()

    # Подстановка милых слов сначала
    for word, cute in uwu_words.items():
        text = re.sub(fr'\b{word}\b', cute, text, flags=re.IGNORECASE)

    # Фонетические искажения английские
    text = re.sub(r'[rl]', 'w', text)
    text = re.sub(r'[RL]', 'W', text)
    text = re.sub(r'n([aeiou])', r'ny\1', text, flags=re.IGNORECASE)
    text = re.sub(r'N([aeiou])', r'Ny\1', text)

    # Фонетические искажения русские
    text = text.replace('р', 'ль').replace('Р', 'Ль')
    text = text.replace('л', 'ль').replace('Л', 'Ль')
    text = text.replace('в', 'ув').replace('В', 'Ув')
    text = text.replace('н', 'нь').replace('Н', 'Нь')
    text = text.replace('с', 'сь').replace('С', 'Сь')
    text = text.replace('з', 'зь').replace('З', 'Зь')

    # Добавление милых шумов
    noises = cute_noises_general.copy()
    if any(word in original_text for word in canine_keywords):
        noises += cute_noises_dog
    if any(word in original_text for word in feline_keywords):
        noises += cute_noises_cat
    if any(word in original_text for word in other_keywords):
        noises += [" *покачивает хвостиком*", " *цокает лапкой*", " *махает ушками*"]

    text = re.sub(r'([.!?])', lambda m: random.choice(noises) + m.group(1), text)

    return text

# GUI
def run_gui():
    def convert_text(event=None):
        input_text = input_box.get("1.0", tk.END).strip()
        output_text = uwu_translate(input_text)
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output_text)
        output_box.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("🐾 UWU-Фурри Переводчик: Мимими-режим")

    tk.Label(root, text="Введи текст, ня~:").pack(pady=5)
    input_box = scrolledtext.ScrolledText(root, width=60, height=10)
    input_box.pack(padx=10, pady=5)

    # Добавляем возможность вставки текста через стандартные сочетания клавиш
    input_box.bind("<Control-v>", convert_text)
    input_box.bind("<Command-v>", convert_text)

    tk.Button(root, text="✨ Перевести в UWU ✨", command=convert_text).pack(pady=10)

    tk.Label(root, text="Результат ня~:").pack(pady=5)
    output_box = scrolledtext.ScrolledText(root, width=60, height=10, state=tk.DISABLED)
    output_box.pack(padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
