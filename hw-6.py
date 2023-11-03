"""
جهانگیر توی یه شرکت کامپیوتری کار می کنه. قراره جهانگیر برنامه ای
بنویسه که تعیین کنه آیا می توان ABو BAرو در یک رشته ی دیگه پیدا کرد
بدونه اینکه با هم همپوشانی ) (overlapداشته باشن؟ ترتیبش ABو BAهم
مهم نیست. یعنی مثال اگه ورودی ABBAباشه پاسخ YESهست. اگه ورودی
BAABهم باشه بازم پاسخ YESهست. ولی اگه ورودی ABAباشه پاسخ
NOهست یا اگه ورودی ABHAباشه بازم پاسخ NOهست. می تونید کمک
جهانگیر کنید این برنامه رو بنویسه؟
لطفا YESو NOرا دقیقا به همین شکل با حروف بزرگ در خروجی چاپ کنید
"""

def check_AB_BA(string):
    result = "NO"
    
    if "AB" in string:
    
        if "BA" in string[string.index("AB")+2:]:
            result = "YES"
    
    if "BA" in string:
        
        if "AB" in string[string.index("BA")+2:]:
            result = "YES"
    
    return result

print(check_AB_BA("ABBA")) 
print(check_AB_BA("BAAB")) 
print(check_AB_BA("ABA")) 
print(check_AB_BA("ABHA")) 
