import spacy
#Installerat spacy och importat
#Laddar in spaCy modellen
nlp = spacy.load('en_core_web_lg')

#skapar en funktion som jämför text1 och text2
def similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    #Beräknar likheter mellan dokumenten
    similarity_score = doc1.similarity(doc2)
    return similarity_score

# Funktion för att extrahera nyckelord
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return keywords

while True:
    #Ber användaren mata in 2 texter
    text1 = input('Input your first text here: ')
    text2 = input('Input your second text here: ')


    #skapar en variabel som storear likhetspoäng.
    similarity_score = similarity(text1, text2)

    #Printar en meny med olika alternativ för att analysera texten.
    while True:
        print('Choose what you want to do')
        print('1. Show similarity score')
        print('2. Extract meaningful words')
        print('3. Enter new texts')
        print('0. Quit')
        choice = input('Enter your choice (1, 2, 3 or 0): ')

        if choice == '1':
            print(f"Similarity score between the texts: {similarity_score}")
        elif choice == '2':
            #skapar variabler med de extractade keywordsen
            keywords_text1 = extract_keywords(text1)
            keywords_text2 = extract_keywords(text2)
            print("Keywords in Text 1: ", keywords_text1)
            print("Keywords in Text 2: ", keywords_text2)
        elif choice == '3':
            break
        elif choice == '0':
            exit()
        else:
            print("Invalid choice")
