"""Module to manipulate UUID."""

from typing import Any
import uuid

from mlcroissant._src.core.constants import BASE_IRI
from mlcroissant._src.core.context import Context
from mlcroissant._src.core.types import Json


def generate_uuid() -> str:
    """Generates a UUID of version 4 because it's random and simple."""
    return str(uuid.uuid4())


def uuid_from_jsonld(uuid: Json | None) -> str:
    """Retrieves uuid from a JSON-LD fragment. If no uuid, it will generate one."""
    if isinstance(uuid, dict):
        uuid = uuid.get("@id")
    if isinstance(uuid, str):
        return uuid
    return generate_uuid()


def uuid_to_jsonld(uuid: str | None) -> str | None:
    """Removes the base IRI from an expanded @id."""
    if uuid is None:
        return None
    return uuid.split(BASE_IRI)[-1]


def formatted_uuid_to_json(
    ctx: Context, uuid: None | str
) -> str | None | dict[str, Any]:
    """Return a formatted node's uuid depending on the Croissant version."""
    if ctx.is_v0():
        return uuid
    else:
        return {"@id": uuid_to_jsonld(uuid)}
