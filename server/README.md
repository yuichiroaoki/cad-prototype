
## Start development server
```bash
poetry run uvicorn server.main:app --reload
```

or 

```bash
poetry run start
```

## Lint
```bash
poetry run ruff check .
```


# Export requirements
```bash
poetry export -f requirements.txt --output requirements.txt
```