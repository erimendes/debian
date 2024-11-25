from fastapi import FastAPI, WebSocket
from graphene import ObjectType, String, Schema
from starlette.graphql import GraphQLApp

# Criação do aplicativo FastAPI
app = FastAPI()

# Definindo o schema GraphQL
class Query(ObjectType):
    hello = String(description="A simple query to say hello")

    def resolve_hello(self, info):
        return "Hello, World!"

# Criando o Schema GraphQL com a query definida
schema = Schema(query=Query)

# Rota para GraphQL, usando o GraphQLApp
app.add_route("/api/gql", GraphQLApp(schema=schema))

# Rota WebSocket simples
@app.websocket("/api/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Aceita a conexão WebSocket
    while True:
        data = await websocket.receive_text()  # Recebe mensagens do cliente
        await websocket.send_text(f"Message received: {data}")  # Envia de volta para o cliente

# Rota simples de teste (GET)
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with GraphQL and WebSocket!"}
