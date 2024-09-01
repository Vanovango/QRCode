import qrcode
from PIL import Image


def create_qrcode(parent_name, cadette_name, family_status):
    # taking image which user wants
    # in the QR code center
    logo_link = 'vas.png'

    logo = Image.open(logo_link).convert("RGBA")  # Convert logo to RGBA

    # taking base width
    base_width = 250

    # adjust image size
    w_percent = (base_width / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(w_percent)))
    logo = logo.resize((base_width, hsize), Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    qr.add_data(f'ФИО гостя: {parent_name} \n')
    qr.add_data(f'Кем приходиться: {family_status} \n')
    qr.add_data(f'ФИО курсанта: {cadette_name} \n')
    qr.add_data(f'✅Доступ разрешен')

    # generating QR code
    qr.make()

    # Create the QR code with a transparent background
    qr_img = qr.make_image(
        fill_color="black", back_color=(255, 255, 255, 0)).convert('RGBA')

    # set size of QR code
    pos = ((qr_img.size[0] - logo.size[0]) // 2,
           (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, pos, mask=logo)  # Use mask to preserve transparency

    return qr_img


if __name__ == '__main__':
    img = create_qrcode(parent_name='Войтенко Александр Сергеевич',
                        cadette_name='Войтенко Иван Александрович',
                        family_status='Отец')
    # save the QR code generated
    img.save('QR.png')
