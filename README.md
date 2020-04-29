# Pizzapalvelu

### Aiheen kuvaus

Aiheena on tehdä yhden ravintolan pizzatilauspalvelu. Ravintolassa on tarjolla useita eri pizzoja, jotka koostuvat eri täytteistä. Pizzoilla on eri hinnat ja niitä voidaan lisätä tilaukseen haluttu määrä.

Asiakas voi valita pizzat valikosta ja tehdä tilauksen. Asiakkaan tulee rekisteröityä ja olla kirjautunut, jotta voi tehdä tilauksen. Rekistöitymisessä asiakas täyttää yhteystietonsa ja tekee käyttäjätunnukset.

Ylläpitäjä voi hallita sisältöjä. Eli katsella, lisätä, muokata ja poistaa täytteitä, pizzoja, tilauksia sekä asiakkaita.

Tietokannan taulut ovat: Account, Orders, Pizza, Topping

Liitostauluja ovat: OrderPizza, PizzaTopping


### Sovellus netissä

[Pizzapalvelu Herokussa](https://desolate-bayou-52025.herokuapp.com/)


### Testitunnukset

Admin
- teppo
- testaaja

Asiakas
- ari
- asiakas

### Dokumentaatio

- [Sovelluksen käyttöohje](documentation/kayttoohje.md)
- [Sovelluksen asennusohje](documentation/asennusohje.md)
- [Työn ja sovelluksen rajoitteet, puuttuvat ominaisuudet](documentation/rajoitteet.md)
- [Käyttötapaukset / user storyt ja niihin liittyvät SQL-kyselyt](documentation/userstoryt.md)
- [Tietokantarakenteen kuvaus](documentation/tietokantarakenne.md)

### Omat kokemukset

- Kurssi on ollut erittäin mielenkiintoinen ja opettavainen
- En ollut ennen tätä kurssia tehnyt mitään Pythonilla, nyt sekin tuli tutuksi
- Tietokantojen käyttö sovelluksen taustalla oli mielenkiintoista. Erilaisten liitostaulujen rakentaminen ja niiden hyödyntäminen sovelluksessa oli haastavaa
- SQliten ja PostgreSql:n erilainen toiminta aiheutti jonkin verran harmaita hiuksia. Ongelmien ratkaisussa auttoi, kun oppi tulkitsemaan Herokun logeja
- Flask Forms ja lomakkeiden huolellinen validointi tuli tutuksi ja osoittautui tärkeäksi työvaiheeksi (frontend ja backend)
- Bootstrap oli myös käytössä ensimmäistä kertaa ja siihenkin pääsi hyvin sisälle
- Tiedon ja ratkaisujen hakeminen netistä oli iso osa tätä prosessia
- Tietynlaisten kompromissien tekeminen oli tarpeen sovellusta suunnitellessa, jotta paketti pysyi kasassa huomioiden aikataulu ja potentiaalinen työmäärä
