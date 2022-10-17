import React from 'react'

export default function Footer(props) {
  return (
    
    <div style={{margin:"auto"}} className='row'>
        <div style={{height:"300px"}}>
        </div>
        <div className='row fixed-bottom mb-3'>
        <button id="redbtn" className='ms-5 me-4 btn text-light col-2' onClick={()=>{props.resetQuantity()}} >Reset</button>
        <div style={{backgroundColor:"#B0EFEB"}} className='border border-5 me-5 ms-5 col-6 text-center '>
            {props.totalAmount}
        </div>
        <button id ="bluebtn" className='btn text-light col-2 me-5 ms-4' >Pay now</button>
        </div>
    </div>
  )
}
