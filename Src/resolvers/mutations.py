from prisma import Prisma
from audit_log.audit_log import create_data
from utils.audit_python import  resolve_user_info
from utils.prisma_connect import connect_to_prisma
from datetime import datetime


prisma = Prisma()


class AuditLog:
    # decorator audit log
    # @audit_request_resolver
    async def create_audit_log(self, info, input):
        if await connect_to_prisma(prisma):
            # 2 types of audit logs
            create_data(input['created_by'], input)
            resolve_user_info(info)

            action_name = input.get('action_name')
            note = input.get('note')
            created_by = input.get('created_by')
            return await prisma.audit_log.create(
                data={
                    'action_name': action_name,
                    'note': note.strip() if note else "",
                    'created_by': created_by,
                    'created_at': datetime.now()
                }
            )
