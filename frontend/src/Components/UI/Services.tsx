import React from 'react';

import './Services.css';

const serviceData = [
    {
        icon:'ri-user-search-line',
        title: 'Search Doctor',
        description: 'Choose your doctor from thousands of specialist, general, and trusted practitioners'
    },
    {
        icon:'ri-apps-line',
        title: 'Search Doctor',
        description: 'Choose your doctor from thousands of specialist, general, and trusted practitioners'
    },
    {
        icon:'ri-apps-line',
        title: 'Search Doctor',
        description: 'Choose your doctor from thousands of specialist, general, and trusted practitioners'
    },
    {
        icon:'ri-apps-line',
        title: 'Search Doctor',
        description: 'Choose your doctor from thousands of specialist, general, and trusted practitioners'
    }
]

const Services = () => {
  return (
    <section id="service">
        <div className="container">
            <div className="services__top-content">
                <h6 className="subtitle">
                    Our Services
                </h6>
                <h2>Save time while taking care of yourself with</h2>
                <h2 className="highlight">Our best services</h2>
            </div>
            <div className="service__item-wrapper">
                {
                    React.Children.toArray(
                        serviceData.map(
                            (item, index) => (
                                <div className="service__item">
                                    <span className="service__icon">
                                        <i className={item.icon}></i>
                                    </span>
                                    <h3 className="service__title">
                                        {item.title}
                                    </h3>
                                    <p className="description">
                                        {item.description}
                                    </p>
                                </div>
                            )
                        )
                    )
                }



            </div>
        </div>
    </section>
  )
}


export default Services