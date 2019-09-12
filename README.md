```provider.stage = local(default)```

# Local

```
cp env/env.yml.example env/local.yml
cp .env.example .env
python manage.py collectstatic
npx sls wsgi serve
```

# Deploy

```
cp env/env.yml.example env/dev.yml
cp .env.example .env
python manage.py collectstatic
npx sls deploy --stage dev
```
