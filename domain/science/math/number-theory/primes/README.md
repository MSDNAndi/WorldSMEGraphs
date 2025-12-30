# Prime Numbers Domain

**Domain Path**: `science/math/number-theory/primes`  
**Status**: Active  
**AKU Count**: 6  
**Last Updated**: 2025-12-30

## Overview

This domain contains Atomic Knowledge Units (AKUs) about prime numbers and their connections to various disciplines. Prime numbers are fundamental to mathematics and have surprising applications across multiple domains including cryptography, biology, physics, computer science, and economics.

## Domain Structure

```
primes/
├── akus/
│   ├── definitions/          (1 AKU)
│   │   └── aku-001-prime-number-definition.json
│   ├── theory/              (1 AKU)
│   │   └── aku-002-fundamental-theorem-arithmetic.json
│   ├── formulas/            (1 AKU)
│   │   └── aku-003-sieve-eratosthenes.json
│   ├── applications/        (3 AKUs)
│   │   ├── aku-004-primes-cryptography-rsa.json
│   │   ├── aku-005-primes-biology-cicadas.json
│   │   └── aku-006-primes-physics-quantum.json
│   └── examples/            (0 AKUs - future)
├── .renders/
│   └── english/
│       └── (renderings to be created)
├── concept-index.yaml
└── README.md (this file)
```

## Core Concepts

### Foundational
- **Prime Number Definition** (AKU-001): What makes a number prime
- **Fundamental Theorem of Arithmetic** (AKU-002): Unique factorization into primes
- **Sieve of Eratosthenes** (AKU-003): Ancient algorithm for finding primes

### Cross-Domain Applications
- **Cryptography** (AKU-004): RSA encryption and prime factorization
- **Biology** (AKU-005): Periodical cicadas with 13 and 17-year cycles
- **Physics** (AKU-006): Quantum mechanics and prime distribution patterns

## Key Relationships

### Prerequisites
- Natural numbers and basic arithmetic
- Division and divisibility concepts
- Multiplication and factors

### Enables
- RSA cryptography and modern security
- Number theory research
- Computational complexity studies
- Understanding of quantum chaos
- Evolutionary biology insights

### Cross-Domain Connections

1. **Mathematics → Cryptography**
   - Prime factorization difficulty enables RSA encryption
   - Used in HTTPS, SSH, PGP, blockchain

2. **Mathematics → Biology**
   - Periodical cicada life cycles (13, 17 years)
   - Evolutionary strategy to avoid predators
   - Natural selection favoring mathematical properties

3. **Mathematics → Physics**
   - Prime gap statistics match quantum energy level spacing
   - Montgomery-Odlyzko law connecting number theory to quantum mechanics
   - Riemann zeta function zeros correspond to eigenvalues

4. **Mathematics → Computer Science**
   - Primality testing algorithms
   - Computational complexity theory
   - Hash functions and data structures

5. **Mathematics → Economics**
   - Prime-based models for market cycles
   - Cryptographic security for financial systems
   - Digital currency authentication

## Learning Paths

### For Middle/High School Students
1. Start with AKU-001 (Prime Definition)
2. Explore AKU-003 (Sieve of Eratosthenes) - hands-on algorithm
3. Learn AKU-005 (Cicadas) - fascinating real-world connection

### For Undergraduate Math/CS Students
1. AKU-001 (Prime Definition)
2. AKU-002 (Fundamental Theorem)
3. AKU-003 (Sieve of Eratosthenes)
4. AKU-004 (RSA Cryptography)

### For Advanced/Graduate Students
1. All foundational AKUs (001-003)
2. AKU-004 (RSA Cryptography)
3. AKU-006 (Quantum Mechanics Connection)
4. Pursue connections to analytic number theory

### For General Public
1. AKU-001 (Basic definition with intuitive explanation)
2. AKU-005 (Cicadas - accessible and fascinating)
3. AKU-004 (Cryptography - practical relevance)

## Research Directions

### Open Questions
- Are there infinitely many twin primes? (Twin Prime Conjecture)
- Are there infinitely many Mersenne primes?
- What is the largest prime gap?
- Can we find a formula that generates all primes?

### Active Research Areas
- Prime distribution and the Riemann Hypothesis
- Connections between primes and quantum mechanics
- Efficient factorization algorithms
- Post-quantum cryptography alternatives

## Historical Context

- **~300 BCE**: Euclid proves infinitely many primes exist
- **~240 BCE**: Eratosthenes develops his sieve algorithm
- **1801**: Gauss proves Fundamental Theorem of Arithmetic
- **1859**: Riemann connects prime distribution to complex analysis
- **1973**: Montgomery discovers prime-quantum connection
- **1978**: RSA algorithm published
- **1999**: Berry-Keating conjecture on quantum primes

## Educational Resources

### Visualizations Needed
- Number line with primes highlighted
- Sieve of Eratosthenes animation
- Prime gap distribution graphs
- RSA key generation flowchart
- Cicada emergence timeline
- Quantum correlation plots

### Interactive Tools
- Prime number checker
- Sieve of Eratosthenes simulator
- RSA encryption/decryption demo
- Prime gap explorer

## Contributing

To add AKUs to this domain:
1. Follow the AKU format specification (v2)
2. Use appropriate subdirectories (definitions, theory, formulas, examples, applications)
3. Validate using `validate_aku_v2.py --domain science/math`
4. Update concept-index.yaml
5. Cross-reference related AKUs
6. Include proper provenance and sources

## Standards and References

### Mathematical Standards
- Hardy & Wright: "An Introduction to the Theory of Numbers"
- Apostol: "Introduction to Analytic Number Theory"
- Knuth: "The Art of Computer Programming, Vol 2"

### Cryptography Standards
- NIST guidelines for RSA key sizes
- RSA Security recommendations

### Biology Research
- Yoshimura's work on cicada evolution
- Cox & Carlton on paleoclimatic influences

### Physics Research
- Montgomery-Odlyzko correlation
- Berry-Keating conjecture

## Status

- **Phase**: Initial pilot complete
- **Coverage**: Foundational concepts and major cross-domain applications
- **Next Steps**: 
  - Add more example AKUs
  - Create renderings for different audiences
  - Add more cross-domain connections (economics, engineering)
  - Develop visualization tools

## Contact

For questions or contributions to this domain, please refer to the main project documentation.

---

**Last Updated**: 2025-12-30  
**Maintained By**: Math Expert Agent, Number Theory Knowledge Base
