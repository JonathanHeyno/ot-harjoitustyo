# Testausdokumentti

Ohjelmaa on testattu sekä laitoksen Linux ympäristössä että Windows ympäristössä manuaalisesti bugien löytämiseksi. Yksikkö- ja integraatiotestausta on suoritettu automaattisesti unittesteillä päivitysten jälkeen.

## Yksikkö- ja integraatiotestaus
Testauskessa käytetyt tiedostot ovat **tests** hakemistossa, joka noudattaa samanlaista rakennetta kuin itse sovelluskin.

### Sovelluslogiikka
`GameService` luokkaa testataan **services** kansiossa *game_service_test.py* tiedostossa luomalla `MockPlayerScoreRepository` olio joka injektoidaan testeissä käytetylle `GameService`-oliolle. **Entities** kansiossa tiedosto *game_test.py* testaa `Game` luokkaa,

### Repository
**repositories** hakemistossa *player_scores_repository_test.py* sitä vastaavaa luokkaa käyttämällä ![.env.test](../.env.test)-tiedostossa määriteltyä tietokantaa tavallisesti käytettävän tietokannan sijaan.

### Testauskattavuus
Käyttöliittymän testaus on jätetty testauksen ulkopuolelle. Tällöin haarautumakattavuus on 87%

![](./dokumentaatio/kuvat/haaraumakattavuus.jpg)

`config.py` tiedoston haaraumakattavuus on alhainen koska siinä muodostetaan aina polut eri tavalla riippuen onko käytössä Windows ympäristö vai Linux. Näin ollen vaiin jompi kumpi haara tulee käytyä läpi kun testit ajetaan.

`human` ja `uniform` luokille ei testata difficulty -vaikeusasetusta koska koska vaikeustason määrittäminen ei ole mielekästä ihmispelaajalle ja pelaajalle joka arpoo satunnaisesti ruudun. Tietokoneen käytössä olevalle `valuebased` algoritmille ei testata voittorivin muodostusta jokaiseen mahdolliseen suuntaan eikä satunnaisesti valitun ruudun oikeellisuutta.

initialize_database() metodin testaus komentoriviltä ajettaessa on myös jätetty pois. `GameService`-luokan testeissä kaikkien eri mahdollisten pelitilanteiden lataamista ei käydä läpi eikö katsota löytääkö järjestelmä kaikki **save** kansiossa olevat tiedostot koska ei pystytä määrittämään mitä kaikkia tiedostoja sinne on tultu luotua käyttäjän toimesta.

## Järjestelmätestaus
`game_service_test.py` tiedostossa on joitain testejä joilla käydään läpi lyhyehkö peli kokonaisuudessa ja katsotaan päätyykö peli oikein loppuun. Muilta osin järjestelmää on testattu manuaalisesti. Etenkin käyttöliittymän toiminnan varmentaminen on suoritettu täysin manuaalisesti

### Asennus ja konfigurointi
Sovellus on haettu ja asennettu alusta alkaensekä linux että Windows ympäristössä ![käyttöohjeessa](./dokumentaatio/kayttoohje.md) kuvatulla tavalla.

### Toiminnallisuudet
![Määrittelydokumentissa](./dokumentaatio/vaatimusmaarittely.md) listatut toiminnallisuudet on käyty myös manuaalisesti läpi ja todettu että ne toimivat sekä Windows että Linux ympäristössä. Ohjelmaa ei olla saatu kaatumaan tai toimimaan virheellisesti millään käyttöliittymän kautta annetulla syötteellä tai toiminnolla.
