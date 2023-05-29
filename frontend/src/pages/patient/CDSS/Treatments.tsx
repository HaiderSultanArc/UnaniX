import {useState} from 'react'
import './_Diagnosis.scss'
import { TreatmentsList } from './TreatmentsLst'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import Button from '@mui/material/Button';
import CardActions from '@mui/material/CardActions';

import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import {Row, Col, Container} from 'react-bootstrap';


const TreatmentsPage: React.FC<TreatmentsList> = ( {treatments}: TreatmentsList) => {
	return ( 
        <div className= "diseases">
            <Card sx={{ maxWidth: 1600}}  >
                <CssBaseline />
                <Container >
                    
                    <Box sx={{ width: '127vh' }}>  
                     
                    <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                        Treatments
                    
                    </Typography>
                    </Box>
                    
                    
                    
                </Container>
                <CssBaseline />
                <Container  >
                  
                   
                    <div className="diseases-cards">
                        <div className="disease-card">
                            {treatments.map(
                                (treatment) => (   
                                   <Box sx={{ height: 320 }}>
                                        <Card sx={{ maxWidth: 2000}} style={{backgroundColor: "#131524"}}>
                                            <CardActionArea>
                                                <div className='greenTask'></div>
                                                <div>
                                                    <CardContent >
                                                        <Typography gutterBottom variant="h4" component="div" style={{color: "white"}} >
                                                            <Box sx={{width:'20vh', height: '10vh' }} > 
                                                            {treatment.name}
                                                            </Box>
                                                            
                                                        </Typography>
                                                        <Typography variant="h5" component="div" style={{color: "grey"}} >
                                                          Instructions:  {treatment.description}
                                                        </Typography>
                                                        
                                                        
                                                    </CardContent>
                                                </div>
                                                
                                            </CardActionArea>
                                        </Card>
                                    </Box>    
                                )
                            )}       
                        </div>   
                    </div>
                
                </Container>
            </Card>
        </div>
	)
}

export default TreatmentsPage
