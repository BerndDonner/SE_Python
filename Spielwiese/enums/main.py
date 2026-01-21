import types
from typing import Any, ClassVar, Dict, Generic, List, Type, TypeVar


T = TypeVar("T")  # Rohwert-Typ der Member (z.B. int)


class Member(Generic[T]):
    def __init__(self, name: str, value: T):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"<Member {self.name}={self.value!r}>"


class MiniEnumMeta(type):
    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        raw_members: Dict[str, Any] = {}

        for key, val in list(namespace.items()):
            if key.startswith("_"):
                continue
            if isinstance(val, (types.FunctionType, types.BuiltinFunctionType)):
                continue
            if isinstance(val, (classmethod, staticmethod, property)):
                continue

            raw_members[key] = val

        for key in raw_members:
            del namespace[key]

        cls = super().__new__(mcls, name, bases, namespace)

        # Diese Attribute existieren ab jetzt immer (für den Typchecker explizit setzen)
        cls._member_map_ = {}   # type: ignore[attr-defined]
        cls._value_map_ = {}    # type: ignore[attr-defined]

        for member_name, raw_value in raw_members.items():
            mem = Member(member_name, raw_value)
            setattr(cls, member_name, mem)
            cls._member_map_[member_name] = mem  # type: ignore[attr-defined]
            cls._value_map_[raw_value] = mem     # type: ignore[attr-defined]

        return cls


E = TypeVar("E", bound="MiniEnum[Any]")


class MiniEnum(Generic[T], metaclass=MiniEnumMeta):
    # Für Pylance: diese Klassenattribute “gehören dazu”
    _member_map_: ClassVar[Dict[str, Member[Any]]]
    _value_map_: ClassVar[Dict[Any, Member[Any]]]

    @classmethod
    def from_value(cls: Type[E], value: Any) -> Member[Any]:
        return cls._value_map_[value]

    @classmethod
    def members(cls: Type[E]) -> List[Member[Any]]:
        return list(cls._member_map_.values())

# --- Nutzung ---
class KartenStatus(MiniEnum[int]):
    VERDECKT = 0
    AUFGEDECKT = 1
    GEFUNDEN = 2
    
    def hallo(self):
        return "ich bin eine normale Methode"
    


print(KartenStatus.VERDECKT) # <Member VERDECKT=0>
print(type(KartenStatus.VERDECKT)) # <class '__main__.Member'>
print(KartenStatus.from_value(1)) # <Member AUFGEDECKT=1>
print(KartenStatus.members()) # [<Member ...>, ...]
print(KartenStatus().hallo()) # "ich bin eine normale Methode"
