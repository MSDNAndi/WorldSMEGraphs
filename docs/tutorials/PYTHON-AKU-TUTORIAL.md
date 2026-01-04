# Python Tutorial: Working with AKUs

> **Purpose**: Learn how to create, read, and validate Atomic Knowledge Units (AKUs) using Python  
> **Audience**: Python developers contributing to WorldSMEGraphs  
> **Prerequisites**: Basic Python knowledge, understanding of JSON  
> **Estimated Time**: 30 minutes

## Table of Contents
1. [Introduction](#introduction)
2. [Reading AKUs](#reading-akus)
3. [Creating AKUs](#creating-akus)
4. [Validating AKUs](#validating-akus)
5. [Batch Processing](#batch-processing)
6. [Best Practices](#best-practices)
7. [Common Patterns](#common-patterns)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

Atomic Knowledge Units (AKUs) are JSON files containing structured knowledge. This tutorial shows you how to work with them programmatically in Python.

### AKU Structure Overview

```json
{
  "@context": "aku-v2",
  "@type": "definition",
  "@id": "unique-identifier",
  "metadata": { ... },
  "classification": {
    "domain_path": "formal-sciences/mathematics/...",
    ...
  },
  "content": { ... }
}
```

---

## Reading AKUs

### Basic Reading

```python
import json
from pathlib import Path

def read_aku(filepath):
    """Read an AKU file and return parsed JSON."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# Example usage
aku_path = Path("domain/formal-sciences/mathematics/.../aku-001.json")
aku = read_aku(aku_path)

print(f"AKU ID: {aku['@id']}")
print(f"Type: {aku['@type']}")
print(f"Domain: {aku['classification']['domain_path']}")
```

For full content, see the complete tutorial file.
