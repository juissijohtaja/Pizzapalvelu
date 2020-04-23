# Asennusohje

## Sovelluksen asennus lokaalisti

Avaa komentoterminaali ja siirry kansioon, jonne haluat asentaa sovelluksen.

#### [Komentoterminaali]
##### [Komentoterminaali]
###### (Komentoterminaali)
[Komentoterminaali]
(Komentoterminaali)

Hae sovelluksen tiedostot GitHubin repositoriosta:
git clone https://github.com/juissijohtaja/Pizzapalvelu.git

Siirry äskeen luotuun Pizzpalvelu-kansioon:
> cd Pizzapalvelu

Luodaan hakemiston sisälle Python-virtuaaliympäristö:
> python3 -m venv venv

Aktivoidaan tämän jälkeen virtuaaliympäristö:
> source venv/bin/activate

Sovelluksen riippuvuudet on määritelty tiedostossa requirements.txt. Lataa riippuvuudet:
> pip install -r requirements.txt

Käynnistä sovellus:
> python run.py

#### Selain

Mene selaimella osoitteeseen:
- http://localhost:5000/

Luo käyttäjätili menemällä selaimella osoitteeseen:
- http://localhost:5000/auth/signup/

Tämän jälkeen sinulla on tavallinen käyttäjätili (USER), jonka voi muuttaa ylläpitäjän (ADMIN) tiliksi seuraavalla tavalla.

#### Komentoterminaali

(Tässä vaiheessa kannattaa avata uusi komentoterminaali ja mennä sillä Pizzapalvelu-hakemistoon, jotta voit ottaa sillä yhteyden tietokantaan ja sovellusta voi edelleen pitää käynnissä alkuperäisessä terminaalissa. Vaihtoehtoisesti voit sammuttaa sovelluksen ja käynnistää sen uudelleen tietokantakomentojen jälkeen.)

Luo yhteys paikalliseen tietokantaan:
- sqlite3 application/pizzapalvelu.db

Huom. mikäli olet jo luonut useampia kuin yhden käyttäjätilin, tarkista tietokannasta sen käyttäjän id-numero, jolle ylläpito-oikeudet halutaan antaa. Katso käyttäjien tiedot tietokannasta:
- SELECT * FROM account;

Anna haluamallesi käyttäjätilille (id) ylläpitäjän oikeudet. Tee muutos tietokantaan:
- UPDATE account SET admin = True WHERE id = 1;

Voit halutessasi sulkea yhteyden tietokantaan:
- .quit

#### Selain

Nyt voit kirjautua valitsemallasi käyttäjätilillä uudelleen sisään ja pääset ylläpitopuolelle.
Tämän jälkeen voit käyttää sovellusta, hallinnoida sisältöjä ja antaa haluamillesi käyttäjille ylläpitäjän oikeudet ylläpitosivujen kautta.

Lisää aiheesta:
[Sovelluksen käyttöohje](documentation/kayttoohje.md)


## Sovelluksen asennus Herokuun

Avaa Pizzapalvelu-hakemisto komentoterminaalissa.

Herokun (sovelluksen käynnistämistä varten) tarvitsema Procfile-tiedosto on jo olemassa, joten voimme suoraan luoda sovellukselle paikan Herokuun.

#### Komentoterminaali

Luo sovellukselle paikka Herokuun: 
- heroku create

Nyt sovellukselle on paikka Herokussa. Samalla saat Herokuun luodun sivuston osoitteen esim.
Creating app... done, ⬢ afternoon-tundra-13408
https://afternoon-tundra-13408.herokuapp.com/ | https://git.heroku.com/afternoon-tundra-13408.git

(Mikäli avaat osoitteen selaimella, huomaat että sovellus ei ole vielä siellä.)

Lähetä projekti Herokuun:
- git push heroku master

#### Selain

Operaation valmistuttua voit mennä edellisessä vaiheessa saamaasi osoitteeseen (pävitä sivu tarvittaessa) ja huomaat, että sovellus pyörii nyt Herokun palvelimella.

#### Komentoterminaali

Sovelluksella ei ole vielä Herokussa tietokantaa, joten korjataan tilanne.

Luo Herokuun ympäristömuuttuja HEROKU:
- heroku config:set HEROKU=1

Ota käyttöön Herokun PostgreSQL-tietokanta:
- heroku addons:add heroku-postgresql:hobby-dev

Tietokanta onnyt käytössä.

#### Selain

Luo uusi käyttäjätili sovelluksessa.

Nyt sinulla on tavallinen käyttäjätili (USER), jonka voi muuttaa ylläpitäjän (ADMIN) tiliksi seuraavalla tavalla.

#### Komentoterminaali

Luo yhteys Herokun tietokantaan:
- heroku pg:psql

Huom. mikäli olet jo luonut useampia kuin yhden käyttäjätilin, tarkista tietokannasta sen käyttäjän id-numero, jolle ylläpito-oikeudet halutaan antaa. Katso käyttäjien tiedot tietokannasta:
- SELECT * FROM account;

Anna haluamallesi käyttäjätilille (id) ylläpitäjän oikeudet. Tee muutos tietokantaan:
- UPDATE account SET admin = True WHERE id = 1;

Voit halutessasi sulkea yhteyden tietokantaan:
- \q

#### Selain

Nyt voit kirjautua valitsemallasi käyttäjätilillä uudelleen sisään ja pääset ylläpitopuolelle.
Tämän jälkeen voit käyttää sovellusta, hallinnoida sisältöjä ja antaa haluamillesi käyttäjille ylläpitäjän oikeudet ylläpitosivujen kautta.

Lisää aiheesta:
[Sovelluksen käyttöohje](documentation/kayttoohje.md)