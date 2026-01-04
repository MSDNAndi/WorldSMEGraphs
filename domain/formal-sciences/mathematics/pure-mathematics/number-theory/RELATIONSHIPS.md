# Number Theory Concept Relationships

## Visual Relationship Map

```
                            ┌──────────────────┐
                            │  Natural Numbers │
                            └────────┬─────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
          ┌─────────▼──────────┐          ┌──────────▼────────┐
          │  Prime Numbers (10) │          │  Composite Numbers │
          └─────────┬──────────┘          └───────────────────┘
                    │                              │
      ┌─────────────┼─────────────┐                │
      │             │             │                │
┌─────▼─────┐ ┌────▼────┐  ┌────▼──────┐         │
│ Mersenne  │ │ Fermat  │  │ Fibonacci │         │
│ Primes    │ │ Primes  │  │ Sequence  │         │
│ (2^p-1)   │ │(2^2^n+1)│  │ (Fn=Fn-1+ │         │
│           │ │         │  │  Fn-2)    │         │
│ Only 51   │ │ Only 5  │  └───────────┘         │
│ known     │ │ known   │                        │
└─────┬─────┘ └────┬────┘                        │
      │            │                              │
      │            │                              │
  ┌───▼────────────▼──┐                          │
  │                   │                          │
  │  Perfect Numbers  │◄─────────────────────────┘
  │  (σ(n)-n = n)    │    (All perfect > 6
  │                   │     are composite)
  │  51 known         │
  │  (connected to    │
  │   Mersenne via    │
  │   Euclid-Euler)   │
  └─────────┬─────────┘
            │
            │ (generalization)
            │
     ┌──────▼────────┐
     │   Amicable    │
     │   Numbers     │
     │ (σ(m)-m = n)  │
     │ (σ(n)-n = m)  │
     │               │
     │ 12M+ pairs    │
     │ known         │
     └───────────────┘
```

## Fundamental Relationships

### 1. Primes ↔ Composites (Partition)
- **Type**: Complementary partition
- **Rule**: Every natural number n > 1 is either prime OR composite
- **Connection**: Together they exhaust ℕ \ {1}

### 2. Primes → Perfect Numbers (via Mersenne)
- **Type**: Generation via Euclid-Euler theorem
- **Rule**: If 2^p - 1 is prime (Mersenne), then 2^(p-1) × (2^p - 1) is perfect
- **Consequence**: Every even perfect ↔ unique Mersenne prime (bijection)

### 3. Mersenne Primes ↔ Perfect Numbers (Bijection)
- **Type**: One-to-one correspondence
- **Euclid's part** (~300 BCE): Mersenne prime → even perfect number
- **Euler's part** (1747): Even perfect number → Mersenne prime
- **Result**: 51 Mersenne primes = 51 even perfect numbers

### 4. Perfect Numbers → Amicable Numbers (Generalization)
- **Type**: Conceptual generalization
- **Perfect**: σ(n) - n = n (self-referential)
- **Amicable**: σ(m) - m = n AND σ(n) - n = m (mutual)
- **Pattern**: Self-amicable → mutually amicable → sociable (chains)

### 5. Fermat Primes → Constructible Polygons (Gauss)
- **Type**: Geometric application
- **Gauss's Theorem** (1796): Regular n-gon constructible ⟺ n = 2^k × p₁ × ... × pₘ
  where pᵢ are **distinct** Fermat primes
- **Examples**: 3, 5, 17, 257, 65537-gons are constructible
- **Non-examples**: 7, 9, 11, 13-gons are NOT constructible

### 6. Fibonacci → Golden Ratio (Limit)
- **Type**: Asymptotic convergence
- **Rule**: lim(n→∞) Fₙ₊₁/Fₙ = φ = (1+√5)/2 ≈ 1.618
- **Binet's Formula**: Fₙ = (φⁿ - ψⁿ)/√5 (closed form using irrational φ, ψ)

### 7. Fibonacci ∩ Primes = Fibonacci Primes
- **Type**: Intersection
- **Examples**: F₃=2, F₄=3, F₅=5, F₇=13, F₁₁=89, F₁₃=233
- **Note**: If Fₙ is prime, n must be prime (except F₄=3 where n=4)

