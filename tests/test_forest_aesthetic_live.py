from pathlib import Path
import re
import unittest


APP = Path(__file__).parents[1] / "index.html"


class ForestAestheticLiveTrackerTests(unittest.TestCase):
    def setUp(self):
        self.html = APP.read_text(encoding="utf-8")

    def test_uses_the_selected_forest_aesthetic_preview_title(self):
        self.assertIn("<title>Steady 75 — Forest Aesthetic</title>", self.html)

    def test_keeps_the_tracker_controls_and_persistence(self):
        for required in (
            'id="settingsBtn"', 'id="prevDay"', 'id="nextDay"',
            'id="habitList"', 'id="nudgeBtn"', 'id="resetBtn"',
            "localStorage", "function render()",
        ):
            self.assertIn(required, self.html)

    def test_renders_the_preview_style_surface_and_accessible_habit_checkboxes(self):
        for required in ("class=\"frame\"", "class=\"aura\"", "class=\"flower\"", 'class="check" type="checkbox"'):
            self.assertIn(required, self.html)

    def test_uses_a_real_forest_photo_not_abstract_background_shapes(self):
        self.assertIn("assets/images/forest-wellness-background.jpg", self.html)
        self.assertIn(".frame:before,.frame:after,.float{display:none!important}", self.html)

    def test_defaults_to_the_five_daily_75_hard_requirements(self):
        for requirement in (
            "Two 45-minute workouts — one outdoors",
            "Follow your diet — no cheat meals or alcohol",
            "Drink one gallon of water",
            "Read 10 pages of a non-fiction book",
            "Take a progress photo",
        ):
            self.assertIn(requirement, self.html)

    def test_has_no_per_promise_ellipsis_or_edit_actions(self):
        self.assertNotIn('class="more edit"', self.html)
        self.assertNotIn('aria-label="Edit ${esc(title)}"', self.html)
        self.assertIn("Every requirement resets at midnight.", self.html)

    def test_today_standard_uses_reference_matched_fused_flower_not_orb_rings(self):
        self.assertIn("/* Reference-matched fused four-lobed flower for the Today Standard panel. */", self.html)
        self.assertIn('<svg class="flower"', self.html)
        self.assertIn('id="flowerPetalMaterial"', self.html)
        self.assertIn('id="flowerSoftShadow"', self.html)
        self.assertNotIn("mask:radial-gradient(ellipse at 28% 28%", self.html)
        self.assertNotIn("radial-gradient(circle at 72% 46%", self.html)

    def test_includes_the_forest_background_asset_for_public_deployment(self):
        self.assertTrue((APP.parent / "assets/images/forest-wellness-background.jpg").is_file())


if __name__ == "__main__":
    unittest.main()
