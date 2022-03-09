import React, { useState, useEffect } from 'react'
import { Table } from 'react-bootstrap'
import axios from 'axios'

function Showproblem() {
    const [data, setData] = useState([])

    useEffect(() => {
        allproblem()
        
    },[])
    
    function allproblem() {
        axios({
  
            method: "GET",
            url: "http://127.0.0.1:8000/problem/"
            

        }).then((res) => {
            setData(res.data.problem)
            console.log("=========>",res.data.problem)
    })
}
 return (
     <div>
         <Table striped bordered hover>
             <thead>
                 <tr>
                     
                     <th>problem name</th>
                     <th>probelm</th>
                     <th>created at</th>
                     <th>updated at</th>
                 </tr>
             </thead>
             {
                 data.map(item=>(
                     <tbody>
                         <tr>
                             
                             <td>{item.prblm_name}</td>
                             <td>{item.problem}</td>
                             <td>{item.Created_at}</td>
                             <td>{item.updated_at}</td>

                         </tr>
                     </tbody>

                 ))
                         
             }
             
         </Table>

     </div>
     
    
 )
} 
export default Showproblem