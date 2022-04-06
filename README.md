# Tic Tac Toe
Sovelluksella pelataan ristinollaa mielivaltaisen kokoisella ruudukolla mielivaltaista määrää vastustajia vastaan. Ohjelmalla voi pelata myös tietokonepelaajaa vastaan. Ohjelma pitää kirjaa voitoista ja tappioista jokaisen pelaajan (ihmisen) osalta.

## Toimintaympäristö
Ohjelman toiminta on testattu Python versiolla 3.8 laitoksen Linux ympäristössä. Ohjelma voi toimia myös aikaisemmilla versioilla ja muilla käyttöjärjestelmillä, mutta tätä ei ole varmennettu.

## Dokumentaatio
- [Tuntikirjanpito](https://github.com/JonathanHeyno/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Vaatimusmäärittely](https://github.com/JonathanHeyno/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/JonathanHeyno/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/JonathanHeyno/ot-harjoitustyo/new/master/dokumentaatio)

## Komentorivitoiminnot
### Ohjelman suorittaminen
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
Koodin laadun tiedoston [.pylintrc](https://github.com/JonathanHeyno/ot-harjoitustyo/blob/master/.pylintrc) määrittelemien ehtojen mukaisesti voi arvioida komennolla
```
poetry run invoke lint
```
