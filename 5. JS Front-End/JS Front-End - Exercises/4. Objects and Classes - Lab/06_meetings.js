function meetingsManagement(meetingsArr) {
    meetings = {}

    for (let meetingPerson of meetingsArr) {
        let meetingPersonArr = meetingPerson.split(' ')
        let day = meetingPersonArr[0]
        
        if (Object.keys(meetings).includes(day)) {
            console.log(`Conflict on ${day}!`)
        } else {
            meetings[day] = meetingPersonArr[1]
            console.log(`Scheduled for ${day}`)
        }
    }

    for (let currDay of Object.keys(meetings)) {
        console.log(`${currDay} -> ${meetings[currDay]}`)
    }
}
