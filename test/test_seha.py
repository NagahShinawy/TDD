def setup_module(module):
    print("\nModule", module)  # module(file) path


def teardown_module(module):
    print("\nDestroying module", module)


class TestBloodType:
    @classmethod
    def setup_class(cls):
        print("\nMy class is ", cls)

    def setup(
        self,
    ):  # RUNS BEFORE EVERY METHOD BUT based on priority, setup_method then setup
        print("\nSETUP IN GENERAL FOR ", self.blood_types)

    def test_name(self):
        print("TESTING NAME")

    def test_blood_type(self):
        self.check_blood_type("A+")
        self.check_blood_type("A-")
        self.check_blood_type("B+")
        self.check_blood_type("B-")
        self.check_blood_type("AB+")
        self.check_blood_type("AB-")
        self.check_blood_type("O+")
        self.check_blood_type("O-")

    def setup_method(
        self, method
    ):  # naming conventions is setup( MUST ), run before every unittest
        if method == self.test_blood_type:
            print("\nSET UP FOR CHECKING BLOOD TYPE")
        elif method == self.test_name:
            print("\nSET UP FOR CHECKING NAME")
        self.blood_types = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")

    def teardown_method(self, method):
        print("\nDestroying method ", method)

    def teardown(
        self,
    ):  # naming conventions is teardown ( MUST ), run after every unittest
        print("\nDestroying in general for every method", self.blood_types)

    @classmethod
    def teardown_class(cls):
        print("\nDestroying class", cls)

    def check_blood_type(self, blood_type):
        assert blood_type in self.blood_types, "Blood types should one of {}".format(
            ",".join(self.blood_types)
        )
