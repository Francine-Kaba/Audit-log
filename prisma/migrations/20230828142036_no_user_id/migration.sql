/*
  Warnings:

  - You are about to drop the column `user_id` on the `audit_log` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "audit_log" DROP COLUMN "user_id";
