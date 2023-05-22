import {ArcElement, Chart as ChartJS, Legend, Title, Tooltip} from 'chart.js';
import {Doughnut} from 'react-chartjs-2';

ChartJS.register(
    ArcElement, 
    Title,
    Tooltip,
    Legend
);

const options = {
    responsive: true,
    cutout: 70,
    plugins: {
        legend: {
            position: 'bottom' as const,
        },
        title: {
            display: true,
            text: 'Income',
        },
    },
};

const data = {
    labels: ['Income', 'Expenses'],
    datasets: [
        {
            label: 'Income',
            data: [45000, 19000],
            backgroundColor: [
                'rgb(64, 203, 226)',
                'rgb(255, 99, 68)'
            ],
            borderColor: [
                'rgb(64, 203, 226)',
                'rgb(255, 99, 68)'
            ],
            borderWidth: 1,
        },
    ],
};

export default function Income() {
    return (
        <div style={{height: "18vw", width: "18vw"}}>
            <Doughnut data={data} options={options} />
        </div>
    )
}
