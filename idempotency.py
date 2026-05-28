def build_idempotency_key(task_type: str, tenant_id: str, tags: list[str]) -> str:
    joined = ",".join(tags)
    return f"{tenant_id}:{task_type}:{joined}"
