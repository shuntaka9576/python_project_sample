# python-project-template

## Start Project
### install packages
create .venv directory
```bash
poetry install
```
### install pre-commit
```bash
poetry run pre-commit install
```

## Poetry commands
### add packages
```bash
poetry add matplotlib

# devDependencies
poetry add black --dev
```

### check config
```bash
poetry config --list
```

### create .venv directory
```bash
poetry config --local virtualenvs.in-project true
# => create poetry.toml file
```
