# Legal Informatics

This application serves as a platform for retrieving legal documents, including judgments and laws, through a user-friendly interface. It leverages cutting-edge technologies for rule-based and case-based reasoning to facilitate efficient decision-making processes.

## Features

- **Legal Document Retrieval**: Users can retrieve judgments and laws stored in AkomaNtoso by providing the document name.
- **Rule-Based Reasoning**: Utilizes DR-Device and RuleML for rule-based reasoning to assist in legal decision-making.
- **Case-Based Reasoning**: Employs ANNOY for case-based reasoning to find similar cases based on provided case base facts.

## Server-Side Documentation

For detailed documentation on the server-side functionality and API endpoints, please refer to the [Server-Side Documentation](server\README.md).

## Client-Side Documentation

The client-side of the application interacts with the server to retrieve legal documents. For information on how to use the client-side application, please refer to its documentation.

## Technologies Used

- Flask: Python web framework for building the server-side application.
- AKOMANTOSO: XML-based legal document standard for legal document retrieval and analysis.
- RuleML: XML-based language for representing rules in rule-based reasoning.
- DR-Device: Legal reasoner.
- ANNOY: Approximate Nearest Neighbors Oh Yeah - a C++ library for efficient approximate nearest neighbor search.

## Installation

To install and set up the application, please follow the instructions provided in the [Server-Side Documentation](server\README.md).

## Usage

Once the server-side application is set up, users can interact with it through the provided API endpoints to retrieve legal documents. Detailed usage instructions are available in the [Server-Side Documentation](server_documentation.md).

---

This README provides an overview of the Legal Document Retrieval Application, its features, technologies used, and links to detailed documentation for both the server-side and client-side applications.
