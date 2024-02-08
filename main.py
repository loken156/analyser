import spacy
#Installerat spacy och importat
#Laddar in spaCy modellen
nlp = spacy.load('en_core_web_lg')

#skapar en funktion som jämför text1 och text2
def similarity(text1, text2): # Förklara detta resultat!!
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    #Beräknar likheter mellan dokumenten
    similarity_score = doc1.similarity(doc2)
    return similarity_score

# Funktion för att extrahera nyckelord
def extract_keywords(text): # dela upp namn och ord
    doc = nlp(text)
    #skapar en variabel som exkluderar alla extra or som and, is och of. samt tar bort allt som innehåller andra tecken än alfabetiska.
    keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return keywords


#Extraherar lika ord ifrån texterna
def extract_similar_words(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    # Extraherar unika tokens från texterna
    tokens_text1 = set(token.text.lower() for token in doc1 if token.is_alpha and not token.is_stop)
    tokens_text2 = set(token.text.lower() for token in doc2 if token.is_alpha and not token.is_stop)

    # Hittar vilka ord som matchar
    similar_words = tokens_text1.intersection(tokens_text2)
    return similar_words

while True:
    #Ber användaren mata in 2 texter
    print("Welcome to this Text-analyze app")
    text1 = input('Input your first text here: ')
    text2 = input('Input your second text here: ')


    #skapar en variabel som storear likhetspoäng.
    similarity_score = similarity(text1, text2)

    #Printar en meny med olika alternativ för att analysera texten.
    while True:
        print('Choose what you want to do')
        print('1. Show similarity score')
        print('2. Show matching words')
        print('3. Extract keywords')
        print('4. Enter new texts')
        print('0. Quit')
        choice = input('Enter your choice (1, 2, 3, 4 or 0): ')

        # Case meny?
        # Låsa menyn i en loop så att man väljer för att få se den.

        if choice == '1':
            print(f"Similarity score between the texts: {similarity_score}")
            continue
        elif choice == '2':
            similar_words = extract_similar_words(text1, text2)
            print("Matching words in both texts:", similar_words)
        elif choice == '3':
            #skapar variabler med de extractade keywordsen
            keywords_text1 = extract_keywords(text1)
            keywords_text2 = extract_keywords(text2)
            print("Keywords in Text 1: ", keywords_text1)
            print("Keywords in Text 2: ", keywords_text2)
        elif choice == '4':
            break
        elif choice == '0':
            exit()
        else:
            print("Invalid choice")
