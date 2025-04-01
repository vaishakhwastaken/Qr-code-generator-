import qrcode

def generate_qr_code(url, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f'QR code generated and saved as {filename}')

# Example usage
website_url = "https://forms.gle/fud9b6XvJxZCo3GB7"  # Replace with your target URL
generate_qr_code(website_url)