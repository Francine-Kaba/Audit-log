from ariadne import load_schema_from_path
from ariadne.contrib.federation import (FederatedObjectType, make_federated_schema)
from ariadne.asgi import GraphQL
from Src.resolvers.mutations import AuditLog
from Src.resolvers.queries import AuditLogQuery
from flask import Flask

app = Flask(__name__)

type_defs = load_schema_from_path("schema")

query = FederatedObjectType("Query")
mutation = FederatedObjectType("Mutation")

# login
mutation.set_field("createAuditLog", AuditLog.create_audit_log)
query.set_field("allAuditLog", AuditLogQuery.audit_log_query)


url = "http://127.0.0.1:8000"

print("🚀🚀 Server is up and running on 🔥🔥 " + url)

schema = make_federated_schema(type_defs, mutation, query)
app = GraphQL(schema, debug=True)

if __name__ == '__main__':
    app.run()
