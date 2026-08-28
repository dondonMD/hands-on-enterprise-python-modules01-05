"""
Module 2 activity: Factory + Adapter.

Northwind Orders needs to support two payment providers behind one
interface: a modern gateway you control the shape of, and a legacy SDK
whose method signature you don't control.
"""

from typing import Protocol


class PaymentGateway(Protocol):
    def charge(self, amount: float, token: str) -> bool: ...


class ModernGateway:
    """Already implements PaymentGateway directly — nothing to do here."""

    def __init__(self) -> None:
        self.charges: list[tuple[float, str]] = []

    def charge(self, amount: float, token: str) -> bool:
        self.charges.append((amount, token))
        return amount > 0


class LegacyPaymentSdk:
    """
    A stand-in for a third-party SDK you don't control. Note the shape:
    it wants *cents* as an int and calls the token `card_token`, and it
    returns a dict, not a bool.
    """

    def __init__(self) -> None:
        self.calls: list[tuple[int, str]] = []

    def make_payment(self, cents: int, card_token: str) -> dict:
        self.calls.append((cents, card_token))
        return {"ok": cents > 0}


class LegacyPaymentAdapter:
    """
    TODO: adapt LegacyPaymentSdk to the PaymentGateway protocol.

    charge(amount, token) should call self._sdk.make_payment(...) with the
    amount converted to an integer number of cents, and return the "ok"
    value from the result dict.
    """

    def __init__(self, sdk: LegacyPaymentSdk) -> None:
        self._sdk = sdk

    def charge(self, amount: float, token: str) -> bool:
        # TODO: implement using self._sdk.make_payment
        raise NotImplementedError


def payment_gateway_factory(provider: str) -> PaymentGateway:
    """
    TODO: return a ModernGateway() when provider == "modern", and a
    LegacyPaymentAdapter wrapping a fresh LegacyPaymentSdk() when
    provider == "legacy". Raise ValueError for anything else.
    """
    raise NotImplementedError
