import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
import DashboardIcon from "@mui/icons-material/Dashboard";
import EventAvailableIcon from "@mui/icons-material/EventAvailable";
import LogoutIcon from "@mui/icons-material/Logout";
import MailIcon from "@mui/icons-material/Mail";
import MenuIcon from "@mui/icons-material/Menu";
import PersonIcon from "@mui/icons-material/Person";
import MuiAppBar, {AppBarProps as MuiAppBarProps} from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Divider from "@mui/material/Divider";
import MuiDrawer from "@mui/material/Drawer";
import IconButton from "@mui/material/IconButton";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import {CSSObject, styled, Theme, useTheme} from "@mui/material/styles";
import Toolbar from "@mui/material/Toolbar";
import * as React from "react";
import {Link, Route, Routes} from "react-router-dom";
import NavBar from "../../../Components/Navbar/Navbar";
import {auth} from "../../../firebase/firebase";
import Appointmentdashboard from "../Appointments/Appointmentdashboard";
import {appointmentsData} from "../Appointments/appointmentsData";
import MakeAppointment from "../Appointments/MakeAppointment";
import DiagnosisPage from "../CDSS/Diagnosis";
import {DiseasesData} from "../CDSS/Diagnosisdata";
import AddSymptoms from "../CDSS/SymtomsForm";
import TreatmentsPage from "../CDSS/Treatments";
import {TreatmentsData} from "../CDSS/TreatmentsData";
import Dashboard from "../Dashboard/Dashboard";
import PractitionersTab from "../Practitioners/PractitionersTab";
import {practitonersData} from "../Practitioners/practitonersdata";
import Profile from "../Profile/Profile";
import user from "/src/assets/user.png";

const drawerWidth = 300;

const openedMixin = (theme: Theme): CSSObject => ({
  width: drawerWidth,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: "hidden",
});

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: "hidden",
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up("sm")]: {
    width: `calc(${theme.spacing(8)} + 1px)`,
  },
});

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(["width", "margin"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  width: drawerWidth,
  flexShrink: 0,
  whiteSpace: "nowrap",
  boxSizing: "border-box",
  ...(open && {
    ...openedMixin(theme),
    "& .MuiDrawer-paper": openedMixin(theme),
  }),
  ...(!open && {
    ...closedMixin(theme),
    "& .MuiDrawer-paper": closedMixin(theme),
  }),
}));

export default function Home() {
  const theme = useTheme();
  const [open, setOpen] = React.useState(false);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <Box sx={{ display: "flex", width: "100vw" }}>
      <CssBaseline />
      <AppBar position="fixed" open={open}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            sx={{
              marginRight: 5,
              ...(open && { display: "none" }),
            }}
          >
            <MenuIcon />
          </IconButton>
          <NavBar />
        </Toolbar>
      </AppBar>
      <Drawer variant="permanent" open={open}>
        <DrawerHeader>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === "rtl" ? (
              <ChevronRightIcon />
            ) : (
              <ChevronLeftIcon />
            )}
          </IconButton>
        </DrawerHeader>
        <Divider />

        <List>
            <ListItem key="Dashboard" disablePadding sx={{ display: "block" }}>
              <Link to="/dashboard">
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    <DashboardIcon />
                  </ListItemIcon>
                  <ListItemText primary="Dashboard" sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </Link>
            </ListItem>
        </List>

        <List>
            <ListItem key={"Appointments"} disablePadding sx={{ display: "block" }}>
              <Link to={"/appointments"}>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    <EventAvailableIcon />
                  </ListItemIcon>
                  <ListItemText primary={"Appointments"} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </Link>
            </ListItem>
        </List>
        <List>
            <ListItem key={"Patients"} disablePadding sx={{ display: "block" }}>
              <Link to={"/patients"}>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    <PersonIcon />
                  </ListItemIcon>
                  <ListItemText primary={"Patients"} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </Link>
            </ListItem>
        </List>

        <List>
            <ListItem key={"Messages"} disablePadding sx={{ display: "block" }}>
              <Link to={"/messages"}>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    <MailIcon />
                  </ListItemIcon>
                  <ListItemText primary={"Messages"} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </Link>
            </ListItem>
        </List>
        <List>
            <ListItem key={"DiseaseDiagnosis"} disablePadding sx={{ display: "block" }}>
              <Link to={"/symptoms"}>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    <MailIcon />
                  </ListItemIcon>
                  <ListItemText primary={"DiseaseDiagnosis"} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </Link>
            </ListItem>
        </List>
        <Divider />
        <List>
            <ListItem key={"Logout"} disablePadding sx={{ display: "block" }}>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                  onClick={auth.signOut()}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    {<LogoutIcon />}
                  </ListItemIcon>
                  <ListItemText primary={"Logout"} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
            </ListItem>
        </List>
      </Drawer>
      <Box component="main" sx={{ width: "100vw", height: "70vh" }}>
        <DrawerHeader />
        <Routes>
          <Route path="/profile" element={<Profile image={user} username={"UNANI"} role={"Practitioner"} age={"42"} description={"This is a Practitioner"}/>} />
          <Route path="/make_appointments" />
          <Route path="/dashboard" element={<Dashboard />}/>
          <Route path="/appointments" element={<Appointmentdashboard appointments={appointmentsData} />} />
          <Route path="/patients" element={<PractitionersTab practitioners={practitonersData}/> }/>
          <Route path="/messages"/>
          <Route path="/symptoms"element={<AddSymptoms/>}/>
          
          <Route path="/Diagnosis" element={<DiagnosisPage diseases={DiseasesData}/>}/>
          
          <Route path="/MakeAppointment" element={<MakeAppointment/>}/>
          <Route path="/Treatments" element={<TreatmentsPage treatments={TreatmentsData}/>}/>
        </Routes>
      </Box>
    </Box>
  );
}
