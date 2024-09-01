def create_qrcode(parent_name, cadette_name, family_status):
    import qrcode
    from PIL import Image
    import base64
    from io import BytesIO

    logo_link = 'vas.png'
    logo = Image.open(logo_link)

    base_width = 250
    w_percent = (base_width / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(w_percent)))
    logo = logo.resize((base_width, hsize))

    web = open(qrcode.html)

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(web)

    qr.make()

    qr_color = 'Black'
    qr_img = qr.make_image(fill_color=qr_color, back_color="white").convert('RGB')

    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, pos)

    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return img_str


def create_html_file(parent_name, cadette_name, family_status):
    qr_code_base64 = open('vas.png')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>QR Code</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
            }}
            .info {{
                margin-top: 20px;
                font-size: 18px;
                line-height: 1.5;
            }}
            .qr-code {{
                margin: 20px auto;
            }}
        </style>
    </head>
    <body>        
        <div class="info">
            <p>ФИО гостя: <strong>{parent_name}</strong></p>
            <p>Кем приходиться: <strong>{family_status}</strong></p>
            <p>ФИО курсанта: <strong>{cadette_name}</strong></p>
            <p>Доступ разрешен</p>
        </div>
    </body>
    </html>
    """

    with open('qrcode.html', 'w', encoding='utf-8') as file:
        file.write(html_content)


if __name__ == '__main__':
    create_html_file(
        parent_name='Войтенко Александр Сергеевич',
        cadette_name='Войтенко Иван Александрович',
        family_status='Отец'
    )

