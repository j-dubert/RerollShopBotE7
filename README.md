# RerollShopBotE7

## Installation 

Il est nécessaire d'avoir Python 3 pour faire fonctionner le bot. 
Normalement, l'installeur install également le programme pip3 qui permet d'installer les dépendances nécessaires au bot. Si ce n'est pas le cas, procéder à l'installation manuelle.

### Dépendances

Il est nécessaire d'installer la librairie [PyAutoGUI](https://pypi.org/project/PyAutoGUI/).

## Préparation du bot

Il y a dans le dossier templates les images de références que le bot utilise pour retrouver les merveilleux signets dans le shop.
Vous devez remplacer les images par des screenshots de vos écrans. <br>
**Attention :** Prenez bien des screenshots de votre jeu dans la taille avec laquelle vous lancerez votre bot. **La taille de l'image compte !** D'où la nécessité de refaire chacun ses captures.

## Lancement du bot

Une fois la mise en place terminé,
 - lancez votre jeu dans votre émulateur favoris
 - lancez un invité de commande *(dans le menu démarrer chercher commande)*
 - allez à l'emplacement du bot *(exemple: ***cd Documents/bot***)*
 - lancez le bot avec la commande ``py main.py``
 - regardez le bot acheter les précieux signets pour vous

## Réglages

Si vous voulez accélérer le bot, vous pouvez baisser le temps d'attente du bot au niveau des ``time.sleep()``. <br>
**Attention** cela risque de faire rater des signets au bot si il va plus vite que le rendu du jeu par votre ordinateur.

**Conseil :** ***Ne toucher qu'aux lignes à l'intérieur du ``try{}`` entre les lignes 49 et 63***

Si vous avez la moindre question, hésitez pas à la poser sur le discord :D