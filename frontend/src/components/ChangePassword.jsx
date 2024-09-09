import React, { useState } from 'react';
import "../assets/css/changePassword.css"

const ChangePassword = ({ isOpen, onClose }) => {

  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [repNewPassword, setRepNewPassword] = useState('');
  const [message, setMessage] = useState('');

  if (!isOpen) return null;


  const handleChangePassword = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5000/change_password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ currentPassword, newPassword, repNewPassword }),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(data.message);
      } else {
        setMessage(data.error);
      }
    } catch (error) {
      setMessage('Error en el cambio de contraseña');
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h1><b>Change Password</b></h1>
        <br></br>
        <form onSubmit={handleChangePassword}>
          <div className="form-group">
            <label htmlFor="currentPassword">Current password</label>
                <input
                  type="password"
                  id="currentPassword"
                  placeholder="Enter current password" 
                  value={currentPassword}
                  onChange={(e) => setCurrentPassword(e.target.value)}
                  required
              />
          </div>
          <div className="form-group">
            <label htmlFor="newPassword">New password</label>
                <input
                  type="password"
                  id="newPassword"
                  placeholder="Enter new password" 
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  required
              />
          </div>
          <div className="form-group">
            <label htmlFor="repNewPassword">Repite new password</label>
                <input
                  type="password"
                  id="repNewPassword"
                  placeholder="Repite new password" 
                  value={repNewPassword}
                  onChange={(e) => setRepNewPassword(e.target.value)}
                  required
              />
          </div>
          <div className="modal-buttons">
            <button type="button" onClick={onClose}>Cancel</button>
            <button type="submit">Change Password</button>
          </div>
          {message && <p className="message">{message}</p>}
        </form>
      </div>
    </div>
  );
};

export default ChangePassword;
