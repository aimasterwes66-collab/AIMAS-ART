#!/bin/bash

# Inventory script for existing AI art content
# This script helps catalog existing content from your Google Photos accounts

echo "DB-air AI Art Portfolio - Content Inventory"
echo "=========================================="

# Create inventory directory
mkdir -p ~/AIMAS/DB-air/inventory

# Function to inventory account content
inventory_account() {
    local account=$1
    echo "Inventorying content for account: $account"
    
    # Create account directory if it doesn't exist
    mkdir -p ~/AIMAS/DB-air/accounts/$account
    
    # Create a basic inventory file for this account
    cat > ~/AIMAS/DB-air/accounts/$account/inventory_$(date +%Y%m%d).txt << EOF
# Content Inventory for $account
# Generated on $(date)

## Collections Found:
- [ ] List collections here

## Individual Images:
- [ ] List individual images here

## Prompts Found:
- [ ] List prompt files here

## Notes:
- [ ] Add any relevant notes here
EOF

    echo "Created inventory template for $account"
    echo "Please update ~/AIMAS/DB-air/accounts/$account/inventory_$(date +%Y%m%d).txt with actual content information"
}

# Inventory both accounts
inventory_account "wesusesaipod"
inventory_account "aimasterwes2"

echo ""
echo "Inventory templates created for both accounts."
echo "Please review and update these files with actual content information."
echo ""
echo "Next steps:"
echo "1. Review the inventory templates in ~/AIMAS/DB-air/accounts/"
echo "2. Update them with actual content information"
echo "3. Run the organization helper script to begin processing"
echo "4. Use the portfolio piece template to catalog individual pieces"