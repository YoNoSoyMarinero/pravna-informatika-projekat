import { React, useState } from "react";
import { Container, Form, Button } from "react-bootstrap";

export const RuleBasedPage = () => {
  const [formData, setFormData] = useState({
    drug_posession: false,
    allowing_usage: false,
    marginalized_group: false,
    providing_logistics: false,
    drug_trafficking: false,
    smuggling: false,
    organized_group: false,
    article_52_violation: false,
    estimated_drug_price: 0
  });
  const [showPenalties, setShowPenalties] = useState("none");
  const [penalties, setPeanlties] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    setShowPenalties("block");
    let headers = new Headers();
    headers.append("Content-type", "application/json");
    console.log(formData);
    fetch("http://localhost:5000/rule_based_reasoning", {
      method: "POST",
      headers: headers,
      body: JSON.stringify(formData),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        const penalties = Array.from({ length: data.max_pen.length }, (_, i) => ({
            max_pen: data.max_pen[i],
            min_pen: data.min_pen[i],
            offenses: data.offenses[i]
           }));
        console.log(penalties)
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
          width: "100%",
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
        <h4>Kривична дела и казне за изнето чињенично стање</h4>
        <h6>Кликни те овде да изађете</h6>
        {penalties.map((penalty) => (
          <p style={{ color: "green" }}>
            Кривично дело: {penalty.offenses} Минмална казна: {penalty.min_pen}{" "} месеци
            Максимална казна: {penalty.max_pen} месеци
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
          <Form.Group controlId="drug_posession">
            <Form.Check
              type="checkbox"
              label="Осуђиван"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="allowing_usage">
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
          <Form.Group controlId="drug_trafficking">
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
          <Form.Group controlId="article_52_violation">
            <Form.Check
              type="checkbox"
              label="Прекршен неки од прописа из закона о злоупотреби дрога члан 52"
              onChange={handleChange}
            />
          </Form.Group>
          <Form.Group controlId="estimated_drug_price">
            <Form.Label>Процењена цена дроге у еврима</Form.Label>
            <Form.Control
              type="number"
              placeholder="Процењена цена дроге у еврима"
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

export default RuleBasedPage;
