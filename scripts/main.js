import React from 'react';
import ReactDOM from 'react-dom';
import JobExperiences from './job-experience';

const myJobData = [
    {
        'title': "Job1",
        'description': "Job1-des",
        'startDate': "1-20",
        'endDate': "2-1"
    },
    {
        'title': "Job2",
        'description': "Job2-des",
        'startDate': "201-1",
        'endDate': "201-1"
    },
    {
        'title': "Job3",
        'description': "Job3",
        'startDate': "24",
        'endDate': "6"
    }
];

ReactDOM.render(
    <JobExperiences jobData={myJobData}/>,
    document.getElementById('job-experience'));
