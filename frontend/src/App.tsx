import {PaletteMode} from '@mui/material';
import {createTheme, ThemeProvider} from '@mui/material/styles';
import React, {useEffect} from 'react';
import {Route, Routes} from 'react-router';
import './App.css';
import LoginAsPatient from './Components/Login/LoginAsPatient';
import LoginAsPractitioner from './Components/Login/LoginAsPractitioner';
import SignUpAsPatient from './Components/SignUp/SignUpAsPatient';
import SignUpAsPractitioner from './Components/SignUp/SignUpPractitioner';
import {auth} from './firebase/firebase';
import Home from './pages/patient/Home/Home';
import {getTheme} from './Theme';


const ColorModeContext = React.createContext({ toggleColorMode: () => {} });

function App() {
	const [mode, setMode] = React.useState<PaletteMode>('dark');
	
	const colorMode = React.useMemo(
		() => (
			{
				// The dark mode switch would invoke this method
				toggleColorMode: () => {
					setMode((prevMode: PaletteMode) =>
						prevMode === 'light' ? 'dark' : 'light',
					);
				},
			}
		),[],
	);
	
	
	useEffect(
        () => {
            const unsubscribe = auth.onAuthStateChanged(
                (authUser) => {
                    if (authUser) {
                        setCurrentUser(authUser);
                    }
                    else {
                        setCurrentUser(null);
                    }
                }
            )
            
            return () => {
                unsubscribe();
            }
        }, []
    )
  
	// Update the theme only if the mode changes
	const theme = React.useMemo(() => createTheme(getTheme(mode)), [mode]);
	
	return (
		<ColorModeContext.Provider value={colorMode}>
			<ThemeProvider theme={theme}>
				{/* <Home /> */}
				{
					
					<Routes>
						<Route path="/" element={<Home />} />
						<Route path="/sign_up_as_patient" element={<SignUpAsPatient />} />
						<Route path="/sign_up_as_practitioner" element={<SignUpAsPractitioner />} />
						<Route path="/login_as_patient" element={<LoginAsPatient />} />
						<Route path="/login_as_practitioner" element={<LoginAsPractitioner />} />
					</Routes>
					// currentUser ? (
					// 	<Routes>
					// 		<Route path={'/'} element={<Navigate to="/home" />} />
					// 		<Route path={'/login'} element={<Navigate to="/home" />} />
					// 		<Route path={'/practitioner_login'} element={<Navigate to="/home" />} />
					// 		<Route path={'/patient_login'} element={<Navigate to="/home" />} />
					// 		<Route path='/home' element={<Home />} />
					// 	</Routes>
					// ) : (
					// 	<Routes>
					// 		<Route path="*" element={<Navigate to="/" />} />
					// 		<Route path="/" element={<LandingPage />} />
					// 		<Route path='/login' element={<Login_As />} />
					// 		<Route path='/practitioner_login' element={<LoginAsPractitioner />} />
					// 		<Route path='/patient_login' element={<LoginAsPatient user={currentUser} setUser={setCurrentUser} />} />
					// 	</Routes>
					// )
				}
				{/* <MakeAppointment /> */}
			</ThemeProvider>
		</ColorModeContext.Provider>
	);
}
  

export default App;
