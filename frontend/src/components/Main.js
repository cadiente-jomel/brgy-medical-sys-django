import Table from './Table';
import { useState, useEffect } from 'react'

const Main = ({ view }) => {
    const [records, setRecs] = useState([])

    useEffect(() => {
        fetch('http://localhost:8000/api/citizen-personal/')
        .then(results => {
            return results.json()
        }).then(response => {
             setRecs(response.results)
        })
    }, [])


    if (view === 'dashboard' || view === 'citizen-rec') {
       return (
                <div>
                    <Table recs={records}/>
                </div>
            )
    } else if (view === 'check-up') {
        return (
                <div>
                    <Table recs={records} col2='Temperature' col3='Pulse Rate' col4='Weight' customRow1='blood_pressure' customRow2='pulse_rate' customRow3='weight' customRow4='temperature' customList={['citizen_medical']}/>
                </div>
            )
    } else if (view === 'pandemic') {
        return (
                <div>
                    <Table recs={records} col2='Address' col3='PUI' col4='Age' customRow3='age' customList={['travel_history', 'contact_trace']} />
                </div>
            )
    }
}


export default Main;