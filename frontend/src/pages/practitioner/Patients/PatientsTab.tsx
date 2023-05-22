import {useState} from 'react'
import { PatientList } from './schema'
import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import {Container} from 'react-bootstrap';
 

const PatientsTab=( {patients}: PatientList ) => {
   
	return (  
        <div className="PatientsTab">
        <Card sx={{ maxWidth: 2000}} style={{backgroundColor: " #171F34"}}>
            <Container>  
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                    Your Patients
                </Typography> 
            </Container> 
            <Container> 
            <div className="patients">
                {
                    patients.map(
                        (patient) => (
                            <div>
                                <Card sx={{ maxWidth: 1500 }}  style={{backgroundColor: "#131524"}}>
                                    <CardActionArea>
                                        <CardMedia
                                        component="img"
                                        height="140"
                                        image={patient.profilepicture}
                                        alt="green iguana"
                                        />
                                        <CardContent>
                                            <Typography gutterBottom variant="h5" component="div">
                                                {patient.username}
                                            </Typography>
                                            <Typography variant="body2" color="text.secondary">
                                                <div className="info-group">
                                                    <img src="/src/assets/phone-icon.png" />
                                                    <p>{patient.phone}</p>
                                                </div>
                                                <div className="info-group">
                                                    <img src="/src/assets/mail-icon.png" />
                                                    <p>{patient.email}</p>
                                                </div>  
                                            </Typography>
                                        </CardContent>
                                    </CardActionArea>
                                </Card>
                                
                                 
                            </div>
                        )
                    )
                }
            </div>
            </Container> 
            </Card>
        </div>
	)
     
}

export default PatientsTab
