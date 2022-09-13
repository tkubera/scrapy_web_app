# Readme

### Poznatky:
stránky https://www.sreality.cz/ jsou javascript hevy. Pro načtení stránky je potřeba cca 300 requestů.
Využil jsem framework scrapy a Scrapy Playwright (využívá hedless prohlížeč pro načtení celé stránky) 
poté je request předán scrapy frameworku.

### Docker příkazy

### Vývojové prostředí
Spuštění se sestavením.
```
docker-compose up --build
```
Vytvoření databáze po spuštění kontejnerů:
```
docker-compose exec web python manage.py create_db
```
Clear cache, smazaní souboru cache.json
```
docker-compose exec web python manage.py clear_cache
```

### Produkční prostředí
Robustnější konstrukce projektu, použití gunicornu a nginxu. (není plně otestovaná funkčnost)

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
-v odstranění volume


