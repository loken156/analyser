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
#Ber användaren mata in 2 texter
text1 = input('Input your first text here')
text2 = input('Input your second text here')


similarity_score = similarity(text1, text2)

print(similarity_score)