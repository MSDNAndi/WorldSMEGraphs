# Functional Theory Quick Reference Card

*Concise reference for practitioners who need a quick refresher*

---

## Category Theory - Core Definitions

### Category
**Definition**: A category **C** consists of:
- Objects: ob(C)
- Morphisms: hom_C(A,B) for each pair A,B ∈ ob(C)
- Composition: ∘ : hom(B,C) × hom(A,B) → hom(A,C)
- Identity: id_A ∈ hom(A,A) for each object A

**Laws**:
- **Associativity**: (h ∘ g) ∘ f = h ∘ (g ∘ f)
- **Identity**: id_B ∘ f = f and f ∘ id_A = f

**Example**: Types and functions form a category
- Objects: `Int`, `String`, `Bool`, etc.
- Morphisms: Functions between types
- Composition: Function composition `g ∘ f`
- Identity: `id x = x`

---

## Functors

### Definition
**Functor F: C → D** consists of:
- Object mapping: F: ob(C) → ob(D)
- Morphism mapping: F: hom_C(A,B) → hom_D(F(A), F(B))

**Laws**:
1. **Preserve identity**: F(id_A) = id_F(A)
2. **Preserve composition**: F(g ∘ f) = F(g) ∘ F(f)

### Type Signatures

**Haskell**:
```haskell
class Functor f where
  fmap :: (a -> b) -> f a -> f b
```

**Scala**:
```scala
trait Functor[F[_]] {
  def map[A, B](fa: F[A])(f: A => B): F[B]
}
```

**TypeScript**:
```typescript
interface Functor<F> {
  map<A, B>(fa: F<A>, f: (a: A) => B): F<B>
}
```

**Rust**:
```rust
trait Functor<A> {
  type Mapped<B>;
  fn fmap<B, F: Fn(A) -> B>(self, f: F) -> Self::Mapped<B>;
}
```

### Common Instances

**List/Array**:
```haskell
fmap f [x1, x2, ...] = [f x1, f x2, ...]
```
```javascript
[1, 2, 3].map(x => x * 2)  // [2, 4, 6]
```

**Maybe/Option**:
```haskell
fmap f Nothing = Nothing
fmap f (Just x) = Just (f x)
```
```scala
Some(5).map(_ * 2)  // Some(10)
None.map(_ * 2)     // None
```

**Function (Reader)**:
```haskell
fmap f g = f . g  -- Composition
```

---

## Monoids

### Definition
**Monoid (M, ⊕, e)** consists of:
- Set M
- Binary operation ⊕: M × M → M
- Identity element e ∈ M

**Laws**:
1. **Associativity**: (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)
2. **Identity**: e ⊕ a = a ⊕ e = a

### Type Signatures

**Haskell**:
```haskell
class Monoid m where
  mempty  :: m
  mappend :: m -> m -> m
  -- Infix: (<>)
```

**Scala**:
```scala
trait Monoid[A] {
  def empty: A
  def combine(x: A, y: A): A
}
```

### Common Instances

| Type | Operation | Identity | Example |
|------|-----------|----------|---------|
| **Int (Sum)** | + | 0 | `1 + 2 + 3 = 6` |
| **Int (Product)** | * | 1 | `2 * 3 * 4 = 24` |
| **String** | ++ (concat) | "" | `"Hello" ++ " " ++ "World"` |
| **List** | ++ (append) | [] | `[1,2] ++ [3] ++ [4,5]` |
| **Bool (AND)** | && | True | `True && True && False = False` |
| **Bool (OR)** | \|\| | False | `False \|\| False \|\| True = True` |
| **Function** | ∘ (compose) | id | `(f ∘ g) ∘ h` |
| **Max** | max | -∞ | `max(max(5, 3), 7) = 7` |
| **Min** | min | +∞ | `min(min(5, 3), 7) = 3` |

### Key Operations

**Reduce/Fold** (generic monoid operation):
```javascript
arr.reduce(mappend, mempty)
```

```haskell
foldl (<>) mempty [x1, x2, x3]
```

**Parallelizable** due to associativity:
```
(1 + 2) + (3 + 4) = ((1 + 2) + 3) + 4
```

---

## Monads

### Definition
**Monad (M, η, μ)** on category C consists of:
- Endofunctor M: C → C
- Unit η: Id ⇒ M (natural transformation)
- Join μ: M ∘ M ⇒ M (natural transformation)

