#!/usr/bin/env python3
"""
MongoDB Portfolio Integration Script
Script to set up and manage MongoDB integration for the AI Art Portfolio
"""

import os
import json
from pymongo import MongoClient
from datetime import datetime

class MongoDBPortfolioManager:
    def __init__(self, connection_string=None):
        # Use the Atlas connection string from the existing configuration
        if connection_string is None:
            # This would normally read from secrets.env
            connection_string = "mongodb://Admin:Sawsall3!@ac-4a0okpb-shard-00-00.ku8cxvc.mongodb.net:27017,ac-4a0okpb-shard-00-01.ku8cxvc.mongodb.net:27017,ac-4a0okpb-shard-00-02.ku8cxvc.mongodb.net:27017/?ssl=true&authSource=admin&replicaSet=atlas-gkl7qy-shard-0&retryWrites=true&w=majority"
        
        try:
            self.client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
            # Test the connection
            self.client.server_info()
            print("Successfully connected to MongoDB Atlas")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            # Fallback to local MongoDB if Atlas fails
            try:
                self.client = MongoClient("mongodb://localhost:27017/?directConnection=true")
                self.client.server_info()
                print("Connected to local MongoDB instance")
            except Exception as e2:
                print(f"Failed to connect to local MongoDB: {e2}")
                self.client = None
                
        self.db = self.client["Project0"] if self.client else None
        
    def setup_collections(self):
        """Set up the required collections for the portfolio"""
        if not self.db:
            print("No database connection available")
            return
            
        collections = [
            "portfolio_pieces",
            "collections",
            "modifiers",
            "accounts",
            "framework_mappings",
            "metadata"
        ]
        
        for collection_name in collections:
            if collection_name not in self.db.list_collection_names():
                self.db.create_collection(collection_name)
                print(f"Created collection: {collection_name}")
            else:
                print(f"Collection already exists: {collection_name}")
                
        # Create indexes for better performance
        try:
            self.db.portfolio_pieces.create_index([("piece_id", 1)], unique=True)
            self.db.portfolio_pieces.create_index([("title", 1)])
            self.db.portfolio_pieces.create_index([("source_account", 1)])
            self.db.portfolio_pieces.create_index([("tags", 1)])
            self.db.portfolio_pieces.create_index([("collections", 1)])
            print("Created indexes for portfolio_pieces collection")
        except Exception as e:
            print(f"Failed to create indexes: {e}")
            
    def insert_portfolio_piece(self, piece_data):
        """Insert a portfolio piece into MongoDB"""
        if not self.db:
            print("No database connection available")
            return None
            
        try:
            # Add timestamp if not present
            if "created_at" not in piece_data:
                piece_data["created_at"] = datetime.now()
                
            result = self.db.portfolio_pieces.insert_one(piece_data)
            print(f"Inserted portfolio piece with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Failed to insert portfolio piece: {e}")
            return None
            
    def query_portfolio_pieces(self, query=None, limit=10):
        """Query portfolio pieces from MongoDB"""
        if not self.db:
            print("No database connection available")
            return []
            
        try:
            if query is None:
                query = {}
                
            results = list(self.db.portfolio_pieces.find(query).limit(limit))
            print(f"Found {len(results)} portfolio pieces")
            return results
        except Exception as e:
            print(f"Failed to query portfolio pieces: {e}")
            return []
            
    def update_portfolio_piece(self, piece_id, update_data):
        """Update a portfolio piece in MongoDB"""
        if not self.db:
            print("No database connection available")
            return False
            
        try:
            result = self.db.portfolio_pieces.update_one(
                {"piece_id": piece_id},
                {"$set": update_data}
            )
            if result.modified_count > 0:
                print(f"Updated portfolio piece: {piece_id}")
                return True
            else:
                print(f"No portfolio piece found with ID: {piece_id}")
                return False
        except Exception as e:
            print(f"Failed to update portfolio piece: {e}")
            return False
            
    def delete_portfolio_piece(self, piece_id):
        """Delete a portfolio piece from MongoDB"""
        if not self.db:
            print("No database connection available")
            return False
            
        try:
            result = self.db.portfolio_pieces.delete_one({"piece_id": piece_id})
            if result.deleted_count > 0:
                print(f"Deleted portfolio piece: {piece_id}")
                return True
            else:
                print(f"No portfolio piece found with ID: {piece_id}")
                return False
        except Exception as e:
            print(f"Failed to delete portfolio piece: {e}")
            return False
            
    def create_collection(self, collection_name, description=""):
        """Create a portfolio collection"""
        if not self.db:
            print("No database connection available")
            return None
            
        try:
            collection_data = {
                "name": collection_name,
                "description": description,
                "created_at": datetime.now(),
                "piece_count": 0,
                "piece_ids": []
            }
            
            result = self.db.collections.insert_one(collection_data)
            print(f"Created collection: {collection_name}")
            return result.inserted_id
        except Exception as e:
            print(f"Failed to create collection: {e}")
            return None
            
    def add_piece_to_collection(self, collection_name, piece_id):
        """Add a portfolio piece to a collection"""
        if not self.db:
            print("No database connection available")
            return False
            
        try:
            # Update the collection
            result = self.db.collections.update_one(
                {"name": collection_name},
                {
                    "$addToSet": {"piece_ids": piece_id},
                    "$inc": {"piece_count": 1}
                }
            )
            
            if result.modified_count > 0:
                print(f"Added piece {piece_id} to collection {collection_name}")
                return True
            else:
                print(f"Collection {collection_name} not found")
                return False
        except Exception as e:
            print(f"Failed to add piece to collection: {e}")
            return False

def main():
    # Initialize MongoDB manager
    manager = MongoDBPortfolioManager()
    
    # Set up collections
    manager.setup_collections()
    
    print("\nMongoDB Portfolio Integration is ready!")
    print("You can now use the following methods:")
    print("- insert_portfolio_piece(piece_data)")
    print("- query_portfolio_pieces(query)")
    print("- update_portfolio_piece(piece_id, update_data)")
    print("- delete_portfolio_piece(piece_id)")
    print("- create_collection(collection_name, description)")
    print("- add_piece_to_collection(collection_name, piece_id)")

if __name__ == "__main__":
    main()