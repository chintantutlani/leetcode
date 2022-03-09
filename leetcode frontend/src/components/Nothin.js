import React from 'react'
import {Navbar, Container,Nav,NavDropdown } from 'react-bootstrap';


function Nothin() {
  return (
    <div>

<>
<Navbar bg="light" expand="lg" variant="light">
    <Container>
    
 

 
    <Navbar.Brand href="#home" >
      <img src ="https://cdn-images-1.medium.com/fit/t/1600/480/1*nFgF8PFbUBqaRVijajytog.jpeg"
      width="255"
      height="55"/></Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav">
      <Nav className="">
        <Nav.Link href="#home">Problems</Nav.Link>
        <Nav.Link href="https://leetcode.com/discuss/interview-question?currentPage=1&orderBy=hot&query=">Discuss</Nav.Link>
        <NavDropdown title="Interview" id="basic-nav-dropdown">
          <NavDropdown.Item href="https://leetcode.com/assessment/">Assesment</NavDropdown.Item>
          <NavDropdown.Item href="https://interview.leetcode.com/interview/login/">Online Interview</NavDropdown.Item>
        </NavDropdown>
      </Nav>
    </Navbar.Collapse>
  </Container>

  </Navbar>
  
</>

    </div>

  )
}

export default Nothin
