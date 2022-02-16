from flask import Flask, jsonify, request
import stripe
import json

app = Flask(__name__)

stripe_keys = {
    "secret_key": "sk_test_531LK67HD32SU"my_secret_key"8AAPCY",
    "publishable_key": "pk_test_51K6AAP"publishable_key"0pKr9mWLE",
    "subscription1": "price_1K6"product_subs_id"plZDd",
    "subscription2" : "price_1Kproduct_subs_idkP6y",
    "endpoint_secret": "whsec_m"endpoint_secret"eK7K0e",
}


@app.route("/get_publishable_key")
def get_publishable_key():
    stripe_config = {"public_key": stripe_keys["publishable_key"]}
    return stripe_config


@app.route("/create_checkout_session")
def create_checkout_session(self, plan=0, user_id=None):
    stripe.api_key = "secret_key"
    try:
        price_id = stripe_keys["subscription1"]
        plan = str({"plan": plan, "user_id": user_id})
        checkout_session = stripe.checkout.Session.create(
            client_reference_id=plan,
            metadata={'user_id': user_id},
            subscription_data={
                "metadata": {"user_id": user_id}
            },
            success_url="google.com",
            cancel_url="google.com",
            payment_method_types=["card"],
            mode="subscription",
            line_items=[
                {
                    "price": price_id,
                    "quantity": 1,
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"], "sessionURL": checkout_session["url"]})
    except:
        return


def webhook_received(self):
    payload = request.data
    endpoint_secret = 'our_endpoint_secret'
#    endpoint_secret = 'our_endpoint_secret from stripe dashboard after registring webhook endpoint'
#    endpoint secret will be different if you register webhook endpoint in stripe dashboard
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
        data = event['data']
    except:
        pass
    event_type = event['type']
    if event_type == 'checkout.session.completed':
        self.handle_checkout_session(data)
    elif event_type == 'invoice.paid':
        pass
    elif event_type == 'invoice.payment_succeeded':
        pass
    elif event_type == 'payment_intent.succeeded':
        pass
    elif event_type == 'payment_intent.payment_failed':
        pass
    elif event_type == 'invoice.payment_failed':
        self.subscription_failure_handling(data)
    elif event_type == 'charge.failed':
        pass
    else:
        print('Unhandled event type {}'.format(event_type))
    return jsonify({'status': "Success"})

def handle_checkout_session(self, data):
    plan_user_id = data["object"]["client_reference_id"].replace("'", "\"")
    plan_user_id = json.loads(plan_user_id)
    plan_id = plan_user_id["plan"]
    user_id = plan_user_id["user_id"]
    try:
        # Save data in case of success
        pass
    except:
        db.session.rollback()
    finally:
        db.session.close()
        return

def subscription_failure_handling(self, data):
    try:
        # Save data in case of failure
        pass
    except:
        db.session.rollback()
    finally:
        db.session.close()
        return
