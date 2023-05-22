import {
    BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title,
    Tooltip
} from 'chart.js';
import {Bar} from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

const options = {
    responsive: true,
    plugins: {
        legend: {
            position: 'bottom' as const,
        },
        title: {
            display: true,
            text: 'Infographics',
        },
    },
};

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

const data = {
    labels,
    datasets: [
        {
            label: 'Male',
            data: labels.map(() => Math.floor(Math.random() * 400)),
            borderColor: 'rgb(255, 99, 68)',
            backgroundColor: 'rgb(255, 99, 68)'
        },
        {
            label: 'Female',
            data: labels.map(() => Math.floor(Math.random() * 400)),
            borderColor: 'rgb(64, 203, 226)',
            backgroundColor: 'rgb(64, 202, 226)',
        },
    ],
};

export default function Infographics() {
    return (
        <div className="infographics" style={{height: "18vw", width: "35vw"}}>
            <Bar options={options} data={data} />
        </div>
    )
}
