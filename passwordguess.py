from random import choice
import time  # لإبطاء الطباعة قليلاً حتى تكون الحروف مرئية للمستخدم

# إدخال كلمة المرور من المستخدم
password = input("Password: ")
guess = [""] * len(password)  # إنشاء قائمة فارغة بطول كلمة المرور

# قائمة الحروف والأرقام
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# التأكد من أن التخمين ليس هو نفسه كلمة المرور
while "".join(guess) != password:
    # تحديث كل حرف عشوائياً في التخمين حتى يتطابق مع كلمة المرور
    for i in range(len(password)):
        if guess[i] != password[i]:  # إذا كان الحرف غير مطابق، جرب حرفا عشوائيا
            guess[i] = choice(characters)
    # طباعة التخمين الحالي على الشاشة
    print("".join(guess), end="\r")
    time.sleep(0.05)  # تأخير بسيط لرؤية التحديثات بوضوح

# عند مطابقة التخمين لكلمة المرور، يتم الطباعة
print("\nPassword guessed successfully!")
input("Press Enter to exit...")