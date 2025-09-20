from fpdf import FPDF

def generar_pdf(resumen, volatilidad, proyecciones):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Reporte de Analisis ASG vs S&P 500", ln=True, align="C")
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Resumen de Rendimientos", ln=True)
    pdf.multi_cell(0, 10, resumen.to_string())

    pdf.cell(200, 10, "Volatilidad Comparativa", ln=True)
    pdf.multi_cell(0, 10, volatilidad.to_string())

    pdf.cell(200, 10, "Proyecciones (30 días)", ln=True)
    pdf.multi_cell(0, 10, proyecciones.to_string())

    pdf.output("outputs/reporte_final.pdf")
