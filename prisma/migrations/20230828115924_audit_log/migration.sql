-- CreateTable
CREATE TABLE "audit_log" (
    "id" SERIAL NOT NULL,
    "user_id" INTEGER NOT NULL,
    "action_name" TEXT NOT NULL,
    "note" TEXT,
    "created_at" TIMESTAMP(3),
    "created_by" INTEGER,

    CONSTRAINT "audit_log_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "audit_log_action_name_key" ON "audit_log"("action_name");
