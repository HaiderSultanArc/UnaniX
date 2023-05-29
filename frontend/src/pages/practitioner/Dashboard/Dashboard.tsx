import React from 'react'
import RecentAppointments from '../Appointments/RecentAppointments'
import { appointmentsData } from '../Appointments/appointmentsData'
import GraphsPage from '../GraphsPage/GraphsPage'

function Dashboard() {
  return (
    <div className='dashboard'>
        <GraphsPage />
        <RecentAppointments appointments={appointmentsData} />
    </div>
  )
}

export default Dashboard