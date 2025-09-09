from dataclasses import dataclass
from typing import Any, Callable, Mapping

from .float import (
    FLOAT_UNARY_OPERATIONS,
    FLOAT_UNARY_CONDITIONS,
    FLOAT_BINARY_OPERATIONS,
    FLOAT_BINARY_CONDITIONS,
)
from .types import Number

DEFAULT_NUMBER = ("NUMBER", {"default": 0.0})


class NumberUnaryOperation:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_UNARY_OPERATIONS.keys()),),
                "a": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("NUMBER",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(self, op: str, a: Number) -> tuple[float]:
        return (FLOAT_UNARY_OPERATIONS[op](float(a)),)


class NumberUnaryCondition:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_UNARY_CONDITIONS.keys()),),
                "a": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "op"
    CATEGORY = "math/Number"

    def op(self, op: str, a: Number) -> tuple[bool]:
        return (FLOAT_UNARY_CONDITIONS[op](float(a)),)


class NumberBinaryOperation:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_BINARY_OPERATIONS.keys()),),
                "a": DEFAULT_NUMBER,
                "b": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("NUMBER",)
    FUNCTION = "op"
    CATEGORY = "math/number"

    def op(self, op: str, a: Number, b: Number) -> tuple[float]:
        return (FLOAT_BINARY_OPERATIONS[op](float(a), float(b)),)


class NumberBinaryCondition:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(FLOAT_BINARY_CONDITIONS.keys()),),
                "a": DEFAULT_NUMBER,
                "b": DEFAULT_NUMBER,
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "op"
    CATEGORY = "math/float"

    def op(self, op: str, a: Number, b: Number) -> tuple[bool]:
        return (FLOAT_BINARY_CONDITIONS[op](float(a), float(b)),)


NODE_CLASS_MAPPINGS = {
    "CM_NumberUnaryOperation": NumberUnaryOperation,
    "CM_NumberUnaryCondition": NumberUnaryCondition,
    "CM_NumberBinaryOperation": NumberBinaryOperation,
    "CM_NumberBinaryCondition": NumberBinaryCondition,
}
