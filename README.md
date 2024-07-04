# TodoApp with FastAPI and Vuetify


This project is a simple Todo application built with FastAPI for the backend and Vuetify (via CDN) for the frontend. The frontend is rendered using FastAPI Templates.

<img src="https://github.com/Mohammadshekari/FastApi-Vuetify-TodoApp/blob/main/screenshots/todo.jpg?raw=true" width="800">

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates how to create a Todo application using FastAPI for the backend API and Vuetify (loaded via CDN) for the frontend. FastAPI Templates are used to render the frontend.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7+
- pip (Python package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/FastApi-Vuetify-TodoApp.git
    cd FastApi-Vuetify-TodoApp
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:8000`.

## Usage

- Navigate to the homepage to see the Todo list.
- Add a new Todo item using the input field.
- Mark Todo items as completed by clicking the checkbox.
- Remove Todo items using the delete button.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

