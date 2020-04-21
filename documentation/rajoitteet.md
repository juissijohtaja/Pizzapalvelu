# Työn ja sovelluksen rajoitteet, puuttuvat ominaisuudet

### Täytteet

## Pizzat
- Pizzoihin voi valita vain neljä täytettä ja samaa täytettä ei voi valita kahdesti
  - Täytteiden mahdollinen määrä voisi olla suurempi ja saman voisi valita useamman kerran
  - Täytteitä ei myöskään voi vaihtaa tilauksen yhteydessä tällä hetkellä

- Pizzapohjia voisi olla useampi vaihtoehto

### Käyttäjät
- Uuden käyttäjän lisäys onnistuu ainoastaan rekisteröintilomakkeen kautta "julkisella" puolella
  - Näin luodusta käyttäjästä tulee automaattisesti "asiakas" roolin omaava käyttäjä
  - Mikäli käyttäjästä halutaan tehdä ylläpitäjä, se pitää tehdää muokkaamalla käyttäjän tietoja
  - Ylläpitopuolelle voisi lisätä toiminnon, jolla ylläpitäjä voi lisätä käyttäjän ja tehdä siitä haluttaessaan suoraan ylläpitäjän

### Tilaukset
- Tilauksen voi tehdä vain yhdelle pizzalle
  - Tähän voisi rakentaa ostoskori-toiminnon, jotta samaan tilaukseen voisi lisätä eri pizzoja halutun määrän

### Käyttöliittymä
- Värimaailma perustuu tällä hetkellä Bootstrapin vakioväreihin
  - Tyylejä ja värimaailmaa voisi kustomoida vielä enemmän omilla css-määrityksillä

- Listaussivut ovat hieman hankalia etenkin mobiililaitteilla, koska kaikki tieto ei mahdu ruudulle samaan aikaan
  - Tietojen taulukkoesitystä voisi parantaa mobiililaitteilla

### Tietokanta
- Käyttäjäroolit on tehty tietokannassa boolean-muuttujalla
  - Tämän johdosta kirjautuneella käyttäjällä on vain kaksi eri roolia
  - Mikäli haluaisi useamman roolin, pitäisi rakentaa oma taulu käyttäjärooleille

- Salasanat tallennetaan selkokielisenä tietokantaan
  - Salasanojen tallennuksessa tulisi käyttää "hashingia"
