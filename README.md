# Topspin2Origin

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Fortran](https://img.shields.io/badge/Fortran-95-734F96?logo=fortran&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FFD43B)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Licence MIT](https://img.shields.io/badge/licence-MIT-green)

Petit outil développé pendant ma thèse pour les expérimentateurs : il convertit
un spectre RMN exporté en texte depuis **TopSpin** (Bruker) en un fichier à deux
colonnes (déplacement chimique en ppm, intensité) directement importable dans
**Origin** (ou tout tableur / logiciel de tracé).

## Fonctionnement

TopSpin exporte un spectre 1D sous forme d'un fichier `.txt` contenant un
en-tête (`# LEFT = … ppm. RIGHT = … ppm.`, `# SIZE = …`) suivi d'une intensité
par ligne. Le programme :

1. lit les bornes spectrales (`LEFT`, `RIGHT`) et le nombre de points (`SIZE`) ;
2. reconstruit l'axe des ppm (pas = (RIGHT − LEFT) / SIZE) ;
3. met à zéro les intensités négatives ;
4. écrit le couple `ppm  intensité` pour chaque point.

## Trois versions

| Fichier | Description | Sortie |
|---|---|---|
| `app.py` | Interface graphique (Tkinter) : bouton « Convertir fichier », menu Fichier → Ouvrir / Convertir, barre de progression | `<nom>.dat` à côté du fichier source |
| `topspin2origin.py` | Version script minimale (nom du fichier d'entrée écrit dans le code) | `tmp.dat` |
| `topspin2origin.f95` | Version Fortran en ligne de commande | `<nom>.CSV` (séparateur `;`) |

## Utilisation

### Interface graphique

```bash
pip install -r requirements.txt
python app.py
```

Cliquer sur **Convertir fichier**, choisir le `.txt` exporté par TopSpin : le
`.dat` est créé dans le même dossier. `logo.png` doit se trouver dans le dossier
courant.

Pour créer un exécutable autonome avec [PyInstaller](https://pyinstaller.org) :

```bash
pyinstaller app.spec
```

(copier ensuite `logo.png` à côté de l'exécutable dans `dist/app/`).

### Version Fortran

```bash
gfortran topspin2origin.f95 -o topspin2origin
./topspin2origin spectre.txt      # produit spectre.CSV
```

## Exemple

`exemples/exemple.txt` est un spectre **synthétique** (trois pics, 256 points)
au format d'export TopSpin, pour tester le programme.

## Licence

[MIT](LICENSE)
