#!/usr/bin/env python3
"""Unit tests for proofread script."""
#
# (C) Pywikibot team, 2015-2023
#
# Distributed under the terms of the MIT license.
#
import unittest
import proofread as cd


class TestSpecificFunctions(unittest.TestCase):

    def test_get_disambig_candidates(self):
        result = cd.get_disambig_candidates("شیر")
        self.assertIn("خلیج شیر", result)
        self.assertIn("شیر (وسیله)|شیر", result)

    def test_process_ambiguous_links(self):
        html = '<a href="" class="mw-disambig" title="شیر">شیر آب</a>'
        res = cd.process_ambiguous_links(html)
        self.assertEqual(res[0]["type"], 8)
        self.assertIn("خلیج شیر", res[0]["suggestions"])
        self.assertIn("شیر (وسیله)|شیر", res[0]["suggestions"])

    def test_suggest_spaced_conjunction(self):
        self.assertEqual(cd.suggest_spaced_conjunction("بااندیشه"), "با اندیشه")
        self.assertEqual(cd.suggest_spaced_conjunction("درفکر"), "در فکر")

    def test_find_asymmetrical_quotation_marks(self):
        self.assertEqual(cd.find_asymmetrical_quotation_marks(""), [])
        self.assertEqual(cd.find_asymmetrical_quotation_marks("متن «درست»"), [])
        self.assertEqual(
            cd.find_asymmetrical_quotation_marks("متن «نادرست"), ["«نادرست"]
        )
        self.assertEqual(
            cd.find_asymmetrical_quotation_marks("متن «درست» و نادرست»"), [" و نادرست»"]
        )
        self.assertEqual(
            cd.find_asymmetrical_quotation_marks(
                "متن «[[نادرست]] و «[[چهارم درست|درست]]»"
            ),
            ["«نادرست و "]
        )

        # special case: currently, not caught by the algorithm
        self.assertEqual(
            cd.find_asymmetrical_quotation_marks(
                "متن نادرست» و «نادرست [[با پیوند]] و مخلفات"
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
