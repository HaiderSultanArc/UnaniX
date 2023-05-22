import {Avatar, Button} from "@mui/material"
import Appointments from "./Appointments"
import Income from "./Income"
import Infographics from "./Infographics"


function GraphsPage() {
    const sx = {
        // avatar: {
        //     padding: '0.5vw',
        // },
        
        btn: {
            width: '10vw',
        }
    }
    
    return (
        <div className="graphs_page">
            {/* <div className="new_patents">
                <p className="heading">New Patients</p>
                <div className="view_patients">
                    <div className="patients_avatars">
                        <Avatar className="avatar_1" alt="Remy Sharp">R</Avatar>
                        <Avatar className="avatar_2" alt="Terry Woods">T</Avatar>
                        <Avatar className="avatar_3" alt="Betty Wunder">B</Avatar>
                        <Avatar className="avatar_4" alt="Lily Potter">L</Avatar>
                        <Avatar className="avatar_more" alt="More">7+</Avatar>
                    </div>
                    <Button variant="text" sx={sx.btn}>View Patients</Button>
                </div>
            </div>
            <div className="patient_requests">
                <p className="heading">Patients Requests</p>
                <div className="patient_details">
                    <p className="name">Charles Mic</p>
                    <p className="issue">High BP</p>
                    <p className="level">Urgent</p>
                    <p className="status">Not Entertained Yet</p>
                </div>
            </div> */}
            <div className="income">
                <Income />
            </div>
            <Appointments />
            <div className="calendar"></div>
            <Infographics />
        </div>
    )
}

export default GraphsPage