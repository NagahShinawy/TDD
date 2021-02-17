from utils import check_blood_type


def test_blood_type():
    check_blood_type("A+")
    check_blood_type("B+")
    check_blood_type("AB+")
    check_blood_type("O+")
