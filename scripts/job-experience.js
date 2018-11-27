import React from 'react';

class JobExperiences extends React.Component {
    render() {
        return (
            <section>
                {
                    this.props.jobData.map((job, idx) => {
                        return (
                            <Job job={job} key={idx}/>
                        )
                    })
                }
            </section>
        )
    }
}

class Job extends React.Component {
    render() {
        let job = this.props.job;
        return (
            <div>
                <h2>{job.title}</h2>
                <p>{job.description}</p>
                <p>{job.startDate} - {job.endDate}</p>
            </div>
        )
    }
}

export default JobExperiences;