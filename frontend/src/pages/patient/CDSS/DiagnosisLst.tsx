export interface DiseasesList {
    diseases: Disease[];
}

interface Disease {
    id: number;
    name: string;
    description: string;
    probability: number;
    
}