import React, {useEffect, useState} from 'react'

function ScoreSheet({courseId, roundId, playerList, scorecards, getScorecards}) {


  const [course, setCourse] = useState({})

    useEffect(() => {
      fetch(`/courses/${courseId}`)
      .then(resp => resp.json())
      .then(data => setCourse(data))
    }, [])


    // useEffect(() => {
    //   fetch(`/rounds/${roundId}/scorecards`)
    //   .then(resp => resp.json())
    //   .then(data => console.log(data))
    // }, [])

    console.log(course.holes)
    
    let scorecardDisplay = null
    let holeDisplay = null

    let totalPar = 0
    let totalDist = 0

    if (course.holes != undefined){
      holeDisplay = course.holes.map((hole) => {
        totalPar = hole.par + totalPar
        totalDist = hole.distance + totalDist
        return (
          <tr key={hole.hole_number}>
            <td>{hole.hole_number}</td>
            <td>{hole.par}</td>
            <td>{hole.distance}</td>
          </tr>
        )
      })}


    if (scorecards.length > 0) {
      scorecardDisplay = scorecards.map((scorecard) => {
 
        const player = playerList.find((player) => player.id === scorecard.player_id)

        return(
          <table className='scoretable'>
              <tbody>
                  <tr>
                    <th>{player?.name}</th>
                  </tr>
                  <tr>
                    <td>{scorecard.score_1 === -1 ? "-" : scorecard.score_1}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_2}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_3}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_4}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_5}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_6}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_7}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_8}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_9}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_10}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_11}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_12}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_13}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_14}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_15}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_16}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_17}</td>
                  </tr>
                  <tr>
                    <td>{scorecard.score_18}</td>
                  </tr>
              </tbody>
          </table>      
        )
      })
    }

    return (
      <div className='scoretable'>
          <table>
              <tbody>
                  <tr>
                      <th>HL</th>
                      <th>PAR</th>
                      <th>DIST</th>
                  </tr>
                  {holeDisplay}
                  <tr>
                      <th>TOT</th>
                      <th>{totalPar}</th>
                      <th>{totalDist}</th>
                  </tr>
              </tbody>
          </table>
          {scorecardDisplay}          
      </div>
    );
  }

export default ScoreSheet;
