from redaction import redact_authorization


def test_redact_authorization_is_case_insensitive_and_preserves_scheme() -> None:
    assert redact_authorization("Bearer sk-live-123") == "Bearer <redacted>"
    assert redact_authorization("bearer sk-live-123") == "bearer <redacted>"
