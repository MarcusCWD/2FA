import base64
from vpn import app
from flask import render_template, redirect, url_for, flash, abort, send_file
from vpn.models import User
from vpn import db
from vpn.forms import LoginForm, RegisterForm
import qrcode
import pyotp
from io import BytesIO


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    # when form is submitted:
    if form.validate_on_submit():
        if form.errors == {}:
            user_dbaccess = db.query(User).filter_by(email_address=form.email.data).first()
            # translate query, map to needed fields
            user_list = [{'id': user_dbaccess.id, 'email_address': user_dbaccess.email_address, 'secret': user_dbaccess.secret, 'last_login': user_dbaccess.last_login, 'active': user_dbaccess.active}]
            # Verify TOTP
            totp = pyotp.TOTP(user_list[0]['secret'])
            if totp.verify(form.otp.data):
                return 'Login successful!'
            else:
                isotpfail= True
                return render_template('login.html', form=form, isotpfail=isotpfail)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        if form.errors == {}:
            user_dbaccess = db.query(User).filter_by(email_address=form.email.data).first()
            # translate query, map to needed fields
            user_list = [{'id': user_dbaccess.id, 'email_address':user_dbaccess.email_address, 'epin': user_dbaccess.epin, 'last_login': user_dbaccess.last_login, 'active': user_dbaccess.active}]

            if user_dbaccess:
                if int(user_list[0]['epin']) == int(form.epin.data):
                    # Generate TOTP secret and URL for QR code
                    secret = pyotp.random_base32()
                    user_dbaccess.secret = secret
                    db.commit()
                    db.close()

                    totp_url = pyotp.totp.TOTP(secret).provisioning_uri(issuer_name='TSC-VPN', name=user_list[0]['email_address'])

                    # Generate QR code for TOTP URL
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=6,
                        border=4,
                    )
                    qr.add_data(totp_url)
                    qr.make(fit=True)
                    qr_img = qr.make_image(fill_color="black", back_color="white")

                    # Convert QR code image to base64
                    buffered = BytesIO()
                    qr_img.save(buffered, format='PNG')
                    qr_img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

                    return render_template('register.html', qr_img=qr_img_str, form=form)

                else:
                    print("epin fail")
                    isepinfail = True
                    return render_template('register.html', form=form, isepinfail=isepinfail)


    return render_template('register.html', form=form)
