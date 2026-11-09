import time
import psycopg2
from pymongo import MongoClient
from neo4j import GraphDatabase


def wait_postgres():
    for _ in range(30):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="erpdb",
                user="erp",
                password="erp"
            )
            conn.close()
            print("PostgreSQL READY")
            return
        except Exception as ex:
            print(f"PostgreSQL not ready: {ex}")
            time.sleep(2)
    raise Exception("PostgreSQL timeout")


def wait_mongo():
    for _ in range(30):
        try:
            client = MongoClient(
                "mongodb://localhost:27017"
            )
            client.admin.command("ping")
            print("MongoDB READY")
            return
        except Exception as ex:
            print(f"MongoDB not ready: {ex}")
            time.sleep(2)
    raise Exception("MongoDB timeout")


def wait_neo4j():
    for _ in range(60):
        try:
            driver = GraphDatabase.driver(
                "bolt://localhost:7687",
                auth=("neo4j", "password")
            )
            driver.verify_connectivity()
            print("Neo4j READY")
            return
        except Exception as ex:
            print(f"Neo4j not ready: {ex}")
            time.sleep(2)
    raise Exception("Neo4j timeout")

wait_postgres()
wait_mongo()
wait_neo4j()

print("ALL SERVICES READY")
