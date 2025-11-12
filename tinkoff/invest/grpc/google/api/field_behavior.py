from enum import IntEnum


class FieldBehavior(IntEnum):
    FIELD_BEHAVIOR_UNSPECIFIED = 0
    OPTIONAL = 1
    REQUIRED = 2
    OUTPUT_ONLY = 3
    INPUT_ONLY = 4
    IMMUTABLE = 5
    UNORDERED_LIST = 6
    NON_EMPTY_DEFAULT = 7
