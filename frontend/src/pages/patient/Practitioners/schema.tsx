export interface PractitionersList {
    practitioners: Practitioner[];
}

export interface Practitioner {
    id: number;
    username: string;
    email: string;
    phone: string;
    profilepicture: string;
}