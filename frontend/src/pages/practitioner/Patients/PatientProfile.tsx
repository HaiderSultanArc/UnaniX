import {useState} from 'react' 
 
 const PatientProfile=(props:{ id:number})=> {
	  

	return ( 
    <div className="PatientProfile">
        <div className='container emp-profile'>
            <form method=''>
                <div className="row">
                   <div className='col-md-4'>
                        <img src="../../assets/profile.png" alt='profile'/>
                    </div>
                    <div className='col-md-6'>
                        <div className='profile-head'>
                            <h5>Subhan Rashid</h5>
                            <h6>Asthma</h6></div>
                    </div>
                </div>
            </form>
        </div>
   
</div>
	)
}

export default PatientProfile
