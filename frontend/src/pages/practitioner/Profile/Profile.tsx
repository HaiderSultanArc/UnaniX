import React from 'react'
import ReactDOM from 'react-dom/client'
import logo from '/src/assets/logo.png';
import user from '/src/assets/user.png';
import Grid from '@mui/material/Grid';
import Avatar from '@mui/material/Avatar';
import { Dialog } from 'primereact/dialog';
import { InputText } from 'primereact/inputtext';
import { ButtonBase, Card, Divider, Paper } from '@mui/material';
import {grey} from '@mui/material/colors';
import { alignProperty } from '@mui/material/styles/cssUtils';
import { AlignHorizontalCenter } from '@mui/icons-material';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';


const Profile = (props: { image: string | undefined; username: string | number | boolean | React.ReactElement<any, string | React.JSXElementConstructor<any>> | React.ReactFragment | React.ReactPortal | null | undefined; role: string | number | boolean | React.ReactElement<any, string | React.JSXElementConstructor<any>> | React.ReactFragment | React.ReactPortal | null | undefined; age: string | number | boolean | React.ReactElement<any, string | React.JSXElementConstructor<any>> | React.ReactFragment | React.ReactPortal | null | undefined; description: string | number | boolean | React.ReactElement<any, string | React.JSXElementConstructor<any>> | React.ReactFragment | React.ReactPortal | null | undefined; }) => {
    return (
        <Paper
        sx={{
          p: 2,
          margin: 'auto',
          maxWidth: 600,
          flexGrow: 1,
        //   backgroundColor: (theme) =>
        //     theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
        }}
      >
        <Grid container spacing={20}>
          <Grid item>
            <ButtonBase sx={{ width: 128, height: 128 }}>
              {/* <Img alt="complex" src="/static/images/grid/complex.jpg" /> */}
              <Avatar className="avatar" alt="Remy Sharp" src={props.image} sx={{ width: 120, height: 120, alignItems:'center'}} />

            </ButtonBase>
          </Grid>
          <Grid item xs={12} sm container>
            <Grid item xs container direction="column" spacing={2}>
              <Grid item xs>
                <Typography gutterBottom variant="subtitle1" component="div">
                <h2>{props.username}</h2>
                </Typography>
                <Typography variant="body2" color="text.secondary">
                <h4>{props.role}</h4>
                </Typography>
                <Typography variant="body2" color="text.secondary">
                <h4>{props.age}</h4>
                </Typography>
                <Typography variant="body2" gutterBottom>
                {props.description}
              </Typography>

              </Grid>
              <Grid item>
              <Button size="small" variant='outlined'  onClick={() => {alert('clicked');}} >Change Profile Photo</Button>
              <Button size="small" variant='outlined'  onClick={() => {alert('clicked');}} >Edit</Button>
              </Grid>
            </Grid>
            <Grid item>
            </Grid>
          </Grid>
        </Grid>
      </Paper>
  
    )
}

const mapStatetoProps=(state: { user: { username: any; role: any; password: any; confirmPassword: any; msg: any; }; })=>{
    return{
        username:state.user.username,
       role:state.user.role,
       password:state.user.password,
       confirmPassword:state.user.confirmPassword,
       msg:state.user.msg
    }
   }
export default Profile;