import React from 'react';

class AddItem extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            productName:"",
            productPrice:0,
        };
    }
    render() { 
        return (
            <form
            className="row mb-5"
            onSubmit={(e) => {
              e.preventDefault();
              this.props.addItem(this.state.productName,Number(this.state.productPrice));
            }}
          >
        <div className="ms-5 mb-3 col-4">
          <label htmlFor="inputName" className="form-label">Name</label>
          <input type="name" className="form-control" id="inputName" aria-describedby="name" 
          name='productName' onChange={(e)=> this.setState({productName:e.currentTarget.value})} value={this.state.productName}/>
        </div>
        <div className="mb-3 col-3">
          <label htmlFor="inputPrice" className="form-label">Price</label>
          <input type="number" className="form-control" id="price"
          name='productPrice' onChange={(e)=> this.setState({productPrice:Number(e.currentTarget.value)})} value={this.state.productPrice}/>
        </div>
        
        <button type="submit" style ={{margin:"auto"}} id="bluebtn" className="btn text-light col-2 " >Add to Cart</button> 
      </form>);
    }
}
 
export default AddItem;
// we used this.props here since we used class and not a function