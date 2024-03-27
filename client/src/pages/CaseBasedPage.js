import { React, useState } from "react";
import { Container, Form, Button } from "react-bootstrap";

export const CaseBasedPage = () => {
  const [formData, setFormData] = useState({
    convicted: false,
    self_usage: false,
    marginalized_group: false,
    providing_logistics: false,
    married: false,
    smuggling: false,
    organized_group: false,
    trafficking: false,
    snitched: false,
    admited: false,
    great_amount_without_trafficking: false,
    small_amount_without_trafficking: false,
    allowed_usage: false,
    has_children: false,
    amount_of_cocaine: 0,
    amount_of_heroine: 0,
    amount_of_marijuana: 0,
  });
  const [showPenalties, setShowPenalties] = useState("none");
  const [penalties, setPeanlties] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    setShowPenalties("block");
    let headers = new Headers();
    headers.append("Content-type", "application/json");
    console.log(formData);
    fetch("http://localhost:5000/case_based_reasoning", {
      method: "POST",
      headers: headers,
      body: JSON.stringify(formData),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setPeanlties(data.similar_cases);
      })
      .catch((e) => {
        console.log("Error: ", e);
      });
  };

  const handleChange = (event) => {
    const { id, checked, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [id]: id.includes("amount_of") ? parseInt(value) : checked,
    }));
  };

  return (
    <div style={{ position: "relative" }}>
      <div
        style={{
          position: "center",
          top: "40%",
          left: "25%",
          width: "50%",
          height: "30%",
          textAlign: "center",
          zIndex: "999",
          backgroundColor: "rgba(255, 255, 255, 1)",
          padding: "20px",
          borderRadius: "1%",
          display: showPenalties,
        }}
        onClick={() => setShowPenalties("none")}
      >
        <h4>Најсличнији случајеви Вашем</h4>
        <h6>Кликни те овде да изађете</h6>
        {penalties.map((penalty) => (
          <p style={{ color: "green" }}>
            ИД случаја: {penalty.case_id} Сличност: {penalty.case_similarity}{" "}
            Казна: {penalty.case_punishments} месеци
          </p>
        ))}
      </div>
      <Container
        style={{ height: "100vh", color: "white" }}
        className="d-flex justify-content-center align-items-center"
      >
        <Form
          onSubmit={handleSubmit}
          style={{
            width: "1000px",
            padding: "20px",
            border: "2px solid lightgrey",
            borderRadius: "10px",
            boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.1)",
          }}
        >
          <h1>Oдлучивање на основу праксе</h1>
          <Form.Group controlId="convicted">
            <Form.Check
              type="checkbox"
              label="Осуђиван"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="self_usage">
            <Form.Check
              type="checkbox"
              label="Властита употреба"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="marginalized_group">
            <Form.Check
              type="checkbox"
              label="Наводио или продавао угроженим групама"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="providing_logistics">
            <Form.Check
              type="checkbox"
              label="Омогућио ставаљње у промет или производњу логистиком"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="married">
            <Form.Check
              type="checkbox"
              label="Ожењен"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="smuggling">
            <Form.Check
              type="checkbox"
              label="Шверцовао"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="organized_group">
            <Form.Check
              type="checkbox"
              label="Огранизована група"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="trafficking">
            <Form.Check
              type="checkbox"
              label="Стављање у промет"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="snitched">
            <Form.Check
              type="checkbox"
              label="Дао информације о групи"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="admited">
            <Form.Check
              type="checkbox"
              label="Признао кривично дело"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="great_amount_without_trafficking">
            <Form.Check
              type="checkbox"
              label="Поседовао малу количину без стављања у промет"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="small_amount_without_trafficking">
            <Form.Check
              type="checkbox"
              label="Поседовао велику количину без стављања у промет"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="allowed_usage">
            <Form.Check
              type="checkbox"
              label="Омогућио уживање"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="has_children">
            <Form.Check
              type="checkbox"
              label="Окривљени има децу"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="amount_of_cocaine">
            <Form.Label>Koличина кокаина у грамима</Form.Label>
            <Form.Control
              type="number"
              placeholder="Koличина кокаина у грамима"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="amount_of_heroine">
            <Form.Label>Количина хероина у грамима</Form.Label>
            <Form.Control
              type="number"
              placeholder="Количина хероина у грамима"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="amount_of_marijuana">
            <Form.Label>Количина марихуане у грамима</Form.Label>
            <Form.Control
              type="number"
              placeholder="Количина марихуане у грамима"
              onChange={handleChange}
            />
          </Form.Group>
          <div
            style={{
              paddingTop: "10px",
              display: "flex",
              justifyContent: "center",
            }}
          >
            <Button variant="light" type="submit">
              Submit
            </Button>
          </div>
        </Form>
      </Container>
    </div>
  );
};

export default CaseBasedPage;
