class RuleResult:
    def __init__(self, passed: bool, reason: str = ""):
        self.passed = passed
        self.reason = reason

    def __bool__(self):
        return self.passed


def get_default_policy():
    return {
        "banned": {"spam", "scam", "fraud"},
        "allowed": {"help", "support", "contact"},
    }


def evaluate(text: str, policy=None):
    if policy is None:
        policy = get_default_policy()

    text_lower = text.lower()

    for allowed_word in policy.get("allowed", []):
        if allowed_word in text_lower:
            return RuleResult(True, reason=f"Contains allowed word: {allowed_word}")

    for banned_word in policy.get("banned", []):
        if banned_word in text_lower:
            return RuleResult(False, reason=f"Contains banned word: {banned_word}")

    return RuleResult(True, reason="No banned content detected")
