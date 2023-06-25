import requests
from telebot import types
import telebot,random
from time import sleep
from user_agent import generate_user_agent
token = "5695533879:AAES_v1Yiw6zHsZU2QeurPGCcDcDL83YkwY"
bot = telebot.TeleBot(token)
r = requests.session()
def check(A):
 FA7ES = requests.get(f'https://t.me/{A}').text
 if ('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link') in FA7ES :
  return "✅"
 else:
  return "❌"
def getnum(A):
 QQ='qwertyuiopasdf68052882281239807ghjklzxcvbnm1243567890_'
 user =str("".join(random.choice(QQ)for i in range (A)))
 return user
def get(A):
 QQ='qwertyuiopasdfghjklzxcvbnm_'
 user =str("".join(random.choice(QQ)for i in range (A)))
 return user
def getps(A):
 QQ='qwe__rtyuiopasdf68052882281239807ghjklzxcvbnm1243567890__. opas####dfghjklz@@xcvbnm_'
 user =str("".join(random.choice(QQ)for i in range (A)))
 return user
@bot.message_handler(commands=['start'])
def start_message(message):
 keyboard = telebot.types.ReplyKeyboardMarkup(True)
 keyboard.row("يوزرات سداسية🧩","يوزرات خماسية🎗")
 keyboard.row("إنشاء باسوورد قوي 🔐","يوزرات شبة رباعية🍀")

 bot.send_message(message.chat.id,'''

*- مرحبا بك عزيزي المشترك
انت الان في القائمة الرئيسية لجلب المعرفات وتخمينها يمكنك استخدام الازرار في الأسفل لتخمين يوزرك المفضل شكرا لاستخدامك بوتنا المتميز للمزيد تابع قناة المطور الرسمية *

📡┇› لمـعرفهہ‌‏ المزيد تابع @x0f3b
👨‍✈️┇› مـطـور آلبوت Ahmed-Rat
ـ @x0f3b🛒''',parse_mode='markdown', reply_markup=keyboard)
@bot.message_handler(func=lambda m: True)
def gettin(message):
    if message.text =="يوزرات خماسية🎗":
     A1=get(5);A=check(A1)
     A2=get(5);B=check(A2)
     A3=get(5);C=check(A3)
     A4=get(5);D=check(A4)
     B1=getnum(5);E=check(B1)
     B2=getnum(5);F=check(B2)
     B3=getnum(5);G=check(B3)
     B4=getnum(5);H=check(B4)
     print(A1)
     bot.send_message(message.chat.id,f"""
DONE GET LIST✅
تم جلب لستة وفحصها✅


 👨🏻‍💻¦ تخمين بدون ارقام
 ______________________
@{A1} {A}
@{A2} {B}
@{A3} {C}
@{A4} {D}

 ______________________
👨🏻‍💻¦ تخمين مع الارقام 
 ______________________
@{B1}  {E} 
@{B2}  {F} 
@{B3}  {G} 
@{B4}  {H} 

BY:- Ahmed-Rat- @x0f3b
""")
    elif message.text =="يوزرات سداسية🧩":
     A1=get(6);A=check(A1)
     A2=get(6);B=check(A2)
     A3=get(6);C=check(A3)
     A4=get(6);D=check(A4)
     B1=getnum(6);E=check(B1)
     B2=getnum(6);F=check(B2)
     B3=getnum(6);G=check(B3)
     B4=getnum(6);H=check(B4)
     print(A1)
     bot.send_message(message.chat.id,f"""
DONE GET LIST✅
تم جلب لستة وفحصها✅

 👨🏻‍💻¦ تخمين بدون ارقام
 ______________________
@{A1} {A}
@{A2} {B}
@{A3} {C}
@{A4} {D}

 ______________________
👨🏻‍💻¦ تخمين مع الارقام 
 ______________________
@{B1}  {E} 
@{B2}  {F} 
@{B3}  {G} 
@{B4}  {H} 

BY:- Ahmed-Rat- @x0f3b
""")
    elif message.text =="لا تنسي ذكر الله":
     A1=get(1)+'_'+get(1)+'_'+get(1)+'_'+get(1);A=check(A1)
     A2=get(1)+'_'+get(1)+'_'+get(1)+'_'+get(1);B=check(A2)
     A3=get(1)+'_'+get(1)+'_'+get(1)+'_'+get(1);C=check(A3)
     A4=get(1)+'_'+get(1)+'_'+get(1)+'_'+get(1);D=check(A4)
     B1=getnum(1)+'_'+getnum(1)+'_'+getnum(1)+'_'+getnum(1);E=check(B1)
     B2=getnum(1)+'_'+getnum(1)+'_'+getnum(1)+'_'+getnum(1);F=check(B2)
     B3=getnum(1)+'_'+getnum(1)+'_'+getnum(1)+'_'+getnum(1);G=check(B3)
     B4=getnum(1)+'_'+getnum(1)+'_'+getnum(1)+'_'+getnum(1);H=check(B4)
     print(A1)
     bot.send_message(message.chat.id,f"""
DONE GET LIST✅
تم جلب لستة وفحصها✅

 👨🏻‍💻¦ تخمين بدون ارقام
 ______________________
@{A1} {A}
@{A2} {B}
@{A3} {C}
@{A4} {D}

 ______________________
👨🏻‍💻¦ تخمين مع الارقام 
 ______________________
@{B1}  {E} 
@{B2}  {F} 
@{B3}  {G} 
@{B4}  {H} 

BY:- Ahmed-Rat- @x0f3b
""")
    elif message.text =="إنشاء باسوورد قوي 🔐":
    	Q=getps(8)
    	bot.send_message(message.chat.id,f"""*
الباسوورد الخاص بك هو:*
`{Q}`

*BY:- لمسات برمجية🍀*""",parse_mode='markdown')
bot.infinity_polling()
