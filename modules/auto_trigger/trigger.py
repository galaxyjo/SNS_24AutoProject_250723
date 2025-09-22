def trigger_execution():
    print("Auto trigger 실행됨")


def check_conditions(ctx: dict) -> bool:
    return ctx.get("enabled", False)
