#!/bin/bash
# crm_manager.sh - Local CRM database manager
# Path: ~/.openclaw/scripts/crm_manager.sh
# Protocol: MASTER AGENT PROTOCOL v5.0

CRM_FILE="$HOME/.openclaw/memory-data/crm_database.json"
SCHEMA_FILE="$HOME/.openclaw/memory-data/crm_schema.json"

# Ensure CRM file exists
if [ ! -f "$CRM_FILE" ]; then
    echo "Error: CRM database not found at $CRM_FILE"
    exit 1
fi

# Function to add a contact
add_contact() {
    local name="$1"
    local email="$2"
    local org="$3"
    local role="$4"
    local country="$5"
    local source="$6"
    
    # Generate UUID
    local uuid=$(uuidgen 2>/dev/null || echo "contact_$(date +%s)")
    
    # Create contact JSON
    local contact=$(cat <<EOF
{
  "id": "$uuid",
  "name": "$name",
  "email": "$email",
  "email_status": "pending_validation",
  "organisation": "$org",
  "role": "$role",
  "country": "$country",
  "industry": "",
  "source": "$source",
  "added_date": "$(date +%Y-%m-%d)",
  "status": "active",
  "notes": "",
  "tags": [],
  "last_contact": null,
  "next_action": null,
  "crm_stage": "prospect"
}
EOF
)
    
    # Add to CRM (requires jq)
    if command -v jq &> /dev/null; then
        jq ".contacts += [$contact]" "$CRM_FILE" > "${CRM_FILE}.tmp" && mv "${CRM_FILE}.tmp" "$CRM_FILE"
        echo "Contact added: $name ($email)"
    else
        echo "Error: jq is required to manage CRM"
        exit 1
    fi
}

# Function to list contacts
list_contacts() {
    if command -v jq &> /dev/null; then
        echo "=== CONTACTS ==="
        jq -r '.contacts[] | "\(.name) | \(.email) | \(.crm_stage) | \(.status)"' "$CRM_FILE" 2>/dev/null || echo "No contacts yet"
    else
        cat "$CRM_FILE"
    fi
}

# Function to show stats
show_stats() {
    if command -v jq &> /dev/null; then
        echo "=== CRM STATS ==="
        jq '.stats' "$CRM_FILE"
    fi
}

# Main command handler
case "$1" in
    add)
        add_contact "$2" "$3" "$4" "$5" "$6" "$7"
        ;;
    list)
        list_contacts
        ;;
    stats)
        show_stats
        ;;
    *)
        echo "Usage: $0 {add|list|stats}"
        echo "  add <name> <email> <org> <role> <country> <source>"
        echo "  list"
        echo "  stats"
        ;;
esac
