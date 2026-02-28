## **Kojo Chat – Description du projet**

**Nom du projet :** Kojo Chat
**Technologies utilisées :** Python (Flask), HTML, CSS, JavaScript, Google GenAI (Gemini API)

### **Description générale :**

Kojo Chat est une application web de chat en ligne interactive qui permet aux utilisateurs de communiquer avec un chatbot intelligent propulsé par le modèle de langage **Gemini** de Google. L’application est conçue pour offrir une expérience proche des applications de messagerie modernes comme WhatsApp, avec des bulles de message stylisées, un affichage mot par mot des réponses et un bouton “copier” pour faciliter l’usage.

---

### **Fonctionnalités principales :**

1. **Chat en temps réel**

   * Les utilisateurs peuvent envoyer des messages via une interface simple et intuitive.
   * Les réponses du bot apparaissent en bulles, mot par mot, pour un effet naturel de conversation.

2. **Interface moderne et responsive**

   * Design inspiré de WhatsApp avec header, zone de messages scrollable et footer avec input.
   * Compatible avec ordinateurs, tablettes et smartphones grâce au responsive design.

3. **Messages formatés**

   * Support du **gras** via `**texte**`.
   * Support des **listes à puces** via `* item`.

4. **Bouton “COPIER”**

   * Chaque réponse du bot est accompagnée d’un bouton permettant de copier le texte directement dans le presse-papier.

5. **Interaction avec Google Gemini AI**

   * Les messages sont envoyés au serveur Flask, qui communique avec le modèle **Gemini-2.5-Flash** pour générer des réponses intelligentes et contextuelles.

6. **Envoi via bouton ou touche Entrée**

   * Les utilisateurs peuvent envoyer un message en cliquant sur le bouton **Envoyer** ou en appuyant sur la touche **Entrée**.

7. **Gestion des erreurs**

   * Si le serveur rencontre une erreur ou si le message est vide, l’utilisateur reçoit un retour clair dans la bulle du bot.

---

### **Architecture du projet :**

* **Backend (Flask)**

  * Route `/` : renvoie le fichier HTML principal.
  * Route `/chat` : API POST qui reçoit le message utilisateur, envoie au modèle Gemini et renvoie la réponse au format JSON.

* **Frontend (HTML/CSS/JS)**

  * HTML : structure de la page (header, messages, footer).
  * CSS : design moderne type WhatsApp, bulles colorées, responsive.
  * JS : gestion des messages, effet mot par mot, bouton copier, envoi via fetch au serveur Flask.

---

### **Installation et utilisation (en local) :**

1. Cloner le projet sur votre machine.
2. Installer les dépendances Python :

   ```bash
   pip install flask google-genai
   ```
3. Ajouter votre clé API Gemini :

   ```python
   API_KEY = "VOTRE_CLE_API"
   ```
4. Lancer le serveur Flask :

   ```bash
   python app.py
   ```
5. Accéder à `http://127.0.0.1:5000` dans votre navigateur et commencer à chatter.

---

### **Objectif du projet :**

Kojo Chat est conçu pour démontrer l’intégration d’un **modèle d’IA avancé** dans une application web moderne. Il sert à la fois de projet pédagogique et de démo pratique de messagerie intelligente, tout en offrant une expérience utilisateur agréable et interactive.

---

💡 **Idées d’amélioration futures :**

* Ajouter la possibilité de sauvegarder l’historique des conversations.
* Ajouter un mode multi-utilisateurs avec authentification.
* Intégrer des réponses plus contextuelles basées sur l’historique complet de la conversation.
* Ajouter un thème sombre / clair dynamique.

---

Si tu veux, je peux aussi te **rédiger une version courte et percutante** adaptée pour **la page principale de ton compte Kojo-Codeur**, prête à copier-coller, pour que ça fasse très pro aux visiteurs.

Veux‑tu que je fasse ça ?
