# AI Product Recommendation System

A lightweight AI-powered product recommendation app built with FastAPI, Jinja2, and Google Gemini. Users can enter a product name or category and receive curated recommendations with prices, descriptions, and reasoning in an easy-to-read web interface.

## Overview

This project demonstrates how to combine a modern Python web app with a large language model to generate product suggestions based on a user query. The backend exposes a FastAPI endpoint that calls a Gemini model and returns structured JSON recommendations, while the frontend renders the results in a clean product card layout.

## Features

- AI-powered recommendations for product names and categories
- FastAPI backend with a REST endpoint
- Jinja2-based frontend UI
- Structured JSON response format
- Product cards with name, price, description, and recommendation reason
- CORS enabled for frontend integration
- Responsive styling for a clean user experience

## Tech Stack

- Python
- FastAPI
- Jinja2
- HTML/CSS
- LangChain
- Google Generative AI / Gemini
- python-dotenv

## Project Structure

```text
AI-Product-Recommendation-System/
├── main.py
├── requirements.txt
├── styles.css
├── .gitignore
├── templates/
│   └── index.html
└── README.md
```

## How It Works

1. The user enters a product name or category in the web UI.
2. The frontend sends a request to the `/product` endpoint.
3. The FastAPI backend calls a Gemini model using a prompt template.
4. The model returns 5 product recommendations in JSON format.
5. The frontend displays the recommendations as product cards.

## API Endpoint

### GET `/product?name={product_name}`

Example:

```bash
http://127.0.0.1:8000/product?name=laptop
```

Example response:

```json
{
  "recommendations": [
    {
      "name": "Dell XPS 13",
      "price": "₹89,990",
      "Description": "A premium ultrabook with a compact design and strong performance.",
      "reason": "Ideal for professionals who want portability and reliable productivity."
    }
  ]
}
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/preethamreddytn/AI-Product-Recommendation-System.git
cd AI-Product-Recommendation-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> Note: The app uses `langchain_google_genai`, so ensure your Google API key is valid and has access to the Gemini model.

## Run the Application

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## Screenshots

The app provides a clean product search UI where users can enter a product or category and view AI-generated recommendations.

## Future Improvements

- Add product filtering by budget and use case
- Add category-based recommendations
- Store user search history
- Improve recommendation quality with a custom retrieval layer
- Add authentication and user profiles

## License

This project is available for educational and personal use.

## Author

Preetham Reddy
