4
import random as r
def oylagan_sonni_top():
    print('ARIFMETIK O\'YIN.')
    print(f"O'yin sharti:"
          f"Siz 2 dan 9 gacha bolgan 2ta bir xil son o'ylaysiz va bir biriga qoshasiz "
          f"keyin men aytgan raqamga yoki songa bo'lasiz. ")
    print('Men esa sizga javobni aytaman(hisob kitob amalini miyangizda amalga oshirasiz.!!!)')
    
    while True:
      hisob = r.randint(2,1000)
      input('oyinni boshlash uchun ikkita bir xil raqam oylang,va "ENTER" tugmasini bosing ')
      
      print(f"O'ylagan raqamingizni bir biriga qoshing va shu {hisob}ga ko'paytiring")
      print('Boshida oylagan ikkta raqamingizni bitasiga boling.')
      savol = input(f"Hisob kitob qilib boldingizmi?(yes/no): ")
      if savol=='yes':
         print(f"Chiqan javob {hisob*2} ")
      savol2 = input('yana davom etiramizmi?(yes/no): ')
      if savol2!='yes':
          break
oylagan_sonni_top()      
print('oyin tugadi')         