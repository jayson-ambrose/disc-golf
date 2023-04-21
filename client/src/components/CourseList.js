import React, { useEffect, useState } from 'react'

function CourseList() {

    const [courses, setCourses] = useState([])
    const [filter, setFilter] = useState("")

    function handleChange (e) {
        setFilter(e.target.value)
    }

    useEffect(() => {
        fetch('/courses')
        .then(resp => resp.json())
        .then(data => setCourses(data))
    }, [])

    const displayCourses = courses.filter((course => course.state.toLowerCase().includes(filter.toLowerCase()))).map(course => {
        const {city, state, id, name} = course

        return(
            <tr key={id}>
                <td>{id}</td>
                <td>{name}</td>
                <td>{city}</td>
                <td>{state}</td>
            </tr>
        )
    })
    
  return (
    <div>
      <p>Use the course ID to start a new round.</p>
      <div>
        <label>Filter by state: </label>
        <input placeholder="State" value={filter} onChange={handleChange}/> 
      </div>
      <table className='coursetable'>
        <tbody>
            <tr>
                <th>Course ID</th>
                <th>Name</th>
                <th>City</th>
                <th>State</th>
            </tr>
            {displayCourses}
        </tbody>
      </table>
      
    </div>

  );
}

export default CourseList;
