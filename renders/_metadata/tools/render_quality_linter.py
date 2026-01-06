#!/usr/bin/env python3
"""
Render Quality Linter

Checks rendered content for quality issues:
- Readability scores
- Missing metadata
- Broken references
- Accessibility issues
- Audience compliance

Usage:
    python render_quality_linter.py [path]
    python render_quality_linter.py renders/by-domain/natural-sciences/physics/
"""

import os
import re
import sys
import yaml
from collections import defaultdict

class RenderLinter:
    def __init__(self):
        self.issues = defaultdict(list)
        self.warnings = defaultdict(list)
        self.stats = {'files_checked': 0, 'issues': 0, 'warnings': 0}
    
    def lint_file(self, filepath):
        """Lint a single render file."""
        self.stats['files_checked'] += 1
        filename = os.path.basename(filepath)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except (IOError, UnicodeDecodeError) as e:
            self.issues[filepath].append(f"Cannot read file: {e}")
            return
        
        # Check file naming
        self._check_filename(filepath, filename)
        
        # Check content
        self._check_readability(filepath, content)
        self._check_metadata(filepath, content)
        self._check_headings(filepath, content)
        self._check_images(filepath, content)
        self._check_links(filepath, content)
        self._check_length(filepath, content)
    
    def _check_filename(self, filepath, filename):
        """Check filename conventions."""
        # Should use kebab-case
        if not re.match(r'^[a-z0-9\-]+\.[a-z]+$', filename):
            if filename not in ['README.md', 'INDEX.md', 'NOTES.md']:
                self.warnings[filepath].append(
                    "Filename should use kebab-case (lowercase-with-hyphens.ext)"
                )
        
        # Should have clear audience or purpose
        ambiguous = ['file', 'document', 'content', 'render', 'output']
        name_part = filename.rsplit('.', 1)[0]
        if name_part.lower() in ambiguous:
            self.warnings[filepath].append(
                f"Filename '{filename}' is too generic, use descriptive name"
            )
    
    def _check_readability(self, filepath, content):
        """Check readability metrics."""
        # Count sentences and words (simple heuristic)
        sentences = re.findall(r'[.!?]+', content)
        words = re.findall(r'\b\w+\b', content)
        
        if len(sentences) == 0:
            return  # Skip for non-text files
        
        avg_words_per_sentence = len(words) / len(sentences) if sentences else 0
        
        # Warn if sentences too long (>30 words avg)
        if avg_words_per_sentence > 30:
            self.warnings[filepath].append(
                f"Average sentence length {avg_words_per_sentence:.1f} words "
                "(consider breaking into shorter sentences)"
            )
        
        # Check for very long sentences
        paragraphs = content.split('\n\n')
        for para in paragraphs:
            para_sentences = re.split(r'[.!?]+', para)
            for sent in para_sentences:
                sent_words = len(re.findall(r'\b\w+\b', sent))
                if sent_words > 40:
                    self.warnings[filepath].append(
                        f"Very long sentence ({sent_words} words): {sent[:50]}..."
                    )
                    break  # Only report first occurrence per file
    
    def _check_metadata(self, filepath, content):
        """Check for metadata (YAML frontmatter)."""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    metadata = yaml.safe_load(parts[1])
                    if not isinstance(metadata, dict):
                        self.warnings[filepath].append("Metadata is not a dictionary")
                        return
                    
                    # Check for recommended fields
                    recommended = ['title', 'audience', 'language']
                    missing = [f for f in recommended if f not in metadata]
                    if missing:
                        self.warnings[filepath].append(
                            f"Missing recommended metadata: {', '.join(missing)}"
                        )
                except yaml.YAMLError as e:
                    self.issues[filepath].append(f"Invalid YAML metadata: {e}")
    
    def _check_headings(self, filepath, content):
        """Check heading structure."""
        lines = content.split('\n')
        heading_levels = []
        
        for line in lines:
            if line.startswith('#'):
                level = len(re.match(r'^#+', line).group())
                heading_levels.append(level)
        
        if not heading_levels:
            return  # No headings (OK for short files)
        
        # Check for skipped levels (e.g., H1 -> H3)
        for i in range(len(heading_levels) - 1):
            if heading_levels[i+1] > heading_levels[i] + 1:
                self.warnings[filepath].append(
                    f"Skipped heading level: H{heading_levels[i]} -> H{heading_levels[i+1]}"
                )
                break
        
        # Check for multiple H1s
        h1_count = heading_levels.count(1)
        if h1_count > 1:
            self.warnings[filepath].append(
                f"Multiple H1 headings ({h1_count}), should have only one"
            )
    
    def _check_images(self, filepath, content):
        """Check image references."""
        # Find markdown images: ![alt](path)
        images = re.findall(r'!\[(.*?)\]\((.*?)\)', content)
        
        for alt_text, img_path in images:
            # Check for missing alt text
            if not alt_text or alt_text.strip() == '':
                self.issues[filepath].append(
                    f"Image missing alt text: {img_path}"
                )
            
            # Check if image exists (relative to render file)
            if not img_path.startswith('http'):
                render_dir = os.path.dirname(filepath)
                full_img_path = os.path.join(render_dir, img_path)
                if not os.path.exists(full_img_path):
                    self.warnings[filepath].append(
                        f"Image file not found: {img_path}"
                    )
    
    def _check_links(self, filepath, content):
        """Check link quality."""
        # Find markdown links: [text](url)
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        
        for link_text, url in links:
            # Skip image links (already checked)
            if re.search(r'!\[', content[:content.find(f'[{link_text}]')]):
                continue
            
            # Check for poor link text
            poor_text = ['click here', 'here', 'link', 'this']
            if link_text.lower().strip() in poor_text:
                self.warnings[filepath].append(
                    f"Poor link text: '{link_text}' (use descriptive text)"
                )
    
    def _check_length(self, filepath, content):
        """Check content length."""
        word_count = len(re.findall(r'\b\w+\b', content))
        
        # Warn if very short (< 100 words) or very long (> 10000 words)
        if word_count < 100:
            self.warnings[filepath].append(
                f"Very short content ({word_count} words)"
            )
        elif word_count > 10000:
            self.warnings[filepath].append(
                f"Very long content ({word_count} words), consider splitting"
            )
    
    def print_report(self):
        """Print linting report."""
        print("\n" + "="*70)
        print("Render Quality Linter Report")
        print("="*70)
        
        print(f"\nFiles checked: {self.stats['files_checked']}")
        
        # Count issues and warnings
        total_issues = sum(len(v) for v in self.issues.values())
        total_warnings = sum(len(v) for v in self.warnings.values())
        
        print(f"Issues: {total_issues}")
        print(f"Warnings: {total_warnings}")
        
        if total_issues > 0:
            print("\n" + "="*70)
            print("ISSUES (must fix)")
            print("="*70)
            for filepath, issue_list in sorted(self.issues.items()):
                print(f"\n{filepath}:")
                for issue in issue_list:
                    print(f"  ❌ {issue}")
        
        if total_warnings > 0:
            print("\n" + "="*70)
            print("WARNINGS (should fix)")
            print("="*70)
            for filepath, warning_list in sorted(self.warnings.items()):
                print(f"\n{filepath}:")
                for warning in warning_list:
                    print(f"  ⚠️  {warning}")
        
        if total_issues == 0 and total_warnings == 0:
            print("\n✅ No issues or warnings found!")
        
        print("\n" + "="*70)

def main():
    if len(sys.argv) < 2:
        print("Usage: python render_quality_linter.py [path]")
        print("Examples:")
        print("  python render_quality_linter.py renders/by-domain/")
        print("  python render_quality_linter.py renders/by-domain/natural-sciences/physics/")
        sys.exit(1)
    
    target_path = sys.argv[1]
    
    if not os.path.exists(target_path):
        print(f"Error: Path not found: {target_path}")
        sys.exit(1)
    
    linter = RenderLinter()
    
    # Lint files
    if os.path.isfile(target_path):
        if target_path.endswith(('.md', '.html', '.txt')):
            linter.lint_file(target_path)
    else:
        # Lint directory
        for root, dirs, files in os.walk(target_path):
            # Skip hidden and metadata directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '_metadata']
            
            for filename in files:
                if filename.endswith(('.md', '.html', '.txt')):
                    filepath = os.path.join(root, filename)
                    linter.lint_file(filepath)
    
    linter.print_report()

if __name__ == "__main__":
    main()
