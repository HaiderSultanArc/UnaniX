import {useState} from 'react'
import './_Symtoms.scss'
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
import {Routes, Route, useNavigate, Link} from 'react-router-dom'
import MenuItem from '@mui/material/MenuItem';
import DiagnosisPage from './Diagnosis';
import {DiseasesData} from './Diagnosisdata';

// import {auth} from '../../firebas'

const AddSymptoms= ( ) => {
  
const Symptoms = [
  {
    value: 'Nausea',
    label: 'Nausea',
  },
  {
    value: 'Rash',
    label: 'Rash',
  },
  {
    value: 'Body Ache',
    label: 'Body Ache',
  },
  {
    value: 'Pain behind eye',
    label: 'Pain behind eye',
  },
];
  
    const [symptom1, setSymptom1] = React.useState(String);
    const [symptom2, setSymptom2] = React.useState(String);
    const [symptom3, setSymptom3] = React.useState(String);
    const [symptom4, setSymptom4] = React.useState(String);
    const [symptom5, setSymptom5] = React.useState(String);
    const [symptom6, setSymptom6] = React.useState(String);

    const navigate= useNavigate();

    const handleSymptom1Value = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setSymptom1(event.target.value);
      };
      const handleSymptom2Value = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setSymptom2(event.target.value);
      };
      const handleSymptom3Value = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setSymptom3(event.target.value);
      };
      const handleSymptom4Value = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setSymptom4(event.target.value);
      };
      const handleSymptom5Value = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setSymptom5(event.target.value);
      };
      const handleSymptom6Value = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setSymptom6(event.target.value);
      };
      
      const navigatetoDiagnosis=()=>{
        navigate('/Diagnosis');
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
        <div className= "symptoms">
            <Card sx={{ maxWidth: 2000}} style={{backgroundColor: " #171F34"}}>
            <>
              <Container>
                <Typography gutterBottom variant="h4" component="div" style={{color: "#E0E1E4"}} >
                  Add Patient's Symptoms
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
                          id="outlined-select-currency"
                          select
                          label="Choose your Doctor"
                          value={symptom1}
                          onChange={handleSymptom1Value}
                          helperText="Please select your Doctor"
                        >
                          {Symptoms.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                              {option.label}
                            </MenuItem>
                          ))}
                      </TextField>
                      <TextField
                          sx={{
                            width: '80vw',
                             }}
                          id="outlined-select-currency"
                          select
                          label="Choose your Doctor"
                          value={symptom2}
                          onChange={handleSymptom2Value}
                          helperText="Please select your Doctor"
                        >
                          {Symptoms.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                              {option.label}
                            </MenuItem>
                          ))}
                      </TextField>
                      <TextField
                          sx={{
                            width: '80vw',
                             }}
                          id="outlined-select-currency"
                          select
                          label="Choose your Doctor"
                          value={symptom3}
                          onChange={handleSymptom3Value}
                          helperText="Please select your Doctor"
                        >
                          {Symptoms.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                              {option.label}
                            </MenuItem>
                          ))}
                      </TextField>
                      <TextField
                          sx={{
                            width: '80vw',
                             }}
                          id="outlined-select-currency"
                          select
                          label="Choose your Doctor"
                          value={symptom4}
                          onChange={handleSymptom4Value}
                          helperText="Please select your Doctor"
                        >
                          {Symptoms.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                              {option.label}
                            </MenuItem>
                          ))}
                      </TextField>
                      <TextField
                          sx={{
                            width: '80vw',
                             }}
                          id="outlined-select-currency"
                          select
                          label="Choose your Doctor"
                          value={symptom5}
                          onChange={handleSymptom5Value}
                          helperText="Please select your Doctor"
                        >
                          {Symptoms.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                              {option.label}
                            </MenuItem>
                          ))}
                      </TextField>
                      <TextField
                          sx={{
                            width: '80vw',
                             }}
                          id="outlined-select-currency"
                          select
                          label="Choose your Doctor"
                          value={symptom6}
                          onChange={handleSymptom6Value}
                          helperText="Please select your Doctor"
                        >
                          {Symptoms.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                              {option.label}
                            </MenuItem>
                          ))}
                      </TextField>

                  </div>
                  <Link to="/Diagnosis">
                    <Button variant="contained" onClick={navigatetoDiagnosis}>Get Diagnosis</Button>
                  </Link>
                </Box>
              </Container>

              </>
 
            </Card>
        </div>
	)
}

export default AddSymptoms
