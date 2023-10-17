import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [promotions, setPromotions] = useState([]);
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Récupération des promotions depuis le serveur
    axios.get('/api/promotions')
      .then(response => {
        setPromotions(response.data);
      })
      .catch(error => {
        console.error(error);
      });

    // Vérification de l'authentification de l'utilisateur
    axios.get('/api/user')
      .then(response => {
        setUser(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const login = () => {
    // Authentification de l'utilisateur
    axios.post('/api/token', {
      username: 'admin', // Remplacez par les informations de connexion de l'utilisateur
      password: 'password123', // Remplacez par le mot de passe de l'utilisateur
    })
      .then(response => {
        setUser(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const logout = () => {
    // Déconnexion de l'utilisateur
    axios.post('/api/logout')
      .then(() => {
        setUser(null);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div className="App">
      <header>
        <h1>Mercadona</h1>
        {user ? <button onClick={logout}>Déconnexion</button> : <button onClick={login}>Connexion</button>}
      </header>
      <main>
        <h2>Promotions</h2>
        <ul>
          {promotions.map(promotion => (
            <li key={promotion.id}>
              <div>
                <p>{promotion.productName}</p>
                <p>Prix réduit de {promotion.discountPercentage}%</p>
                <p>Début: {promotion.startDate}, Fin: {promotion.endDate}</p>
              </div>
            </li>
          ))}
        </ul>
      </main>
    </div>
  );
}

export default App;
