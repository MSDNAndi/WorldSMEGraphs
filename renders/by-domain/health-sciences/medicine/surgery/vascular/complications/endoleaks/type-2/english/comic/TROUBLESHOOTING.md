# Troubleshooting Guide - Common Issues & Solutions

## 🔧 Generation Issues

### Issue: "AI_FOUNDRY_API_KEY not found"

**Symptoms:**
- Error when running image generation
- Message about missing API key

**Solution:**
```bash
# Check if keys are set
env | grep AI_FOUNDRY

# If missing, set them:
export AI_FOUNDRY_API_KEY="your-key-here"
export GPT_IMAGE_1DOT5_ENDPOINT_URL="your-endpoint-url"

# Verify:
env | grep AI_FOUNDRY
```

### Issue: "File not found: gpt-prompts.txt"

**Symptoms:**
- Error referencing old prompt file
- Command fails to find input

**Solution:**
```bash
# Make sure you're using V2 prompts:
--prompt-file gpt-prompts-v2-detailed-all-panels.txt

# NOT the old file:
--prompt-file gpt-prompts.txt  # ❌ OLD
```

### Issue: Generation takes forever or hangs

**Symptoms:**
- Process stuck on one panel
- No progress for 5+ minutes

**Solution:**
```bash
# 1. Check internet connection
ping -c 3 google.com

# 2. Check API endpoint accessible
curl -I $GPT_IMAGE_1DOT5_ENDPOINT_URL

# 3. Reduce parallel count if rate limited
--parallel 2  # Instead of 4

# 4. Try single panel first
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt "[paste panel 1 prompt]" \
  --output-dir panels-gpt-v2 \
  --filename image_001_test.png
```

### Issue: "Only generated 28/32 images"

**Symptoms:**
- Process completes but some images missing
- Specific panels failed

**Solution:**
```bash
# 1. Check error logs for failed panels
# Look for panel numbers that failed

# 2. Regenerate missing panels individually
# Extract prompt for missing panel from gpt-prompts-v2-detailed-all-panels.txt
# Run generation for that panel only

# 3. Check if those panels have issues in prompts
# Sometimes very long prompts may timeout
```

## 🎨 Quality Issues

### Issue: Characters look different across panels

**Symptoms:**
- Camila's braid on wrong shoulder
- Vest colors inconsistent
- Patches missing or different

**Cause:**
- Using old (V1) prompts
- AI interpretation variance

**Solution:**
```bash
# 1. Verify using V2 prompts
grep "warm light brown skin (hex #D4A574)" gpt-prompts-v2-detailed-all-panels.txt
# Should show 32 matches (one per panel)

# 2. If using V2 and still inconsistent:
# Regenerate problematic panels:
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt "[paste panel prompt]" \
  --output-dir panels-gpt-v2 \
  --filename image_XXX_retry.png
```

### Issue: Colors don't match specifications

**Symptoms:**
- Teal vest looks blue or green
- Purple backpack looks pink
- Colors washed out

**Solution:**
```bash
# 1. Ensure using --quality high flag
--quality high

# 2. Verify hex codes in prompts
grep "#20B2AA" gpt-prompts-v2-detailed-all-panels.txt  # Teal
grep "#9370DB" gpt-prompts-v2-detailed-all-panels.txt  # Purple

# 3. Regenerate with --enhance flag
--enhance
```

### Issue: Speech bubbles text is wrong or unreadable

**Symptoms:**
- Text doesn't match storyboard
- Font too small
- Text cut off

**Solution:**
```bash
# 1. Check prompts have correct text
grep "Ready to map Type 2 endoleaks" gpt-prompts-v2-detailed-all-panels.txt

# 2. If prompts correct but rendering wrong:
# May need to regenerate with explicit font size adjustment

# 3. Check storyboard.json matches prompts
diff <(jq -r '.[0].dialogue[0].text' storyboard.json) \
     <(grep "Camila.*Ready to map" gpt-prompts-v2-detailed-all-panels.txt)
```

## 📄 PDF Issues

### Issue: PDF build fails

**Symptoms:**
- `build_gpt_pdf.py` throws error
- No PDF file created

**Solution:**
```bash
# 1. Check all 32 images present
ls panels-gpt-v2/*.png | wc -l
# Should show 32

# 2. Check Pillow installed
python3 -c "import PIL; print(PIL.__version__)"

# 3. If missing:
pip install pillow

# 4. Retry PDF build
python build_gpt_pdf.py --input-dir panels-gpt-v2 --output type2-endoleak-comic-v2.pdf
```

### Issue: PDF quality is poor

**Symptoms:**
- Images look pixelated in PDF
- Text unreadable

**Solution:**
```bash
# 1. Check source images are high quality
ls -lh panels-gpt-v2/*.png
# Should be 1-3 MB each

# 2. If images are small (<500KB):
# Regenerate with higher quality
--quality high

# 3. Check PDF settings in build script
# May need to adjust compression settings
```

## 🔄 Update Issues

### Issue: Prompt changes not reflected

**Symptoms:**
- Updated storyboard.json but prompts unchanged
- Images generated with old content

**Solution:**
```bash
# 1. Regenerate prompts after storyboard changes
python generate_detailed_prompts.py

# 2. Verify new prompts generated
ls -lh gpt-prompts-v2-detailed-all-panels.txt
# Check timestamp is recent

# 3. Use new prompts file for generation
--prompt-file gpt-prompts-v2-detailed-all-panels.txt
```

### Issue: Script can't find storyboard.json

