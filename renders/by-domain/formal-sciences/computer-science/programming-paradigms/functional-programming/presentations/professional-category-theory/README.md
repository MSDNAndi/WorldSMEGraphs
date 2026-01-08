# Professional Category Theory Presentation for .NET Developers

> **Status**: Example storyboard demonstrating workflow-compliant content creation  
> **Created**: 2026-01-08  
> **Purpose**: Demonstrate proper workflow order (Storyboard → Prompts → Images → Documents)

## Workflow Status

- [x] Phase 1-2: Storyboard created
- [ ] Phase 3: Complete prompts (next step)
- [ ] Phase 4: Images generated
- [ ] Phase 5: Final documents created
- [ ] Phase 6: Archive management (when replacing versions)

## Presentation Overview

**Title**: Category Theory for .NET Developers  
**Subtitle**: Understanding Functors in C# and F#  
**Target Audience**: Professional developers with C#/F# background  
**Duration**: 15-20 minutes (2-slide example)  
**Style**: Professional, Microsoft ecosystem aligned

## Educational Objectives

1. Establish that category theory is practical, not purely theoretical
2. Show developers already use functors (LINQ Select)
3. Provide concrete examples in C# and F#

## Current Status

This is an **example storyboard** demonstrating the proper workflow order.

### Completed

✅ **Phase 1-2: Storyboard** (`storyboard.yaml`)
- 2 slides defined with educational goals
- Visual descriptions provided
- Content structured for professional audience

### Next Steps

To complete this example following proper workflow:

1. **Phase 3: Write Complete Prompts**
   ```bash
   mkdir prompts
   # Create prompt-slide-01.txt (8K-20K characters)
   # Create prompt-slide-02.txt (8K-20K characters)
   # NO placeholders, super explicit directions
   
   # Validate prompts
   python .project/agents/image-generation/tools/validate_prompts.py prompts/
   ```

2. **Phase 4: Generate Images**
   ```bash
   mkdir images
   
   # Generate all images
   python .project/agents/image-generation/tools/gpt_image_generator.py \
     --prompt-file prompts/prompt-slide-01.txt \
     --output-dir images/ \
     --aspect landscape --quality high --output-prefix slide_01
   
   python .project/agents/image-generation/tools/gpt_image_generator.py \
     --prompt-file prompts/prompt-slide-02.txt \
     --output-dir images/ \
     --aspect landscape --quality high --output-prefix slide_02
   
   # Validate workflow
   python .project/agents/image-generation/tools/validate_workflow.py .
   ```

3. **Phase 5: Create Documents**
   ```bash
   # Only after images exist!
   python .project/agents/image-generation/tools/presentation_generator.py \
     --slides storyboard.yaml \
     --image-dir images/ \
     --output professional-category-theory
   
   # Generates:
   # - professional-category-theory.pptx
   # - professional-category-theory.pdf
   ```

## Workflow Validation

Before creating final documents, always validate:

```bash
# Check workflow order
python .project/agents/image-generation/tools/validate_workflow.py .

# Should show:
# ✅ Phase 1-2: Storyboard exists
# ✅ Phase 3: Prompts complete (no placeholders)
# ✅ Phase 4: Images generated
# ✅ Phase 5: Ready to create documents
```

## Why This Example?

This demonstrates the **correct workflow order** learned from PR #36 and PR #38:

1. **Storyboard First**: Define what you want to create
2. **Complete Prompts**: Write full, explicit prompts (no placeholders)
3. **Generate Images**: Create ALL images before ANY documents
4. **Create Documents**: Use pre-generated images

**Key Rule**: Images MUST be generated BEFORE creating final documents.

## References

- **Workflow Guide**: `.project/agents/image-generation/WORKFLOW-ENFORCEMENT.md`
- **Quick Start**: `.project/agents/image-generation/QUICK-START.md`
- **Tools**: `.project/agents/image-generation/tools/README.md`

## See Also

- PR #36: Original comic generation with lessons learned
- PR #38: Improved workflow with hyper-detailed prompts
- This example: Demonstrates workflow compliance from start

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-08 | Initial example storyboard |
