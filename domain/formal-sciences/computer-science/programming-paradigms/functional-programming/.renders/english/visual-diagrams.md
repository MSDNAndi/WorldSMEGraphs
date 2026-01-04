# Functional Programming Visual Companion

**Supplement to**: "The Functional Programming Adventure" and "Professional Guide"  
**Format**: ASCII diagrams and visual explanations

---

## Visual 1: The Functor Box Concept

```
┌─────────────────────────────────────┐
│  FUNCTOR: A Box You Can Map Over   │
├─────────────────────────────────────┤
│                                     │
│   Before:          After:           │
│   ┌───┐            ┌───┐            │
│   │ 5 │  .map()    │10 │            │
│   └───┘  x => x*2  └───┘            │
│                                     │
│   The BOX stays the same!           │
│   Only the VALUE changes!           │
└─────────────────────────────────────┘
```

---

## Visual 2: Functor Laws Illustrated

### Identity Law: map(id) = id

```
Input:  [1, 2, 3]
         ↓
    map(x => x)     (identity function)
         ↓
Output: [1, 2, 3]   (unchanged!)
```

### Composition Law: map(g ∘ f) = map(g) ∘ map(f)

```
Option A: Compose first, then map
    [1, 2, 3] → map(x => double(inc(x))) → [4, 6, 8]

Option B: Map twice
    [1, 2, 3] → map(inc) → [2, 3, 4] → map(double) → [4, 6, 8]

Result: SAME! ✓
```

---

## Visual 3: Common Functors in the Wild

```
┌──────────────┬───────────────────┬─────────────────┐
│   Functor    │   What it holds   │   map example   │
├──────────────┼───────────────────┼─────────────────┤
│   Array      │   Multiple values │   [1,2].map()   │
│   Option     │   Maybe a value   │   Some(5).map() │
│   Promise    │   Future value    │   promise.then()│
│   Result     │   Success/Error   │   Ok(x).map()   │
└──────────────┴───────────────────┴─────────────────┘
```

---

## Visual 4: The Monad Pipeline

```
Railway-Oriented Programming:

Success Track:  ════════════════════════════════>
                   ║        ║        ║
Error Track:    ═══╩════════╩════════╩═══════════>
                   
Each step can:
  ║  Stay on success track
  ╩  Switch to error track (and stay there)
```

---

## Visual 5: Monad vs Functor

```
FUNCTOR (map):
┌─────┐              ┌─────┐
│  5  │──f: x→x*2──→ │ 10  │
└─────┘              └─────┘
 Box                  Box

MONAD (flatMap):
┌─────┐              ┌─────┐
│  5  │──f: x→Box(x*2)→ │ 10  │  (flattened!)
└─────┘              └─────┘
 Box                  Box (not Box<Box>)
```

---

## Visual 6: Option Monad in Action

```
getUserById(5)           Some(User)
    ↓ flatMap                ↓
getAddress(user)         Some(Address)  
    ↓ flatMap                ↓
getZipCode(address)      Some("12345")
    ↓ map                    ↓
formatForDisplay         Some("Zip: 12345")

If ANY step returns None:
getUserById(999)         None
    ↓ flatMap               ↓
getAddress(user)         None (skipped!)
    ↓ flatMap               ↓
getZipCode(address)      None (skipped!)
    ↓ map                   ↓
formatForDisplay         None
```

---

## Visual 7: Monoid Combining

```
String Monoid:
    "Hello" + "" + "World" = "HelloWorld"
            ↑
         identity

Array Monoid:
    [1,2] + [] + [3,4] = [1,2,3,4]
          ↑
       identity

Associativity:
    (a + b) + c  =  a + (b + c)
    
This means we can parallelize:
    Thread 1: a + b
    Thread 2: c + d
    Combine:  (a+b) + (c+d)
```

---

## Visual 8: Category Theory Mapping

```
MATHEMATICS                 PROGRAMMING
───────────────────────────────────────
Category C                  Types
  Objects ───────────→       Int, String, User
  Morphisms ─────────→       Functions
  Composition ───────→       f ∘ g

Functor F: C → D            Type Constructor
  F(X) ──────────────→       List<T>, Option<T>
  F(f) ──────────────→       map: (A→B) → F<A>→F<B>

Natural Transformation      Polymorphic function
  η: F ⇒ G ──────────→       toArray: Option<T> → Array<T>
```

---

## Visual 9: The Callback Pyramid vs Functional Chain

```
BEFORE (Pyramid of Doom):
getUser(id, (user) => {
  getPosts(user, (posts) => {
    getComments(posts, (comments) => {
      render(comments, (result) => {
        console.log(result);
      });
    });
  });
});

AFTER (Functional Chain):
getUser(id)
  .flatMap(getPosts)
  .flatMap(getComments)
  .flatMap(render)
  .map(console.log);
```

---

## Visual 10: Type Signatures Decoded

```
map :: (a -> b) -> f a -> f b
       └──┬──┘    └─┬─┘   └─┬─┘
          │         │       │
   Function   Functor   Functor
   to apply    input    output

flatMap :: f a -> (a -> f b) -> f b
          └─┬─┘   └────┬────┘   └─┬─┘
            │          │          │
         Monad    Function    Monad
         input    returning   output
                   Monad
```

---

## Visual 11: Practical Application - Form Validation

```
validateEmail(input)     Result<Email, Error>
    ↓ flatMap
validatePassword(input)  Result<Password, Error>
    ↓ flatMap
validateAge(input)       Result<Age, Error>
    ↓ map
createUser              Result<User, Error>

Error path:
validateEmail("bad")     Error("Invalid email")
    ↓ flatMap               ↓
validatePassword(x)      Error(...) (skipped)
    ↓ flatMap               ↓
validateAge(x)           Error(...) (skipped)
    ↓ map                   ↓
createUser               Error("Invalid email")
```

---

## Visual 12: The Complete Picture

```
┌─────────────────────────────────────────┐
│    FUNCTIONAL PROGRAMMING STACK         │
├─────────────────────────────────────────┤
│                                         │
│  Category Theory (Mathematics)          │
│         ↓                               │
│  Functors, Monads, Monoids             │
│         ↓                               │
│  Type Classes & Laws                    │
│         ↓                               │
│  Programming Patterns                   │
│         ↓                               │
│  Production Code                        │
│                                         │
│  Each layer built on rigor below!       │
└─────────────────────────────────────────┘
```

---

**Document Metadata:**
- **Version**: 1.0
- **Created**: 2026-01-04
- **Format**: ASCII diagrams
- **Companion to**: Professional guide and developer adventure story
- **License**: CC-BY-4.0
