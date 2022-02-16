# Retrieve Subscription from Session iD

# import stripe
# stripe.api_key = "sk_test_531LK67HD32SU8AAPCY"my_api_key"Vg7K00vJF7TjAF"
# ab = stripe.checkout.Session.retrieve(
#   "cs_test_a161Imv32s496emZ"checkout_Session_id"0svDrm1uBYKu6v6qfMwD",
# )
# print(ab)




# Retrieve Subscription from Subscription iD

# import stripe
# stripe.api_key = "sk_test_531LK67HD32SU8AAPCY"my_api_key"UA9GDLkXVg7K00vJF7TjAF"
# ad = stripe.Subscription.retrieve(
#   "sub_1K9RZ"subs_id"EoJACG",
# )
# print(ad)



# Update a subscription (place order id in Metadata)

# import stripe
# stripe.api_key = "sk_test_531LK67HD32SU8AAPCY"my_api_key"UA9GDLkXVg7K00vJF7TjAF"
# aa = stripe.Subscription.modify(
#   "sub_1K9Uct"subs_id"E",
#   metadata={"order_id": "6735"},
# )
# print(aa)



# Cancel a Subscription

# import stripe
# stripe.api_key = "sk_test_531LK67HD32SU8AAPCY"my_api_key"UA9GDLkXVg7K00vJF7TjAF"

# aa = stripe.Subscription.delete(
#   "sub_1K9Uv"sub_id"WJv",
# )
# print(aa)



# Retrieve Customer

# import stripe
# stripe.api_key = "sk_test_531LK67HD32SU8AAPCY"my_api_key"UA9GDLkXVg7K00vJF7TjAF"

# a = stripe.Customer.retrieve("cus_KxP"customer_id"yu4")
# print(a)


# import stripe
# stripe.api_key = "sk_test_531LK67HD32SU8AAPCY"my_api_key"UA9GDLkXVg7K00vJF7TjAF"

# a = stripe.PaymentIntent.retrieve(
#   "pi_3KIqHs"payment_intent_id"W",
# )
# print(a)