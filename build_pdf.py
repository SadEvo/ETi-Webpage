import markdown
import pathlib
import re
from fpdf import FPDF

base = pathlib.Path("/home/user/ETi-Webpage")

# Each output PDF -> list of source markdown docs (in order)
BUNDLES = {
    "Elite-Ti-1-Marketing-Execution-Plan.pdf": [
        "docs/marketing-execution-plan.md",
    ],
    "Elite-Ti-2-Promo-and-Discount-Calendar.pdf": [
        "docs/promo-discount-calendar.md",
        "docs/group-buy-playbook.md",
    ],
}

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

try:
    from fpdf.fonts import FontFace
    TAG_STYLES = {
        "h1": FontFace(color=(192, 57, 43), size_pt=20, emphasis="BOLD"),
        "h2": FontFace(color=(192, 57, 43), size_pt=14, emphasis="BOLD"),
        "h3": FontFace(color=(34, 34, 34), size_pt=12, emphasis="BOLD"),
    }
except Exception:
    TAG_STYLES = None


def build_pdf(out_name, docs, title):
    pdf = FPDF(format="A4")
    pdf.set_margins(14, 14, 14)
    pdf.set_auto_page_break(True, margin=14)
    pdf.add_font("DejaVu", "", f"{DEJAVU}/DejaVuSans.ttf")
    pdf.add_font("DejaVu", "B", f"{DEJAVU}/DejaVuSans-Bold.ttf")
    pdf.add_font("DejaVu", "I", f"{LIB}/LiberationSans-Italic.ttf")
    pdf.add_font("DejaVu", "BI", f"{LIB}/LiberationSans-BoldItalic.ttf")
    pdf.set_font("DejaVu", size=10.5)
    pdf.set_title(title)
    pdf.set_author("Elite Ti")
    for doc in docs:
        html = strip_inline_in_cells(sanitize(md.convert((base / doc).read_text())))
        md.reset()
        pdf.add_page()
        kwargs = dict(text=html, table_line_separators=True)
        if TAG_STYLES:
            kwargs["tag_styles"] = TAG_STYLES
        try:
            pdf.write_html(**kwargs)
        except TypeError:
            pdf.write_html(html)
    out = base / out_name
    pdf.output(str(out))
    print("wrote", out.name, out.stat().st_size, "bytes")


TITLES = {
    "Elite-Ti-1-Marketing-Execution-Plan.pdf": "Elite Ti - Marketing Execution Plan",
    "Elite-Ti-2-Promo-and-Discount-Calendar.pdf": "Elite Ti - Promo & Discount Calendar",
}
for out_name, docs in BUNDLES.items():
    build_pdf(out_name, docs, TITLES[out_name])
