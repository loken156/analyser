# analyser
Jag har skapat ett program som tar emot två text input ifrån användaren och analyserar dem på lite olika sätt.
Jag har importerat biblioteket spaCy för att komma åt NLP för att lätt kunna göra likhetsjämförelser samt extrahera nyckelord från texterna.
Jag har skapat olika funktioner som används senare i meny loopen, en funktion tar fram similarityscore, en tar fram nyckelord 
och den tredje letar fram vilka ord som har likheter i båda texterna.

En while loop startas och användaren bes om 2 inputs av text. Efter kommer användaren in i menyn där man kan välja vad man vill
se för information om texterna.
menyn är strukturerad med hjälp av if och elif på choice så att jag lätt kan navigera användaren med hjälp av deras 0-4 input.

Med den här applikationen kan användare lätt jämföra större stycken text, se vilka likheter de har, eller om de inte har någon likhets score 
alls. Eller om man vill ta bort alla utfyllnadsord och bara se nyckelorden kan man göra det. applikationen hålls igång med hjälp av en loop
tills användern väljer att stänga av den.

Jag har valt att importera det engelska bilbioteket av NLP så input av använderan bör vara på Engelska!