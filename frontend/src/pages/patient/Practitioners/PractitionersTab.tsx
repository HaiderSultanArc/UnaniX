import {CardActionArea} from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import {Container} from 'react-bootstrap';
import {PractitionersList} from './schema';
 

const PatientsTab=( {practitioners}: PractitionersList ) => {
   
	return (  
        <div className="PatientsTab">
        <Card sx={{ maxWidth: 2000}} style={{backgroundColor: " #171F34"}}>
            <Container>  
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                    Your Patients
                </Typography> 
            </Container> 
            <Container> 
            <div className="practitioners">
                {
                    practitioners.map(
                        (practitioner) => (
                            <div>
                                <Card sx={{ maxWidth: 1500 }}  style={{backgroundColor: "#131524"}}>
                                    <CardActionArea>
                                        <CardMedia
                                        component="img"
                                        height="140"
                                        image={practitioner.profilepicture}
                                        alt="green iguana"
                                        />
                                        <CardContent>
                                            <Typography gutterBottom variant="h5" component="div">
                                                {practitioner.username}
                                            </Typography>
                                            <Typography variant="body2" color="text.secondary">
                                                <div className="info-group">
                                                    <img src="/src/assets/phone-icon.png" />
                                                    <p>{practitioner.phone}</p>
                                                </div>
                                                <div className="info-group">
                                                    <img src="/src/assets/mail-icon.png" />
                                                    <p>{practitioner.email}</p>
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
