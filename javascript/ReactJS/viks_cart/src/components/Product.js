import React from "react";

export default function Product(props) {
    
  return (
    <div className="row mt-3 ">
      <div className="col-5">
        <h2>
          {props.product.name}
          <span style={{backgroundColor:"#EBD671",padding:"1.1%",fontSize:"70%"}} className="badge">₹{props.product.price}</span>
        </h2>
      </div>
      <div className="col-3">
        <div
          className="btn-group"
          role="group"
          aria-label="Basic mixed styles example"
        >
          <button type="button" id="redbtn" className="btn text-light " onClick={()=>{props.decrementQuantity(props.index);}}>
            -
          </button>
          <button type="button" style={{backgroundColor:"#B0EFEB"}} className="btn ">
            {props.product.quantity}
          </button>
          <button type="button"  style={{backgroundColor:"#5FD068"}} className="btn text-light" onClick={()=>{props.incrementQuantity(props.index);}}>
            +
          </button>
        </div>
      </div>
      <div className="col-1 me-5  text-center border border-5" style={{backgroundColor:"#B0EFEB"}} >
        {props.product.quantity * props.product.price}
      </div>
      <button id="redbtn" className="ms-4 col-2 btn text-light" onClick={()=>{props.removeItem(props.index)}} >
        Remove
      </button>
    </div>
    
  );
}
