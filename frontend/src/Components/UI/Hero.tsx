import Button from '@mui/material/Button';
import './Hero.css';
// import {ButtonProps} from '@mui/material/Button';

import heroImg from '../../assets/images/12.png';

const Hero = () => {
  return (
    <section className='hero__section'>
        <div className="container">
            <div className="hero__wrapper">
                <div className="hero__content">
                    <div>
                        <h2>We are providing</h2>
                        <h2>virually healthcare </h2>
                        <h2 className='highlight'>With Unani Med</h2>
                    </div>
                    <p className="description">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Deserunt vitae aut facilis quam blanditiis sint.
                    </p>
                    <div className="hero__btns">
                        <Button sx={{color: "white", "text-transform": "none" }} variant="outlined" size="medium">
                            Book Appointments
                        </Button>
                        <Button variant="contained" sx={{"text-transform": "none"}} size="medium">
                            Discover More
                        </Button>
                    </div>
                </div>
                <div className="hero__img">
                    <img src={heroImg} alt="Hero-Img" />
                </div>
            </div>
        </div>

    </section>
  )
}

export default Hero