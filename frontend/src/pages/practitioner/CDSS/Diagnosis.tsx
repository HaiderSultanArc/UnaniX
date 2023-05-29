import {useState} from 'react'
import './_Diagnosis.scss'
import { DiseasesList } from './DiagnosisLst'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import Button from '@mui/material/Button';
import CardActions from '@mui/material/CardActions';
import {Link, useNavigate} from 'react-router-dom';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import {Row, Col, Container} from 'react-bootstrap';


const DiagnosisPage: React.FC<DiseasesList> = ( {diseases}: DiseasesList) => {
    const navigate= useNavigate();

    const navigatetoTreatments=()=>{
        navigate('/Treatments');
    }

    return ( 
        <div className= "diseases">
            <Card sx={{ maxWidth: 1600}}  >
                <CssBaseline />
                <Container >
                    
                    <Box sx={{ width: '127vh' }}>  
                     
                    <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                        Predicted Diseases
                    
                    </Typography>
                    </Box>
                    
                    
                    
                    
                </Container>
                <CssBaseline />
                <Container  >
                  
                   
                    <div className="diseases-cards">
                        <div className="disease-card">
                            {diseases.map(
                                (disease) => (   
                                   <Box sx={{ height: 350 }}>
                                        <Link to="/Treatments">
                                            <Card sx={{ maxWidth: 2000}} style={{backgroundColor: "#131524"}}>
                                                <CardActionArea>
                                                    <div className='RedTask'></div>
                                                    <div>
                                                        <CardContent >
                                                            <Typography gutterBottom variant="h4" component="div" style={{color: "white"}} >
                                                                <Box sx={{width:'20vh', height: '10vh' }} > 
                                                                {disease.name}
                                                                </Box>
                                                                <Typography variant="h6" component="div" style={{color: "grey"}}  >
                                                                    Probability:    {disease.probability}
                                                                </Typography>
                                                            </Typography>
                                                            <Typography variant="h5" component="div" style={{color: "grey"}} >
                                                                {disease.description}
                                                            </Typography>
                                                            
                                                            
                                                        </CardContent>
                                                    </div>
                                                    
                                                </CardActionArea>
                                            </Card>
                                        </Link>
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

export default DiagnosisPage
