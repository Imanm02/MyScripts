import Messages
import pandas as pd
import numpy as np
import Mailer
import time

HW_SUBJECTS = [
    "آرایه (با فرض تدریس ورودی و خروجی، عملگرهای بیتی، شرط و حلقه، مفهوم تابع (ولی بدون تابع بازگشتی) و آرایه"
    ,
    "تابع بازگشتی (با فرض تدرسی ورودی و خروجی، عملگرهای بیتی، شرط و حلقه، تابع، آرایه و تابع بازگشتی)"
    ,
    "شرط و حلقه (با فرض تدریس ورودی و خروجی، عملگرهای بیتی و شرط و حلقه)"
]

DIFFICULTY = [
    "آسان",
    "متوسط",
    "سخت"
]


def generate_email_challenge(name, email):
    subject2 = None
    subject1 = HW_SUBJECTS[np.random.randint(0, len(HW_SUBJECTS))]
    while subject2 == subject1 or subject2 is None:
        subject2 = HW_SUBJECTS[np.random.randint(0, len(HW_SUBJECTS))]
    diff2 = None
    diff1 = DIFFICULTY[np.random.randint(0, len(DIFFICULTY))]
    while diff2 == diff1 or diff2 is None:
        diff2 = DIFFICULTY[np.random.randint(0, len(DIFFICULTY))]

    msg_plain = Messages.MAIL_CHALLENGE_TEMPLATE_PLAIN.format(name=name, subject1=subject1, subject2=subject2,
                                                              diff1=diff1, diff2=diff2)
    msg_html = Messages.MAIL_CHALLENGE_TEMPLATE_HTML.format(name=name, subject1=subject1, subject2=subject2,
                                                            diff1=diff1, diff2=diff2)
    return {"dest": email, "plain": msg_plain, "html": msg_html}


responses = pd.read_csv("ta1.csv")


emails = [generate_email_challenge(name, email) for name, email in
          zip(responses["Name"], responses["Email"], )]

for email in emails:
    dest = email["dest"]
    plain_text = email["plain"]
    html = email["html"]
    print(email)
    print("Sending Email to {dest} ...".format(dest=dest))
    Mailer.mail2(src="sharif_fop2022@outlook.com", dest=dest, subject="دستیاری آموزشی درس مبانی برنامه سازی",
                plain_text=plain_text, html=html)
    print("Email sent to {dest}.".format(dest=dest))
    sleep_time = np.random.uniform(4000, 15000, 1)
    print("Sleeping for {sleep_time} ms.\n\n".format(sleep_time=sleep_time))
    time.sleep(sleep_time[0] / 1000)
