# Golden Ratio Quick Reference

> **Model**: Claude 3.5 Sonnet (claude-3-5-sonnet-20241022)  
> **Purpose**: Quick lookup for golden ratio concepts  
> **Last Updated**: 2025-12-30

---

## The Golden Ratio (φ)

**φ = (1 + √5)/2 ≈ 1.618033988...**

### Defining Property
```
φ² = φ + 1
```

This unique equation makes φ the only positive number where squaring it equals adding 1.

### Exact Value
```
φ = (1 + √5)/2
```

### Decimal
```
1.618033988749894848204586834365638117720309179805...
```

---

## Key Formulas

### Golden Angle
```
θ = 360°(1 - 1/φ) = 360°/φ² ≈ 137.508°
```

Used in plant phyllotaxis for optimal packing.

### Golden Rectangle
```
For rectangle with width w:
height h = φw

Removing square of side w leaves rectangle:
(φw - w) × w with ratio φ
```

### Golden Spiral
```
Polar form: r = ae^(bθ)
where b = (2/π)ln(φ) ≈ 0.306

Growth property: r(θ + π/2) = φ·r(θ)
```

### Fibonacci Connection
```
lim (Fₙ₊₁/Fₙ) = φ as n → ∞
n→∞

Binet's formula: Fₙ = (φⁿ - ψⁿ)/√5
where ψ = (1 - √5)/2 ≈ -0.618
```

---

## Quick Facts

### Mathematical Properties
- **Most irrational**: Continued fraction [1; 1, 1, 1, ...] 
- **Reciprocal**: 1/φ = φ - 1 ≈ 0.618
- **Conjugate**: ψ = (1 - √5)/2 ≈ -0.618
- **Product**: φ × ψ = -1
- **Sum**: φ + ψ = 1

### Verified in Nature ✓
- **Sunflowers**: Seeds at ~137.5° intervals
- **Pinecones**: Fibonacci spiral patterns (5/8, 8/13)
- **Romanesco**: Fractal Fibonacci spirals
- **Leaves**: Divergence angles in many species

### Common Myths ✗
- **Nautilus shell**: FALSE (ratio ~1.33, not 1.618)
- **Parthenon**: WEAK EVIDENCE (measurements vary)
- **Mona Lisa**: NO EVIDENCE (retrospective fitting)
- **Great Pyramids**: COINCIDENTAL (no historical basis)
- **Human body**: NO CORRELATION (scientific studies)

---

## Python Code

### Calculate φ
```python
import math

# Method 1: Direct formula
phi = (1 + math.sqrt(5)) / 2
print(f"φ = {phi}")  # 1.618033988749895

# Method 2: From quadratic equation
# φ² - φ - 1 = 0
# φ = (1 ± √5) / 2
```

### Generate Fibonacci and Show Convergence
```python
def fibonacci_to_phi(n):
    """Show Fibonacci ratios converging to φ"""
    a, b = 0, 1
    phi = (1 + 5**0.5) / 2
    
    for i in range(1, n+1):
        a, b = b, a + b
        if a > 0:
            ratio = b / a
            error = abs(ratio - phi)
            print(f"F{i+1}/F{i} = {b}/{a} = {ratio:.10f}, error = {error:.2e}")

fibonacci_to_phi(15)
```

### Check if Rectangle is Golden
```python
def is_golden_rectangle(width, height, tolerance=0.01):
    """Check if rectangle approximates golden ratio"""
    phi = (1 + 5**0.5) / 2
    ratio = max(width, height) / min(width, height)
    return abs(ratio - phi) < tolerance

# Test
print(is_golden_rectangle(1, 1.618))  # True
print(is_golden_rectangle(1, 1.5))    # False
```

### Golden Spiral Points
```python
import math

def golden_spiral_points(n_points=100, a=1):
    """Generate points on golden spiral"""
    phi = (1 + 5**0.5) / 2
    b = (2/math.pi) * math.log(phi)
    
    points = []
    for i in range(n_points):
        theta = i * math.pi / 10  # Angle increment
        r = a * math.exp(b * theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    
    return points
```

---

## Common Calculations

### From Width to Height (Golden Rectangle)
```
width = 10 cm
height = 10 × φ = 10 × 1.618 = 16.18 cm
```

### From Height to Width
```
height = 20 cm
width = 20 / φ = 20 / 1.618 = 12.36 cm
```

### Golden Angle in Degrees
```
360° × (1 - 1/1.618) = 360° × 0.382 = 137.5°
```

### Golden Angle in Radians
```
2π × (1 - 1/φ) = 2π × 0.382 = 2.399 radians
```

---

## Quick Comparisons

### φ vs Other Constants
| Constant | Symbol | Value | Type |
|----------|--------|-------|------|
| Pi | π | 3.14159... | Transcendental |
| e | e | 2.71828... | Transcendental |
| **Golden Ratio** | **φ** | **1.61803...** | **Algebraic** |
| √2 | √2 | 1.41421... | Algebraic |
| √3 | √3 | 1.73205... | Algebraic |

### Rectangle Ratios
| Type | Ratio | Decimal |
|------|-------|---------|
| Square | 1:1 | 1.000 |
| **Golden** | **φ:1** | **1.618** |
| HD/4:3 | 4:3 | 1.333 |
| HD/16:9 | 16:9 | 1.778 |
| Credit Card | varies | ~1.586 |

---

## Historical Timeline

| Year | Event |
|------|-------|
| ~300 BCE | Euclid: "Extreme and mean ratio" (Elements, Book VI) |
| 1509 | Pacioli: "De Divina Proportione" (divine proportion) |
| 1876 | Fechner: First psychological study of rectangle preferences |
| 1917 | Thompson: "On Growth and Form" (φ in biology) |
| 1948 | Le Corbusier: Modulor system (architecture) |
| 1979 | Vogel: Mathematical model of sunflower phyllotaxis |
| 1992 | Markowsky: Systematic debunking of myths |
| 2002 | Livio: "The Golden Ratio" (comprehensive critical analysis) |

---

## 5-Minute Summary

**What is it?**  
φ ≈ 1.618, the only number where φ² = φ + 1

**Why special?**  
- Most irrational number (hardest to approximate)
- Limit of Fibonacci ratios
- Optimizes packing (golden angle in plants)

**Where it appears:**  
✓ Math (Fibonacci, continued fractions)  
✓ Nature (sunflowers, pinecones - golden angle ~137.5°)  
✓ Some art/architecture (Le Corbusier's Modulor)

**Common myths:**  
✗ NOT in nautilus shells (wrong ratio)  
✗ NOT in Parthenon (measurements don't match)  
✗ NOT universal in human body  
✗ Doesn't guarantee beauty

**Key insight:**  
Nature uses golden angle because φ is "most irrational" - avoids resonance patterns, optimizes spacing. Not mystical, just good engineering selected by evolution.

---

## See Also
- **[Golden Ratio README](../domain/science/math/geometry/golden-ratio/README.md)** - Full domain documentation
- **[Fibonacci Sequence](../domain/science/math/number-theory/fibonacci/README.md)** - Fibonacci convergence to φ
- **[Number Theory Overview](../domain/science/math/number-theory/README.md)** - Related mathematical concepts

---

**Version**: 1.0  
**Maintained by**: Claude 3.5 Sonnet, math-expert-agent  
**Last Review**: 2025-12-30
