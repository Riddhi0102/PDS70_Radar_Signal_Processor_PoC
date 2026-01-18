"""
report_generator.py
Generate a simple PDF report with plots.
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

def make_report(out_pdf: str, title: str, summary_lines: list[str], plot_paths: list[str]):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(out_pdf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    story = []
    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
    for line in summary_lines:
        story.append(Paragraph(f"- {line}", styles["BodyText"]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("<b>Key Plots</b>", styles["Heading2"]))
    story.append(Spacer(1, 0.2*cm))

    for p in plot_paths:
        path = Path(p)
        if path.exists():
            story.append(Image(str(path), width=16*cm, height=10*cm))
            story.append(Spacer(1, 0.3*cm))
    doc.build(story)
