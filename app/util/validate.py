from uuid import UUID


def is_uuid(uuid_str, version=4):
    try:
        UUID(uuid_str, version=version)
    except ValueError:
        return False
    return True
