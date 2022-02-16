# stripe-checkout-subscription-flask
# Stripe Dashboard
log in to stripe dashboard as a test account and get secret, publishable keys.
create a product which user will subscribe and set recurring if you want user to automatically pay every month.
get product API ID for subscription

## Listen webhhok on local Machine
download stripe latest linux tar.gz file from here https://stripe.com/docs/stripe-cli
### Stripe CLI
use these 2 commands while your flask application server is running in other terminal
stripe login
stripe listen --forward-to 127.0.0.1:5000/webhook

### Refrenced Tutorials
https://stripe.com/docs/payments
https://testdriven.io/blog/flask-stripe-tutorial/
