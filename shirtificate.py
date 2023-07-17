from fpdf import FPDF

name = input("What is your name?: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image("shirtificate.png",x=12,y=50, h=0, w=pdf.epw*98/100,keep_aspect_ratio=True)
pdf.set_font("helvetica","",35)
pdf.text(60, 28, "CS50 Shirtificate")
pdf.set_text_color(255,255,255)
pdf.set_stretching(70)
pdf.cell(
            190,
            190,
            name + " took CS50",
            border=0,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=False,
        )
pdf.output("shirtificate.pdf")