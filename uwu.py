import re
import random
import tkinter as tk
from tkinter import scrolledtext, messagebox
import pyperclip  # pip install pyperclip


# === ВОЛЧЬЯ ЛИЧНОСТЬ ===
WOLF_NOISES = [
    " *тихо порыкивает*", " *уши настороже*", " *принюхивается*", " *хвост вильнул*",
    " *клыки блеснули*", " *взгляд в сумраке*", " *шерсть встала дыбом*", " *низкий вой*",
    " *прижал уши*", " *лапа легла на клавиатуру*", " *клацает когтями*", " *зарычал одобрительно*",
    " *вгляделся в терминал*", " *обнюхал пакеты*", " *следы в логах*", " *скалится в темноте*",
    " *лунный свет в глазах*", " *неоновый отблеск на шерсти*"
]

CYBER_VIBES = [
    " ▓▒░", " [0x", " //", " >>", " >>>", " ┃", " ━━", " ◆", " ●", " ▲"
]

# Расширенный словарь (русский + английский)
UWU_DICT = {
    # Cyber/Tech термины
    'код': 'кодик~', 'баг': 'багуля~', 'система': 'сьистемка~', 'сервер': 'сельвельчик~',
    'хакер': 'хакелуня~', 'exploit': 'эксплойтик~', 'malware': 'мальуэлька~',
    'firewall': 'файльуолик~', 'terminal': 'тельминалюнька~', 'script': 'сцльиптик~',
    'network': 'нетуольчик~', 'password': 'пассуольдик~', 'encryption': 'шифльулечка~',
    'packet': 'пакетуля~', 'server': 'сельвельчик~', 'database': 'базулька~',
    
    # Волчья тематика
    'волк': 'уольчек', 'волки': 'уольчата', 'клык': 'клычок', 'клыки': 'клычки',
    'лапа': 'лапуля', 'лапы': 'лапульки', 'хвост': 'хвостуля', 'шерсть': 'шельстюля',
    'вой': 'воюля', 'рык': 'рычулька', 'охота': 'охотуля', 'добыча': 'добычуля',
    'стая': 'стайка', 'луна': 'лунечка', 'ночь': 'ночуля', 'тьма': 'тьмулька',
    
    # Базовые слова
    'привет': 'пльивветик~', 'пока': 'покасики~', 'спасибо': 'спасибуля~',
    'да': 'дася~', 'нет': 'нетя~', 'хорошо': 'хольошенько~', 'плохо': 'плёхенько~',
    'друг': 'дльужок~', 'враг': 'вльажулька~', 'страх': 'стльахуля~',
    'сила': 'сильуля~', 'слабость': 'слабюнька~', 'опасность': 'опаснюська~',
    
    # English
    'wolf': 'wuffie', 'pack': 'packie', 'hunt': 'huntie', 'fang': 'fangie',
    'claw': 'clawie', 'howl': 'howlie', 'code': 'codie', 'hack': 'hackie',
    'cyber': 'cybie', 'system': 'systie', 'network': 'netwolkie', 'data': 'datie',
    'hello': 'hewwo', 'thanks': 'thankies', 'yes': 'yesh', 'no': 'nuu',
    'friend': 'fwend', 'enemy': 'enemie', 'dark': 'darkie', 'night': 'nitey'
}


def uwu_translate(text):
    """Волчья трансформация текста с кибер-эстетикой"""
    original = text.lower()
    
    # 1. Словарные замены (приоритет)
    for word, cute in UWU_DICT.items():
        text = re.sub(fr'\b{word}\b', cute, text, flags=re.IGNORECASE)
    
    # 2. Фонетические мутации (русский)
    text = text.replace('р', 'ль').replace('Р', 'Ль')
    text = text.replace('л', 'лью').replace('Л', 'Лью')
    text = re.sub(r'([внсз])([аеёиоуыэюя])', r'\1ь\2', text, flags=re.IGNORECASE)
    
    # 3. Фонетика (английский)
    text = re.sub(r'(?<![A-Za-zА-Яа-я])[rl](?![A-Za-zА-Яа-я])', 'w', text)
    text = re.sub(r'(?<![A-Za-zА-Яа-я])[RL](?![A-Za-zА-Яа-я])', 'W', text)
    text = re.sub(r'n([aeiou])', r'ny\1', text)
    
    # 4. Добавление волчьих звуков и кибер-символов
    sentences = re.split(r'([.!?…])', text)
    result = []
    
    for i, segment in enumerate(sentences):
        if segment.strip():
            result.append(segment)
            # Добавляем шумы после знаков препинания
            if segment in '.!?…':
                if random.random() > 0.4:  # 60% вероятность
                    result.append(random.choice(WOLF_NOISES))
                if random.random() > 0.7:  # 30% вероятность кибер-символов
                    result.append(random.choice(CYBER_VIBES))
    
    return ''.join(result)


