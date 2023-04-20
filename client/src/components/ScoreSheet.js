import React from 'react'

//score sheet display

function ScoreSheet() {
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
            </tbody>
        </table>
    </div>
  );
}

export default ScoreSheet;
