import {useState} from 'react'
import './_RecentAppointments.scss'
import { AppointmentsList } from './appointments'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import Button from '@mui/material/Button';
import CardActions from '@mui/material/CardActions';


const RecentAppointments: React.FC<AppointmentsList> = ( {appointments}: AppointmentsList) => {
	return ( 
        <div className= "appointments">
            <Card sx={{ maxWidth: 450}} style={{backgroundColor: " #171F34"}}>
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                    Upcoming Appointments
                </Typography>  

                <div className="appointments-cards">
                    <div className="appointment-card">
                        {appointments.map(
                            (appointment) => (   
                                <Card sx={{ maxWidth: 450 }} style={{backgroundColor: "#131524"}}>
                                    <CardActionArea>
                                            <div className='RedTask'></div>
                                            <div>
                                                <CardContent >
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
                                                </CardContent>
                                            </div>
                                    </CardActionArea>
                                </Card>
                            )
                        )}       
                    </div>   
                </div>
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                    Recent Appointments
                </Typography>  
                <div className="appointments-cards">
                    <div className="appointment-card">
                    {appointments.map(
                        (appointment) => (   
                            <Card sx={{ maxWidth: 450 }} style={{backgroundColor: "#131524"}}>
                                <CardActionArea>
                                        <div className='greyTask'></div>
                                        <div><CardContent >
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
                                            </CardContent>
                                        </div>
                                </CardActionArea>
                            </Card>
                        )
                    )}
                </div>
            </div>
            </Card>
        </div>
	)
}

export default RecentAppointments
