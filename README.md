# ai-powered-knowledge-graph



knowledge-graph-ai/
│
├── main.py
├── ml_model.py
├── requirements.txt
├── README.md
└── .gitignore

This project demonstrates how to use FastAPI, Neo4j, and TensorFlow to build an internal knowledge graph for product information access. An AI model built with TensorFlow scans and validates product data before adding it to the graph.

 Features
- FastAPI for RESTful API interaction
- Neo4j for graph data modeling
- TensorFlow machine learning model to validate product data

Installation

1. Clone the repository:
  
   git clone https://github.com/yourusername/knowledge-graph-ai.git
   cd knowledge-graph-ai
   

2. Install the dependencies:
   bash
   pip install -r requirements.txt
  

3. Set up Neo4j and run it locally.

4. Run the FastAPI application:
   
   uvicorn main:app --reload
   

5. Use the API via `http://127.0.0.1:8000`.



