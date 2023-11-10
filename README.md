# Flower Generator

## Qu'est ce que c'est ?
L'application Flower Generator est un projet de NSI qui permet de créer des fleurs en prenant différentes valuers.

## Les valeurs
- Length: longueur du pétal en pixel
- Height: la largeur d'un côté de pétal en pixel
- Color: la couleur RGB du contour
- Fill color: la couleur RGB de remplissage de la feuile
- Petal number: le nombre de pétal par couches
- Lag: le décalage en degrés par rapport à l'angle au centre

## Les fonctionalités
- Un boutton d'aide en haut à droite en forme de point d'intérogation
- Un système de couches pour la création des pétals modifiable
- Une fonction d'exportation des réglages de la fleur avec un fichier au format JSON
- Une fonction d'inportation des réglages de la fleur en récupérant un fichier JSON
- Une fonction permettant de prendre en photo la fleur et de la sauvegarder

Toutes les fonctions ayants besoins de sauvegarder ou exporter des données demande la direction du fichier.

## Les références du projet
[Arc de cercle](https://fr.wikipedia.org/wiki/Arc_de_cercle)

## Les formules

Calcule du rayon du cercle en conaissant la longueur de la corde $2c$ et la hauteur de la flèche $t$:
$$\frac{c^2 + t^2}{2t}$$

Calcul de l'angle au centre en conaissant la longueur de la corde $2c$ et le rayon $R$:
$$2 * asin(\frac{c}{R})$$