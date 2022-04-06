# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksella pelataan ristinollaa mielivaltaisen kokoisella ruudukolla mielivaltaista määrää vastustajia vastaan. Ohjelmalla voi pelata myös tietokonepelaajaa vastaan. Ohjelma pitää kirjaa voitoista ja tappioista jokaisen pelaajan (ihmisen) osalta.

## Toimintaympäristö
Ohjelmiston tulee toimia työpöytäsovelluksena laitoksen Linux-koneilla tai uusimmat päivitykset sisältävällä cubbli-linuxilla. Ohjelmisto toimii Python versiolla 3.8. Aiempien python versioiden suhteen ohjelmiston toimintaa ei testata.

## Käyttäjät
Peliä voi pelata normaalisti ihminen. Ohjelmistoon voi helposti lisätä omatekoisia algoritmeja joilla tietokone pelaa. Näin ollen peliä voi myös pelata kaksi tai useampi tietokonepelaaja käyttäen mahdollisesti eri algoritmeja.

## Perusversion tarjoama toiminnallisuus
### New game näkymä
  - Käyttäjä voi määrittää ruudukon koon :green_check_mark:
  - Käyttäjä voi määrittää montako merkkiä pitää saada jonoon
  - Käyttäjä voi rekisteröidä uusia pelaajia
  - Käyttäjä voi määrittää ketkä pelaavat. Pelaajia voi olla enemmän kuin kaksi
  - Käyttäjä voi määrittää millä algoritmeilla tietokonepelaajat pelaavat
  - Käyttäjä voi määrittää tietokonepelaajille vaikeustason
  - Käyttäjä voi määrittää millä symbolilla kukin pelaaja pelaa

### Save näkymä
  - Käyttäjä voi tallentaa pelin tietyllä nimellä
 
### Load näkymä
  - Käyttäjä voi ladata tallennetun pelin
 
### Scores näkymä
  - Ohjelma näyttää kullekin (ihmis) käyttäjälle voitot, tappiot ja tasapelit

## Jatkokehitysideoita
Perusversion toteutuksen jälkeen seuraavia lisäyksiä voidaan lähteä toteuttamaan ajan riittäessä
  - Peliä voi pelata joukkueilla (jokainen päättää vuorollaan mihin joukkue laittaa seuraavaksi)
  - Kompleksisempi muoto: Pelaajat voivat kuulua useampiin eri joukkuesseen siten että jos yksikin niistä voittaa, pelaaja voittaa. Täytyy siis pitää kirjaa mitkä symbolit ovat mukana missäkin joukkueessa 
  - Voittamisen yhteydessä soitetaan fanfaari
  - Peliä voi pelata netin kautta toisia pelaajaa vastaan
  - Tulokset päivittyvät nettiin
  - 3D versio pelistä
