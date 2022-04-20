# Tic Tac Toe
Sovelluksella pelataan ristinollaa mielivaltaisen kokoisella ruudukolla mielivaltaista määrää vastustajia vastaan. Ohjelmalla voi pelata myös tietokonepelaajaa vastaan. Ohjelma pitää kirjaa voitoista ja tappioista jokaisen pelaajan (ihmisen) osalta.

## Toimintaympäristö
Ohjelman toiminta on testattu Python versiolla 3.8 laitoksen Linux ympäristössä. Ohjelma voi toimia myös aikaisemmilla versioilla ja muilla käyttöjärjestelmillä, mutta tätä ei ole varmennettu.

## Dokumentaatio
- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

- [Changelog](./dokumentaatio/changelog.md)

- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot
### Ohjelman suorittaminen
Asenna riippuvuudet komennolla
```
poetry install
```
Ohjelman voi käynnistää komentoriviltä komennolla
```
poetry run invoke start
```

### Testaus
Ohjelmalle voi ajaa testit komentoriviltä komennolla
```
poetry run invoke test
```

### Testikattavuusraportti
Ohjelmalle saa muodostetua testikattavuusraportin *htmlcov* -hakemistoon komennolla
```
poetry run invoke coverage-report
```

### Koodin laatuvarmistukset
Koodin laadun tiedoston [.pylintrc](./.pylintrc) määrittelemien ehtojen mukaisesti voi arvioida komennolla
```
poetry run invoke lint
```
