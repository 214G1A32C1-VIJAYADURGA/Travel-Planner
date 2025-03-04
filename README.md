# Travel Planner App

## Overview
The **Travel Planner App** is a Streamlit-based web application that provides AI-powered travel recommendations. It helps users find the best travel options between two locations by considering multiple modes of transportation such as cabs, trains, buses, and flights.

## Features
- Accepts user input for **source** and **destination** cities.
- Uses **LangChain** and **Google Generative AI (Gemini-1.5-Pro)** to analyze and generate travel recommendations.
- Provides detailed comparisons of **cost, time, pros, cons, and additional notes** for each travel mode.
- Highlights the **cheapest** and **fastest** travel options.
- Displays results in a user-friendly, structured format with expandable details.
- Provides a disclaimer about cost estimations and travel time variations.

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Streamlit
- LangChain
- Google Generative AI SDK

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/your-repository/travel-planner.git
cd travel-planner
```

### Install dependencies
```bash
pip install streamlit langchain langchain-google-genai
```
