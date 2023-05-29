export interface PatientList {
    patients: Patient[];
}

export interface Patient {
    id: number;
    username: string;
    email: string;
    phone: string;
    profilepicture: string;
}