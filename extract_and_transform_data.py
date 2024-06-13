from neo4j import GraphDatabase
from pymongo import MongoClient

def execute_cypher_query(query):
    uri = "bolt://localhost:7687"
    username = 'neo4j'
    password = 'pass@123'
    
    driver = GraphDatabase.driver(uri, auth=(username, password))
    
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]

def extract_and_transform_data():
    queries = {
        "players": "MATCH (p:PLAYER) RETURN p",
        "coaches": "MATCH (c:COACH) RETURN c",
        "teams": "MATCH (t:TEAM) RETURN t",
        "plays_for": "MATCH (p:PLAYER)-[r:PLAYS_FOR]->(t:TEAM) RETURN p, r, t",
        "coaches_for": "MATCH (c:COACH)-[r:COACHES_FOR]->(t:TEAM) RETURN c, r, t",
        "teammates": "MATCH (p1:PLAYER)-[:TEAMMATES]->(p2:PLAYER) RETURN p1, p2"
    }

    data = {key: execute_cypher_query(query) for key, query in queries.items()}
    return data

def insert_data_to_mongodb(data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sportsdb"]

    # Drop existing collections
    db.players.drop()
    db.coaches.drop()
    db.teams.drop()
    db.plays_for.drop()
    db.coaches_for.drop()
    db.teammates.drop()

    # Insert Players
    player_docs = [{"name": record["p"]["name"], "age": record["p"]["age"]} for record in data["players"]]
    player_ids = db.players.insert_many(player_docs).inserted_ids

    # Insert Coaches
    coach_docs = [{"name": record["c"]["name"]} for record in data["coaches"]]
    coach_ids = db.coaches.insert_many(coach_docs).inserted_ids

    # Insert Teams
    team_docs = [{"name": record["t"]["name"]} for record in data["teams"]]
    team_ids = db.teams.insert_many(team_docs).inserted_ids

    # Insert Plays For Relationships
    plays_for_docs = [
        {
            "player_id": db.players.find_one({"name": record["p"]["name"]})["_id"],
            "team_id": db.teams.find_one({"name": record["t"]["name"]})["_id"],
            "salary": record["r"]["salary"]
        }
        for record in data["plays_for"]
    ]
    db.plays_for.insert_many(plays_for_docs)

    # Insert Coaches For Relationships
    coaches_for_docs = [
        {
            "coach_id": db.coaches.find_one({"name": record["c"]["name"]})["_id"],
            "team_id": db.teams.find_one({"name": record["t"]["name"]})["_id"]
        }
        for record in data["coaches_for"]
    ]
    db.coaches_for.insert_many(coaches_for_docs)

    # Insert Teammates Relationships
    teammates_docs = [
        {
            "player1_id": db.players.find_one({"name": record["p1"]["name"]})["_id"],
            "player2_id": db.players.find_one({"name": record["p2"]["name"]})["_id"]
        }
        for record in data["teammates"]
    ]
    db.teammates.insert_many(teammates_docs)

    print("Data transferred successfully to MongoDB.")

if __name__ == "__main__":
    data = extract_and_transform_data()  # Extract and transform data from Neo4j
    insert_data_to_mongodb(data)  # Insert the transformed data into MongoDB
