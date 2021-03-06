from . import stripe


def create_card(user, token):
    # El primero guardado es el que se define como default_source del cliente.
    return stripe.Customer.create_source(user.customer_id, source=token)
