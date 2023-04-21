import React, {useEffect, useState} from 'react'

function ScoreSheet({courseId, roundId}) {

  const [course, setCourse] = useState({})

    useEffect(() => {
      fetch(`/courses/${courseId}`)
      .then(resp => resp.json())
      .then(data => setCourse(data))
    }, [])

    useEffect(() => {
      fetch(`/rounds/${roundId}/scorecards`)
      .then(resp => resp.json())
      .then(data => console.log(data))
    }, [])

    console.log(course.holes)

    let holeDisplay = null

    if (course.holes != undefined){
      holeDisplay = course.holes.map((hole) => {
        return (
          <tr key={hole.hole_number}>
            <td>{hole.hole_number}</td>
            <td>{hole.par}</td>
            <td>{hole.distance}</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        )
      })}

    return (
      <div className='component'>
          <table>
              <tbody>
                  <tr>
                      <th>HL</th>
                      <th>PAR</th>
                      <th>DIST</th>
                      <th>P1</th>
                      <th>P2</th>
                      <th>P3</th>
                      <th>P4</th>
                  </tr>
                  {holeDisplay}
              </tbody>
          </table>
      </div>
    );
  }

export default ScoreSheet;
