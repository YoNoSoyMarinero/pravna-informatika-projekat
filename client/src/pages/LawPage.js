import React from "react";
import { Card } from "react-bootstrap";

export const LawPage = () => {
  return (
    <div
      className="container"
      style={{
        marginTop: "20px",
      }}
    >
      <div className="row">
        <div>
          <Card
            bg="dark"
            text="white"
            style={{
              marginTop: "20px",
            }}
          >
            <Card.Body>
              <Card.Title>
                Кривични законик Црне Горе - Чланови који се односе на дрогу
              </Card.Title>
              <Card.Link
                href="http://localhost:5000/law?legal_document_name=krivicni"
                style={{ color: "green", textDecoration: "none" }}
                target="_blank"
              >
                Кривични законик
              </Card.Link>
            </Card.Body>
          </Card>
        </div>
        <div>
          <Card
            bg="dark"
            text="white"
            style={{
              marginTop: "20px",
            }}
          >
            <Card.Body>
              <Card.Title>Закон о спречавању злоупотреби дроге</Card.Title>
              <Card.Link
                href="http://localhost:5000/law?legal_document_name=zakon_o_sprecavanju_zloupotrebi_droga"
                style={{ color: "green", textDecoration: "none" }}
                target="_blank"
              >
                Закон о спречавању злоупотреби дроге
              </Card.Link>
            </Card.Body>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default LawPage;
