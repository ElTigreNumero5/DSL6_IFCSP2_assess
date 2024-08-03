import unittest  # import the unittest testing framework
import union_data_capture  # import our app's main code module


class UnionDataUnitTests(unittest.TestCase):
    def test_name_entered_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("Baz Cookies")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_name_entered_check_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("")
        expect_output = False
        unexpect_output = {}  # objects are truthy
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_name_entered_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("Sarah Ritz")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, {"Forward": "W", "Back": "S", "Left": "A", "Right": "D"})

    def test_name_entered_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, dict)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ["TRUE", "FALSE"])

    def test_name_length_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_length_check("Emily Bourbon")
        expect_output = True
        unexpect_output = None  # nulls are falsy
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_name_length_check_fail_short(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_length_check("x")
        expect_output = False
        unexpect_output = "Truthy"  # strings are truthy
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_name_length_check_fail_long(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_length_check("Tarquin Penguin-Shortbread-Digestive")
        expect_output = False
        unexpect_output = 2  # numerical values except zero are truthy
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_name_length_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("Gianni Nice")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, {"Cat": 17, "Rabbit": 1000034, "Dog": 6, "Bird": 56})

    def test_name_length_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("y")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, [5, 100, 3])

    def test_name_format_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_format_check("Tejinder Oreo-O'Oreo")
        expect_output = True
        unexpect_output = 0  # zero is falsy
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_name_format_check_fail_symbols(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_format_check("Scott !£%$#")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_name_format_check_fail_numbers(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_format_check("Deb 1234")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_name_format_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("Saj Gingernut")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_name_format_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.name_entered_check("123#@{")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_dob_year_check_old_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_old("19-07-2000")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_dob_year_check_old_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_old("19-07-1900")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_dob_year_check_old_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_old("19-07-2000")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_dob_year_check_old_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_old("19-07-1900")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_dob_year_check_young_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_young("19-07-2000")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_dob_year_check_young_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_young("19-07-2020")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_dob_year_check_young_pass_type(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_old("19-07-2000")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_dob_year_check_young_fail_type(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.dob_year_check_young("19-07-2020")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_email_entered_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_entered_check("x")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_email_entered_check_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_entered_check("")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_email_entered_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_entered_check("x")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_email_entered_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_entered_check("")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_email_length_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_length_check("x")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_email_length_check_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_length_check("this is a sentence that needs to include at least fifty characters")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_email_length_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_length_check("x")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_email_length_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_length_check("this is a sentence that needs to include at least fifty characters")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_email_format_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_format_check("checkthis_test@email-address.{}+^")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_email_format_check_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_format_check("(])[£$")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_email_format_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_format_check("checkthis_test@email-address.£{}+^")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_email_format_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_format_check("(])[£$")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_email_ending_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_ending_check("test@bigcorpo.uk")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_email_ending_check_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_ending_check("test@smallbiz.nz")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_email_ending_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_ending_check("test@bigcorpo.uk")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_email_ending_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_ending_check("test@smallbiz.nz")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_email_start_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_start_check("test@")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_email_start_check_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_start_check("£$/")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_email_start_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_start_check("test@")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_email_start_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.email_start_check("£$/")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_role_selected_check_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.role_selected_check("Rep")
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_role_selected_check_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.role_selected_check("Select")
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_role_selected_check_type_pass(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.role_selected_check("Rep")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_role_selected_check_type_fail(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.role_selected_check("Select")
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_rep_resp_notrep_check_pass_rep(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_notrep_check(
            "Rep", ["True", "False", "False", "True", "True", "False"])
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_rep_resp_notrep_check_pass_notrep(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_notrep_check(
            "Advocate", ["False", "False", "False", "False", "False", "False"])
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_rep_resp_notrep_check_fail_notrep_resp(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_notrep_check(
            "Advocate", ["True", "False", "False", "True", "True", "False"])
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_rep_resp_notrep_check_type_pass_rep(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_notrep_check(
            "Rep", ["True", "False", "False", "True", "True", "False"])
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_rep_resp_notrep_check_type_pass_notrep(self):
        my_app = union_data_capture.UnionCollect()
        self.assertIsInstance(my_app.rep_resp_notrep_check(
            "Advocate", ["False", "False", "False", "False", "False", "False"]), bool)

    def test_rep_resp_notrep_check_type_fail_notrep_resp(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_notrep_check(
            "Advocate", ["True", "False", "False", "True", "True", "False"])
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))

    def test_rep_resp_rep_check_pass_notrep(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_rep_check(
            "Member", ["True", "False", "False", "True", "True", "False"])
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_rep_resp_rep_check_pass_rep(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_rep_check(
            "Rep", ["True", "False", "False", "False", "False", "False"])
        expect_output = True
        unexpect_output = False
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertTrue(app_output)
        self.assertIs(app_output, True)
        self.assertIn(app_output, [True])

    def test_rep_resp_rep_check_fail_rep_noresp(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_rep_check(
            "Rep", ["False", "False", "False", "False", "False", "False"])
        expect_output = False
        unexpect_output = True
        self.assertEqual(app_output, expect_output)
        self.assertNotEqual(app_output, unexpect_output)
        self.assertFalse(app_output)
        self.assertIs(app_output, False)
        self.assertIn(app_output, [False])

    def test_rep_resp_rep_check_type_pass_notrep(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_rep_check(
            "Member", ["True", "False", "False", "True", "True", "False"])
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_rep_resp_rep_check_type_pass_rep(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_rep_check(
            "Rep", ["True", "False", "False", "False", "False", "False"])
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, ("One", "Two", "Three"))

    def test_rep_resp_rep_check_type_fail_rep_noresp(self):
        my_app = union_data_capture.UnionCollect()
        app_output = my_app.rep_resp_rep_check(
            "Rep", ["False", "False", "False", "False", "False", "False"])
        self.assertIsInstance(app_output, bool)
        self.assertNotIsInstance(app_output, list)
        self.assertIsNotNone(app_output)
        self.assertNotIn(app_output, (234, 543, 6534))


if __name__ == '__main__':
    unittest.main(verbosity=1, exit=True)
    my_app = union_data_capture.UnionCollect()
    my_app.mainloop()
