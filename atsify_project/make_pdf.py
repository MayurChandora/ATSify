from reportlab.pdfgen import canvas

c = canvas.Canvas("dummy_resume.pdf")
c.drawString(100, 750, "John Doe")
c.drawString(100, 730, "Software Engineer")
c.drawString(100, 710, "Experience with Python, Django, Tailwind CSS, MySQL")
c.drawString(100, 690, "Team player, good communication skills, problem solver.")
c.save()
