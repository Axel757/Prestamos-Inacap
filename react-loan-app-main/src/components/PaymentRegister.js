import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import billete1k from '../media/1000_anverso.jpg';
import billete2k from '../media/2000_anverso.jpg';
import billete5k from '../media/5000_anverso.jpg';
import billete10k from '../media/6557-10000-pesos-2.jpg';
import billete20k from '../media/20000-anverso.jpg';
import moneda10 from '../media/10-reverso.png';
import moneda50 from '../media/50-reverso.png';
import moneda100 from '../media/100Moneda.png';
import moneda500 from '../media/500Moneda.png';

class PaymentRegister extends React.Component {
  state = {
    totalAmount: 0,
  };

  handleClick = (imageValue) => {
    this.setState((prevState) => ({
      totalAmount: prevState.totalAmount + imageValue,
    }));
  };

  resetTotalAmount = () => {
    this.setState({
      totalAmount: 0,
    });
  };

  render() {
    const { totalAmount } = this.state;

    return (
      <main>
        <Link to={"/PaymentScreen"}>
            <button type="button" className="btn btn-secondary volver" >Volver</button>
        </Link>
        <div className='moneyForm'>
          <h1>Resgistrar pago de multas</h1>
          <table>
            <tr>
              <td>
                <a>
                  <img src={billete1k} className='billete' onClick={() => this.handleClick(1000)} />
                </a>
              </td>
              <td>
                <img src={moneda10} className='moneda' onClick={() => this.handleClick(10)} />
              </td>
            </tr>
            <tr>
              <td>
                <a>
                  <img src={billete2k} className='billete' onClick={() => this.handleClick(2000)} />
                </a>
              </td>
              <td>
                <img src={moneda50} className='moneda' onClick={() => this.handleClick(50)} />
              </td>
            </tr>
            <tr>
              <td>
                <a>
                  <img src={billete5k} className='billete' onClick={() => this.handleClick(5000)} />
                </a>
              </td>
              <td>
                <img src={moneda100} className='moneda' onClick={() => this.handleClick(100)} />
              </td>
            </tr>
            <tr>
              <td>
                <a>
                  <img src={billete10k} className='billete' onClick={() => this.handleClick(10000)} />
                </a>
              </td>
              <td>
                <img src={moneda500} className='moneda' onClick={() => this.handleClick(500)} />
              </td>
            </tr>
            <tr>
              <td>
                <a>
                  <img src={billete20k} className='billete' onClick={() => this.handleClick(20000)} />
                </a>
              </td>
            </tr>
          </table>
          <div className='totalAmount'>
            <p>Monto total: {totalAmount}</p>
            <button type="button" className="btn btn-secondary" onClick={this.resetTotalAmount}>
              Eliminar Monto
            </button>
            <button type="button" className="btn btn-secondary">
                Registrar pago con débito
            </button>
          </div>
        </div>
      </main>
    );
  }
}

export default PaymentRegister;
