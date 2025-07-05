# FastAPI Mail Server

A simple and secure FastAPI application designed to handle contact form submissions and send emails via SMTP. This server acts as a backend for your website's contact forms, ensuring your email credentials are not exposed on the client-side.

## Features

- **FastAPI Backend:** Built with FastAPI for high performance and easy API development.
- **CORS Enabled:** Configured with Cross-Origin Resource Sharing to allow requests from specified frontend domains.
- **Secure Email Sending:** Uses `smtplib.SMTP_SSL` for secure communication with the email server.
- **Environment Variable Management:** Utilizes `python-dotenv` to manage sensitive credentials securely.
- **Simple Contact Form Integration:** Provides a single `/send-email` endpoint for receiving form data.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+**
- **pip** (Python package installer)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/byali-dev/fastapi.mailserver.git](https://github.com/byali-dev/fastapi.mailserver.git)
    cd fastapi.mailserver
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    _If you don't have a `requirements.txt` yet, create one with:_

    ```bash
    pip install fastapi uvicorn python-dotenv python-multipart # python-multipart is needed for Form data
    pip freeze > requirements.txt
    ```

## Environment Variables

This application uses environment variables to store sensitive information like email credentials. You **must** create a `.env` file in the root directory of your project.

**`.env` file example:**
