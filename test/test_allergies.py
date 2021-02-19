import pytest


AllERGIES = [
    {"name_en": "eggs", "name_ar": "بيض"},
    {"name_en": "fish", "name_ar": "سمك"},
    {"name_en": "milk", "name_ar": "لبن"},
]


@pytest.fixture
def is_valid_allergy_ar_name(allergy_ar_name):
    for allergy in AllERGIES:
        if allergy.get("name_ar") == allergy_ar_name:
            return allergy.get("name_ar")


@pytest.fixture()
def is_valid_allergy_en_name(allergy_en_name):
    for allergy in AllERGIES:
        if allergy.get("name_en") == allergy_en_name:
            return allergy.get("name_en")


class TestAllergy:
    @pytest.mark.parametrize("allergy_en_name", ["eggs"])
    # allergy_en_name is the params of is_valid_allergy_en_name
    # ["eggs"] is list of values that passed as "eggs" to "is_valid_allergy_en_name"
    def test_egg_en_allergy(self, is_valid_allergy_en_name, allergy_en_name):
        assert "eggs" == is_valid_allergy_en_name

    @pytest.mark.parametrize("allergy_ar_name", ["بيض"])
    def test_egg_ar_allergy(self, is_valid_allergy_ar_name, allergy_ar_name):
        assert "بيض" == is_valid_allergy_ar_name

    @pytest.mark.parametrize("allergy_ar_name", ["سمك"])
    def test_fish_ar_allergy(self, is_valid_allergy_ar_name, allergy_ar_name):
        assert "سمك" == is_valid_allergy_ar_name

    @pytest.mark.parametrize("allergy_en_name", ["fish"])
    def test_fish_en_allergy(self, is_valid_allergy_en_name, allergy_en_name):
        assert "fish" == is_valid_allergy_en_name

    @pytest.mark.parametrize("allergy_ar_name", ["لبن"])
    def test_milk_ar_allergy(self, is_valid_allergy_ar_name, allergy_ar_name):
        assert "لبن" == is_valid_allergy_ar_name

    @pytest.mark.parametrize("allergy_en_name", ["milk"])
    def test_milk_en_allergy(self, is_valid_allergy_en_name, allergy_en_name):
        assert "milk" == is_valid_allergy_en_name
