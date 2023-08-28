from prisma import Prisma
from utils.prisma_connect import connect_to_prisma

prisma = Prisma()


class AuditLogQuery:
    # Listing all project hours configurations
    async def audit_log_query(self, info):
        if await connect_to_prisma(prisma):
            audit_log = await prisma.audit_log.find_many(
                
                order={
                    'id': 'desc'
                }
            )
            return audit_log