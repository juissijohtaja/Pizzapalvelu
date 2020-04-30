# Työn ja sovelluksen rajoitteet, puuttuvat ominaisuudet

### Tietokanta
- Käyttäjäroolit on tehty tietokannassa boolean-muuttujalla
  - Tämän johdosta kirjautuneella käyttäjällä on vain kaksi eri roolia
  - Mikäli haluaisi useamman roolin, pitäisi rakentaa oma taulu käyttäjärooleille

- Tässä sovelluksessa tarvittavat tietomäärät ovat melko pieniä (suuruusluokka enintään satoja rivejä)
  - Tietokannan hallinnassa ei ole huomioitu suurien tietomäärien käsittelyä esim. pitäisi hakea/tallentaa "miljoonia" rivejä tietoa
  - Tämä vaatisi sovelluksen ja käyttöliittymän toteutukseen vielä runsaasti lisätyötä, joten lisätään ne backlogiin

### Täytteet ja Pizzat
- Pizzoihin voi valita vain neljä täytettä ja samaa täytettä ei voi valita kahdesti
  - Täytteiden enimmäismäärää voisi kasvattaa
  - Saman täytteen voisi valita useamman kerran
  - Pizzoihin voisi valita lisätäytteitä tilauksen yhteydessä
- Pizzan kokoa ei voi valita

- Pizzapohjia voisi olla useampi vaihtoehto esim. gluteeniton, kuitu

### Käyttäjät
- Salasanan ja muidenkaan tietojen muodolle ei ole vaatimuksia

### Tilaukset
- Tilauksen voi tehdä vain yhdelle pizzalle
  - Tähän voisi rakentaa ostoskori-toiminnon, jotta samaan tilaukseen voisi lisätä eri pizzoja halutun määrän

### Käyttöliittymä
- Listaussivut ovat hieman hankalia etenkin mobiililaitteilla, koska kaikki tieto ei mahdu ruudulle samaan aikaan
  - Tietojen taulukkoesitystä voisi parantaa mobiililaitteilla
  - Taulukoissa ei ole sivutusta, tosin tämän sovelluksen pienillä tietomäärillä se ei juurikaan haittaa

- Jos käyttäjä ei ole kirjautunut sisään ja hän yrittää mennä sivulle joka vaatii kirjaumista, hänet ohjataan kirjautumissivulle. Sisäänkirjautumisen jälkeen sovellus siirtää käyttäjän etusivulle.
  - Olisi parempi, jos sovellus muistaisi minne käyttäjä halusi alunperin mennä ja ohjaisi kirjautumisen jälkeen sinne sivulle

- Värimaailma perustuu tällä hetkellä Bootstrapin vakioväreihin
  - Tyylejä ja värimaailmaa voisi kustomoida omilla css-määrityksillä