import Box from '@mui/material/Box';
import Button from '@mui/material/Button/Button.js';
import Toolbar from '@mui/material/Toolbar';
import React from 'react';
import BarSide from './Barside.tsx';


import {useNavigate} from 'react-router-dom';

export default function CDSS() {
    const navigate=useNavigate();
  return (
    <Box sx={{ display: 'flex' }}>
     <BarSide />
    <h1>CDSS</h1>
    <Box
        component="main"
        sx={{ flexGrow: 1, bgcolor: 'background.default', p: 3 }}
      >
        <Toolbar />
        {/* Here addd link of CDSS*/}
        <gradio-app space="haidersultanarc/unani-medicine-ai-engine" theme_mode="light"></gradio-app>
{/*Here above*/}
        <Button variant="contained" style={{backgroundColor: '#FC7209'}} onClick={()=>{navigate("/Treatments")}} >
        Treatments
        </Button>
      </Box>
     
     
    </Box>
  )
}
