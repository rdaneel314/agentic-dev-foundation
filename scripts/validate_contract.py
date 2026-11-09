"""Validate the repository's small schema subset and domain rules without packages."""
import json
from pathlib import Path, PurePosixPath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SUPPORTED = {"$schema", "title", "description", "type", "required", "properties", "additionalProperties",
             "enum", "pattern", "minLength", "minItems", "minimum", "items"}


def validate(value, schema, location="record"):
    if set(schema) - SUPPORTED:
        raise ValueError("Unsupported schema keyword")
    types = {"object": dict, "array": list, "string": str, "boolean": bool, "integer": int}
    if schema.get("type") not in types or type(value) is not types[schema["type"]]:
        raise ValueError(f"{location}: invalid type")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(f"{location}: invalid enum")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        if set(schema.get("required", [])) - set(value):
            raise ValueError(f"{location}: missing required field")
        if schema.get("additionalProperties") is False and set(value) - set(properties):
            raise ValueError(f"{location}: unknown field")
        for key, child in value.items():
            if key in properties:
                validate(child, properties[key], location + "." + key)
    elif isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            raise ValueError(f"{location}: empty required array")
        for child in value:
            validate(child, schema["items"], location + "[]")
    elif isinstance(value, str):
        if len(value.strip()) < schema.get("minLength", 0) or ("pattern" in schema and not re.fullmatch(schema["pattern"], value)):
            raise ValueError(f"{location}: invalid string")
    elif type(value) is int and value < schema.get("minimum", value):
        raise ValueError(f"{location}: integer below minimum")


def check_record(kind, record):
    if kind not in {"task", "finding"}:
        raise ValueError("Unknown contract type")
    schema = json.loads((ROOT / f"workflows/schemas/{kind}.schema.json").read_text())
    validate(record, schema)
    if kind == "task":
        for raw in record["allowed_paths"]:
            path = PurePosixPath(raw)
            if path.is_absolute() or ".." in path.parts or "\\" in raw or ":" in raw:
                raise ValueError("Allowed path escapes portable repository scope")
    else:
        if record["severity"] in {"critical", "high"} and not record["blocking"]:
            raise ValueError("Critical/high finding must block")
        if record["status"] == "resolved" and (not record["disposition"].strip() or not record["verified_by"].strip() or record["verified_by"].casefold() == record["reporter_id"].casefold()):
            raise ValueError("Resolved finding requires independent disposition")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: validate_contract.py task|finding path.json")
    check_record(sys.argv[1], json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")))
    print("PASS: contract shape and deterministic rules; not authenticated approval")
