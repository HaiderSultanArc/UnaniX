import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Checkbox from '@mui/material/Checkbox';
import CssBaseline from '@mui/material/CssBaseline';
import FormControlLabel from '@mui/material/FormControlLabel';
import TextField from '@mui/material/TextField';
import * as React from 'react';
// import Link from '@mui/material/Link';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import {Card} from '@mui/material';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import {Link} from 'react-router-dom';



const theme = createTheme({
	palette: {
		mode: 'dark',
	},
});


export default function LoginAsPractitioner() {
	const [email, setEmail] = React.useState('');
	const [password, setPassword] = React.useState('');

	const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault();
		
		signInWithEmailAndPassword(auth, email, password).then(
			async (userCredential) => {
				userCredential.user.getIdToken().then(
					async (IDToken) => {
						const res = await fetch('http://localhost:8000/practitioner_login',
							{
								method: 'POST',
								headers: {
									'Content-Type': 'application/json',
								},
								body: JSON.stringify(
									{
										IDToken: IDToken,
									}
								),
							}
						);
		
						const data = res.json();
						console.log(data);
						
						if (data !== null) {
							window.open('/', '_self');
						}
					}
				)
			}
		).catch(
			(error) => {
				window.alert(error.message);
			}
		)
	};

	return (
		<ThemeProvider theme={theme}>
			<Container component="main" maxWidth="xs">
				<CssBaseline />
					<Card className='container' variant="outlined" style={{ backgroundColor: "#171F34",
						boxShadow:"10", border:"0.4px solid black", padding: "2vw", margin: "2vw"
					}}>
						<Box sx={{
							marginTop: 8,
							display: 'flex',
							flexDirection: 'column',
							alignItems: 'center',

						}}>
						<Avatar sx={{ m: 1, bgcolor: 'primary.main' }}>
							<LockOutlinedIcon />
						</Avatar>
						<Typography component="h1" variant="h5">
							Sign in
						</Typography>
						<Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
							<TextField
								margin="normal"
								required
								fullWidth
								id="email"
								label="Email Address"
								name="email"
								autoComplete="email"
								autoFocus
								value={email}
								onChange={(e) => setEmail(e.target.value)}
							/>
							<TextField
								margin="normal"
								required
								fullWidth
								name="password"
								label="Password"
								type="password"
								id="password"
								autoComplete="current-password"
								value={password}
								onChange={(e) => setPassword(e.target.value)}
							/>
							<FormControlLabel
								control={<Checkbox value="remember" color="primary" />}
								label="Remember me"
							/>
							<Button
								type="submit"
								fullWidth
								variant="contained"
								sx={{ 
									mt: 3, 
									mb: 2 
								}}
							>
								Sign In
							</Button>
							<Grid container >
								<Grid item sx={{alignItems:"center"}}>
									<Link href="#" variant="body2">
										Forgot password?
									</Link>
								</Grid>
							<Grid item>
								<Link to='/register' variant="body2">
									{"Don't have an account? Sign Up"}
								</Link>
							</Grid>
							</Grid>
						</Box>
					</Box>
				</Card>
			</Container>
		</ThemeProvider>
	);
}
