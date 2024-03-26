# Legal Informatics - Server

Welcome to the Legal Informatics Server directory! This repository houses a server-side application tailored for legal professionals. It offers tools for efficiently generating judgments using rule-based and case-based reasoning methodologies, as well as extracting metadata from PDF judicial documents. Additionally, it provides an API for accessing various functionalities, including rule and case-based reasoning, and querying laws and judgments.

## Installation and Environment Setup

To set up the environment for the Legal Informatics Server, follow these steps:

### Install Poetry

First, install Poetry using pip:

```bash
pip install poetry
```

### Clone the Repository

Clone this repository using the git clone command:

```bash
git clone https://github.com/YoNoSoyMarinero/pravna-informatika-projekat.git
```

### Navigate to the Server Directory

Move to the server directory:

```bash
cd pravna-informatika-projekat/server
```

### Install Dependencies

Configure Poetry to create a virtual environment within the project and install the required dependencies:

```bash
poetry config virtualenvs.in-project true
poetry install
```

This will create a .venv directory in your repository.

### Activate the Virtual Environment

Activate the virtual environment:

```bash
source .venv/bin/activate  # For Unix/Linux
.venv\Scripts\activate     # For Windows
```

### Set Up .env File

Create a .env file in the server directory and define the following environment variables:

```bash
HOST=localhost
PORT=port_you_want_to_run_this
OPENAI_API_KEY=your_openai_api_key
```

### Run the app in dev mode

```bash
flask --app app.py --debug run
```

## API

The Legal Informatics Server API documentation is as follows:

### [API Documentation](api_documentation.md)

Please refer to the API documentation for detailed information on endpoints and usage instructions.

Feel free to reach out if you have any questions or need further assistance!
