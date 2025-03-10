import logging

logger = logging.getLogger(__name__)

def show_subscription(query, context):
    user_id = query.from_user.id
    # Add logging for database check
    db_payment_config = db.child("config").child("wallet_address").get().val()
    logger.info(f"Database wallet config: {db_payment_config}")
    
    wallet_address = "0xe2732e0ec6798193285dae905bb534c40bdd6ccc"
    logger.info(f"Using wallet address: {wallet_address}")
    # ... rest of the code