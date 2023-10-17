from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# Exemple de données de promotions
promotions = [
    {"id": 1, "productName": "Produit 1", "discountPercentage": 10, "startDate": "2023-10-01", "endDate": "2023-10-10"},
    {"id": 2, "productName": "Produit 2", "discountPercentage": 20, "startDate": "2023-10-05", "endDate": "2023-10-15"},
]

# Exemple de données d'utilisateur (admin)
admin_user = {"username": "admin", "password": "password123"}

# Middleware pour l'authentification
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Route de récupération des promotions
@app.get("/api/promotions")
def get_promotions():
    return promotions

# Route pour l'authentification
@app.post("/api/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == admin_user["username"] and form_data.password == admin_user["password"]:
        return {"access_token": "fake-access-token", "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Mauvaise authentification")

# Route de vérification de l'utilisateur actuellement connecté
@app.get("/api/user")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    if token == "fake-access-token":
        return {"username": admin_user["username"]}
    raise HTTPException(status_code=401, detail="Non authentifié")

# Route de déconnexion
@app.post("/api/logout")
def logout():
    return {"message": "Déconnecté"}
