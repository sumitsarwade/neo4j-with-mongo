Neo4j_graph with mongo
Documentation for neo4j_graph.py


Purpose:
This script creates a graph in a Neo4j database, establishing nodes and relationships between players, coaches, and teams.

Functions:

1) execute_cypher_query(query):

Purpose: Executes a Cypher query on the Neo4j database.
Parameters:query (str): The Cypher query to execute.
Returns: A list of records returned by the query.

result = execute_cypher_query("MATCH (n) RETURN n")


2) create_graph():

Purpose: Creates a predefined graph in Neo4j with nodes representing players, coaches, and teams, and relationships representing team memberships and coaching.
Parameters: None.
Returns: None.


Documentation for extract_transform.py
Purpose:
This script extracts data from a Neo4j database and inserts it into a MongoDB database, transforming the data as necessary to maintain relationships.

Functions:

1) execute_cypher_query(query):

Purpose: Executes a Cypher query on the Neo4j database.
Parameters:
query (str): The Cypher query to execute.
Returns: A list of records returned by the query.




2) extract_and_transform_data():

Purpose: Extracts data from the Neo4j database and transforms it into a format suitable for MongoDB.
Parameters: None.
Returns: A dictionary containing the extracted data


3) insert_data_to_mongodb(data):

Purpose: Inserts the extracted and transformed data into MongoDB.
Parameters:
data (dict): The data to insert into MongoDB.
Returns: None.

Ensure that Neo4j and MongoDB are running on your local machine before executing the scripts. Run neo4j_graph.py first to create the graph in Neo4j, and then run extract_transform.py to transfer the data to MongoDB.

