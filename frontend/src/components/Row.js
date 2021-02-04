const Row = ({ data, customRow0, customRow1, customRow2, customRow3, customRow4, customList, isTravel, isContactTrace }) => {
    let secondColData = () => {
    //     customList: 'citizen_contact',
    // customRow0: 'email',
    // customRow1: 'contact_no',
    // customRow2: 'gender',
    // customRow3: 'age',
    // customRow4: 'address'
        if (customList[0] === 'citizen_contact' || customList[0] === 'travel_history') {
            return data[customRow4]
        } else if (customList[0] === 'citizen_medical') {
            return `${data[customList[0]][0][customRow4]} °C` 
        }
    }

    let thirdColData = () => {
        if (customList[0] === 'citizen_contact') {
            return data[customRow2]
        } else if (customList[0] === 'citizen_medical') {
            return `${data[customList[0]][0][customRow2]} Heart Rate` 
        }
    }

    let fourthColData = () => {
        if (customList[0] === 'citizen_contact') {
            return data['citizen_medical'][0][customRow3]  
        } else if (customList[0] === 'citizen_medical') {
            return `${data[customList[0]][0][customRow3]} kg` 
        } else if (customList[0] === 'travel_history') {
            return `${data['age']}`
        }
    }

    return (
        <tr>
            <td className="px-6 py-4 whitespace-nowrap">
                <div className="flex items-center">
                <div className="flex-shrink-0 h-10 w-10">
                    <img className="h-10 w-10 rounded-full" src={data['citizen_profile'][0]['profile_pic']} alt="" />
                </div>
                <div className="ml-4">
                    <div className="text-sm font-medium text-gray-900">
                    {data.first_name}
                    </div>
                    <div className="text-sm text-gray-500">
                    {data['citizen_contact'].map((contact) => (
                        contact[customRow0]
                    ))}
                    {/* {data.citizen_contact[0].email} */}
                    </div>
                </div>
                </div>
            </td>
            {/* °C */}
            <td className="px-6 py-4 whitespace-nowrap">
                <div className="text-sm text-gray-900">
                        {secondColData()}
                 </div>
                <div className="text-sm text-gray-500"> 
                {customList[0] === 'citizen_contact' || customList[0] === 'citizen_medical' ? data[customList[0]].map((temp) => (
                        temp[customRow1] 
                )) : data['citizen_contact'][0]['contact_no'] }
                </div>   
            </td>
            <td className="px-6 py-4 whitespace-nowrap">
                <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                {customList[0] === 'citizen_contact' || customList[0] === 'citizen_medical' ? thirdColData() : data['cc_status'][0]['status']}
                </span>
            </td>
            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {fourthColData()}
            </td>
            <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <a href="/" className="text-indigo-600 hover:text-indigo-900 mr-2">Edit</a>
                <a href="/" className="text-red-600 hover:text-red-900">Delete</a>
            </td>
        </tr>
    )
}

Row.defaultProps = {
    customList: ['citizen_contact'],
    customRow0: 'email',
    customRow1: 'contact_no',
    customRow2: 'gender',
    customRow3: 'last_checkup',
    customRow4: 'address'
}

export default Row;