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
                    <Table col2='Temperature' col3='Blood Pressure' col4='Medical History'/>
                </div>
            )
    } else if (view === 'pandemic') {
        return (
                <div>
                    <Table col2='Address' col3='PUI' col4='Age' />
                </div>
            )
    }
}


export default Main;