**Laws**:
1. **Associativity**: μ ∘ Mμ = μ ∘ μM
2. **Left identity**: μ ∘ Mη = id
3. **Right identity**: μ ∘ ηM = id

### Alternative Formulation (Bind)

**Type Signatures**:

**Haskell**:
```haskell
class Monad m where
  return :: a -> m a
  (>>=)  :: m a -> (a -> m b) -> m b
```

**Scala**:
```scala
trait Monad[M[_]] extends Functor[M] {
  def pure[A](x: A): M[A]
  def flatMap[A, B](ma: M[A])(f: A => M[B]): M[B]
}
```

**TypeScript**:
```typescript
interface Monad<M> extends Functor<M> {
  pure<A>(x: A): M<A>
  flatMap<A, B>(ma: M<A>, f: (a: A) => M<B>): M<B>
}
```

**Rust**:
```rust
trait Monad<A>: Functor<A> {
  fn pure(x: A) -> Self;
  fn bind<B, F: Fn(A) -> Self::Mapped<B>>(self, f: F) -> Self::Mapped<B>;
}
```

### Laws (Bind Formulation)

1. **Left identity**: `return x >>= f` ≡ `f x`
2. **Right identity**: `m >>= return` ≡ `m`
3. **Associativity**: `(m >>= f) >>= g` ≡ `m >>= (\x -> f x >>= g)`

### Relationship Between Formulations

```haskell
-- join from bind
join m = m >>= id

-- bind from join
m >>= f = join (fmap f m)
```

### Common Instances

**Maybe/Option**:
```haskell
return x = Just x
Nothing >>= f = Nothing
Just x >>= f = f x
```

**List**:
```haskell
return x = [x]
xs >>= f = concat (map f xs)
```

**Either/Result**:
```haskell
return x = Right x
Left e >>= f = Left e
Right x >>= f = f x
```

**IO** (Haskell):
```haskell
-- Wraps side-effecting computations
return :: a -> IO a
(>>=) :: IO a -> (a -> IO b) -> IO b
```

**State**:
```haskell
return x = State $ \s -> (x, s)
(State m) >>= f = State $ \s ->
  let (x, s') = m s
      State n = f x
  in n s'
```

**Reader**:
```haskell
return x = Reader $ \_ -> x
(Reader m) >>= f = Reader $ \r ->
  let x = m r
      Reader n = f x
  in n r
```

---

## Language-Specific Patterns

### JavaScript/TypeScript

**Array (Functor & Monad)**:
```javascript
// Functor
[1, 2, 3].map(x => x * 2)  // [2, 4, 6]

// Monad
[1, 2, 3].flatMap(x => [x, x * 2])  // [1, 2, 2, 4, 3, 6]
```

**Promise (Monad)**:
```javascript
// return/pure
Promise.resolve(5)

// bind (>>=)
promise.then(x => asyncOperation(x))

// Syntactic sugar
async function f() {
  const x = await promise;  // Extract from monad
  return x * 2;             // Wraps in monad
}
```

### Scala

**Option (Functor & Monad)**:
```scala
// Functor
Some(5).map(_ * 2)  // Some(10)

// Monad
Some(5).flatMap(x => if (x > 0) Some(10/x) else None)

// For-comprehension (do-notation)
for {
  x <- Some(5)
  y <- Some(10)
} yield x + y  // Some(15)
```

### Haskell

**Do-notation** (syntactic sugar for `>>=`):
```haskell
-- With explicit bind
action = getLine >>= \name ->
         putStrLn ("Hello, " ++ name)

-- With do-notation
action = do
  name <- getLine
  putStrLn ("Hello, " ++ name)
```

### Rust

**Option (Functor & Monad)**:
```rust
// Functor
Some(5).map(|x| x * 2)  // Some(10)

// Monad
Some(5).and_then(|x| if x > 0 { Some(10/x) } else { None })

// Question mark operator (syntactic sugar)
fn f() -> Option<i32> {
  let x = some_computation()?;  // Early return on None
  let y = another_computation(x)?;
  Some(y * 2)
}
```

### C#

