import React, { useState } from "react";
import ReactDOM from 'react-dom/client'
// import Sidebar from '../Sidebar/Sidebar'
// import "./_Navbar.scss";
import SearchIcon from '@mui/icons-material/Search';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import NotificationsOutlinedIcon from '@mui/icons-material/NotificationsOutlined';
import ContentCut from '@mui/icons-material/ContentCut'
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import ChatBubbleOutlineOutlinedIcon from '@mui/icons-material/ChatBubbleOutlineOutlined';
import img from '/src/assets/img.jpg';
import edit from '/src/assets/edit.png';
import settings from '/src/assets/settings.png';
import user from '/src/assets/user.png';
import logout from '/src/assets/log-out.png';
import { Divider, FormControl, IconButton, Input, InputAdornment, InputLabel, Link, ListItemIcon, ListItemText, Menu, MenuItem, MenuList, Paper, Typography } from "@mui/material";
import { Cloud, ContentCopy, ContentPaste } from "@mui/icons-material";
import ProfileMenu from "./ProfileMenu";
import NotificationMenu from "./NotificationMenu";
import MessagesMenu from "./MessagesMenu";



function NavBar(){
    var showdate = new Date();
    var time=showdate.getHours()+':'+showdate.getMinutes();
    const [open, setOpen] = useState(false);
    
    const sx = {
        icon: {
            color: "white"
        },

        input: {
            color: "white",
            width: "40vw"
        },

        dropDown: { 
            color: "white",
            width: 320, 
            maxWidth: '100%', 
        }
    }

    return (
        <div className="Navbar">
            <FormControl variant="standard">
                <Input 
                    sx={sx.input}
                    placeholder="Search..."
                    startAdornment={
                        <InputAdornment position="start">
                            <SearchIcon sx={sx.icon} />
                        </InputAdornment>
                    }
                />
            </FormControl>

            <div className="Right" >
                <NotificationMenu />
                <MessagesMenu />
                <ProfileMenu />
            </div>
        </div>
    )
}

export default NavBar;