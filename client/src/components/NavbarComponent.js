import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import React from "react";

export const NavbarComponent = () => {
  return(
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="/home">Сервис за судије</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="rule-based">Oдлучивање на оснуву правила</Nav.Link>
            <Nav.Link href="case-based">Одлучивање на основу праксе</Nav.Link>
            <Nav.Link href="judgments">Пресуде</Nav.Link>
            <Nav.Link href="laws">Закони</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  )
}

export default NavbarComponent;

