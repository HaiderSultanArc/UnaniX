
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import BarSide from './Barside.tsx';

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

export default function Treatments() {
  return (
   <div>
     <Box sx={{ display: 'flex' }}>
     <BarSide />
     <h1>CDSS</h1>
    <Box
        component="main"
        sx={{ flexGrow: 1, bgcolor: 'background.default', p: 3 }}
      >
        <h1>CDSS</h1>
     <h1 style={{ paddingTop: '30px', paddingBottom: '30px' }}>Treatments</h1>
    <Card sx={{ minWidth: 275 , border: '4px solid #FDC990'}}>
      <CardContent>
        
        <Typography variant="h4" component="div">
          Qarshi
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          Remedy
        </Typography>
        <Typography variant="body2">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam dolore, voluptates quidem dignissimos, adipisci repudiandae officiis ab exercitationem labore facere quas corrupti quasi facilis dolor pariatur odit earum cum soluta.
          <br />
          {'"a benevolent smile"'}
        </Typography>
      </CardContent>
     
    </Card>
    </Box>
    </Box>
    </ div>
  );
}
