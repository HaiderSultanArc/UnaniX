import {
    CategoryScale, Chart as ChartJS, Legend, LinearScale, LineElement, PointElement, Title,
    Tooltip
} from 'chart.js';
import {Line} from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

export const options = {
    responsive: true,
    plugins: {
        legend: {
            position: 'bottom' as const,
        },
        title: {
            display: true,
            text: 'Activity',
        },
    },
};

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

export const data = {
    labels,
    datasets: [
        {
            label: 'Appiontments',
            data: labels.map(() => Math.floor(Math.random() * 80)),
            borderColor: 'rgb(255, 99, 68)',
            backgroundColor: 'rgb(255, 99, 68)',
        },
        {
            label: 'Chat Patients',
            data: labels.map(() => Math.floor(Math.random() * 80)),
            borderColor: 'rgb(64, 203, 226)',
            backgroundColor: 'rgb(64, 202, 226)',
        },
    ],
};

export default function Appointments() {
    return (
        <div className="appointment" style={{height: "18vw", width: "35vw"}}>
            <Line data={data} options={options} />
        </div>
    )
}
