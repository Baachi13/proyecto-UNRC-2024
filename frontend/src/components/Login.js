import React, { useState } from 'react';
import '../assets/css/Login.css';

const Login = ({toggleForm}) => {
  // Define los estados para username, password y message usando el hook useState.
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  // Función que maneja el envío del formulario.
  const handleLogin = async (e) => {
    e.preventDefault(); // Previene el comportamiento por defecto del formulario (recargar la página).

    try {
      // Realiza una solicitud POST al servidor para autenticar al usuario.
      const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json', // Indica que el cuerpo de la solicitud está en formato JSON.
        },
        body: JSON.stringify({ username, password }), // Convierte los valores de username y password a JSON.
      });

      const data = await response.json(); // Parsea la respuesta del servidor como JSON.

      if (response.ok) {
        setMessage(data.message);
      } else {
        setMessage(data.error);
      }
    } catch (error) {
      setMessage('Error en la conexión');
    }
  };

  // JSX que define la estructura y el contenido del formulario de login.
  return (
      <div className="login-container">
        <div className="login-form">
          <h2>Login</h2>
          <form onSubmit={handleLogin}>
            <div className="input-group">
              <label>Username:</label>
              <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)} // Actualiza el estado de username cuando cambia el valor del input.
                  required
              />
            </div>
            <div className="input-group">
              <label>Password:</label>
              <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)} // Actualiza el estado de password cuando cambia el valor del input.
                  required
              />
            </div>
            <button type="submit">Login</button> {}
            {message && <p className="message">{message}</p>} {}
          </form>
          <p>
          If you're not registered,{' '}
          <span
            onClick={toggleForm}
            className="hover-link"
          >
            click here
          </span>
          .
        </p>
        </div>
      </div>
  );
};

export default Login;
