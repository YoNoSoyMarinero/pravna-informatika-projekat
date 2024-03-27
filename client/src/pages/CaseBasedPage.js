import React from 'react';
import { Container, Form, Button } from 'react-bootstrap';

export const CaseBasedPage = () => {
  return (
    <Container style={{ height: '100vh', color: 'white' }} className="d-flex justify-content-center align-items-center">
      <Form style={{ width: '400px', padding: '20px', border: '2px solid lightgrey', borderRadius: '10px', boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.1)' }}>
        <Form.Group controlId="convicted">
          <Form.Check type="checkbox" label="Convicted" />
        </Form.Group>

        <Form.Group controlId="selfUsage">
          <Form.Check type="checkbox" label="Self Usage" />
        </Form.Group>

        <Form.Group controlId="marginalizedGroup">
          <Form.Check type="checkbox" label="Marginalized Group" />
        </Form.Group>

        <Form.Group controlId="providingLogistics">
          <Form.Check type="checkbox" label="Providing Logistics" />
        </Form.Group>

        <Form.Group controlId="married">
          <Form.Check type="checkbox" label="Married" />
        </Form.Group>

        <Form.Group controlId="smuggling">
          <Form.Check type="checkbox" label="Smuggling" />
        </Form.Group>

        <Form.Group controlId="organizedGroup">
          <Form.Check type="checkbox" label="Organized Group" />
        </Form.Group>

        <Form.Group controlId="trafficking">
          <Form.Check type="checkbox" label="Trafficking" />
        </Form.Group>

        <Form.Group controlId="snitched">
          <Form.Check type="checkbox" label="Snitched" />
        </Form.Group>

        <Form.Group controlId="admitted">
          <Form.Check type="checkbox" label="Admitted" />
        </Form.Group>

        <Form.Group controlId="greatAmountWithoutTrafficking">
          <Form.Check type="checkbox" label="Great Amount Without Trafficking" />
        </Form.Group>

        <Form.Group controlId="smallAmountWithoutTrafficking">
          <Form.Check type="checkbox" label="Small Amount Without Trafficking" />
        </Form.Group>

        <Form.Group controlId="allowedUsage">
          <Form.Check type="checkbox" label="Allowed Usage" />
        </Form.Group>

        <Form.Group controlId="hasChildren">
          <Form.Check type="checkbox" label="Has Children" />
        </Form.Group>

        <Form.Group controlId="amountOfCocaine">
          <Form.Label>Amount of Cocaine</Form.Label>
          <Form.Control type="number" placeholder="Enter amount of Cocaine" />
        </Form.Group>

        <Form.Group controlId="amountOfHeroine">
          <Form.Label>Amount of Heroine</Form.Label>
          <Form.Control type="number" placeholder="Enter amount of Heroine" />
        </Form.Group>

        <Form.Group controlId="amountOfMarijuana">
          <Form.Label>Amount of Marijuana</Form.Label>
          <Form.Control type="number" placeholder="Enter amount of Marijuana" />
        </Form.Group>

        <div style={{paddingTop: "10px", display: 'flex', justifyContent: 'center'}}>
          <Button variant="success" type="submit" style={{background: 'black'}}>
            Submit
          </Button>
        </div>
      </Form>
    </Container>
  );
};

export default CaseBasedPage;
