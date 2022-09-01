# Readme
Projekt obsahuje dvě řešení.
1) (nefunkční) Řešení založené na dockeru s připojenou databází.
2) Funkční částečné řešení (umýstěné v flask_scrapy) - flask + scrapy. Spouštěné z příkazové řádky, jako výsledek json. Spuštění sreveru ```python flask_scrapy/pwdemo/server.py```

### Poznatky:
stránky https://www.sreality.cz/ jsou javascript hevy. Pro načtení stránky je potřeba cca 300 requestů.
Vyuzil jsem framevork scrapy a Scrapy Playwright (využívá hedless prohlížeč pro načtení celé stránky) 
poté je request předán scrapy.

#### K dořešení
Nalézt cestu jak provolat scrapy a Scrapy Playwright z webového rozhraní.

### Docker příkazy - 1 řešení

### Vývojové prostřendí
Při každém spuštění dochazí k přemazání databáze.

```
docker-compose up --build
```

### Produkce
Robustnější konstrukce projektu, použití gunicornu a nginxu. 
Build:
```
docker-compose -f docker-compose.prod.yml up -d --build
```

Běh:
```
docker-compose -f docker-compose.prod.yml up -d
```
Vytvoření databáze:
```
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
```

Stop
```
docker-compose -f docker-compose.prod.yml down -v
```
-v odstranení volume


