#--------------------------------------------------
# ToolName   : Installer
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2022
# Language   : Python
#--------------------------------------------------


import os, time, sys

from colorama import Fore, Style

os.system('clear')

print(f'\33]0; Installer - Настройки\a',
                  end='', flush=True)




os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

filename = "sypexhack"

if os.path.exists(filename):
  os.system('clear')
  print("Installer запускается командой: python installer.py")
  print("")
  sys.exit()


else:
  os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/sypexhack")
  os.system('clear')   








def res():
    print(Style.RESET_ALL)


def exit():
    print(Fore.WHITE+'', Style.BRIGHT)
    exit = input(' [Нажмите Enter чтобы закрыть]')
    os.chdir('/data/data/com.termux/files/home/installer')
    os.system('clear')


def baner():
    os.system('clear')
    os.system('lolcat ~/installer/banner/baner.txt')
    res()
    os.chdir('/data/data/com.termux/files/home/Installer_Files')


def delet():
    if os.path.exists(filename):
      baner()
      print(Style.BRIGHT, Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита "+led+" успешно удалена!")
      exit()

    else:
      baner()
      print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита "+led+" еще не установлена!")
      exit()
      


while True:
    os.system('lolcat ~/installer/banner/banerset.txt')
    inp = input('\n Выбери пункт ➤ ')
    os.system('clear')


  
    if inp == '1':
        os.system('clear')
        baner()
        print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Вы точно хотите Обновить/Переустановить Installer?")
        res()
        tru_201 = input(' Выбери пункт [y/n] ➤ ')
        if tru_201 == 'y':
            os.system('rm -fr /data/data/com.termux/files/home/setup_installer.py')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('mv setup_installer.py /data/data/com.termux/files/home/')
            os.system('rm ~/.bashrc')
            os.system('echo "cd && python setup_installer.py" >> ~/.bashrc')
            print(f'\33]0; Создайте новый сезон!\a',
                    end='', flush=True)  
            while True:
                os.system('clear')
                baner()
                print(Style.BRIGHT, Fore.YELLOW+"["+Fore.CYAN+"i"+Fore.YELLOW+"] Перезапустите Termux или создайте новый сезон!")
                lol = input('')
        else:
            os.system('clear')

  
  
    
    if inp == '3':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        baner()
        print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Переместить скачаные утилты в "+Fore.YELLOW+"/files/home"+Fore.CYAN+" ?")
        res()
        tru_401 = input(' Выбери пункт [y/n] ➤ ')
        if tru_401 == 'y':
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
          
            os.system('mv PyPhisher /data/data/com.termux/files/home/')
            os.system('mv zphisher /data/data/com.termux/files/home/')
            os.system('mv CamHacker /data/data/com.termux/files/home/')
            os.system('mv VidPhisher /data/data/com.termux/files/home/')
            os.system('mv Telephish /data/data/com.termux/files/home/')
            os.system('mv Dnnme2 /data/data/com.termux/files/home/')
            os.system('mv maskphish /data/data/com.termux/files/home/')

            os.system('mv PhoneInfoga /data/data/com.termux/files/home/')
            os.system('mv sherlock /data/data/com.termux/files/home/')
            os.system('mv mmail /data/data/com.termux/files/home/')
            os.system('mv Discord-Nitro-Generator-and-Checker /data/data/com.termux/files/home/')
            os.system('mv shorturl /data/data/com.termux/files/home/')
            os.system('mv seeker /data/data/com.termux/files/home/')

            os.system('mv k-fuscator /data/data/com.termux/files/home/')
            os.system('mv TigerVirus /data/data/com.termux/files/home/')
            os.system('mv hammer /data/data/com.termux/files/home/')
            os.system('clear')
            baner()
            print(Fore.GREEN+" Все утилиты УСПЕШНО перенесены в папку /files/home")
            exit()

        else:
            os.system('clear')


  
    if inp == '4':
      
        while True:
          
          os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

          filename = "serveo"
          if os.path.exists(filename):
            serveo = ""+Fore.RED+"X"
          else:
            serveo = ""+Fore.GREEN+"✓"
  
          filename = "lochost"
          if os.path.exists(filename):
            Localhost = ""+Fore.RED+"X"
          else:
            Localhost = ""+Fore.GREEN+"✓"
        
          filename = "IP"
          if os.path.exists(filename):
            IPTracer = ""+Fore.RED+"X"
          else:
            IPTracer = ""+Fore.GREEN+"✓"
  
          filename = "holehe"
          if os.path.exists(filename):
            Holehe = ""+Fore.RED+"X"
          else:
            Holehe = ""+Fore.GREEN+"✓"

          filename = "h8mail"
          if os.path.exists(filename):
            h8mail = ""+Fore.RED+"X"
          else:
            h8mail = ""+Fore.GREEN+"✓"
        
          os.chdir('/data/data/com.termux/files/home/Installer_Files')
        
          filename = "PyPhisher"
          if os.path.exists(filename):
            PyPhisher = ""+Fore.GREEN+"✓"
          else:
            PyPhisher = ""+Fore.RED+"X"
  
          filename = "zphisher"
          if os.path.exists(filename):
            Zphisher = ""+Fore.GREEN+"✓"
          else:
            Zphisher = ""+Fore.RED+"X"

          filename = "CamHacker"
          if os.path.exists(filename):
            CamHacker = ""+Fore.GREEN+"✓"
          else:
            CamHacker = ""+Fore.RED+"X"

          filename = "VidPhisher"
          if os.path.exists(filename):
            VidPhisher = ""+Fore.GREEN+"✓"
          else:
            VidPhisher = ""+Fore.RED+"X"

          filename = "Telephish"
          if os.path.exists(filename):
            Telephish = ""+Fore.GREEN+"✓"
          else:
            Telephish = ""+Fore.RED+"X"
  
          filename = "Dnnme2"
          if os.path.exists(filename):
            Dnnme2 = ""+Fore.GREEN+"✓"
          else:
            Dnnme2 = ""+Fore.RED+"X"

          filename = "maskphish"
          if os.path.exists(filename):
            Maskphish = ""+Fore.GREEN+"✓"
          else:
            Maskphish = ""+Fore.RED+"X"



          filename = "PhoneInfoga"
          if os.path.exists(filename):
            PhoneInfoga = ""+Fore.GREEN+"✓"
          else:
            PhoneInfoga = ""+Fore.RED+"X"

          filename = "sherlock"
          if os.path.exists(filename):
            Sherlock = ""+Fore.GREEN+"✓"
          else:
            Sherlock = ""+Fore.RED+"X"

          filename = "mmail"
          if os.path.exists(filename):
            Mmail = ""+Fore.GREEN+"✓"
          else:
            Mmail = ""+Fore.RED+"X"

          filename = "Discord-Nitro-Generator-and-Checker"
          if os.path.exists(filename):
            Discord = ""+Fore.GREEN+"✓"
          else:
            Discord = ""+Fore.RED+"X"

          filename = "shorturl"
          if os.path.exists(filename):
            ShortUrl = ""+Fore.GREEN+"✓"
          else:
            ShortUrl = ""+Fore.RED+"X"

          filename = "seeker"
          if os.path.exists(filename):
            Seeker = ""+Fore.GREEN+"✓"
          else:
            Seeker = ""+Fore.RED+"X"


          
          filename = "TigerVirus"
          if os.path.exists(filename):
            TigerVirus = ""+Fore.GREEN+"✓"
          else:
            TigerVirus = ""+Fore.RED+"X"

          filename = "hammer"
          if os.path.exists(filename):
            Hammer = ""+Fore.GREEN+"✓"
          else:
            Hammer = ""+Fore.RED+"X"
          
          filename = "k-fuscator"
          if os.path.exists(filename):
            Kfuscator = ""+Fore.GREEN+"✓"
          else:
            Kfuscator = ""+Fore.RED+"X"
          
          baner()
          print(Style.BRIGHT, Fore.CYAN+"Выбери какую именно удалить Утилиту:")
          res()
          print(Style.BRIGHT, Fore.WHITE+"Утилиты страницы (1) ➤")
          res()
          print(Style.BRIGHT, Fore.YELLOW+"[01] Serveo      ("+serveo+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[02] Localhost   ("+Localhost+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[03] PyPhiser    ("+PyPhisher+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[04] Zphisher    ("+Zphisher+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[05] CamHacker   ("+CamHacker+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[06] VidPhisher  ("+VidPhisher+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[07] Telephish   ("+Telephish+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[08] Dnnme2      ("+Dnnme2+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[09] Maskphish   ("+Maskphish+""+Fore.YELLOW+")")
          res()
          print(Style.BRIGHT, Fore.WHITE+"Утилиты страницы (2) ➤")
          res()
          print(Style.BRIGHT, Fore.YELLOW+"[11] PhoneInfo   ("+PhoneInfoga+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[12] Holehe      ("+Holehe+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[13] IP-Tracer   ("+IPTracer+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[14] Sherlock    ("+Sherlock+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[15] H8mail      ("+h8mail+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[16] Mmail       ("+Mmail+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[17] Discord     ("+Discord+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[18] ShortUrl    ("+ShortUrl+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[19] Seeker      ("+Seeker+""+Fore.YELLOW+")")
          res()
          print(Style.BRIGHT, Fore.WHITE+"Утилиты страницы (3) ➤")
          res()
          print(Style.BRIGHT, Fore.YELLOW+"[21] Скоро...    ("+CamHacker+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[22] Скоро...    ("+VidPhisher+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[23] Скоро...    ("+Telephish+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[24] Скоро...    ("+Dnnme2+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[25] Скоро...    ("+Discord+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[26] Скоро...    ("+CamHacker+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[27] Скоро...    ("+VidPhisher+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[28] Скоро...    ("+Telephish+""+Fore.YELLOW+")")
          print(Style.BRIGHT, Fore.YELLOW+"[29] Скоро...    ("+Dnnme2+""+Fore.YELLOW+")")
          res()
          print(Style.BRIGHT, Fore.RED+"[a] Выбрать все утилиты")
          res()
          print(Style.BRIGHT, Fore.YELLOW+"[e] Назад")
          res()
          tsu_501 = input(' Выбери пункт ➤ ')
          os.system('clear')



          if tsu_501 == '1':
              os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
              filename = "serveo"
              if os.path.exists(filename):
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита Serveo еще не установлена!")
                exit()
                
              else:
                os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/serveo")
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита Serveo успешно удалена!")
                exit()

          
          if tsu_501 == '2':
              os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
              filename = "lochost"
              if os.path.exists(filename):
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита Localhost еще не установлена!")
                exit()
                
              else:
                os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/lochost")
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита Localhost успешно удалена!")
                exit()

          
          if tsu_501 == '13':
              os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
              filename = "IP"
              if os.path.exists(filename):
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита IP-Tracer еще не установлена!")
                exit()
                
              else:
                os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/IP")
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита IP-Tracer успешно удалена!")
                exit()

          
          if tsu_501 == '12':
              os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
              filename = "holehe"
              if os.path.exists(filename):
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита Holehe еще не установлена!")
                exit()
                
              else:
                os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/holehe")
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита Holehe успешно удалена!")
                exit()

          
          if tsu_501 == '15':
              os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
              filename = "h8mail"
              if os.path.exists(filename):
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита H8mail еще не установлена!")
                exit()
                
              else:
                os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/h8mail")
                baner()
                print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Утилита H8mail успешно удалена!")
                exit()



          
          if tsu_501 == '3':
              filename = "PyPhisher"
              led = "PyPhish"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/PyPhisher')

          if tsu_501 == '4':
              filename = "zphisher"
              led = "Zphisher"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/zphisher')

          if tsu_501 == '5':
              filename = "CamHacker"
              led = "CamHacker"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/CamHacker')

          if tsu_501 == '6':
              filename = "VidPhisher"
              led = "VidPhisher"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/VidPhisher')

          if tsu_501 == '7':
              filename = "Telephish"
              led = "Telephish"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Telephish')

          if tsu_501 == '8':
              filename = "Dnnme2"
              led = "Dnnme2"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Dnnme2')

          if tsu_501 == '9':
              filename = "maskphish"
              led = "Maskphish"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/maskphish')


          
      
          if tsu_501 == '11':
              filename = "PhoneInfoga"
              led = "PhoneInfoga"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/PhoneInfoga')

          if tsu_501 == '14':
              filename = "sherlock"
              led = "Sherlock"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/sherlock')
          
          if tsu_501 == '15':
              filename = "mmail"
              led = "Mmail"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/mmail')

          if tsu_501 == '17':
              filename = "Discord-Nitro-Generator-and-Checker"
              led = "Discord"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Discord-Nitro-Generator-and-Checker')

          if tsu_501 == '18':
              filename = "shorturl"
              led = "ShortUrl"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/shorturl')
            
          if tsu_501 == '19':
              filename = "seeker"
              led = "Seeker"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/seeker')
          


          
          if tsu_501 == '21':
              filename = "k-fuscator"
              led = "K-fuscator"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/k-fuscator')

          if tsu_501 == '22':
              filename = "TigerVirus"
              led = "TigerVirus"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/TigerVirus')

          if tsu_501 == '23':
              filename = "hammer"
              led = "Hammer"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/zphisher')




          if tsu_501 == 'a':
              baner()
              print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Вы действительно хотите удалить ВСЕ утилиты?")
              res()
              tru_502 = input(' Выбери пункт [y/n] ➤ ')
              if tru_502 == 'y':
                
                  os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
                
                  filename = "serveo"
                  if os.path.exists(filename):
                    os.system('clear')
                  else:
                    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/serveo")

                  filename = "lochost"
                  if os.path.exists(filename):
                    os.system('clear')
                  else:
                    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/lochost")

                  filename = "IP"
                  if os.path.exists(filename):
                    os.system('clear')
                  else:
                    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/IP")

                  filename = "holehe"
                  if os.path.exists(filename):
                    os.system('clear')
                  else:
                    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/holehe")

                  filename = "mmail"
                  if os.path.exists(filename):
                    os.system('clear')
                  else:
                    os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/mmail")
                
                  os.chdir('/data/data/com.termux/files/home/Installer_Files')
                
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/PyPhisher')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/zphisher')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/CamHacker')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/VidPhisher')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Telephish')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Dnnme2')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/maskphish')

                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/PhoneInfoga')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/sherlock')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/mmail')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Discord-Nitro-Generator-and-Checker')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/shorturl')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/seeker')
                
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/hammer')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/TigerVirus')
                  os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/k-fuscator')
    
                  baner()
                  print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] ВСЕ Утилиты успешно удалены!")
                  exit()


          if tsu_501 == 'e':
              break




  
    if inp == '5':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

        filename = "Auto"
        if os.path.exists(filename):
          Auto = ""+Fore.RED+"Выключено"
        else:
          Auto = ""+Fore.GREEN+"Включено"
      
        os.system('clear')
        baner()
        print (Style.BRIGHT,Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Запускать Installer при запуске Termux")
        res()
        print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Статус: "+Auto+"")
        res()
        print(Style.BRIGHT,Fore.YELLOW+'[1] Включить')
        print(Style.BRIGHT,Fore.YELLOW+'[2] Выключить')
        res()
        print(Style.BRIGHT ,Fore.YELLOW+'[e] выход')
        res()
        tru_101 = input(' Выбери пункт ➤ ')

        if tru_101 == '1':
            os.system("""sed -i '/^cd && cd installer && python testinstaller.py$/d' ~/.bashrc""")
            os.system('echo "cd && cd installer && python testinstaller.py" >> ~/.bashrc')
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/Auto')
            os.system('clear')
            baner()
            print(Style.BRIGHT,Fore.GREEN+"["+Fore.CYAN+"!"+Fore.GREEN+"] Включено!")
            exit()
            
        if tru_101 == '2':
            os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
            filename = "Auto"
          
            if os.path.exists(filename):
              baner()
              print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"!"+Fore.YELLOW+"] Авто-запуск еще не включен!")
              exit()
              
            else:
              os.system("""sed -i '/^cd && cd installer && python testinstaller.py$/d' ~/.bashrc""")
              os.mkdir("/data/data/com.termux/files/home/Installer_Files/trash/Auto")
              baner()
              print(Style.BRIGHT,Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Выключено!")
              exit()
            
        else:
            os.system('clear')


  

  
    
    if inp == '6':
        os.system('xdg-open https://t.me/SYPEXHACK_fail/51')
        os.system('clear')



  

    if inp == '7':
        os.system('git clone https://github.com/777-oleg-777/test')
        os.chdir('test')
        os.system('sh test.sh')
        os.system('clear')







  
  

    if inp == 't':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')

  
  
    if inp == 'h':
        os.system('xdg-open https://t.me/SYPEXHACK_help_bot')
        os.system('clear')


  
    if inp == 'p':
        os.system('xdg-open https://forms.gle/qi2HKCi3Lu9mDrsF6')
        os.system('clear')
  

    
    if inp == 'e':
        res()
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('clear')
        break
