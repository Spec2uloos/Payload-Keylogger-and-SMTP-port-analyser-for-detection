import os
import subprocess
import psutil

# Paramètres
time = 1
black_list = []
white_list = []

# Dans cette partie, on scanne continuellement les ports “587, 465, 2525”.
# Ces ports représentent les ports de communication avec le serveur SMTP.
while True:
    if time == 1:
        print("Scanning in progress...")
        proc = subprocess.Popen('netstat -ano -p tcp | findstr "587 465 2525"',
                                shell=True, stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        out, err = proc.communicate()
        output = out.decode()

        my_list = output.split(" ")
        # PID sera le dernier numéro une fois séparé
        pid = my_list[-1]

        # Obtenir la sortie en vérifiant le nom de l'application associée à PID
        cmd_output = subprocess.getoutput(f'tasklist /fi "pid eq {pid}"')
        process_name = cmd_output.split()

        time += 1

        if "ESTABLISHED" in output:
            # Supprimer les éléments vides du tableau
            my_list = list(filter(None, my_list))

            # Obtenir l'adresse IP complète avec le numéro de port depuis le dernier élément de la sortie
            port_num = my_list[-3]
            # Diviser au niveau de ':' pour obtenir le numéro de port à la dernière position du tableau
            get_port = port_num.split(":")
            port = get_port[-1]

            p = psutil.Process(int(pid))

            if int(pid) not in white_list:
                print("POTENTIAL KEYLOGGER!")
                # Terminer le processus s'il existe dans la blacklist
                if int(pid) in black_list:
                    p.kill()
                    print("Blacklist application found running. \nProcess automatically terminated.")
                    time = 1
                # Si le processus n'est pas dans la whitelist, vérifier s'il doit l'être
                elif int(pid) not in white_list:
                    print("Pausing application...")
                    p.suspend()
                    print("Information on application identified in your system to be a potential threat...")
                    print(f'Application info: {p}\n')

                    selected = False
                    while not selected:
                        is_safe = input("Would you like to whitelist this application? (Y/N): ").lower()
                        if is_safe == 'n':
                            print("Terminating process...")
                            p.kill()
                            print("Adding to blacklist...")
                            black_list.append(int(pid))
                            selected = True
                        elif is_safe == 'y':
                            print("Resuming process...")
                            p.resume()
                            print("Adding to whitelist...")
                            white_list.append(int(pid))
                            selected = True

        print("whitelist:", white_list)
        print("blacklist:", black_list)
