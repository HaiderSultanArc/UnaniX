import {useState} from 'react'
import './_SignUp_As.scss'

import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import * as React from 'react';

import {Container} from 'react-bootstrap';
import Button from '@mui/material/Button';


// import {auth} from '../../firebas'

const SignUp_As= ( ) => {
  
  
    const [User, setUser] = React.useState(String);
     

   
    const handlePractitionerValue = () => {
        setUser("Practitioner");
      };
      const handlePatientValue = () => {
        setUser("Patient");
      };
      
     
    return ( 
        <div className= "card">
            <Card sx={{ maxWidth: 2000}} style={{backgroundColor: " #171F34"}}>
            <>
              <Container>
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                  SignUp As
                </Typography>  
              </Container>

              <Container>
                <Button style={{width:'85vh'}} variant="contained" value={User} onClick={()=>handlePractitionerValue()}>Practitioner</Button>
                <Button  style={{width:'85vh'}} variant="outlined"value={User} onClick={()=>handlePatientValue()}>Patient</Button>
              </Container>
              </>
 
            </Card>
        </div>
	)
}

export default SignUp_As
