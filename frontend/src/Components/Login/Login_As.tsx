import './_Login_As.scss';

import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';

import Button from '@mui/material/Button';
import {Container} from 'react-bootstrap';
import {Link} from 'react-router-dom';


// import {auth} from '../../firebas'

const Login_As= ( ) => {
    return ( 
        <div className= "card">
            <Card sx={{ maxWidth: 2000}} style={{backgroundColor: " #171F34"}}>
            <>
              <Container>
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                  Login As
                </Typography>  
              </Container>

              <Container>
                <Link to="/practitioner_login">
                  <Button style={{width:'85vh'}} variant="contained">Practitioner</Button>
                </Link>
                <Link to="/patient_login">
                <Button  style={{width:'85vh'}} variant="outlined">Patient</Button>
                </Link>
              </Container>
              </>
 
            </Card>
        </div>
	)
}

export default Login_As
