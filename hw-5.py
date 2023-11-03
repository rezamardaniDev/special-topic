"""
زرگیسو که تازه با برنامه نویسی آشنا شده می خواد برنامه ای بنویسه که
تعیین کنه آیا یک کلمه palindromeهست یا خیر. به کلمه ای میگن
palindromeکه چه از چپ چه از راست بخونیش یه چیز بشه. مثال
Madamیه palindromeهستش ولی tehranیک palindromeنیست.
حاال شما باید به زرگیسو کمک کنی این برنامه رو بنویسه.
لطفا توجه کنید که کوچک یا بزرگ بودن حروف مهم نیست همونطور که گفتیم
Madam یک palindromeهست همانطور که maDAMیک palindrome
است

مثال ورودی -> madam 
خروجی نمونه -> palindrome

مثال ورودی -> tehran 
خروجی نمونه -> not palindrome
"""

string = input("enter a word: ")
reverse = string[::-1] 
if string == reverse:
    print("palindrome")
else:
    print("no palindrome")