## Cross-Domain Applications

### Cryptography
- **Primes**: RSA encryption (factoring problem)
- **Mersenne Primes**: Large primes for crypto
- **Fermat Primes**: F₄=65537 common RSA exponent

### Biology
- **Primes**: Cicada 13 and 17-year life cycles
- **Fibonacci**: Phyllotaxis (plant spirals), seed patterns

### Physics
- **Primes**: Quantum chaos (prime gap statistics)

### Computer Science
- **Primes**: Hash table sizing (coprimality)
- **Fibonacci**: Recursion examples, algorithm analysis
- **Mersenne**: GIMPS distributed computing

### Geometry
- **Fermat Primes**: Constructible regular polygons

### Economics
- **Primes**: Cryptocurrency security

## Open Problems Network

### Connected Open Problems
1. **Infinitely many primes?** ✅ SOLVED (Euclid, ~300 BCE)
2. **Infinitely many twin primes?** ⚠️ UNSOLVED
3. **Infinitely many Mersenne primes?** ⚠️ UNSOLVED (likely yes)
4. **Infinitely many Fermat primes?** ⚠️ UNSOLVED (likely no - only 5)
5. **Infinitely many perfect numbers?** ⚠️ UNSOLVED (tied to Mersenne)
6. **Do odd perfect numbers exist?** ⚠️ UNSOLVED (if yes, > 10^1500)
7. **Do odd amicable pairs exist?** ⚠️ UNSOLVED (if yes, > 10^500)
8. **Infinitely many Fibonacci primes?** ⚠️ UNSOLVED

### Problem Dependencies
- Perfect numbers ⇄ Mersenne primes (same question due to bijection)
- Twin primes ← Prime gaps
- Fibonacci primes ← Fibonacci + Primes

## Historical Timeline

```
~300 BCE    Euclid: Primes infinite, perfect number theorem
~500 BCE    Pythagoreans: Amicable pairs (220, 284)
~300 BCE    Euclid: Fundamental Theorem of Arithmetic
1202 CE     Fibonacci: Introduces sequence to Europe
1640        Fermat: (Incorrect) conjecture about Fermat numbers
1732        Euler: Disproves Fermat, factors F₅
1747        Euler: Completes Euclid-Euler theorem (perfects ↔ Mersenne)
1796        Gauss (age 19): Proves 17-gon constructible
1850        Lucas: Lucas-Lehmer test foundations
1866        Paganini (age 16): Discovers (1184, 1210) amicable pair
1930        Lehmer: Refines Lucas-Lehmer test
1996-now    GIMPS: Distributed Mersenne prime search
```

## Summary Statistics

| Concept | Known Count | Growth Pattern | Computational Difficulty |
|---------|-------------|----------------|-------------------------|
| Primes | Infinite | ~x/ln(x) | Testing: Easy (AKS); Finding next: Moderate |
| Composites | Infinite | Complement of primes | Factoring: Hard (NP?) |
| Perfect Numbers | 51 (even only) | Tied to Mersenne | Testing: Easy via Mersenne |
| Mersenne Primes | 51 | Unknown, sparse | Testing: Easy (Lucas-Lehmer) |
| Fermat Primes | 5 (likely all) | Extremely sparse | Testing: Moderate (Pépin) |
| Fibonacci Numbers | Infinite | Exponential (φⁿ) | Computing: Easy (iterative) |
| Fibonacci Primes | Unknown count | Unknown | Testing: Standard primality |
| Amicable Pairs | 12 million+ | Unknown | Finding: Moderate |

## Key Insights

1. **Rarity Spectrum**: Fermat primes (5) < Mersenne primes (51) < Perfect numbers (51) ≪ Primes (∞)

2. **Computational Ease**: Mersenne primes are easiest large primes to find (Lucas-Lehmer test)

3. **Ancient to Modern**: Some concepts span 2500+ years (primes, perfect, amicable)

4. **Cross-Domain Rich**: Number theory connects to geometry, physics, biology, CS, cryptography

5. **Open Problem Dense**: 7 major unsolved problems in just these concepts

6. **Elegant Connections**: Euclid-Euler theorem, Gauss construction theorem, Binet's formula

Last Updated: 2025-12-30
