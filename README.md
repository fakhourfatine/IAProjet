# IAProjet
🌟 Projet de Reconnaissance Faciale avec Retour Vocal Multilingue

📌 Choix du Projet

Nous avons choisi de développer un système de reconnaissance faciale intégrant un retour vocal multilingue, dans le but de créer une solution innovante pour la gestion de présence. Ce projet réunit plusieurs domaines technologiques : la vision par ordinateur, la reconnaissance faciale, la synthèse vocale, et la prise en compte de la diversité linguistique.

Ce choix est motivé par le besoin croissant de solutions de pointage sans contact, pratiques, rapides et adaptées à des environnements multiculturels (ex: écoles, entreprises, événements internationaux).

⚙️ Installation

Prérequis

Python 3.7 ou version supérieure

Installation des dépendances

Exécutez la commande suivante pour installer les bibliothèques nécessaires :

pip install opencv-python
pip install face_recognition
pip install SpeechRecognition
pip install gTTS
pip install playsound
pip install googletrans==4.0.0-rc1

💡 Conseil : face_recognition dépend de dlib, qui peut poser problème sur Windows. L'utilisation d'Anaconda ou de roues précompilées peut faciliter l'installation.

🚀 Utilisation et Résultat Attendu

Les visages connus sont encodés à partir d'images de référence.

Le programme analyse une nouvelle image ou une vidéo, compare les visages, et identifie les correspondances.

Si une personne est reconnue :

Son nom est ajouté à Attendance.csv avec l'heure actuelle.

Un message vocal de confirmation est joué :

En anglais pour les noms non-arabes.

En arabe pour les noms spécifiés comme "Fatine", "Mouad", etc.

🔹 Ce système est adapté pour être utilisé dans des contextes réels où l'automatisation et la communication multilingue sont essentielles.

😧 Problèmes Rencontrés

Installation de dlib : complexe, surtout sur Windows. Solution : installation via roues précompilées ou usage d'Anaconda.

Erreur d'index : lorsqu'aucun visage n'est détecté, face_encodings(img)[0] plante. Une vérification a été ajoutée pour éviter cela.

Temps de chargement vocal : les fichiers audio doivent être sauvegardés complètement avant la lecture. Cela a nécessité des délais d'attente dans le code.

Traduction automatique limitée : googletrans a été installé mais peu utilisé car la traduction automatique de noms est souvent erronée.

💪 Conclusion

Ce projet offre une solution simple, pratique et inclusive pour l'identification et la gestion de présence, tout en exploitant des technologies modernes et accessibles. Il peut être facilement adapté à d'autres langues ou contextes professionnels.
