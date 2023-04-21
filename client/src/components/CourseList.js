import React, { useEffect, useState } from 'react'

function CourseList() {

    const [courses, setCourses] = useState([])

    fetch('/courses')
    .then(resp => resp.json())
    .then(data => console.log(data))

  return (
    <div>
      Hello World!
    </div>

  );
}

export default CourseList;
