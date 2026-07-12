from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def create_pdf(patient_data, probability, risk, advice, reminders):

    pdf = SimpleDocTemplate("reports/Health_Report.pdf")

    story = []

    story.append(Paragraph("<b>AI Health Guardian Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Patient Information</b>", styles["Heading2"]))
    story.append(Paragraph(patient_data.replace("\n","<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Risk Probability:</b> {probability*100:.2f}%", styles["BodyText"]))

    story.append(Paragraph(f"<b>Risk Level:</b> {risk}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>AI Medical Advice</b>", styles["Heading2"]))

    story.append(Paragraph(advice.replace("\n","<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Health Reminders</b>", styles["Heading2"]))

    for reminder in reminders:
        story.append(Paragraph(reminder, styles["BodyText"]))

    pdf.build(story)

    return "reports/Health_Report.pdf"