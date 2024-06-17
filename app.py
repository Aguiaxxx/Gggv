from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # Inicializar o navegador (você pode escolher entre 'chromium', 'firefox' e 'webkit')
        browser = p.chromium.launch(headless=False)  # headless=False significa que você verá o navegador em ação
        # Abrir uma nova página
        page = browser.new_page()
        # Navegar para o site do Google
        page.goto("https://www.google.com")
        # Manter o navegador aberto por 10 segundos para que você possa ver a página
        page.wait_for_timeout(10000)
        # Fechar o navegador
        browser.close()

if __name__ == "__main__":
    main()
