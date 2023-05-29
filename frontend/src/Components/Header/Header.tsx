import React from 'react';
import {Link} from 'react-router-dom';
import '../Header/Header.css';

const nav__links = [
    {
        path: '#home',
        display:'Home'
    },
    {
        path: '#about',
        display:'About'
    },
    {
        path: '#service',
        display:'Service'
    },
    {
        path: '#resaerch',
        display:'Research'
    },
    {
        path: '/login',
        display:'Login'
    },
]

const Header = () => {
  return (

    <header className="header">
        <div className="container">
            <div className="nav__wrapper">
                <div className="logo">
                    <h2>Unanix</h2>
                    <p>Take care of yourself</p>
                </div>

                {/* =============Nav Bar ===================== */}
                <div className="navigation">
                    <ul className="menu">
                        {
                            React.Children.toArray(
                                nav__links.map(
                                (item, index) => (
                                    <li className="menu__item">
                                        <Link to={item.path} className="menu__link">{item.display}</Link>
                                    </li>
                                )
                            )
                            )
                        }
                    {/* ==============Light Mode================= */}
                    <div className="light__mode">
                        <span>
                    <i className="ri-sun-line"></i>
                    Light Mode
                    </span>
                    </div>

                    </ul>
                </div>

            </div>
        </div>
    </header>
  )
}

export default Header