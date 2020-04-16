# Pizzapalvelu

Aiheena on tehdä yhden ravintolan pizzatilauspalvelu. Ravintolassa on tarjolla useita eri pizzoja, jotka koostuvat eri täytteistä. Pizzoilla on eri hinnat ja niitä voidaan lisätä tilaukseen haluttu määrä.

Asiakas voi valita pizzat valikosta ja tehdä tilauksen. Asiakkaan tulee rekisteröityä ja olla kirjautunut, jotta voi tehdä tilauksen. Rekistöitymisessä asiakas täyttää yhteystietonsa ja tekee käyttäjätunnukset.

Ylläpitäjä voi hallita sisältöjä. Eli katsella, lisätä, muokata ja poistaa täytteitä, pizzoja, tilauksia sekä asiakkaita.

Tietokannan taulut ovat: Account, Orders, Pizza, Topping

Liitostauluja ovat: OrderPizza, PizzaTopping

## Sovellus netissä

[Pizzapalvelu Herokussa](https://desolate-bayou-52025.herokuapp.com/)

## Testitunnukset

Admin
- teppo
- testaaja

Asiakas
- ari
- asiakas

## Dokumentaatio
 
[Tietokantakaavio](https://github.com/juissijohtaja/Pizzapalvelu/blob/master/documentation/Pizzapalvelu-dbdiagram.png)

[Käyttötapaukset / user storyt](https://github.com/juissijohtaja/Pizzapalvelu/blob/master/documentation/userstoryt.md)

[Käyttöohje](https://github.com/juissijohtaja/Pizzapalvelu/blob/master/documentation/kayttoohje.md)

[Asennusohje](https://github.com/juissijohtaja/Pizzapalvelu/blob/master/documentation/asennusohje.md)


# Osan 5 etapit

- Autorisointi 
  - kirjauneella asiakkaalla (USER) ja ylläpitäjällä (ADMIN) on eri oikeudet sisältöihin
  - ylläpitäjälle näytetään navigaatiossa linkit hallinnointisivuille
  - sisältöjen lisäys/muokkaus/poisto onnistuu vain ylläpitäjäroolilla

- Käytettävyyden viilausta
  - Bootstrap käytössä koko sivustolla
  - visuaalisuutta sekä käytettävyyttä parannettu
  - navigaatiota muokattu
  - lomakkeet muotoiltu uudelleen ja ne reagoivat täytettyyn tietoon

- Toiminnallisuuden täydentäminen (uusia ominaisuuksia)
  - pizzalomakkeet saavat täytteet dynaamisesti ja käyttöliittymä reagoi tehtyhin valintoihin
  - lomakkeiden validointia parannettu, nyt tarkistukset sekä front- että backendissä
  - käyttäjärooleihin reagoiva käyttöliittymä
  - Tilaukset-osion alustava versio olemassa, mutta siitä puuttuu vielä paljon ominaisuuksia

- Kirjoita työhösi alustava asennusohje ja käyttöohje
  - työstö aloitettu
  - tietokantakaavio ja backlog päivitetty

