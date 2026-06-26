#!/bin/bash

# DB-air Organization Helper Script

echo "DB-air AI Art Portfolio Framework - Organization Helper"
echo "======================================================"

# Function to create a new portfolio piece entry
create_portfolio_piece() {
    echo "Creating new portfolio piece entry..."
    read -p "Enter piece title: " title
    read -p "Enter source account (wesusesaipod/aimasterwes2): " account
    read -p "Enter image filename: " image_file
    read -p "Enter prompt filename: " prompt_file
    
    # Generate a unique ID
    piece_id="piece_$(date +%Y%m%d_%H%M%S)"
    
    # Create directory for this piece
    mkdir -p ~/AIMAS/DB-air/portfolio-data/$piece_id
    
    # Create basic metadata file
    cat > ~/AIMAS/DB-air/portfolio-data/$piece_id/metadata.json << EOF
{
  "piece_id": "$piece_id",
  "title": "$title",
  "creation_date": "$(date +%Y-%m-%d)",
  "source_account": "$account",
  "image_file": "$image_file",
  "prompt_file": "$prompt_file",
  "status": "new"
}
EOF

    echo "Created portfolio piece: $piece_id"
}

# Function to list existing portfolio pieces
list_portfolio_pieces() {
    echo "Existing portfolio pieces:"
    ls -la ~/AIMAS/DB-air/portfolio-data/ | grep "^d" | grep -v "total"
}

# Function to update portfolio catalog
update_catalog() {
    echo "Updating portfolio catalog..."
    # This would be expanded to actually read piece metadata and update the CSV
    echo "Catalog update placeholder"
}

# Main menu
echo "Select an option:"
echo "1. Create new portfolio piece"
echo "2. List existing portfolio pieces"
echo "3. Update portfolio catalog"
echo "4. Exit"

read -p "Enter choice (1-4): " choice

case $choice in
    1) create_portfolio_piece ;;
    2) list_portfolio_pieces ;;
    3) update_catalog ;;
    4) echo "Exiting..." ;;
    *) echo "Invalid choice" ;;
esac