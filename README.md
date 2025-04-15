# IAProjet
🎯 Projet de Reconnaissance Faciale avec Retour Vocal Multilingue
📌 Choix du Projet
L'objectif de ce projet est de développer un système de reconnaissance faciale capable d'enregistrer automatiquement la présence des personnes identifiées à partir d'une image ou d'une caméra, avec une confirmation vocale dans différentes langues. Ce système peut être utilisé dans des écoles, des entreprises ou des événements pour automatiser la gestion de présence tout en tenant compte de la diversité linguistique des utilisateurs.

Nous avons choisi ce projet car il combine plusieurs domaines passionnants de l'informatique :

La vision par ordinateur

La synthèse vocale

La reconnaissance faciale

Le traitement multilingue

⚙️ Installation
Prérequis
Avant de lancer le projet, vous devez avoir Python installé (version 3.7 ou plus recommandée).

Ensuite, installez les bibliothèques nécessaires via pip :

bash
Copier
Modifier
pip install opencv-python
pip install face_recognition
pip install SpeechRecognition
pip install gTTS
pip install playsound
pip install googletrans==4.0.0-rc1
ℹ️ Remarque : la bibliothèque face_recognition dépend de dlib, qui peut être complexe à installer sur certaines machines. Sous Windows, il est parfois recommandé d'utiliser une distribution Python comme Anaconda.

🚀 Utilisation
Le script fonctionne en deux étapes principales :

Encodage des visages depuis des images connues (ex : photos de personnes autorisées).

Reconnaissance des visages à partir d’une nouvelle image ou d’un flux vidéo (caméra), suivi d’une confirmation vocale dans une langue adaptée.

Lorsque qu’un visage est reconnu :

Son nom est ajouté dans un fichier CSV (Attendance.csv) avec l'heure.

Un message vocal de confirmation est joué :

En anglais, si la personne n’est pas dans la liste des noms arabes.

En arabe, si le nom est reconnu comme un prénom arabe (ex : "Fatine", "Mouad").

✅ Résultat Attendu
Si une personne connue est reconnue par le système :

Son nom et l’heure sont enregistrés dans un fichier CSV.

Un retour vocal confirme son identification dans une langue adaptée.

Si une personne inconnue est présentée :

Aucun ajout dans le fichier.

Aucun son n'est joué.

Ce système permet une présence sans contact, rapide et intuitive.

🐞 Problèmes Rencontrés
Installation de dlib : cette dépendance est essentielle pour face_recognition mais peut poser problème, notamment sur Windows. Il a fallu compiler certaines versions manuellement.

Absence de visage détecté : si l’image ne contient pas de visage clair, le programme plante. Une vérification a été ajoutée pour éviter les erreurs de type IndexError.

Synchronisation audio : dans certains cas, le son se joue avant que le fichier audio ne soit entièrement écrit. Un léger délai peut être nécessaire pour s'assurer du bon fonctionnement.

Traduction automatique non utilisée : bien que googletrans soit installé, nous avons finalement opté pour une prononciation directe des noms sans traduction complète, pour éviter des erreurs de contexte.
