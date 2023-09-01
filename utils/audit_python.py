# Python logging
import logging

# Create a logger
logger = logging.getLogger('audit_logger')
logger.setLevel(logging.INFO)

# Create a file handler for the audit log
handler = logging.FileHandler('python.log')
handler.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


# Custom decorator for auditing requests
def audit_request_resolver(resolver_func):
    def wrapper(*args, **kwargs):
        request_data = {
            'resolver_function': resolver_func.__name__,
            'arguments': kwargs
        }
        logger.info(f'Request: {request_data}')
        return resolver_func(*args, **kwargs)
    return wrapper


# Another audit example that uses info and requests
def resolve_user_info(audit_request):
    # Configure logging
    logging.basicConfig(filename='python.log', filemode='w', format='%(asctime)s - %(message)s')

    # Create a log entry with both the message and audit_request
    log_message = f'Created audit log: {audit_request}'
    logging.warning(log_message)
