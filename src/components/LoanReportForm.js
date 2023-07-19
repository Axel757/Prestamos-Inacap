import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

class LoanReportForm extends React.Component {
  state = {};

  render() {
    const inputStyle = {
      width: '500px', 
      padding: '10px', 
      border: '1px solid #ccc', 
      borderRadius: '4px', 
      fontSize: '16px', 
    };

    return (
      <main>
        <Link to={"/MainScreen"}>
                <button type="button" className="btn btn-secondary volver" >Volver</button>
        </Link>
        <h1>Generar un reporte</h1>
        <div className="input-group mb-3">
          <input
            type="text"
            className="form-control"
            placeholder="Ingrese la fecha de la cual desea obtener un reporte (DD-MM-AAAA)"
            aria-label="Recipient's username"
            aria-describedby="button-addon2"
            style={inputStyle}
          />
        </div>
        <button type="button" class="btn btn-secondary">Generar</button>
      </main>
    );
  }
}

export default LoanReportForm;