**LINQ (Monadic)**:
```csharp
// SelectMany is bind (>>=)
var result = 
  from x in list1
  from y in list2
  where x + y > 10
  select x * y;

// Desugars to:
list1.SelectMany(x => 
  list2.Where(y => x + y > 10)
       .Select(y => x * y))
```

---

## Common Patterns Cheat Sheet

### Functor Patterns

| Pattern | Operation | Example |
|---------|-----------|---------|
| **Transform container contents** | `map/fmap` | `[1,2,3].map(x => x*2)` |
| **Preserve structure** | Laws guarantee | Mapping over list keeps order/length |
| **Compose transformations** | `fmap (g . f)` | Chain multiple maps efficiently |

### Monoid Patterns

| Pattern | Operation | Example |
|---------|-----------|---------|
| **Aggregate/reduce** | `fold/reduce` | `[1,2,3].reduce((+), 0)` |
| **Parallel computation** | Split-combine | MapReduce, Spark |
| **Configuration merging** | `mappend` | Combine config objects |
| **Accumulate results** | Repeated `<>` | String building, list concatenation |

### Monad Patterns

| Pattern | Operation | Example |
|---------|-----------|---------|
| **Chain effectful operations** | `>>=` / `flatMap` | Pipeline of async operations |
| **Error propagation** | Either/Result | Short-circuit on first error |
| **Null safety** | Maybe/Option | Avoid null checks |
| **State threading** | State monad | Implicit state passing |
| **Dependency injection** | Reader monad | Access environment |
| **Logging/tracing** | Writer monad | Accumulate logs |
| **Async composition** | Promise/Future | Sequential async operations |

---

## Quick Comparisons

### Functor vs Applicative vs Monad

| Abstraction | Power | Type Signature | Use Case |
|-------------|-------|----------------|----------|
| **Functor** | Weakest | `(a → b) → F a → F b` | Transform contents |
| **Applicative** | Medium | `F (a → b) → F a → F b` | Independent effects |
| **Monad** | Strongest | `F a → (a → F b) → F b` | Dependent effects |

### When to Use What

**Use Functor when**:
- Transforming values in a context
- No chaining needed
- Example: Double all numbers in a list

**Use Monoid when**:
- Combining values
- Need associativity
- Example: Summing numbers, concatenating strings

**Use Monad when**:
- Chaining operations
- Each step depends on previous
- Example: Sequential API calls, error handling

---

## Debugging Checklist

### Functor Not Working?
- [ ] Check identity law: `fmap id = id`
- [ ] Check composition law: `fmap (g . f) = fmap g . fmap f`
- [ ] Verify type constructor is consistent

### Monoid Not Working?
- [ ] Check associativity: `(a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)`
- [ ] Check left identity: `e ⊕ a = a`
- [ ] Check right identity: `a ⊕ e = a`
- [ ] Ensure `mempty` is truly neutral

### Monad Not Working?
- [ ] Check left identity: `return x >>= f ≡ f x`
- [ ] Check right identity: `m >>= return ≡ m`
- [ ] Check associativity: `(m >>= f) >>= g ≡ m >>= (λx → f x >>= g)`
- [ ] Ensure functor instance exists and is correct
- [ ] Verify you're not breaking effect ordering

---

## Further Reading

### Essential Books
1. **Mac Lane, S. (1971)**. *Categories for the Working Mathematician*. Springer.
2. **Awodey, S. (2010)**. *Category Theory* (2nd ed.). Oxford University Press.
3. **Lipovača, M. (2011)**. *Learn You a Haskell for Great Good!*
4. **Milewski, B. (2018)**. *Category Theory for Programmers*.

### Key Papers
1. **Moggi, E. (1991)**. "Notions of computation and monads." *Information and Computation*, 93(1), 55-92.
2. **Wadler, P. (1992)**. "The essence of functional programming." *POPL '92*.

### Online Resources
- [Haskell Wiki: Typeclassopedia](https://wiki.haskell.org/Typeclassopedia)
- [Category Theory for Programmers (blog)](https://bartoszmilewski.com/2014/10/28/category-theory-for-programmers-the-preface/)
- [Functors, Applicatives, and Monads in Pictures](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)

---

*Version: 1.0*  
*Last Updated: 2026-01-03*  
*Based on: 27 validated AKUs from functional-theory domain*  
*Target Audience: Practitioners needing quick reference*
