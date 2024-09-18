from fastapi import FastAPI, HTTPException
from neo4j import GraphDatabase
import uvicorn
from ml_model import predict_validity  # Import ML prediction function

app = FastAPI()

# Neo4j connection setup
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

# Function to interact with the Neo4j database
def add_product_to_graph(product):
    with driver.session() as session:
        session.write_transaction(create_product_node, product)

def create_product_node(tx, product):
    query = (
        "MERGE (p:Product {name: $name, category: $category, price: $price}) "
        "RETURN p"
    )
    tx.run(query, name=product["name"], category=product["category"], price=product["price"])

# FastAPI route to add product data into the knowledge graph
@app.post("/add_product/")
async def add_product(product: dict):
    try:
        # Get product features (category and price)
        category_map = {"Electronics": 0, "Home": 1, "Books": 2}
        product_features = [category_map[product["category"]], product["price"] / 1000]  # Normalize price

        # Use the ML model to predict validity
        validity = predict_validity(product_features)
        if validity > 0.5:
            add_product_to_graph(product)
            return {"message": "Product added successfully!"}
        else:
            return {"message": "Product is invalid and not added."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
