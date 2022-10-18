from flask import render_template, request, jsonify
from flask_login import current_user

from models.contact import Contact


def contact():
    if request.method == 'POST':
        # Get the form data
        name = request.form.get('contactName')
        email = request.form.get('contactEmail')
        text = request.form.get('contactText')
        # Send the message
        user_id = current_user.id if current_user.is_authenticated else None

        try:
            message = Contact(name, email, text, user_id)
        except Exception as e:
            return jsonify({'success': False, 'err': str(e)})
        else:
            message.save()
            return jsonify({'success': True})

    return render_template("contact.html")
