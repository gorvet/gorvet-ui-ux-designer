from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")

errors=[]
for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    f=d/'SKILL.md'
    if not f.exists():
        errors.append(f"{d.name}: missing SKILL.md")
        continue
    text=f.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        errors.append(f"{d.name}: missing YAML frontmatter")
        continue
    parts=text.split('---\n',2)
    if len(parts)<3:
        errors.append(f"{d.name}: malformed frontmatter")
        continue
    fm=parts[1]
    m_name=re.search(r'^name:\s*(.+?)\s*$', fm, re.M)
    m_desc=re.search(r'^description:\s*(.+?)\s*$', fm, re.M)
    if not m_name: errors.append(f"{d.name}: missing name")
    if not m_desc: errors.append(f"{d.name}: missing description")
    if m_name:
        name=m_name.group(1).strip().strip('"\'')
        if name != d.name: errors.append(f"{d.name}: frontmatter name is {name}")
        if len(name)>64 or not NAME_RE.match(name): errors.append(f"{d.name}: invalid Agent Skills name")
    if m_desc:
        desc=m_desc.group(1).strip().strip('"\'')
        if not desc or len(desc)>1024: errors.append(f"{d.name}: invalid description length")
    for rel in LINK_RE.findall(text):
        rel=rel.split('#',1)[0]
        if rel and not (d/rel).exists(): errors.append(f"{d.name}: broken local link {rel}")

if errors:
    print('Validation failed:')
    for e in errors: print(' -',e)
    sys.exit(1)
print(f'OK: {len([p for p in SKILLS.iterdir() if p.is_dir()])} skills validated.')
