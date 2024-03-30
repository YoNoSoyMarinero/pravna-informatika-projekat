import React, { useState, useEffect } from "react";
import { Card } from "react-bootstrap";

export const JudgmentPage = () => {
  const [judgmentNames, setJudgmentNames] = useState([]);

  useEffect(() => {
    const fetchJudgmentNames = async () => {
      try {
        const response = await fetch("http://localhost:5000/judgment_name");
        if (!response.ok) {
          throw new Error("Failed to fetch judgment names");
        }
        const data = await response.json();
        setJudgmentNames(data.legal_document_names);
      } catch (error) {
        console.error("Error fetching judgment names:", error);
      }
    };

    fetchJudgmentNames();
  }, []);

  return (
    <div>
      {judgmentNames.map((name, index) => (
        <div key={index}>
          <Card
            bg="dark"
            text="white"
            style={{
              marginTop: "20px",
              width: "50%",
              marginLeft: "25%",
              textAlign: "center",
            }}
          >
            <Card.Body>
              <Card.Title>{name}</Card.Title>
              <Card.Link
                href={`http://localhost:5000/judgment?legal_document_name=${name}`}
                style={{ color: "green", textDecoration: "none" }}
                target="_blank"
                rel="noopener noreferrer"
              >
                View Judgment
              </Card.Link>
            </Card.Body>
          </Card>
        </div>
      ))}
    </div>
  );
};

export default JudgmentPage;
