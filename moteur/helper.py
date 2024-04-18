import re


def extract_vedio_name(commande):
  #  Définir un modèle d'expression régulière pour extraire le nom de la vidéo
   pattern =r'play\s+(.*?)\s+on\s+youtube'

  #  Rechercher le modèle dans le texte de la commande
  #  re.IGNORECASE pour chercher le nom soit en majuscule ou minuscule
   match=re.search(pattern ,commande ,re.IGNORECASE)

   # Renvoie le nom de la vidéo extraite (groupe 1) si une correspondance est trouvée, sinon Aucune
   return match.group(1) if match else None 