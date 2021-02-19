"""
    testing code
"""


import pytest
from .checkout import Checkout


@pytest.fixture
def checkout():
    co = Checkout()
    co.add_item_price("mobile", 1)
    co.add_item_price("tablet", 10)
    co.add_item_price("laptop", 6)
    return co


class TestCheckout:
    def test_calculate_total(self, checkout: Checkout):
        checkout.add_item("mobile")
        assert checkout.cal_total() == 1

    def test_total_with_multiple_items(self, checkout: Checkout):
        checkout.add_item("laptop")  # price 6
        checkout.add_item("tablet")  # price 10
        checkout.add_item("mobile")  # price 1

        assert checkout.cal_total() == 17  # 6 + 10 + 1

    def test_discount_rules(self, checkout: Checkout):
        checkout.add_discount("mobile", 3, 2)

    # @pytest.mark.skip(reason="NOT IMPLEMENTED YET")
    def test_apply_discount_rules(self, checkout: Checkout):
        checkout.add_discount("mobile", 3, 2)
        checkout.add_item("mobile")
        checkout.add_item("mobile")
        checkout.add_item("mobile")
        assert checkout.cal_total() == 2

    def test_exception_with_bad_item(self, checkout: Checkout):
        with pytest.raises(Exception):
            checkout.add_item("head phone")