**Symptoms:**
- `generate_detailed_prompts.py` fails
- FileNotFoundError

**Solution:**
```bash
# 1. Ensure in correct directory
pwd
# Should end with: .../endoleaks/type-2/english/comic

# 2. Check storyboard.json exists
ls storyboard.json

# 3. If missing or incorrect:
# Restore from git or backup
```

## 🗃️ Archive Issues

### Issue: Can't find original images

**Symptoms:**
- Need to compare with old version
- archive/ directory empty

**Solution:**
```bash
# 1. Check archive structure
ls archive/

# 2. Original images should be in:
ls archive/2026-01-07-original-pr36/*.png | wc -l
# Should show 32

# 3. If missing, may be in git history:
git log --name-only | grep panels-gpt
```

## �� Python Issues

### Issue: Python version too old

**Symptoms:**
- Syntax errors in scripts
- Import failures

**Solution:**
```bash
# 1. Check Python version
python3 --version
# Should be 3.10 or higher

# 2. If too old:
# Use newer Python or virtual environment
python3.10 -m venv venv
source venv/bin/activate
```

### Issue: Module not found

**Symptoms:**
- ImportError: No module named 'PIL'
- ImportError: No module named 'json'

**Solution:**
```bash
# 1. For Pillow (PIL):
pip install pillow

# 2. For json (should be built-in):
python3 -c "import json"
# If fails, Python installation issue

# 3. Check Python installation
which python3
python3 --version
```

## 📝 Documentation Issues

### Issue: Can't find documentation

**Symptoms:**
- Don't know which file to read
- Lost in documentation

**Solution:**
```bash
# 1. Start with main README
cat README.md

# 2. Use INDEX.md for navigation
cat INDEX.md

# 3. Quick start:
cat QUICK-REFERENCE.md

# 4. Complete overview:
cat PROJECT-SUMMARY.md
```

## 🔍 Validation Issues

### Issue: Validation script fails

**Symptoms:**
- `validate_comic.py` throws error
- Unexpected validation failures

**Solution:**
```bash
# 1. Check script expects v2 structure
python validate_comic.py --version v2

# 2. If v1 validation:
python validate_comic.py  # Uses v1 by default

# 3. Manual validation using checklist
cat VALIDATION-CHECKLIST.md
```

## 💾 Storage Issues

### Issue: Out of disk space

**Symptoms:**
- Generation fails partway through
- Can't save new images

**Solution:**
```bash
# 1. Check disk usage
df -h .

# 2. Clean up old/temp files
rm -rf panels-gpt-v2-test/  # If have test directories
rm -f *.tmp

# 3. Archive old versions
mkdir -p archive/old-versions
mv panels-gpt archive/old-versions/
```

## 🌐 Network Issues

### Issue: API timeouts

**Symptoms:**
- Slow generation
- Timeout errors

**Solution:**
```bash
# 1. Check internet speed
ping -c 10 google.com

# 2. Reduce parallel load
--parallel 2  # Instead of 4

# 3. Increase timeout (if script supports)
# May need to modify script

# 4. Try during off-peak hours
# Less API congestion
```

## 📊 Comparison Issues

### Issue: Can't compare V1 vs V2

**Symptoms:**
- Want to see improvements
- Don't have both versions

**Solution:**
```bash
# 1. V1 archived at:
ls archive/2026-01-07-original-pr36/*.png

# 2. V2 generated at:
ls panels-gpt-v2/*.png

# 3. Side-by-side PDFs:
# V1: type2-endoleak-comic-gpt.pdf (or in archive)
# V2: type2-endoleak-comic-v2.pdf

# 4. See metrics:
cat BEFORE-AFTER-COMPARISON.md
```

## 🎯 Character Consistency Deep Dive

### Checklist for Character Issues

**Camila issues:**
```bash
# Braid should be LEFT shoulder (viewer perspective)
# Check panels: 1, 8, 15, 24, 32
# Vest should be teal #20B2AA
# Backpack should be purple #9370DB
# Sunflower patch on RIGHT chest
```

**Camilo issues:**
```bash
# Vest should be green #3CB371
# Backpack should be orange #FFA500
# Topo map patch on RIGHT chest
# Short straight dark hair
```

**Diego issues:**
```bash
# Vest should be orange #FF8C00
# Backpack should be green #90EE90
# Compass patch on RIGHT chest
# Glasses present
# Short curly dark hair
```

## 🆘 Emergency Procedures

### If everything is broken

```bash
# 1. Fresh start - restore from git
git status
git restore .

# 2. Re-pull latest
git pull origin copilot/refactor-image-generation-workflow

# 3. Verify key files present
ls -lh gpt-prompts-v2-detailed-all-panels.txt
ls -lh generate_detailed_prompts.py
ls -lh storyboard.json

# 4. Test with single panel
python .project/agents/image-generation/tools/gpt_image_generator.py \
  --prompt "$(head -100 gpt-prompts-v2-detailed-all-panels.txt)" \
  --output-dir test-output \
  --filename test.png

# 5. If test works, proceed with full generation
```

## 📞 Getting Help

**Still stuck?**
1. Review QUICK-REFERENCE.md
2. Check PROJECT-SUMMARY.md
3. Consult INDEX.md for relevant documentation
4. Review SESSION-COMPLETION-SUMMARY.md for context

**Document the issue:**
1. What command did you run?
2. What error message appeared?
3. What files are present/missing?
4. What's the output of `ls -la` in comic directory?

---

**Last Updated**: 2026-01-07  
**Version**: 2.0
