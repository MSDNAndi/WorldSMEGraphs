# Issue and Improvement Tracking System

> **Last Updated**: 2026-01-04  
> **Purpose**: Scalable tracking system for issues and improvements

## Directory Structure

```
.project/tracking/
├── README.md                    # This file
├── archived/                    # Completed/resolved items (by year-month)
│   ├── 2025-12/                # December 2025 completed items
│   │   ├── issues-resolved.md  # Resolved issues
│   │   └── improvements-completed.md  # Completed improvements
│   └── 2026-01/                # January 2026 completed items
│       └── ...
└── (links to main tracking files)
```

## Active Tracking Files

- **Open Issues**: `../.project/issues.md` → Contains only OPEN issues
- **Open Improvements**: `../.project/improvements.md` → Contains only OPEN improvements

## Archival Process

### When to Archive
1. When an issue is marked ✅ Resolved
2. When an improvement is marked ✅ Completed
3. During monthly reviews

### How to Archive
1. Move the resolved/completed entry to the appropriate archived file
2. Organize by year-month folder (e.g., `archived/2026-01/`)
3. Keep a summary reference in the main file with link to archived entry

## Scalability Design

This structure scales because:
1. **Active files stay small**: Only open items in main files
2. **Historical items organized by date**: Easy to find past resolutions
3. **Clear separation**: Active vs completed work
4. **Searchable archives**: Git-tracked history

## File Templates

### Archived Issue Entry
```markdown
### ✅ Issue #X: [Title]
**Resolved**: [Date]  
**Original Created**: [Date]  
**Resolution Summary**: [Brief description]
**Artifacts**: [Links to deliverables]
**Archived From**: issues.md
```

### Archived Improvement Entry
```markdown
### ✅ IMP-XXX: [Title]
**Completed**: [Date]  
**Original Created**: [Date]  
**Completion Summary**: [Brief description]
**Artifacts**: [Links to deliverables]
**Archived From**: improvements.md
```
