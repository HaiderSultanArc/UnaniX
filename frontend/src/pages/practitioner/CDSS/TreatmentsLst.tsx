export interface TreatmentsList {
    treatments: Treatment[];
}

interface Treatment {
    id: number;
    name: string;
    description: string;
    probability: number;
    
}