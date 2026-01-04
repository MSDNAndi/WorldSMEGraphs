# Number Theory Learning Examples

> **Purpose**: Worked examples for understanding number theory concepts  
> **Target Audience**: Students and self-learners  
> **Difficulty**: Progressive (Elementary → Advanced)

---

## Example 1: Identifying Primes and Composites

### Problem
Classify each number as prime or composite: 17, 24, 31, 51, 97

### Solution

**17:**
- Divisibility tests: Not divisible by 2, 3, 5, 7, 11, 13
- Need only check up to √17 ≈ 4.1, so test 2, 3
- No divisors found → **17 is PRIME**

**24:**
- Even number → divisible by 2
- 24 = 2 × 12 = 2³ × 3
- Has divisors: 1, 2, 3, 4, 6, 8, 12, 24
- **24 is COMPOSITE**

**31:**
- Not divisible by 2, 3, 5
- Need only check up to √31 ≈ 5.6
- No divisors found → **31 is PRIME**

**51:**
- Not divisible by 2 (odd)
- Sum of digits: 5 + 1 = 6, divisible by 3
- 51 = 3 × 17
- **51 is COMPOSITE**

**97:**
- Check divisibility by primes up to √97 ≈ 9.8
- Test: 2, 3, 5, 7 (all fail)
- **97 is PRIME**

### Key Insight
Only need to test divisibility by primes up to √n

---

## Example 2: Prime Factorization

### Problem
Find the prime factorization of 360

### Solution

**Method 1: Factor Tree**
```
        360
       /   \
      2    180
           /  \
          2   90
              /  \
             2   45
                 /  \
                3   15
                    /  \
                   3   5
```

**Result**: 360 = 2³ × 3² × 5

**Method 2: Division Algorithm**
```
360 ÷ 2 = 180
180 ÷ 2 = 90
90 ÷ 2 = 45
45 ÷ 3 = 15
15 ÷ 3 = 5
5 ÷ 5 = 1
```

**Prime Factorization**: 360 = 2³ × 3² × 5

### Verification
2³ × 3² × 5 = 8 × 9 × 5 = 72 × 5 = 360 ✓

---

## Example 3: Testing for Perfect Numbers

### Problem
Determine if 28 is a perfect number

### Solution

**Step 1**: Find all divisors of 28
- Test each number from 1 to 27:
- Divisors: 1, 2, 4, 7, 14

**Step 2**: Sum the proper divisors
- Proper divisors (exclude 28): 1, 2, 4, 7, 14
- Sum: 1 + 2 + 4 + 7 + 14 = 28

**Step 3**: Compare
- Sum of proper divisors = 28
- 28 = 28 ✓

**Conclusion**: **28 is PERFECT**

### Connection to Mersenne Primes
- 28 = 2²(2³ - 1) = 4 × 7
- 2³ - 1 = 7 (which is prime, M₃)
- Fits Euclid-Euler pattern ✓

---

## Example 4: Verifying Amicable Pairs

### Problem
Verify that 220 and 284 are amicable

### Solution

**For 220:**
- Prime factorization: 220 = 2² × 5 × 11
- Divisors: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
- Sum of proper divisors: 1+2+4+5+10+11+20+22+44+55+110 = **284**

**For 284:**
- Prime factorization: 284 = 2² × 71
- Divisors: 1, 2, 4, 71, 142
- Sum of proper divisors: 1+2+4+71+142 = **220**

**Verification:**
- σ(220) - 220 = 284 ✓
- σ(284) - 284 = 220 ✓

**Conclusion**: **(220, 284) are AMICABLE** ✓

---

## Example 5: Computing Fibonacci Numbers

### Problem
Compute F₀ through F₁₀ and verify golden ratio approximation

### Solution

**Recursive computation:**
```
F₀ = 0
F₁ = 1
F₂ = F₁ + F₀ = 1 + 0 = 1
F₃ = F₂ + F₁ = 1 + 1 = 2
F₄ = F₃ + F₂ = 2 + 1 = 3
F₅ = F₄ + F₃ = 3 + 2 = 5
F₆ = F₅ + F₄ = 5 + 3 = 8
F₇ = F₆ + F₅ = 8 + 5 = 13
F₈ = F₇ + F₆ = 13 + 8 = 21
F₉ = F₈ + F₇ = 21 + 13 = 34
F₁₀ = F₉ + F₈ = 34 + 21 = 55
```

**Sequence**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

**Golden Ratio Convergence:**
```
F₂/F₁ = 1/1 = 1.000
F₃/F₂ = 2/1 = 2.000
F₄/F₃ = 3/2 = 1.500
F₅/F₄ = 5/3 = 1.667
F₆/F₅ = 8/5 = 1.600
F₇/F₆ = 13/8 = 1.625
F₈/F₇ = 21/13 = 1.615
F₉/F₈ = 34/21 = 1.619
F₁₀/F₉ = 55/34 = 1.618
```

**Golden Ratio**: φ = (1 + √5)/2 ≈ 1.618034

**Conclusion**: Ratio converges to φ ✓

---

