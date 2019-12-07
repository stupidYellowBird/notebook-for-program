import typing as t
# 常用类型
# typing常用类型
# int、long、float：整型、长整形、浮点型
# bool、str：布尔型、字符串类型
# List、 Tuple、 Dict、 Set：列表、元组、字典、集合
# Iterable、Iterator：可迭代类型、迭代器类型
# Generator：生成器类型
# union[str,int] 
# union[str,int,str]==union[str,int] 
# union[union[str,int],list]==union[str,int,list] 
# union[int]==int 
# union[x,None]==optional[x]

# AnyStr
AnyStr = TypeVar('AnyStr', str, bytes)
def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat(u"foo", u"bar")  # Ok, output has type 'unicode'
concat(b"foo", b"bar")  # Ok, output has type 'bytes'
concat(u"foo", b"bar")  # Error, cannot mix unicode and bytes

# ClassVar类变量
class Starship:
    stats: ClassVar[Dict[str, int]] = {} # class variable
    damage: int = 10                     # instance variable

# Literal文本选项
def validate_simple(data: Any) -> Literal[True]:  # always returns True
    pass

MODE = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: MODE) -> str:
    pass
open_helper('/some/path', 'r')  # Passes type check
open_helper('/other/path', 'typo')  # Error in type checker

# Tuple
Tuple[int,...] # int 元组

# 装饰器
@typing.runtime_checkable
# 将协议类标记为运行时协议。
# 这样的协议可以用于 isinstance() 和 issubclass() . 
# 这提出 TypeError 当应用于非协议类时。这使得一个简单的结构检查，非常类似于“一个技巧小马” collections.abc 如 Iterable . 例如：：

@runtime_checkable
class Closable(Protocol):
    def close(self): ...

assert isinstance(open('/some/file'), Closable)
警告： 这将只检查所需方法的存在，而不是它们的类型签名！



# t.NoReturn 不返回值
def stop() -> NoReturn:
    pass
# Final 
# 修饰类,类不能被继承
# 修饰方法,方法不能被子类override
# 修饰变量,不能重新赋值
MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker


# 类型别名
Vector = List[float]
def scale(scale:float,vector:Vector) : ->Vector
    pass

# 重载overload

# 可调用对象
# Callable[[Arg1Type, Arg2Type], ReturnType].
def feeder(get_next_item: Callable[[], str]) -> None:
    # Body
    pass

# 泛型

# any类型

# 类型变量
T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, bytes)  # Must be str or bytes

# 定义协议类
class proto(t.Protocol):
    def methd():
        pass
def fuc(x:proto):
    return x.methd()


class User: ...
class BasicUser(User): ...
class ProUser(User): ...
class TeamUser(User): ...

# Accepts User, BasicUser, ProUser, TeamUser, ...
def make_new_user(user_class: Type[User]) -> User:
    return user_class()




t.AbstractSet()
t.Any
t.AnyStr
t.AsyncContextManager
t.AsyncGenerator
t.AsyncIterable
t.AsyncIterator
t.Awaitable
t.BinaryIO
t.ByteString
t.CT_co
t.Callable
t.CallableMeta
t.ChainMap
t.ClassVar
t.Collection
t.Container
t.ContextManager
t.Coroutine
t.Counter
t.DefaultDict
t.Deque
t.Dict
t.FrozenSet
t.Generator
t.Generic
t.GenericMeta
t.Hashable
t.IO
t.ItemsView
t.Iterable
t.Iterator
t.KT
t.KeysView
t.List
t.Mapping
t.MappingView
t.Match
t.MethodDescriptorType
t.MethodWrapperType
t.MutableMapping
t.MutableSequence
t.MutableSet
t.NamedTuple
t.NamedTupleMeta
t.NewType
t.NoReturn
t.Optional
t.Pattern
t.Reversible
t.Sequence
t.Set
t.Sized
t.SupportsAbs
t.SupportsBytes
t.SupportsComplex
t.SupportsFloat
t.SupportsInt
t.SupportsRound
t.T
t.TYPE_CHECKING
t.T_co
t.T_contra
t.Text
t.TextIO
t.Tuple
t.TupleMeta
t.Type
t.TypeVar
t.TypingMeta
t.Union
t.VT
t.VT_co
t.V_co
t.ValuesView
t.WrapperDescriptorType
t._Any
t._ClassVar
t._FinalTypingBase
t._ForwardRef
t._G_base
t._NoReturn
t._Optional
t._PY36
t._Protocol
t._ProtocolMeta
t._TypeAlias
t._TypingBase
t._TypingEllipsis
t._TypingEmpty
t._Union
t.__all__
t.__builtins__
t.__cached__
t.__doc__
t.__file__
t.__loader__
t.__name__
t.__package__
t.__spec__
t._allowed_types
t._check_generic
t._cleanups
t._collections_abc
t._eval_type
t._generic_new
t._get_defaults
t._get_type_vars
t._make_nmtuple
t._make_subclasshook
t._next_in_mro
t._no_slots_copy
t._overload_dummy
t._prohibited
t._qualname
t._remove_dups_flatten
t._replace_arg
t._special
t._subs_tree
t._tp_cache
t._trim_name
t._type_check
t._type_repr
t._type_vars
t.abc
t.abstractmethod
t.abstractproperty
t.cast
t.collections
t.collections_abc
t.contextlib
t.functools
t.get_type_hints
t.io
t.no_type_check
t.no_type_check_decorator
t.overload
t.re
t.stdlib_re
t.sys
t.types