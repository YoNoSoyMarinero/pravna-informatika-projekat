import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";

export const GenerateDecisionPage = () => {
  const [court_name, setCourtName] = useState("");
  const [date, setDate] = useState("");
  const [title, setTitle] = useState("");
  const [judgment_body, setJudgmentBody] = useState("");
  const [conclusion, setConclusion] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = {
      court_name,
      date,
      title,
      judgment_body,
      conclusion,
    };
    let headers = new Headers();
    headers.append("Content-type", "application/json");
    fetch("http://localhost:5000/create_judgment", {
      method: "POST",
      headers: headers,
      body: JSON.stringify(formData),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        alert(`You sucessfully added judgment with title ${title}`);
        setCourtName("");
        setDate("");
        setTitle("");
        setJudgmentBody("");
        setConclusion("");
      })
      .catch((e) => {
        console.log("Error: ", e);
      });
  };

  return (
    <Form
      onSubmit={handleSubmit}
      style={{
        color: "black",
        backgroundColor: "#008547",
        padding: "20px",
        width: "50%",
        marginLeft: "25%",
      }}
    >
      <Form.Group controlId="courtName">
        <Form.Label style={{ color: "white" }}>Court Name</Form.Label>
        <Form.Control
          type="text"
          value={court_name}
          onChange={(e) => setCourtName(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="date">
        <Form.Label style={{ color: "white" }}>Date</Form.Label>
        <Form.Control
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="title">
        <Form.Label style={{ color: "white" }}>Title</Form.Label>
        <Form.Control
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="judgmentBody">
        <Form.Label style={{ color: "white" }}>Judgment Body</Form.Label>
        <Form.Control
          as="textarea"
          rows={5}
          style={{
            borderColor: "white",
            color: "black",
            backgroundColor: "white",
          }}
          value={judgment_body}
          onChange={(e) => setJudgmentBody(e.target.value)}
        />
      </Form.Group>
      <Form.Group controlId="conclusion">
        <Form.Label style={{ color: "white" }}>Conclusion</Form.Label>
        <Form.Control
          as="textarea"
          rows={5}
          style={{
            borderColor: "white",
            color: "black",
            backgroundColor: "white",
          }}
          value={conclusion}
          onChange={(e) => setConclusion(e.target.value)}
        />
      </Form.Group>
      <Button
        variant="success"
        type="submit"
        style={{ marginTop: "20px", marginLeft: "50%" }}
      >
        Submit
      </Button>
    </Form>
  );
};

export default GenerateDecisionPage;
