import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

class PaymentScreen extends React.Component {
  state = {
    // Estado inicial aquí si es necesario
  };

  // Ciclo de vida, eventos y otros métodos del componente

  render() {

    return (
      <main>
        <Link to={"/MainScreen"}>
            <button type="button" className="btn btn-secondary volver" >Volver</button>
        </Link>
        <h2>Listado de multas pendientes</h2>
        <Link to={"/PaymentRegister"}>
            <button type="button" class="btn btn-secondary">Continuar</button>
        </Link>
      </main>
    );
  }
}

export default PaymentScreen;