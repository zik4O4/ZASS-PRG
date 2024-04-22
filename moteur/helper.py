import re




def extract_vedio_name(commande):
  #  Définir un modèle d'expression régulière pour extraire le nom de la vidéo
   pattern =r'play\s+(.*?)\s+on\s+youtube'

  #  Rechercher le modèle dans le texte de la commande
  #  re.IGNORECASE pour chercher le nom soit en majuscule ou minuscule
   match=re.search(pattern ,commande ,re.IGNORECASE)

   # Renvoie le nom de la vidéo extraite (groupe 1) si une correspondance est trouvée, sinon Aucune
   return match.group(1) if match else None 






def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string


#remove_words test 
# input_string = "make a phone call to pappa"
# words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', '']

# result = remove_words(input_string, words_to_remove)
# print(result)