# === GUI УЛУЧШЕННЫЙ ===
class WolfTranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🐺 Nocturne UWU Translator | Cyber Wolf Protocol")
        self.root.geometry("700x600")
        self.root.configure(bg='#1a1a2e')
        
        # Стилизация
        style_config = {
            'bg': '#16213e',
            'fg': '#00ff41',
            'insertbackground': '#00ff41',
            'font': ('Consolas', 11),
            'relief': tk.FLAT,
            'borderwidth': 2
        }
        
        # Заголовок
        title = tk.Label(
            root, 
            text="━━━━━ 🐺 NOCTURNE PROTOCOL: UWU MODE ━━━━━",
            bg='#1a1a2e', 
            fg='#00ff41', 
            font=('Courier', 14, 'bold')
        )
        title.pack(pady=10)
        
        # INPUT
        tk.Label(
            root, 
            text="▼ INPUT [normal text] *принюхивается*",
            bg='#1a1a2e', 
            fg='#0f3460',
            font=('Consolas', 10)
        ).pack(pady=(10,5))
        
        self.input_box = scrolledtext.ScrolledText(root, width=80, height=10, **style_config)
        self.input_box.pack(padx=15, pady=5)
        
        # Биндинги для input (вставка работает, автоконверт)
        self.input_box.bind('<Control-v>', lambda e: self.root.after(10, self.convert))
        self.input_box.bind('<Command-v>', lambda e: self.root.after(10, self.convert))
        self.input_box.bind('<KeyRelease>', lambda e: self.auto_convert_delayed())
        
        # Кнопки
        btn_frame = tk.Frame(root, bg='#1a1a2e')
        btn_frame.pack(pady=10)
        
        convert_btn = tk.Button(
            btn_frame, 
            text="⚡ TRANSFORM ⚡", 
            command=self.convert,
            bg='#0f3460', 
            fg='#00ff41',
            font=('Consolas', 11, 'bold'),
            activebackground='#00ff41',
            activeforeground='#1a1a2e',
            relief=tk.RAISED,
            borderwidth=3,
            padx=20
        )
        convert_btn.grid(row=0, column=0, padx=10)
        
        copy_btn = tk.Button(
            btn_frame,
            text="📋 COPY OUTPUT",
            command=self.copy_output,
            bg='#16213e',
            fg='#00ff41',
            font=('Consolas', 10),
            relief=tk.RAISED,
            borderwidth=2,
            padx=15
        )
        copy_btn.grid(row=0, column=1, padx=10)
        
        clear_btn = tk.Button(
            btn_frame,
            text="🗑 CLEAR",
            command=self.clear_all,
            bg='#16213e',
            fg='#ff4757',
            font=('Consolas', 10),
            relief=tk.RAISED,
            borderwidth=2,
            padx=15
        )
        clear_btn.grid(row=0, column=2, padx=10)
        
        # OUTPUT
        tk.Label(
            root,
            text="▼ OUTPUT [uwu translated] *хвост вильнул*",
            bg='#1a1a2e',
            fg='#0f3460',
            font=('Consolas', 10)
        ).pack(pady=(10,5))
        
        self.output_box = scrolledtext.ScrolledText(root, width=80, height=10, **style_config)
        self.output_box.pack(padx=15, pady=5)
        
        # КРИТИЧНО: Разрешаем выделение и копирование
        self.output_box.bind('<Control-c>', self.copy_selection)
        self.output_box.bind('<Command-c>', self.copy_selection)
        self.output_box.bind('<Control-a>', self.select_all_output)
        self.output_box.bind('<Button-1>', lambda e: 'break')  # Разрешаем клики
        
        # Футер
        footer = tk.Label(
            root,
            text="*клацает когтями* | Nocturne v2.0 | *неоновый отблеск*",
            bg='#1a1a2e',
            fg='#636e72',
            font=('Courier', 9, 'italic')
        )
        footer.pack(side=tk.BOTTOM, pady=10)
        
        # Задержка для автоконверта
        self.convert_job = None
    
    def convert(self):
        """Основная конверсия"""
        input_text = self.input_box.get("1.0", tk.END).strip()
        if not input_text:
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, "*принюхивается* Пусто... *уши прижал*")
            return
        
        output = uwu_translate(input_text)
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, output)
    
    def auto_convert_delayed(self):
        """Автоконверт с задержкой 500мс"""
        if self.convert_job:
            self.root.after_cancel(self.convert_job)
        self.convert_job = self.root.after(500, self.convert)
    
    def copy_output(self):
        """Копирование всего output в буфер"""
        output_text = self.output_box.get("1.0", tk.END).strip()
        if output_text:
            try:
                pyperclip.copy(output_text)
                # Временное уведомление
                original_text = self.output_box.get("1.0", tk.END)
                self.output_box.delete("1.0", tk.END)
                self.output_box.insert(tk.END, "✓ COPIED! *одобрительно рычит*")
                self.root.after(800, lambda: self.restore_output(original_text))
            except:
                messagebox.showerror("Error", "Не удалось скопировать *скулит*")
    
    def restore_output(self, text):
        """Восстановление текста после уведомления"""
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, text.strip())
    
    def copy_selection(self, event=None):
        """Копирование выделенного текста Ctrl+C"""
        try:
            selected = self.output_box.get(tk.SEL_FIRST, tk.SEL_LAST)
            pyperclip.copy(selected)
        except tk.TclError:
            pass  # Ничего не выделено
        return 'break'
    
    def select_all_output(self, event=None):
        """Выделить весь output (Ctrl+A)"""
        self.output_box.tag_add(tk.SEL, "1.0", tk.END)
        self.output_box.mark_set(tk.INSERT, "1.0")
        self.output_box.see(tk.INSERT)
        return 'break'
    
    def clear_all(self):
        """Очистка всех полей"""
        self.input_box.delete("1.0", tk.END)
        self.output_box.delete("1.0", tk.END)


# === ЗАПУСК ===
if __name__ == "__main__":
    root = tk.Tk()
    app = WolfTranslatorGUI(root)
    root.mainloop()
