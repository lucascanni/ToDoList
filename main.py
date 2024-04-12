# Import du framework
from fastapi import FastAPI

# Import des routers
from routers import router_todos

# Import de la description de l'API
from documentation.description import api_description

# Création de l'application
app = FastAPI(
    title='ToDoListAPI',
    description=api_description,
    docs_url='/',
)

# Ajout des routers
app.include_router(router_todos.router)