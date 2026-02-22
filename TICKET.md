# SEC-301: Fix SQL Injection Vulnerabilities in User Search

**Status:** In Progress · **Priority:** Critical
**Sprint:** Sprint 32 · **Story Points:** 5
**Reporter:** Security Team · **Assignee:** You (Intern)
**Labels:** `security`, `sql-injection`, `python`, `bug-fix`
**Task Type:** Bug Fix

---

## Description

A penetration test found SQL injection vulnerabilities in the user search module.
An attacker can enter `' OR '1'='1` as a search query and dump the entire database.

Three methods use string concatenation for SQL queries instead of parameterized queries.

## Acceptance Criteria

- [ ] All queries use parameterized queries (? placeholders)
- [ ] No string concatenation/f-strings in SQL
- [ ] Search still works correctly for normal input
- [ ] SQL injection attempts return 0 results (not all results)
- [ ] All tests pass
