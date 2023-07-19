import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import '../App.css';
import { Link } from 'react-router-dom';

class MainScreen extends React.Component {

  state = {

  };

  render() {

    return (
        <header>
            <Link to={"/"}>
                <button type="button" className="btn btn-secondary volver" >Cerrar Sesión</button>
            </Link>
            <div className='actionButtons'>
                <table>
                    <tr>
                        <td>
                            <button type="button" class="btn btn-secondary">Registrar un Préstamo</button>
                        </td>
                        <td>
                            <button type="button" class="btn btn-secondary">Realizar búsqueda de Usuarios</button>
                        </td>
                        <td>
                            <Link to={"/PaymentScreen"}>
                            <button type="button" class="btn btn-secondary">Registrar pago de multa</button>
                            </Link>
                        </td>
                        <td>
                            <Link to={"/LoanReportForm"}>
                                <button type="button" class="btn btn-secondary">Generar un Reporte</button>
                            </Link>
                        </td>
                        <td>
                            <button type="button" class="btn btn-secondary">Gestionar Stock de Libros</button>
                        </td>
                        <td>
                            <button type="button" class="btn btn-secondary">Registrar prorroga</button>
                        </td>
                    </tr>
                </table>
            </div>
            <h1>Listado de Préstamos</h1>
        </header>
      );
  }
  
}

export default MainScreen;
