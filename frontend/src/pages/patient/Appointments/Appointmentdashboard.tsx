import {CardActionArea} from '@mui/material';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CssBaseline from '@mui/material/CssBaseline';
import Typography from '@mui/material/Typography';
import {Container} from 'react-bootstrap';
import {Link, useNavigate} from 'react-router-dom';
import {AppointmentsList} from './appointments';
import './_RecentAppointments.scss';


const Appointmentdashboard: React.FC<AppointmentsList> = ( {appointments}: AppointmentsList) => {
    const navigate= useNavigate();

    const navigatetoMakeAppointment=()=>{
        navigate('/MakeAppointment');
      }
    return ( 
        <div className= "appointments">
            <Card sx={{ maxWidth: 1600}}  >
                <CssBaseline />
                <Container >
                    
                    <Box sx={{ width: '127vh' }}>  
                     
                    <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                        Appointments
                    
                    </Typography>
                    </Box>
                    <Link to="/MakeAppointment">
                        <Button
                            variant="contained"
                            onClick={navigatetoMakeAppointment}
                            >
                            Make Appointment
                        </Button>
                    </Link>
                    
                    
                </Container>
                <CssBaseline />
                <Container  >
                    <Box sx={{ bgcolor: '#131524',width:'150vh', height: '100vh' }} >
                
                   
                        <div className="appointments-cards">
                            <div className="appointment-card">
                                {appointments.map(
                                    (appointment) => (   
                                        <Card sx={{ maxWidth: 2000}} style={{backgroundColor: "#131524"}}>
                                            <CardActionArea>
                                                <div className='blueTask'></div>
                                                <div>
                                                    <CardContent>
                                                        <Typography gutterBottom variant="h4" component="div" style={{color: "white"}} >
                                                            {appointment.name}
                                                        </Typography>
                                                        <Typography variant="h5" component="div" style={{color: "grey"}} >
                                                            {appointment.date}
                                                        </Typography>
                                                        <Typography variant="h6" component="div" style={{color: "grey"}}  >
                                                            {appointment.time}
                                                        </Typography>
                                                        <Typography variant="body2" color="text.secondary">
                                                            <div className="Report">
                                                                <a href=''>Reports || Patients History</a>
                                                            </div>
                                                        </Typography>
                                                        <Typography>
                                                            <div className="Status">
                                                                Status: {appointment.status}
                                                            </div>
                                                        </Typography>
                                                    </CardContent>
                                                </div>
                                                
                                                 
                                            </CardActionArea>
                                            
                                        </Card>
                                    )
                                )}       
                            </div>   
                        </div>
                    </Box>
                </Container>
            </Card>
        </div>
	)
}

export default Appointmentdashboard
