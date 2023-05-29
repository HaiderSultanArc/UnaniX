import React from 'react';
import './About.css';

import aboutImg from '../../assets/images/ab2.png';

const chooseData=[
    {
        icon:'ri-medicine-bottle-line',
        title:'Online Medicine Perscription',
        desc: 'Lorem ipsum dolor sit, amet consectetur adipisicing ratione repellat at culpa. Velit, vero incidunt! Quos, quas.'
    },
    {
        icon:'ri-team-line',
        title:'Dedicated Team',
        desc: 'Lorem ipsum dolor sit, amet consectetur adipisicing repellat at culpa. Velit, vero incidunt! Quos, quas.'
    },
    {
        icon:'ri-customer-service-2-line',
        title:'24/7 Emergency Support',
        desc: 'Lorem ipsum dolor sit, amet consectetur adipisicing repellat at culpa. Velit, vero incidunt! Quos, quas.'
    },
]

const About = () => {
  return (
    <section id="about">
        <div className="container">
            <div className="about__wrapper">
                <div className="about__content">
                <h6 className="subtitle">
                    Why choose us?
                </h6>
                <h2>Specialized in abiding</h2>
                <h2 className="highlight">Online Patients</h2>
                <p className="description about__content-desc">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Deleniti non voluptatum magni voluptas, rerum facere ipsam nam,
                    commodi suscipit autem perspiciatis itaque quae iste modi molestiae tempore cupiditate pariatur error?
                </p>
                <div className="choose__item-wrapper">
                    {
                        React.Children.toArray(
                            chooseData.map(
                                (item, index) => (
                                    <div className="choose__us-item">
                                        <span className="choose__us-icon">
                                            <i className={item.icon}></i>
                                        </span>
                                        <div>
                                            <h4 className="choose__us-title">{item.title}</h4>
                                            <p className="description">{item.desc}</p>
                                        </div>
                                    </div>
                                )
                            )
                        )
                    }
                </div>

                </div>
                <div className="about__img">
                    <img src={aboutImg} alt="AboutUsImage" />
                </div>

            </div>
        </div>
    </section>
  )
}

export default About