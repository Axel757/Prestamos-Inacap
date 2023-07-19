import React from 'react';
import LogoInacap from '../media/1200px-Logotipo_Inacap.svg.png';
import InacapImage1 from '../media/header-sede.jpg';
import InacapImage2 from '../media/header3.jpg';
import InacapImage3 from '../media/maxresdefault.jpg';
import { Link } from 'react-router-dom';
import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

class LoginScreen extends React.Component {
  state = {
    // Estado inicial aquí si es necesario
  };

  // Ciclo de vida, eventos y otros métodos del componente

  render() {
    const LogoInacapStyles = {
      width: '200px',
      height: 'auto',
      position: 'absolute',
      top: '0',
      left: '0',
    };
    return (
      <main>
        <h1>Bienvenido!</h1>
        <div id="carouselExampleSlidesOnly" className="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
          <div className="carousel-inner">
            <div className="carousel-item active">
              <img src={InacapImage1} className="carousel-image" alt="..." />
            </div>
            <div className="carousel-item">
              <img src={InacapImage2} className="carousel-image" alt="..." />
            </div>
            <div className="carousel-item">
              <img src={InacapImage3} className="carousel-image" alt="..." />
            </div>
          </div>
        </div>
        <img src={LogoInacap} style={LogoInacapStyles} alt="Logo Inacap" />
        <br></br>
        <div className='LoginForm'>
          <input type='text' placeholder='Ingrese su Rut' />
          <br></br>
          <br></br>
          <input type='password' placeholder='Ingrese su Contraseña' />
          <br></br>
          <br></br>
          <Link to="/MainScreen">
          <button type="button" class="btn btn-secondary">Iniciar Sesión</button>
          </Link>
        </div>
      </main>
    );
  }
}

export default LoginScreen;