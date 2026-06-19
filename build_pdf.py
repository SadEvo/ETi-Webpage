import markdown
import pathlib
import re
from fpdf import FPDF

base = pathlib.Path("/home/user/ETi-Webpage")
files = [
    "README.md",
    "docs/event-sales-calendar.md",
    "docs/group-buy-playbook.md",
    "docs/marketing-distribution-plan.md",
]

# Emoji / glyphs not in DejaVu -> readable substitutes
REPL = {
    "\U0001F7E2": "●",   # green circle -> filled circle (Primary)
    "\U0001F535": "○",   # blue circle  -> open circle   (Secondary)
    "✅": "✓",        # white check  -> check mark
    "➕": "+",             # heavy plus   -> plus
}

def sanitize(s: str) -> str:
    for a, b in REPL.items():
        s = s.replace(a, b)
    return s

def strip_inline_in_cells(html: str) -> str:
    """fpdf2 can't render inline tags inside <td>/<th>; flatten them to text."""
    def clean(m):
        cell = m.group(0)
        cell = re.sub(r"</?(strong|em|code|b|i)>", "", cell)
        cell = re.sub(r"<a [^>]*>", "", cell).replace("</a>", "")
        return cell
    html = re.sub(r"<td.*?</td>", clean, html, flags=re.S)
    html = re.sub(r"<th.*?</th>", clean, html, flags=re.S)
    return html

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])

DEJAVU = "/usr/share/fonts/truetype/dejavu"
LIB = "/usr/share/fonts/truetype/liberation"

pdf = FPDF(format="A4")
pdf.set_margins(14, 14, 14)
pdf.set_auto_page_break(True, margin=14)
pdf.add_font("DejaVu", "", f"{DEJAVU}/DejaVuSans.ttf")
pdf.add_font("DejaVu", "B", f"{DEJAVU}/DejaVuSans-Bold.ttf")
pdf.add_font("DejaVu", "I", f"{LIB}/LiberationSans-Italic.ttf")
pdf.add_font("DejaVu", "BI", f"{LIB}/LiberationSans-BoldItalic.ttf")
pdf.set_font("DejaVu", size=10.5)

pdf.set_title("Elite Ti - Event-Based Sales & Marketing Plan")
pdf.set_author("Elite Ti")

# Style headings: scale + a brand-red color for h1/h2
tag_styles = None
try:
    from fpdf.enums import TextEmphasis  # noqa: F401
    from fpdf.fonts import FontFace
    tag_styles = {
        "h1": FontFace(color=(192, 57, 43), size_pt=20, emphasis="BOLD"),
        "h2": FontFace(color=(192, 57, 43), size_pt=14, emphasis="BOLD"),
        "h3": FontFace(color=(34, 34, 34), size_pt=12, emphasis="BOLD"),
    }
except Exception:
    tag_styles = None

for i, f in enumerate(files):
    text = (base / f).read_text()
    html = md.convert(text)
    md.reset()
    html = strip_inline_in_cells(sanitize(html))
    pdf.add_page()
    kwargs = dict(
        text=html,
        table_line_separators=True,
    )
    if tag_styles:
        kwargs["tag_styles"] = tag_styles
    try:
        pdf.write_html(**kwargs)
    except TypeError:
        pdf.write_html(html)

out = base / "Elite-Ti-Sales-Marketing-Plan.pdf"
pdf.output(str(out))
print("wrote", out, out.stat().st_size, "bytes")
