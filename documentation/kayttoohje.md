# Käyttöohje

Sivustolla on kolme erilaista käyttäjätasoa: kirjautumaton asiakas, kirjautunut asiakas ja kirjautunut ylläpitäjä
- kirjautumaton asiakas voi selailla sivustoa
- kirjautunut asiakas voi edellisen lisäksi tehdä tilauksen ja katsella omia asiakastietojaan
- kirjautunut ylläpitäjä voi edellisten lisäksi selailla ylläpitopuolta sekä hallinnoida sisältöjä (lisätä/muokata/poistaa täytteitä, pizzoja, asiakkaita ja tilauksia)

Mene sivustolle ja selaile sivuja
- [Pizzapalvelu](https://desolate-bayou-52025.herokuapp.com)
- sivusto toimii responsiivisesti, joten kokeile sivustoa eri päätelaitteilla tai muuta selainikkunan kokoa


## Kirjautumaton asiakas

(Huom. mikäli olet jo kirjautunut ylläpitäjänä, kirjaudu ensin ulos)

### Kirjaudu sisään

Klikkaa Kirjaudu sisään -nappia
- [Kirjaudu sisään](https://desolate-bayou-52025.herokuapp.com/auth/login/)
  - Huom. mikäli sinulla ei ole tunnuksia, klikkaa lomakkeen alareunassa kohtaa Luo tunnukset (ks. ohje alla) ja palaa sen jälkeen kirjautumissivulle
- täytä kenttiin omat tunnuksesi tai seuraavat tunnukset
  - käyttäjätunnus: ari
  - salasana: asiakas
- klikkaa Kirjaudu sisään -nappia  

### Luo tunnukset

Voit halutessasi luoda omat käyttäjätunnukset
- [Luo tunnukset](https://desolate-bayou-52025.herokuapp.com/auth/signup/)
- täytä kenttiin käyttäjätunnus ja salasana
  - salasanat tallennetaan tietokantaan kryptattuna
  - salasanalla ei ole muita muotovaatimuksia kuin pituus (2-50 merkkiä)
- klikkaa Luo tunnukset -nappia

## Kirjautunut asiakas

### Tilaa pizza

Klikkaa haluamasi pizzan kohdalla Tilaa-nappia
- tarkista, että yhteystietosi ja haluamasi pizza on tilauksessa oikein
- valitse tilauksen toimitustapa
- klikkaa Lähetä tilaus -nappia

### Katsele asiakastietoja

Klikkaa navigaatiopalkin oikeasta reunasta "käyttäjä" ikonia
- tästä aukeaa valikko, josta voi klikata Asiakastiedot-linkkiä

Asiakastiedo-sivulla näkyvät kirjautuneen käyttäjän yhteystiedot sekä tehdyt tilaukset ja niiden toimituksen tila.

### Kirjaudu ulos

Klikkaa navigaatiopalkin oikeasta reunasta "käyttäjä" ikonia
- tästä aukeaa valikko, josta voi klikata Kirjaudu ulos -nappia


## Ylläpitäjä

(Huom. mikäli olet jo kirjautunut asiakkaana, kirjaudu ensin ulos)

### Kirjaudu sisään

Klikkaa Kirjaudu sisään -nappia
- [Kirjaudu sisään](https://desolate-bayou-52025.herokuapp.com/auth/login/)
- täytä kenttiin seuraavat tunnukset:
  - käyttäjätunnus: teppo
  - salasana: testaaja
- klikkaa Kirjaudu sisään -nappia

Ylläpitonavigaatio
- ylläpidon navigaatiopalkki näkyy ainoastaan ADMIN-oikeudet omaaville sisäänkirjautuneille käyttäjille
- desktop-laitteella ylläpidon navigaatiopalkki ilmestyy päänavigaation alle
- mobiililaitteella ylläpidon navigaatiopalkki aukeaa klikkaamalla Pizzeria-logon vasemmalla puolella olevaa "ratas" painiketta
- muilta osin toiminnallisuudet ovat sama päätelaitteesta riippumatta
  - Huom. kaikkien tietojen listaukset eivät välttämättä mahdu kokonaan mobiililaitteen ruudulle, joten niitä voi joutua "skrollaamaan# sivuttaissuunnassa

### Täytteet

Mene ylläpitosivun Täytteet-välilehdelle
- [Täytteet](https://desolate-bayou-52025.herokuapp.com/taytteet/)

Klikkaa Lisää täyte -nappia
- täytä vaadittavat tiedot ja paina Lisää täyte -nappia
- mikäli haluat poistua lomakesivulta, klikkaa lomakkeen oikeassa yläkulmassa X-nappia

Klikkaa jonkin täytteen kohdalta sen nimeä tai sivun oikeassa reunassa olevaa Muokkaa-nappia
- voit muokata täytteen nimeä
- voit tallentaa muutokset klikkaamalla Tallenna täyte -nappia
- mikäli haluat poistaa täytteen, klikkaa Poista täyte -nappia sekä vahvista poisto avautuvasta ilmoituksesta
- mikäli haluat poistua täytesivulta ilman tallennusta, klikkaa lomakkeen oikeassa yläkulmassa X-nappia

Tallennetut muutokset näkyvät Täytteet-listauksessa.

### Pizzat

Mene ylläpitosivun Pizzat-välilehdelle
- [Pizzat](https://desolate-bayou-52025.herokuapp.com/pizzat/)

Klikkaa Lisää pizza -nappia
- täytä vaadittavat tiedot ja paina Lisää pizza -nappia
- mikäli haluat poistua lomakesivulta, klikkaa lomakkeen oikeassa yläkulmassa X-nappia

Klikkaa jonkin pizaan kohdalta sen nimeä tai sivun oikeassa reunassa olevaa Muokkaa-nappia
- voit muokata pizzan tietoja ja vaihtaa täytteitä pudotusvalikoista
  - huom. ensimmäinen täyte on pakollinen ja kahta samaa täytettä ei voi valita
- voit tallentaa muutokset klikkaamalla Tallenna pizza -nappia
- mikäli haluat poistaa pizzan, klikkaa Poista pizza -nappia sekä vahvista poisto avautuvasta ilmoituksesta
- mikäli haluat poistua pizzasivulta ilman tallennusta, klikkaa lomakkeen oikeassa yläkulmassa X-nappia

Tallennetut muutokset näkyvät Pizzat-listauksessa.

### Käyttäjät

Mene ylläpitosivun Käyttäjät-välilehdelle
- [Käyttäjät](https://desolate-bayou-52025.herokuapp.com/kayttajat/)

Klikkaa jonkin käyttäjän kohdalta sen nimeä tai sivun oikeassa reunassa olevaa Muokkaa-nappia
- voit muokata käyttäjän kaikkia tietoja
- voit tehdä käyttäjästä ylläpitäjän/tavallisen käyttäjän napsauttamalla Ylläpitäjä-valinnan päälle/pois päältä
- voit tallentaa muutokset klikkaamalla Tallenna käyttäjä -nappia
- mikäli haluat poistaa käyttäjän, klikkaa Poista käyttäjä -nappia sekä vahvista poisto avautuvasta ilmoituksesta
- mikäli haluat poistua käyttäjäsivulta ilman tallennusta, klikkaa lomakkeen oikeassa yläkulmassa X-nappia

Tallennetut muutokset näkyvät Käyttäjät-listauksessa.

### Tilaukset

Mene ylläpitosivun Tilaukset-välilehdelle
- [Tilaukset](https://desolate-bayou-52025.herokuapp.com/tilaukset/)

Klikkaa jonkin tilauksen kohdalta sen nimeä tai sivun oikeassa reunassa olevaa Muokkaa-nappia
- muokkaa tilauksen tietoja ja klikkaa Tallenna tilaus -nappia
  - huom. tilaajan tietoja sekä tilattua pizzaa ei voi muokata
- voit vaihtaa toimitustapaa tai merkata tilauksen vastaanotetuksi sekä toimitetuksi napsauttamalla kyseiset valinnat päälle/pois päältä
- mikäli haluat poistaa käyttäjän, klikkaa Poista käyttäjä -nappia sekä vahvista poisto avautuvasta ilmoituksesta
- mikäli haluat poistua tilaussivulta ilman tallennusta, klikkaa lomakkeen oikeassa yläkulmassa X-nappia

Tallennetut muutokset näkyvät Tilaukset-listauksessa.

### Katsele käyttäjätietoja

Klikkaa navigaatiopalkin oikeasta reunasta "käyttäjä" ikonia
- tästä aukeaa valikko, josta voi klikata Käyttäjätiedot-linkkiä

Käyttäjätiedot-sivulla ylläpitäjä voi muokata ja tallentaa käyttäjätietonsa.

### Kirjaudu ulos

Klikkaa navigaatiopalkin oikeasta reunasta "käyttäjä" ikonia
- tästä aukeaa valikko, josta voi klikata Kirjaudu ulos -nappia

### Etusivun nostot

Etusivulla on muutama sisältönosto, joiden käyttäminen hieman poikkeaa muusta sisällöstä. Ylhäällä on iso "jumbotron" ja alempana sivulla on "ananaspizzat" ja "tuliset pizzat" promopaikat.

Jumbotronin sisältö sekä linkki haluttuun pizzaan määritellään manuaalisesti. Linkki haluttuun pizzaan määritellään linkki-elementin sisällä eli pizza_id kohtaan laitetaan halutun pizzan id-numero:
- `<a href="{{ url_for('orders_form', pizza_id=1) }}" ... > `

Ananaspizzat-nostossa näkyvät sellaiset pizzat, joissa on täytteenä valittu "ananas". Nostoa ei näytetä, mikäli tällaisia pizzoja ei ole luotu. Luo siis ensin täyte nimeltä "ananas" ja sen jälkeen luo pizza, johon valitaan täytteeksi ananas.

Tuliset pizzat -nostossa näkyvät sellaiset pizzat, joissa on täytteenä valittu "chili" ja/tai "jalapeno". Nostoa ei näytetä, mikäli tällaisia pizzoja ei ole luotu. Luo siis ensin täyte nimeltä "chili" ja/tai "jalapeno" ja sen jälkeen luo pizza, johon valitaan täytteeksi toinen tai molemmat em. täytteistä.