# Tic Tac Toe
Sovelluksella pelataan ristinollaa maksimissaan 50x50 kokoisella ruudukolla mielivaltaista määrää vastustajia vastaan. Ohjelmalla voi pelata myös tietokonepelaajia vastaan. Ohjelma pitää kirjaa voitoista ja tappioista jokaisen pelaajan (ihmisen) osalta.

## Releases
[Release Viikko 6](https://github.com/JonathanHeyno/ot-harjoitustyo/releases/tag/viikko6)

[Release Viikko 5](https://github.com/JonathanHeyno/ot-harjoitustyo/releases/tag/viikko5)

## Toimintaympäristö
Ohjelman toiminta on testattu Python versiolla 3.8 laitoksen Linux ympäristössä sekä Windowsissa. Ohjelma voi toimia myös aikaisemmilla versioilla ja muilla käyttöjärjestelmillä, mutta tätä ei ole varmennettu.

## Dokumentaatio
- [Käyttöohje](./dokumentaatio/kayttoohje.md)

- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

- [Changelog](./dokumentaatio/changelog.md)

- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](./dokumentaatio/testaus.md)

## Komentorivitoiminnot
### Ohjelman suorittaminen
Mene ohjelman kansioon ja asenna riippuvuudet komennolla
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
