import random
import tkinter as tk
from tkinter import messagebox as mb


class Question:
    def __init__(self, question: str, choices: list[str], right_choice=0):
        self.question = question
        self.choices = choices
        self.right_choice = right_choice

    def answer(self, choice: int):
        return choice == self.right_choice


if __name__ == '__main__':
    window = tk.Tk()
    questions = [
        Question('در مورد تاثیر غلظت سرب در خون بر افزایش میزان خشونت کدام مورد درست است؟', [
            'کاهش غلظت سرب در هوا  قطعا باعث کاهش نرخ جرم و خشونت می شود.',
            'پاسخ این سوال را از طریق آزمایش بالینی روی انسان ها می توان دریافت.',
            'از روی شباهت و همبستگی نمودار های غلظت سرب در خون کودکان و افزایش جرم و خشونت میتوان به وجود ارتباط قطعی بین این دو عامل پی برد.',
            'هیچکدام',
        ], 3),
        Question('کدام گزینه معنای صحیح بازه اطمینان ۹۰ دردصد است؟', [
            'بازه‌ای که ۹۰ درصد داده های ما در اون قرار دارن',
            'بازه‌ای که به احتمال ۹۰ درصد داده‌های ما در اون قرار میگیرن',
            'بازه‌ای که به احتمال ۹۰ درصد پارامتر اصلی ما در اون قرار داره',
            'بازه‌ای که ۹۰ درصد مواقع ۹۰ درصد داده‌های ما در اون قرار میگیرن ',
        ], 2),
        Question('طول بازه اطمینان به کدام مورد ارتباط دارد؟', [
            'پراکندگی داده ها',
            'تعداد نمونه ها',
            'درجه اطمینان',
            'همه موارد',
        ], 3),
        Question('در مورد ارتباط تعداد حملات کوسه‌ها و مصرف بستنی کدام مورد درست است؟', [
            'هرچه مصرف بستنی افراد بیشتر باشد بیشتر احتمال دارد که کوسه به آن‌ها حمله کند.',
            'رابطه حملات کوسه و مصرف بستنی رابطه علت-معلولی است',
            'دلیل ارتباط این دو متغیر وجود یک متغیر سوم است ',
            'هرچه تعداد کوسه‌ها در یک محل بیشتر باشد مصرف بستنی هم در آن محل بیشتر خواهد بود ',
        ], 2),
        Question('کدام مورد درباره تست جایگشت درست نیست؟', [
            'برای بررسی تصادفی یا معنی دار بودن اختلاف میانگین بکار می رود.',
            'تمام حالت های مختلف دسته بندی را مورد بررسی قرار می دهد.',
            'یکبار جامعه نمونه را به دو دسته تقسیم میکند و اختلاف میانگین را گزارش می دهد.',
            'هیچکدام',
        ], 2),
        Question("""در یک کارخانه بسته بندی شکر، دستگاه بسته بندی شکرهای 250 گرمی خراب شده و میخواهیم آن را با دستگاهی جدید جایگزین کنیم. شرکت تامین کننده برای ما اطلاعات سه دستگاه قابل تهیه را فرستاده. کدام دستگاه احتمالا مناسب‌تر است؟
دستگاه اول: 210-220-250-255-270-310
دستگاه دوم: 245-255–255-260-260-263
دستگاه سوم: 225-245-250-250-300-290""", [
            'دستگاه اول',
            'دستگاه دوم',
            'دستگاه سوم',
            'نمی‌توان نظری داد',
        ], 1),
        Question('کدام یک از روابط زیر صحیح می‌باشد؟', [
            'ژن زیر مجموعه کروموزوم می‌باشد',
            'با کنار هم قرار دادن کروموزوم‌ها ژن تشکیل می‌شود.',
            'تمام ژن‌ها در اصل همان راه‌حل‌های نهایی مسئله ما می‌باشند.',
            'جمعیت با تغییر نسل تغییر نمی‌کند.',
        ], 0),
        Question('در بازی دایناسور کروم برآزندگی را چه چیزی تعریف می‌کنید؟', [
            'مکان پریدن دایناسور',
            'تعداد پرش موفق در بازی',
            'میزان زنده ماندن دایناسور در بازی',
            'زمان پریدن دایناسور',
        ], 2),
        Question('کامپیوتر بر چه اساسی می‌تواند خوب یا بد بودن یک جواب را تشخیص دهد؟', [
            'نسلی که جواب در آن قرار دارد',
            'تعداد عضوهای یک جمعیت',
            'میزان برآزندگی جواب',
            'تعداد ژن‌های کروموزوم',
        ], 2),
        Question('در استوا گردباد چگونه تشکیل می‌شود؟', [
            'ساعتگرد',
            'پادساعتگرد',
            'سقوط میکند',
            'نمیتوان تشخیص داد',
        ], 2),
        Question("""دو بادکنک را باد می‌کنیم،یکی را کمتر از دیگری باد می‌کنیم.
اگر دهانه دوبادکنک را به هم وصل کنیم، جریان چگونه برگزار می‌شود؟""", [
            'از کوچکتر به بزرگتر',
            'از بزرگتر به کوچکتر',
            'جریان نداریم',
            'نمیتوان تشخیص داد',
        ], 0),
        Question('سوراخ کوچکی‌در انتهای بطری  پر آبی ایجاد کرده و از سطح بلندی آن را رها می‌کنیم. حالت خارج شدن اب چگونه است؟', [
            'خارج می شود',
            'خارج نمیشود',
            'ابتدا خارج و بعد متوقف میشود.',
            'نمیتوان تعیین کرد.',
        ], 1),
    ]
    base_chance = 0
    base_multiplier = 2
    q_index = 0
    btns = []
    btns_txt = []
    random.shuffle(questions)
    lbl_txt = tk.StringVar()
    lbl = tk.Label(textvariable=lbl_txt, font=("IRANYekan", 28))
    lbl_txt.set(f'{q_index+1}. {questions[0].question}')
    lbl.pack()
    choices = [i for i in range(len(questions[q_index].choices))]
    random.shuffle(choices)
    q_choices = [questions[q_index].choices[i] for i in choices]

    def handle_click(idx):
        def clicker(event):
            global q_index, choices, base_chance, base_multiplier
            if not questions[q_index].answer(choices[idx]):
                mb.showerror('باختی', 'تمام امتیازت رو از دست دادی.')
                window.quit()
            else:
                is_quit = False
                if q_index < len(questions) - 1:
                    q_index += 1
                    lbl_txt.set(f'{q_index+1}. {questions[q_index].question}')
                    choices = [i for i in range(
                        len(questions[q_index].choices))]
                    random.shuffle(choices)
                    q_choices = [questions[q_index].choices[i]
                                 for i in choices]
                    for i in range(len(btns)):
                        btns_txt[i].set(q_choices[i])
                else:
                    is_quit = True
                if base_chance:
                    base_chance += base_chance * (1. / 3.)
                else:
                    base_chance = 1. / 3.
                if base_chance > 0.7:
                    base_multiplier *= base_chance / 0.7
                    base_chance = 0.7
                if not is_quit:
                    is_quit = mb.askyesno('خروج از بازی',
                        f'شانس شما {base_chance * 100:.3f}% است. آيا ميخواهيد خارج شويد؟')
                if is_quit:
                    if random.uniform(0, 1) < base_chance:
                        mb.showinfo('بردی', f'امتیازت {base_multiplier:.3f} برابر شد.')
                        window.quit()
                    else:
                        mb.showerror('باختی', 'تمام امتیازت رو از دست دادی.')
                        window.quit()
                else:
                    return "break"
        return clicker
    for idx, q_ch in enumerate(q_choices):
        btns_txt.append(tk.StringVar())
        btns_txt[idx].set(q_choices[idx])
        btns.append(tk.Button(textvariable=btns_txt[idx], font=("IRANYekan", 24)))
        btns[idx].bind('<Button-1>', handle_click(idx))
        btns[idx].pack()
    window.mainloop()