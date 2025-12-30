# Number Theory Quick Reference Guide

> **Purpose**: Quick lookup for number theory concepts in this repository  
> **Last Updated**: 2025-12-30  
> **Total Concepts**: 7 subdomains, 16 AKUs

---

## Concept Quick Lookup

### Prime Numbers
- **Path**: `domain/science/math/number-theory/primes/`
- **Definition**: Natural number > 1 with exactly two divisors (1 and itself)
- **Examples**: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...
- **Key Property**: Infinitely many exist (Euclid's proof)
- **10 AKUs**: Definition, Fundamental Theorem, Sieve, RSA crypto, Cicadas, Quantum, Distribution, Twin primes, CS applications, Economics

### Composite Numbers
- **Path**: `domain/science/math/number-theory/composite-numbers/`
- **Definition**: Natural number > 1 with at least one divisor other than 1 and itself
- **Examples**: 4, 6, 8, 9, 10, 12, 14, 15, 16, 18...
- **Key Property**: Can be factored into primes (unique factorization)
- **1 AKU**: Definition and properties

### Perfect Numbers
- **Path**: `domain/science/math/number-theory/perfect-numbers/`
- **Definition**: Equals sum of its proper divisors
- **Examples**: 6, 28, 496, 8128, 33550336
- **Key Property**: Every even perfect ↔ unique Mersenne prime (Euclid-Euler)
- **Known Count**: 51 (all even)
- **Open Problem**: Do odd perfect numbers exist?
- **1 AKU**: Definition and Euclid-Euler theorem

### Mersenne Primes
- **Path**: `domain/science/math/number-theory/mersenne-primes/`
- **Definition**: Prime of form 2^p - 1 where p is prime
- **Examples**: M₂=3, M₃=7, M₅=31, M₇=127, M₁₃=8191
- **Key Property**: Largest known primes (efficient Lucas-Lehmer test)
- **Known Count**: 51
- **Largest**: 2^82589933 - 1 (24.8 million digits, 2018)
- **Connection**: Every even perfect number arises from a Mersenne prime
- **1 AKU**: Definition, Lucas-Lehmer, GIMPS

### Fermat Primes
- **Path**: `domain/science/math/number-theory/fermat-primes/`
- **Definition**: Prime of form 2^(2^n) + 1
- **Examples**: F₀=3, F₁=5, F₂=17, F₃=257, F₄=65537
- **Key Property**: Only 5 known; likely no more exist
- **Famous Counterexample**: F₅ = 641 × 6700417 (disproved Fermat's conjecture)
- **Geometric Connection**: Gauss proved regular n-gons constructible iff n = 2^k × product of distinct Fermat primes
- **1 AKU**: Definition, Gauss construction theorem

### Fibonacci Sequence
- **Path**: `domain/science/math/number-theory/fibonacci/`
- **Definition**: F₀=0, F₁=1, Fₙ=Fₙ₋₁+Fₙ₋₂
- **Sequence**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
- **Key Property**: Ratio Fₙ₊₁/Fₙ → φ (golden ratio ≈ 1.618)
- **Binet's Formula**: Fₙ = (φⁿ - ψⁿ)/√5
- **Applications**: Nature (phyllotaxis), recursion, algorithm analysis
- **1 AKU**: Definition, golden ratio, applications

### Amicable Numbers
- **Path**: `domain/science/math/number-theory/amicable-numbers/`
- **Definition**: Pair (m,n) where σ(m)-m=n and σ(n)-n=m
- **Smallest Pair**: (220, 284) - known to Pythagoreans
- **Key Property**: Generalization of perfect numbers (self-amicable → mutually amicable)
- **Known Count**: Over 12 million pairs
- **Open Problem**: Do odd amicable pairs exist?
- **1 AKU**: Definition, Thābit's rule, examples

---

## Quick Formula Reference

### Divisor Functions
```
σ(n) = sum of all divisors of n
s(n) = σ(n) - n = sum of proper divisors of n
```

### Perfect Number
```
σ(n) - n = n
⟺ σ(n) = 2n
```

### Amicable Pair
```
σ(m) - m = n  AND  σ(n) - n = m
```

### Euclid-Euler Theorem
```
n is even perfect ⟺ n = 2^(p-1) × (2^p - 1)
where 2^p - 1 is a Mersenne prime
```

### Fibonacci
```
Recursive: Fₙ = Fₙ₋₁ + Fₙ₋₂
Closed-form (Binet): Fₙ = (φⁿ - ψⁿ)/√5
where φ = (1+√5)/2, ψ = (1-√5)/2
```

### Gauss Construction Theorem
```
Regular n-gon is constructible with compass and straightedge
⟺ n = 2^k × p₁ × p₂ × ... × pₘ
where pᵢ are distinct Fermat primes
```

---

## Testing for Special Properties

### Is n Prime?
```python
# Trial division (simple)
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True
```

### Is Mₚ a Mersenne Prime? (Lucas-Lehmer Test)
```python
def lucas_lehmer(p):
    """Test if Mp = 2^p - 1 is prime (p must be prime)"""
    if p == 2: return True
    Mp = 2**p - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % Mp
    return s == 0
```

### Is n Perfect?
```python
def is_perfect(n):
    """Test if n equals sum of its proper divisors"""
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n
```

### Compute Fibonacci
```python
# Iterative (efficient)
def fibonacci(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```

---

## Common Confusions

### ❌ Common Mistakes

1. **"1 is prime"** → NO, 1 has only one divisor
2. **"All Mersenne numbers are prime"** → NO, M₁₁ = 2047 = 23 × 89
3. **"If 2^n - 1 is prime, then n is prime"** → TRUE (necessary condition)
4. **"If n is prime, then 2^n - 1 is prime"** → FALSE (not sufficient)
5. **"All Fermat numbers are prime"** → NO, only F₀...F₄ are prime
6. **"Perfect numbers are common"** → NO, only 51 known
7. **"Fibonacci grows linearly"** → NO, exponential (≈ φⁿ)

### ✅ Key Facts to Remember

1. **Primes and composites partition ℕ \ {1}** (exactly)
2. **Every even perfect ↔ unique Mersenne prime** (bijection)
3. **Only 5 Fermat primes known** (likely all that exist)
4. **51 Mersenne primes = 51 perfect numbers** (as of 2024)
5. **Fibonacci ratio → golden ratio** (as n → ∞)
6. **No odd perfect numbers found** (if exist, > 10^1500)
7. **No odd amicable pairs found** (if exist, > 10^500)

---

## Validation Commands

```bash
# Validate a single AKU
python .project/agents/quality-assurance/tools/validate_aku_v2.py <path-to-aku.json>

# Validate all AKUs in number theory
python .project/agents/quality-assurance/tools/validate_aku_v2.py --directory domain/science/math/number-theory/

# Check project structure
bash .github/scripts/validate-structure.sh
```

---

## File Organization Pattern

Each subdomain follows this structure:
```
<concept-name>/
├── README.md                      # Overview and key info
├── concept-index.yaml             # Learning paths and relationships
├── RELATIONSHIPS.md (optional)    # Detailed relationship documentation
└── akus/
    ├── definitions/
    │   └── aku-001-<name>.json
    ├── theory/
    │   └── aku-00X-<name>.json
    ├── formulas/
    │   └── aku-00X-<name>.json
    └── applications/
        └── aku-00X-<name>.json
```

---

## Related Documentation

- **Domain Overview**: `domain/science/math/number-theory/README.md`
- **Relationships Map**: `domain/science/math/number-theory/RELATIONSHIPS.md`
- **AKU Creation Guide**: `docs/NEW-AKU-CREATION-GUIDE.md`
- **Validation Tools**: `.project/agents/quality-assurance/tools/`
- **Contributing Guide**: `docs/CONTRIBUTING.md`

---

## Historical Timeline

| Year | Event |
|------|-------|
| ~300 BCE | Euclid: Primes infinite, perfect number theorem |
| ~500 BCE | Pythagoreans: Amicable pair (220, 284) |
| 1202 | Fibonacci introduces sequence to Europe |
| 1640 | Fermat's (incorrect) conjecture |
| 1732 | Euler disproves Fermat, factors F₅ |
| 1747 | Euler completes Euclid-Euler theorem |
| 1796 | Gauss (age 19): 17-gon constructible |
| 1866 | Paganini (age 16): (1184, 1210) amicable |
| 1996 | GIMPS begins Mersenne prime search |
| 2018 | Largest prime: 2^82589933 - 1 discovered |

---

**Version**: 1.0  
**Maintainer**: math_expert_agent  
**Last Review**: 2025-12-30
