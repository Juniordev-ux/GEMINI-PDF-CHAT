import pypdf # biblioteca para manipulação de PDFd

def extract_text_from_pdf(pdf_file):
    """
    Função para extrair o textode um pdf carregado no streamlit

    Parâmetros:
    pdf_file (UploadedFile): Arquivo PDF carregado pelo usuario

    Retorna:
    str: Texto extraido do PDF.
    """

    reader = pypdf.PdfReader(pdf_file) # Cria um objeto para ler o PDF

    # Percorrer todas as paginas eextrai o texto disponivel
    text = "\n".join([page.extract_text() for page in reader.page if page.extract_page_text()])
    return text # Retorna o texto extraido
