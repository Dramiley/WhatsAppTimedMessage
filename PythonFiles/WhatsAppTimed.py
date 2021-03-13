import pywhatkit
import sys
from time import sleep

# Nachicht versenden
print()
print("Geht die Nachricht an eine Gruppe oder an einen Kontakt?" )
was = input("1 = Kontakt || 2 = Gruppe \n")
if int(was) == 1:
    bool1 = True
    bool2 = False
    empfängernummer = input("An wen soll die Nachricht gehen? (z.B. +49 + Nummer) \n")
elif int(was) == 2:
    bool2 = True
    bool1 = False
    print("So findest du die Group ID deiner Gruppe: \nhttps://youtu.be/Vx53spbt_qk")
    empfängergruppe = input("An wen soll die Nachricht gehen? (GroupID) \n")
else:
    print("Du hast keine richtige Zahl eingegeben")
    sleep(3)
    sys.exit(0)

nachricht = input("Schreibe die Nachricht nun hier rein \n")
a = input("Zu welcher Stunde soll die Nachricht gesendet werden? (x:y) \n")
b = input("Zu welcher Minute soll die Nachricht gesendet werden? ("+a+":y) \n")
if bool1:
    pywhatkit.sendwhatmsg(empfängernummer, nachricht, int(a), int(b))
if bool2:
    pywhatkit.sendwhatmsg_to_group(empfängergruppe, nachricht, int(a), int(b))