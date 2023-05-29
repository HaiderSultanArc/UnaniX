export interface AppointmentsList {
    appointments: Appointment[];
}

interface Appointment {
    id: number;
    name: string;
    phone: number;
    date: string;
    time: string;
    report: string;
    status: string;
}