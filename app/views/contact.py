from flask import render_template, request, jsonify, redirect, url_for
from models.contact import Contact


def contact_us():
    return render_template("contact.html")


def contact():
    if request.method == 'POST':
        # Get the form data
        name = request.form.get('contactName')
        email = request.form.get('contactEmail')
        text = request.form.get('contactText')
        # Send the message
        try:
            message = Contact(name, email, text, None)
        except Exception as e:
            return jsonify({'success': False, 'err': str(e)})
        else:
            message.save()
            return jsonify({'success': True})

    return redirect(url_for('contact_us'))
