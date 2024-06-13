# Neo4j_graph with MongoDB

## Description

This repository contains scripts (`neo4j_graph.py` and `extract_transform.py`) for working with Neo4j and MongoDB databases.

### Purpose

- **neo4j_graph.py:** Creates a graph in a Neo4j database with nodes representing players, coaches, and teams, and relationships representing team memberships and coaching.
  
- **extract_transform.py:** Extracts data from Neo4j and inserts it into a MongoDB database, transforming the data as necessary to maintain relationships.

## Installation

1. **Prerequisites:**

   - Install Neo4j: [Neo4j Installation Guide](https://neo4j.com/docs/operations-manual/current/installation/)
   - Install MongoDB: [MongoDB Installation Guide](https://docs.mongodb.com/manual/installation/)
   - Python 3.x installed with pip.

2. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/neo4j_graph_with_mongo.git
   cd neo4j_graph_with_mongodb
