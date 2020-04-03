# Pizzapalvelu

Aiheena on tehdä yhden ravintolan pizzatilauspalvelu. Ravintolassa on tarjolla useita eri pizzoja, jotka koostuvat eri täytteistä. Pizzoilla on eri hinnat ja niitä voidaan lisätä tilaukseen haluttu määrä.

Asiakas voi valita pizzat valikosta ja tehdä tilauksen. Asiakkaan tulee rekisteröityä ja olla kirjautunut, jotta voi tehdä tilauksen. Rekistöitymisessä asiakas täyttää yhteystietonsa ja tekee käyttäjätunnukset.

Ylläpitäjä voi hallita sisältöjä. Eli katsella, lisätä, muokata ja poistaa täytteitä, pizzoja, tilauksia sekä asiakkaita.

Tietokannan taulut ovat: Account, Order, Pizza, Topping

Liitostauluja ovat: OrderPizza, PizzaTopping


[Sovellus Herokussa](https://desolate-bayou-52025.herokuapp.com/)

Testitunnukset:
- teppo
- testaaja
 
[Tietokantakaavio](https://github.com/juissijohtaja/Pizzapalvelu/blob/master/documentation/Pizzapalvelu-dbdiagram.png)

[Käyttötapaukset / user storyt](https://github.com/juissijohtaja/Pizzapalvelu/blob/master/documentation/userstoryt.md)


# Osan 4 etapit

- kolme tietokantataulua käytössä: pizza, täytteet, käyttäjät
- monimutkainen SQL:llä kirjoitettu toimii lokaalisti, mutta hajotti herokun, joten se on vielä työn alla
- bootstrap käytössä
- menupalkki toimii nyt paremmin ja reagoi kirjautuneen tilaan paremmin
- lomakkeissa paluu-napit ja muita parannuksia