## Example 6: Lucas-Lehmer Test for Mersenne Prime

### Problem
Use Lucas-Lehmer test to verify M₅ = 31 is prime

### Solution

**Given**: p = 5 (prime), test Mₚ = 2⁵ - 1 = 31

**Lucas-Lehmer Algorithm:**
```
S₀ = 4
S₁ = (S₀² - 2) mod 31 = (16 - 2) mod 31 = 14
S₂ = (S₁² - 2) mod 31 = (196 - 2) mod 31 = 194 mod 31 = 8
S₃ = (S₂² - 2) mod 31 = (64 - 2) mod 31 = 62 mod 31 = 0
```

**We compute p - 2 = 5 - 2 = 3 iterations**

**Result**: S₃ = 0

**Conclusion**: M₅ = 31 is **PRIME** ✓

### Non-Prime Example: M₁₁
```
p = 11, M₁₁ = 2¹¹ - 1 = 2047

S₀ = 4
S₁ = 14 mod 2047
S₂ = 194 mod 2047
S₃ = 788 mod 2047
... (continue for 9 iterations)
S₉ ≠ 0
```

**Conclusion**: M₁₁ is **NOT PRIME**  
(Actually: 2047 = 23 × 89)

---

## Example 7: Gauss Construction Theorem

### Problem
Can you construct a regular 15-gon with compass and straightedge?

### Solution

**Gauss's Theorem**: Regular n-gon is constructible iff  
n = 2^k × p₁ × p₂ × ... × pₘ  
where pᵢ are **distinct** Fermat primes

**Known Fermat primes**: 3, 5, 17, 257, 65537

**For n = 15:**
- Factor: 15 = 3 × 5
- Both 3 and 5 are Fermat primes ✓
- They are distinct ✓
- k = 0 (no factor of 2)

**Form**: 15 = 2⁰ × 3 × 5 ✓

**Conclusion**: **YES**, a regular 15-gon is constructible!

### Non-Constructible Examples

**n = 7:**
- 7 is prime but NOT a Fermat prime
- **NOT constructible**

**n = 9:**
- 9 = 3²
- Fermat prime 3 appears twice (not distinct)
- **NOT constructible**

**n = 11:**
- 11 is prime but NOT a Fermat prime
- **NOT constructible**

---

## Practice Problems

### Elementary Level

1. Determine if 91 is prime or composite
2. Find the prime factorization of 100
3. Compute the first 5 terms of Fibonacci sequence
4. List all divisors of 36

### Intermediate Level

5. Verify that 496 is a perfect number
6. Show that (1184, 1210) are amicable
7. Compute F₁₂/F₁₁ and compare to φ
8. Can you construct a regular 51-gon? Why or why not?

### Advanced Level

9. Use Lucas-Lehmer to test if M₇ = 127 is prime
10. Prove that if 2^n - 1 is prime, then n must be prime
11. Find all perfect numbers less than 10,000
12. Determine if there's a Fermat prime between F₄ and F₅

---

## Solutions to Practice Problems

### Elementary Solutions

**1. Is 91 prime?**
- 91 = 7 × 13
- **COMPOSITE**

**2. Prime factorization of 100**
- 100 = 10² = (2×5)² = 2² × 5²

**3. First 5 Fibonacci terms**
- F₀=0, F₁=1, F₂=1, F₃=2, F₄=3

**4. Divisors of 36**
- 1, 2, 3, 4, 6, 9, 12, 18, 36

### Intermediate Solutions

**5. Is 496 perfect?**
- Proper divisors: 1,2,4,8,16,31,62,124,248
- Sum: 496 ✓ **PERFECT**

**6. Verify (1184, 1210) amicable**
- σ(1184)-1184 = 1210 ✓
- σ(1210)-1210 = 1184 ✓
- **AMICABLE**

**7. F₁₂/F₁₁ vs φ**
- F₁₁ = 89, F₁₂ = 144
- Ratio: 144/89 ≈ 1.6179775
- φ ≈ 1.618034
- Very close! ✓

**8. Regular 51-gon constructible?**
- 51 = 3 × 17
- Both are distinct Fermat primes
- **YES, constructible** ✓

### Advanced Solutions

**9. Lucas-Lehmer for M₇**
- Compute 5 iterations
- Final result: S₅ = 0
- **M₇ = 127 is PRIME** ✓

**10. Proof that 2^n - 1 prime → n prime**
- By contrapositive: if n composite, then 2^n - 1 composite
- If n = ab with a,b > 1, then 2^n - 1 = (2^a)^b - 1
- This factors using x^b - 1 = (x-1)(x^(b-1) + ... + 1)
- Therefore 2^n - 1 is composite
- QED ✓

**11. Perfect numbers < 10,000**
- 6, 28, 496, 8128
- That's all! (Next is 33,550,336)

**12. Fermat prime between F₄ and F₅?**
- F₄ = 65537
- F₅ = 4,294,967,297
- No Fermat numbers exist between consecutive indices
- **NO**

---

**Last Updated**: 2025-12-30  
**Version**: 1.0  
**Maintainer**: math_expert_agent
