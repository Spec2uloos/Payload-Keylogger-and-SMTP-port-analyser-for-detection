# Payload-Keylogger-and-SMTP-port-analyser-for-detection
Developed a keylogger payload and analyzed SMTP ports for malware detection using Wireshark, tcpdump, and Python libraries (Numpy, Pandas, Scikit-Learn).

## Introduction

Analyse des ports SMTP :

  Le Simple Mail Transfer Protocol (SMTP) est un protocole standard utilisé pour
  l'envoi de courriers électroniques sur Internet. Les pirates informatiques peuvent
  exploiter les ports SMTP pour envoyer des courriers électroniques malveillants, tels
  que des pourriels ou des logiciels malveillants, à des destinataires non désirés. Pour
  protéger les systèmes informatiques contre ces menaces, il est essentiel d'analyser les
  ports SMTP pour détecter les activités suspectes.
  Il existe plusieurs outils d'analyse des ports SMTP, tels que Nmap, Netcat, et
  Metasploit, qui permettent de détecter les ports ouverts et les vulnérabilités associées.
  Les administrateurs de systèmes peuvent également configurer des pare-feux et des
  règles de sécurité pour bloquer les ports SMTP non autorisés.

Identification de Keyloggers :

   Les keyloggers sont des programmes malveillants qui enregistrent les frappes de
   clavier sur un ordinateur, permettant ainsi aux pirates informatiques d'accéder à des
   informations sensibles telles que des mots de passe ou des informations de carte de crédit.
   L'identification des keyloggers est donc essentielle pour protéger les systèmes informatiques contre les attaques.
    
## Objectifs

- Analyser les ports SMTP des principaux fournisseurs de services de messagerie.
- Développer un keylogger pour observer le comportement des entrées utilisateur.
- Implémenter un analyseur de ports SMTP pour surveiller les communications.

## Technologies Utilisées

- **Langages**: Python
- **Outils**: Nmap, Netcat, Metasploit
- **Bibliothèques**: scapy, pynput

