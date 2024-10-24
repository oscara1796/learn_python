# Adapter Pattern Example in Python

"""
Adapter Pattern

The Adapter pattern allows incompatible classes to work together by converting the interface of one class into an interface expected by the clients.

Real-life example:
Suppose you have a third-party payment gateway with a different interface than what your system uses.
By creating an adapter, you can integrate the third-party system without changing your existing code.
"""

# Existing interface
class PaymentProcessor:
    def pay(self, amount):
        pass

# Adaptee (Third-party payment system)
class ThirdPartyPayment:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made using ThirdPartyPayment system.")

# Adapter
class PaymentAdapter(PaymentProcessor):
    def __init__(self):
        self.third_party_payment = ThirdPartyPayment()

    def pay(self, amount):
        # Adapts the interface and delegates the call
        self.third_party_payment.make_payment(amount)

# Usage
if __name__ == "__main__":
    # Client code uses the PaymentProcessor interface
    payment_processor = PaymentAdapter()
    payment_processor.pay(100)

    # Output:
    # Payment of $100 made using ThirdPartyPayment system.
