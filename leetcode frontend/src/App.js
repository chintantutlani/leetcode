import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Showproblem from './components/ShowProblem';
import Nothin from './components/Nothin';
// import Log from './components/Log';
// import { Routes, Route } from 'react-router-dom';
// import { Button } from 'react-bootstrap';


function App() {
  return (
    <>
    <div>
      <Nothin/>
      <Showproblem/>
      

    </div>
    </>
    // // <Showprobelm>
    //   {/* <nav className='nav-bar  bg-secondary p-2 nav w-100' style={{position:"fixed",top:"0",left:"0",zIndex:"9"}}>
    //     <Link className='sm-btn text-info warning-btn p-0 px-2' to="/"><Button variant="warning" size="sm">Home</Button></Link>
    //     <Link className='btn text-info warning-btn p-0 px-2' to="add"><Button variant="warning" size="sm">Add Product</Button></Link>
    //   </nav> */},
    //   {/* <Routes>
    //     <Route exact path="/" element={<ShowProducts />} />
    //   </Routes> */},
    // <Showproblem/>
    
  );
}

export default App;