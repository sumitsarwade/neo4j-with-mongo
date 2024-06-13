import neo4j
from neo4j import GraphDatabase

def execute_cypher_query(query):
    uri = "bolt://localhost:7687"
    username = 'neo4j'
    password = 'pass@123'
    
    driver = GraphDatabase.driver(uri, auth=(username, password))
    
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]

# Define your Cypher query
def create_graph():
    cypher_query = """
    CREATE 
    (russell:PLAYER{name:"Russell Westbrook", age: 33}),
    (lebron:PLAYER{name:"LeBron James", age: 36}),
    (anthony:PLAYER{name:"Anthony Davis", age: 28}),
    (ja:PLAYER{name:"Ja Morant", age: 22}),
    (frank:COACH{name: "Frank Vogel"}),
    (taylor:COACH{name: "Taylor Jenkins"}),
    (jason:COACH{name: "Jason Kidd"}),
    (steve:COACH{name: "Steve Nash"}),
    (lakers:TEAM{name:"LA Lakers"}),
    (memphis:TEAM{name:"Memphis Grizzlies"})

    CREATE 
    (russell)-[:TEAMMATES]->(lebron),
    (russell)-[:TEAMMATES]->(anthony),
    (lebron)-[:TEAMMATES]->(anthony),
    (lebron)-[:PLAYS_FOR {salary: 40000000}]->(lakers),
    (russell)-[:PLAYS_FOR {salary: 33000000}]->(lakers),
    (anthony)-[:PLAYS_FOR {salary: 38000000}]->(lakers),
    (ja)-[:PLAYS_FOR {salary: 8000000}]->(memphis),

    (frank)-[:COACHES]->(lebron),
    (frank)-[:COACHES]->(russell),
    (frank)-[:COACHES]->(anthony),
    (taylor)-[:COACHES_FOR]->(memphis)

    """
    
    try:
        result = execute_cypher_query(cypher_query)
        print("Graph created successfully.")
    except Exception as e:
        print("Error:", e)

# Example usage:
if __name__ == "__main__":
    create_graph()
