# IAProjet
# 🌟 Projet de Reconnaissance Faciale avec Retour Vocal Multilingue

---

## 📌 Choix du Projet

Nous avons choisi de développer un système de reconnaissance faciale intégrant un **retour vocal multilingue**, dans le but de créer une solution innovante pour la **gestion de présence**.

Ce projet réunit plusieurs domaines technologiques :
- Vision par ordinateur
- Reconnaissance faciale
- Synthèse vocale
- Prise en compte de la diversité linguistique

🎯 Ce choix est motivé par le besoin croissant de **solutions de pointage sans contact**, pratiques, rapides et adaptées à des environnements multiculturels :  
→ Écoles, entreprises, événements internationaux, etc.

---

## ⚙️ Installation

### ✅ Prérequis

- Python **3.7 ou version supérieure**

### 📦 Installation des dépendances

Exécutez les commandes suivantes dans votre terminal :

```bash
pip install opencv-python
pip install face_recognition
pip install SpeechRecognition
pip install gTTS
pip install playsound
pip install googletrans==4.0.0-rc1

# Système de Gestion de Présence avec Reconnaissance Faciale

## 💡 Conseil d'installation

Le module `face_recognition` dépend de `dlib`, qui peut poser des problèmes sur Windows. Pour une installation facilitée, il est recommandé d'utiliser **Anaconda** ou des **roues précompilées (whl)**.

✔️ **Solution recommandée :**
Utilisez Anaconda ou installez `dlib` à partir de roues précompilées pour éviter les problèmes d'installation sur Windows.

## 🚀 Utilisation et Résultat Attendu

### 🔍 Étapes de fonctionnement

1. **Encodage des visages connus** à partir d'images de référence.
2. Le programme **analyse une nouvelle image ou une vidéo**.
3. Il compare les visages détectés aux visages enregistrés.
4. Si une correspondance est trouvée :
   - Le nom de la personne est ajouté dans le fichier **Attendance.csv** avec l'heure actuelle.
   - Un **message vocal** est généré pour confirmer l'identité :
     - 🔊 En anglais pour les noms non-arabes.
     - 🔊 En arabe pour les noms spécifiés (ex : "Fatine", "Mouad", etc.).

### 🧠 Ce système est adapté pour une utilisation réelle :

- **Gestion de présence**
- **Automatisation intelligente**
- **Communication multilingue**

## 😧 Problèmes Rencontrés

### 1. Installation de `dlib`

- ⚠️ **Problème** : L'installation de `dlib` peut être difficile sur Windows.
- ✅ **Solution** : Utilisez Anaconda ou une roue précompilée pour une installation plus simple.

### 2. Erreur d'index

- ⚠️ **Problème** : L'appel à `face_encodings(img)[0]` échoue si aucun visage n'est détecté dans l'image.
- ✅ **Solution** : Ajout d'une vérification conditionnelle pour éviter cette erreur.

### 3. Chargement vocal

- ⚠️ **Problème** : La lecture audio échoue tant que le fichier n'est pas entièrement généré.
- ✅ **Solution** : Des délais ont été ajoutés pour garantir que le fichier audio soit complètement généré avant la lecture.

### 4. Traduction automatique

- ⚠️ **Problème** : Le module `googletrans` n'est pas toujours fiable pour la traduction de noms propres (ex : "Fatine", "Falima", etc.).
- ✅ **Solution** : Limitation de l'utilisation de `googletrans` pour les traductions de noms propres.

## 💪 Conclusion

Ce projet propose une solution simple, pratique et inclusive pour l'identification et la gestion de présence. Il exploite des technologies modernes, accessibles et adaptables, pouvant être étendues à :

- D'autres langues
- Différents contextes professionnels
- Divers cas d'utilisation (sécurité, éducation, entreprises)



