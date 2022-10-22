import React from 'react';
import Product from './Product.js';
export default function ProductList(props) {
  
    return ( 
        // use conditional rendering
        props.productList.length>0 ?
        props.productList.map((product,i)=>{
        return <Product product= {product} key={i} decrementQuantity ={props.decrementQuantity} incrementQuantity ={props.incrementQuantity} 
        index={i} removeItem = {props.removeItem} />
        }) 
        : <h1 className='text-center'> Cart is empty</h1>
    )
}
