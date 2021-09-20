# Python Fagkveld 2. september 2021

Denne mappa inneheld den endelege versjonen av kode og konfigurasjonar som blei vist fram under Python-fagkvelden 2. september 2021.

## VS Code 

Microsoft sin offisielle extension [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) gir støtte for Python i VS Code.

## Verktøy

* [pipenv](https://pipenv.pypa.io/en/latest/) - Installasjon av pakker og handering av virtuelle miljø.
* [black](https://github.com/psf/black) - Formattering av kode for å vere lik den "offisielle" kodekonvensjonen for standardbiblioteket i Python.
* [flake8](https://flake8.pycqa.org/en/latest/) - Kode-linter som advarer om syntaks-feil, moglege bugs og har meir kontroll på innhald framfor stil.
* [isort](https://github.com/PyCQA/isort) - Sorterer importerte pakker og modular alfabetisk, separert etter seksjon og type.
* [mypy](http://mypy-lang.org/) - Statisk type-sjekking i Python.
* [pre-commit](https://pre-commit.com/) - Rammeverk for å handtere og vedlikeholde pre-commit-hooks i git.


## Konfigurasjonar 

* `Pipfile` og `Pipfile.lock` for Pipenv. 
* `setup.cfg` for black, flake8, isort og mypy.
* `.pre-commit-config.yaml` for pre-commit.

Fila `.vscode/settings.json` inneheld innstillingane som gjer at dei installerte Python-verktøya blir tatt i bruk av VS Code.


## Installasjon 

Krever Python og pip installert. Pipenv kan då bli installert i heimemappa gjennom terminalen ved å skrive: 

```pip install --user pipenv```

Gå inn i rotmappa for prosjektet med Pipenv sette opp eit virtuelt miljø og installere pakkene som er spesifiserte i Pipfile:

```pipenv install --dev```

Merk at Python 3.8 må vere installert og ligge i `PATH` for at Pipenv skal kunne finne den spesfikke Python-installasjonen og ta den i bruk.

Ved å skrive `Ctrl`+`Shift`+`P` inne i VS Code får ein opp ei kommandoboks, der ein kan skrive `Python: Select Interpreter`. Dette vil gi ei liste over virtuelle miljø på systemet. Velg den som har omtrent same namn som rotmappa. VS Code vil då vere konfigurert til å bruke dette virtuelle miljøet for dette prosjektet.

Dersom git hook scripts ikkje er satt opp, kan det gjerast ved å skrive:

```pipenv run pre-commit install```

Koden kan køyrast ved å skrive følgande:

```python main.py```
