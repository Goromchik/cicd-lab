## Локальный запуск
    pip install -r requirements-dev.txt
    flake8 .
    pytest -v
    python app.py

## Docker
    docker run -p 8080:8080 promchiks/cicd-lab:latest
    # открыть http://localhost:8080

## Ссылки
- Пайплайны: https://github.com/Goromchik/cicd-lab.git
- Docker Hub: https://hub.docker.com/r/promchiks/cicd-lab