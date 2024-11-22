def chiffrement_cesar(message, clef):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultat = ''

    for lettre in message.upper():  
        if lettre in alphabet:  # Vérifier si c'est une lettre
            index = (alphabet.index(lettre) + clef) % 26
            resultat += alphabet[index]
        else:
            resultat += lettre  

    return resultat


texte = input("Entrez un message à chiffrer : ")
decalage = int(input("Entrez une clé (décalage) : "))
print("Message chiffré :", chiffrement_cesar(texte, decalage))

