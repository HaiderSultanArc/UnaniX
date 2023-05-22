import {useState} from 'react'
import './_Profile_Info.scss'
import dayjs, { Dayjs } from 'dayjs';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import * as React from 'react';

import TextField from '@mui/material/TextField';
 
import Box from '@mui/material/Box'; 
import {Container, Form, Row , Col} from 'react-bootstrap';
import Button from '@mui/material/Button';

import MenuItem from '@mui/material/MenuItem'; 

// import {auth} from '../../firebas'

const Profile_Info_Practitioner= ( ) => {
  
const doctors = [
  {
    value: 'Sara Naeem',
    label: 'Sara Naeem',
  },
  {
    value: 'Shah Ali Baba',
    label: 'Shah Ali Baba',
  },
  {
    value: 'Bahadur Shah',
    label: 'Bahadur Shah',
  },
  {
    value: 'Jahmal Khan',
    label: 'Jahmal Khan',
  },
];
  
    const [doctor, setDoctor] = React.useState(String);
    const [date, setDate] = React.useState<Dayjs | null>(dayjs('2014-08-18T21:11:54'));
    const [name, setName] = React.useState(String);
    const [phone, setPhone] = React.useState(String);


    const handleDoctorValue = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
      setDoctor(event.target.value);
    };

    const handleNameValue = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
      setName(event.target.value);
    }
    
    const handlePhoneValue = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
      setPhone(event.target.value);
    }

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();

      const res = await fetch('http://localhost:8000/add_patient_appointment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          
        }),
      });
    }
     
    return ( 
        <div className= "appointments">
            <Card sx={{ maxWidth: 2000}} style={{backgroundColor: " #171F34"}}>
            <>
              <Container>
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                  Your Profile
                </Typography>  
              </Container>

              <Container>
                <Box 
                  component="form"
                  sx={{
                    '& .MuiTextField-root': { m: 1 },
                  }}
                  noValidate
                  autoComplete="off"
                  onSubmit={(e) => handleSubmit(e)}
                  >
                    <div>
                      <TextField
                        sx={{
                          width: '80vw',
                       }}
                        required
                        id="outlined-required"
                        label="Name"
                        defaultValue="Sarah Bosman"
                        value={name}
                        onChange={(e) => handleNameValue(e)}
                      />
                      <TextField
                          sx={{
                          width: '80vw',
                        }}
                        required
                        id="outlined-required"
                        label="Phone Number"
                        defaultValue="03318969807"
                      />
                      <TextField
                          sx={{
                            width: '80vw',
                             }}
                          id="outlined-select-currency"
                          select
                          label="Choose your Doctor"
                          value={doctor}
                          onChange={handleDoctorValue}
                          helperText="Please select your Doctor"
                        >
                          {doctors.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                              {option.label}
                            </MenuItem>
                          ))}
                      </TextField>
                     </div>       
                     
                  <Button variant='contained' > Submit 
                  </Button>
                </Box>
              </Container>
              </>
 
            </Card>
        </div>
	)
}

export default Profile_Info_Practitioner
