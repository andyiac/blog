# Collections

## collection builder functions

Another way of creating a collection is to call a builder function – buildList(), buildSet(), or buildMap(). They create a new, mutable collection of the corresponding type, populate it using write operations, and return a read-only collection with the same elements:


```kotlin
val map = buildMap { // this is MutableMap<String, Int>, types of key and value are inferred from the `put()` calls below
    put("a", 1)
    put("b", 0)
    put("c", 4)
}

println(map) // {a=1, b=0, c=4}
```

## empty collection

There are also functions for creating collections without any elements: emptyList(), emptySet(), and emptyMap(). When creating empty collections, you should specify the type of elements that the collection will hold.


```kotlin
val empty = emptyList<String>()
```

创建一个不可变 (immutable) 的空列表。

使用场景 

1. 作为函数的默认返回值，当函数返回空时返回 emptyList() 而不是 null

```kotlin
fun getData(): List<String> {
  // getdata logic here
  return emptyList()
}
```

2. 避免空指针：通过使用 emptyList() 返回一个空列表

```kotlin
val list: List<String>? = null
val safeList = list ?: emptyList()
```

注意这里的 `?:` 运算符的使用



## Initializer functions for lists


Creates a new read-only list with the specified size, where each element is calculated by calling the specified init function.
The function init is called for each list element sequentially starting from the first one. It should return the value for a list element given its index.

```kotlin
val doubled = List(3, { it * 2 })
println(doubled)

// MutableList if you want to change its content later
val doubled2 = MutableList(3, { it * 3 })
doubled2.add(100)
println(doubled2)

// console: 
// [0, 2, 4]
// [0, 3, 6, 100]
```


