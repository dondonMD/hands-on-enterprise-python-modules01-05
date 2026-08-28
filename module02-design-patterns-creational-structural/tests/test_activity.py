import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "activity"))

import pytest  # noqa: E402
from payments import (  # noqa: E402
    LegacyPaymentAdapter,
    LegacyPaymentSdk,
    ModernGateway,
    payment_gateway_factory,
)


def test_adapter_translates_amount_to_cents_and_ok_to_bool():
    sdk = LegacyPaymentSdk()
    adapter = LegacyPaymentAdapter(sdk)

    result = adapter.charge(19.99, "tok_abc")

    assert result is True
    assert sdk.calls == [(1999, "tok_abc")]


def test_adapter_rejects_zero_amount():
    adapter = LegacyPaymentAdapter(LegacyPaymentSdk())
    assert adapter.charge(0, "tok_abc") is False


def test_factory_returns_modern_gateway():
    gw = payment_gateway_factory("modern")
    assert isinstance(gw, ModernGateway)
    assert gw.charge(10.0, "tok") is True


def test_factory_returns_legacy_adapter():
    gw = payment_gateway_factory("legacy")
    assert isinstance(gw, LegacyPaymentAdapter)
    assert gw.charge(10.0, "tok") is True


def test_factory_rejects_unknown_provider():
    with pytest.raises(ValueError):
        payment_gateway_factory("crypto")
