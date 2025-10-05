import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import color_tools # type: ignore

# This is a sample unit test library
# you can run this by going into the folder and running
# python3 test_color_tools.py   
# or use python is on windows
# this will only work if you at least have each functions stub in place (or you will need to comment out functions)


class TestColorTools(unittest.TestCase):

    # EASY TESTS
    def test_contrast_ratio_basic(self) -> None:
        """Tests contrast_ratio with basic color combinations."""
        self.assertEqual(round(color_tools.contrast_ratio(0, 0, 0, 255, 255, 255), 1), 21.0, "contrast_ratio(0, 0, 0, 255, 255, 255) expected 21.0. Black on white should have maximum contrast")
        self.assertEqual(round(color_tools.contrast_ratio(255, 255, 255, 255, 255, 255), 1), 1.0, "contrast_ratio(255, 255, 255, 255, 255, 255) expected 1.0. Identical colors should have 1:1 ratio")
        self.assertEqual(round(color_tools.contrast_ratio(128, 128, 128, 255, 255, 255), 1), 3.9, "contrast_ratio(128, 128, 128, 255, 255, 255) expected 3.9. Check your luminance calculations")

    def test_passes_wcag_level_basic(self) -> None:
        """Tests passes_wcag_level with standard ratios."""
        self.assertTrue(color_tools.passes_wcag_level(4.5, "AA_NORMAL"), "passes_wcag_level(4.5, \"AA_NORMAL\") expected True. 4.5:1 exactly meets AA normal standard")
        self.assertFalse(color_tools.passes_wcag_level(4.0, "AA_NORMAL"), "passes_wcag_level(4.0, \"AA_NORMAL\") expected False. 4.0:1 does not meet AA normal standard")
        self.assertTrue(color_tools.passes_wcag_level(7.0, "AAA_NORMAL"), "passes_wcag_level(7.0, \"AAA_NORMAL\") expected True. 7.0:1 exactly meets AAA normal standard")

    def test_calculate_brightness_basic(self) -> None:
        """Tests calculate_brightness with standard colors."""
        self.assertEqual(color_tools.calculate_brightness(255, 255, 255), 255, "calculate_brightness(255, 255, 255) expected 255. White should have maximum brightness")
        self.assertEqual(color_tools.calculate_brightness(0, 0, 0), 0, "calculate_brightness(0, 0, 0) expected 0. Black should have zero brightness")
        self.assertEqual(color_tools.calculate_brightness(255, 0, 0), 76, "calculate_brightness(255, 0, 0) expected 76. Check your brightness coefficients")

    def test_recommend_adjustment_basic(self) -> None:
        """Tests recommend_adjustment with clear scenarios."""
        self.assertEqual(color_tools.recommend_adjustment(3.0, 4.5), 'Increase contrast by making colors more different', "recommend_adjustment(3.0, 4.5) - small gap should suggest minor improvement")
        self.assertEqual(color_tools.recommend_adjustment(5.0, 4.5), 'Contrast ratio already meets target', "recommend_adjustment(5.0, 4.5) - current exceeds target should indicate success")
        self.assertEqual(color_tools.recommend_adjustment(2.0, 7.0), 'Significant contrast improvement needed - consider much darker or lighter colors', "recommend_adjustment(2.0, 7.0) - large gap should suggest major changes")

    def test_find_minimum_brightness_steps_basic(self) -> None:
        """Tests find_minimum_brightness_steps with standard cases."""
        self.assertEqual(color_tools.find_minimum_brightness_steps(0, 0, 0, 50), 50, "find_minimum_brightness_steps(0, 0, 0, 50) expected 50. Each step increases brightness by ~1")
        self.assertEqual(color_tools.find_minimum_brightness_steps(100, 100, 100, 50), 0, "find_minimum_brightness_steps(100, 100, 100, 50) expected 0. Already bright enough")
        self.assertEqual(color_tools.find_minimum_brightness_steps(10, 20, 30, 100), 82, "find_minimum_brightness_steps(10, 20, 30, 100) expected 82. Check your while loop logic")

    def test_calculate_contrast_with_grays_basic(self) -> None:
        """Tests calculate_contrast_with_grays with primary colors."""
        self.assertEqual(color_tools.calculate_contrast_with_grays(0, 0, 0), 28, "calculate_contrast_with_grays(0, 0, 0) expected 28. Black has good contrast with many grays")
        self.assertEqual(color_tools.calculate_contrast_with_grays(255, 255, 255), 24, "calculate_contrast_with_grays(255, 255, 255) expected 24. White has good contrast with dark grays")
        self.assertEqual(color_tools.calculate_contrast_with_grays(128, 128, 128), 5, "calculate_contrast_with_grays(128, 128, 128) expected 5. Mid-gray has limited contrast options")

    def test_find_accessible_gray_background_basic(self) -> None:
        """Tests find_accessible_gray_background with standard text colors."""
        self.assertEqual(color_tools.find_accessible_gray_background(0, 0, 0), 117, "find_accessible_gray_background(0, 0, 0) expected 117. Darkest gray for black text")
        self.assertEqual(color_tools.find_accessible_gray_background(255, 255, 255), 0, "find_accessible_gray_background(255, 255, 255) expected 0. White text needs very dark background")
        self.assertEqual(color_tools.find_accessible_gray_background(100, 100, 100), 225, "find_accessible_gray_background(100, 100, 100) expected 225. Dark gray text needs light background")

    # HARDER TESTS 
    def test_contrast_ratio_edge_cases(self) -> None:
        """Tests contrast_ratio with edge cases and boundary conditions."""
        # Test reversed colors (should give same ratio)
        ratio1 = color_tools.contrast_ratio(0, 0, 0, 128, 128, 128)
        ratio2 = color_tools.contrast_ratio(128, 128, 128, 0, 0, 0)
        self.assertAlmostEqual(ratio1, ratio2, places=2, msg="contrast_ratio should give same result regardless of color order")
        
        # Test very similar colors
        self.assertLess(color_tools.contrast_ratio(100, 100, 100, 101, 101, 101), 1.1, "Very similar colors should have low contrast ratio")
        
        # Test pure RGB colors
        red_white = round(color_tools.contrast_ratio(255, 0, 0, 255, 255, 255), 1)
        self.assertEqual(red_white, 4.0, "contrast_ratio(255, 0, 0, 255, 255, 255) expected 4.0. Red on white contrast")

    def test_passes_wcag_level_edge_cases(self) -> None:
        """Tests passes_wcag_level with boundary values and invalid inputs."""
        # Test exact boundary values
        self.assertTrue(color_tools.passes_wcag_level(3.0, "AA_LARGE"), "passes_wcag_level(3.0, \"AA_LARGE\") expected True. Exactly meets AA large text standard")
        self.assertFalse(color_tools.passes_wcag_level(2.99, "AA_LARGE"), "passes_wcag_level(2.99, \"AA_LARGE\") expected False. Just below AA large text threshold")
        
        # Test all four levels
        self.assertTrue(color_tools.passes_wcag_level(4.5, "AAA_LARGE"), "AAA_LARGE has same threshold as AA_NORMAL")
        self.assertFalse(color_tools.passes_wcag_level(6.9, "AAA_NORMAL"), "6.9:1 should not meet AAA normal (7.0:1)")
        
        # Test invalid level
        self.assertFalse(color_tools.passes_wcag_level(10.0, "INVALID"), "Invalid level string should return False")

    def test_calculate_brightness_edge_cases(self) -> None:
        """Tests calculate_brightness with edge cases and color extremes."""
        # Test pure color channels
        self.assertEqual(color_tools.calculate_brightness(255, 0, 0), 76, "Pure red brightness")
        self.assertEqual(color_tools.calculate_brightness(0, 255, 0), 149, "Pure green brightness (highest coefficient)")
        self.assertEqual(color_tools.calculate_brightness(0, 0, 255), 29, "Pure blue brightness (lowest coefficient)")
        
        # Test that green dominates the formula
        green_brightness = color_tools.calculate_brightness(0, 255, 0)
        red_brightness = color_tools.calculate_brightness(255, 0, 0)
        blue_brightness = color_tools.calculate_brightness(0, 0, 255)
        self.assertGreater(green_brightness, red_brightness, "Green should contribute more to brightness than red")
        self.assertGreater(red_brightness, blue_brightness, "Red should contribute more to brightness than blue")

    def test_recommend_adjustment_boundary_conditions(self) -> None:
        """Tests recommend_adjustment with boundary conditions around the 1.5 threshold."""
        # Test exactly at threshold
        self.assertEqual(color_tools.recommend_adjustment(3.0, 4.5), 'Increase contrast by making colors more different', "Gap of exactly 1.5 should suggest minor improvement")
        
        # Test just over threshold  
        self.assertEqual(color_tools.recommend_adjustment(2.9, 4.5), 'Significant contrast improvement needed - consider much darker or lighter colors', "Gap of 1.6 should suggest major improvement")
        
        # Test negative gap (already exceeding target)
        self.assertEqual(color_tools.recommend_adjustment(8.0, 4.5), 'Contrast ratio already meets target', "Higher current than target should indicate already meeting")

    def test_find_minimum_brightness_steps_edge_cases(self) -> None:
        """Tests find_minimum_brightness_steps with challenging scenarios."""
        # Test when target is impossible to reach
        steps = color_tools.find_minimum_brightness_steps(200, 200, 200, 300)
        self.assertGreater(steps, 0, "Should return positive steps even when target unreachable")
        
        # Test with one channel already at maximum
        steps = color_tools.find_minimum_brightness_steps(255, 0, 0, 150)
        self.assertGreater(steps, 0, "Should handle mixed channel values correctly")
        
        # Test exact target match
        current_brightness = color_tools.calculate_brightness(100, 150, 200)
        steps = color_tools.find_minimum_brightness_steps(100, 150, 200, current_brightness)
        self.assertEqual(steps, 0, "Steps should be 0 when already at exact target brightness")

    def test_calculate_contrast_with_grays_edge_cases(self) -> None:
        """Tests calculate_contrast_with_grays with extreme and boundary cases."""
        # Test colors that should have maximum compatibility
        black_grays = color_tools.calculate_contrast_with_grays(0, 0, 0)
        white_grays = color_tools.calculate_contrast_with_grays(255, 255, 255)
        self.assertGreater(black_grays, 20, "Black should be compatible with many gray levels")
        self.assertGreater(white_grays, 20, "White should be compatible with many gray levels")
        
        # Test mid-range color (should have fewer compatible grays)
        mid_grays = color_tools.calculate_contrast_with_grays(128, 128, 128)
        self.assertLess(mid_grays, black_grays, "Mid-gray should have fewer compatible grays than black")
        self.assertLess(mid_grays, white_grays, "Mid-gray should have fewer compatible grays than white")
        
        # Test that function counts correctly (should test 52 total grays: 0,5,10...255)
        total_grays_tested = (255 // 5) + 1  # 52 total values
        self.assertLessEqual(black_grays, total_grays_tested, "Cannot have more compatible grays than total tested")

    def test_find_accessible_gray_background_edge_cases(self) -> None:
        """Tests find_accessible_gray_background with challenging text colors."""
        # Test with very bright text (should need very dark backgrounds)
        bright_text_gray = color_tools.find_accessible_gray_background(200, 200, 200)
        self.assertLess(bright_text_gray, 100, "Bright text should require dark background")
        
        # Test with very dark text (should allow lighter backgrounds)
        dark_text_gray = color_tools.find_accessible_gray_background(50, 50, 50)
        self.assertGreater(dark_text_gray, 150, "Dark text should allow lighter backgrounds")
        
        # Test mid-range text
        mid_text_gray = color_tools.find_accessible_gray_background(128, 128, 128)
        self.assertTrue(0 <= mid_text_gray <= 255, "Should return valid gray value for mid-range text")
        
        # Verify the returned gray actually provides sufficient contrast
        test_text_r, test_text_g, test_text_b = 100, 100, 100
        result_gray = color_tools.find_accessible_gray_background(test_text_r, test_text_g, test_text_b)
        result_contrast = color_tools.contrast_ratio(test_text_r, test_text_g, test_text_b, result_gray, result_gray, result_gray)
        self.assertGreaterEqual(result_contrast, 4.5, "Returned gray background should actually provide AA contrast")

    def test_while_loop_functions_integration(self) -> None:
        """Tests integration between while loop functions and core accessibility functions."""
        # Test that brightness steps function works correctly with calculate_brightness
        start_r, start_g, start_b = 50, 75, 100
        target_brightness = 150
        steps = color_tools.find_minimum_brightness_steps(start_r, start_g, start_b, target_brightness)
        
        if steps > 0:
            # Verify the logic: after 'steps' increments, brightness should meet target
            final_r = min(start_r + steps, 255)
            final_g = min(start_g + steps, 255) 
            final_b = min(start_b + steps, 255)
            final_brightness = color_tools.calculate_brightness(final_r, final_g, final_b)
            self.assertGreaterEqual(final_brightness, target_brightness, "After calculated steps, brightness should meet target")
        
        # Test that gray compatibility and gray background functions are consistent
        test_color = (100, 150, 200)
        gray_count = color_tools.calculate_contrast_with_grays(*test_color)
        best_gray = color_tools.find_accessible_gray_background(*test_color)
        
        # The best gray should provide at least AA contrast
        best_contrast = color_tools.contrast_ratio(*test_color, best_gray, best_gray, best_gray)
        self.assertGreaterEqual(best_contrast, 4.5, "Best gray background should provide AA contrast")
        
        # If any grays are compatible, the best gray should be among them
        if gray_count > 0:
            self.assertLessEqual(best_gray, 255, "Best gray should be a valid gray value")


    def test_function_robustness(self) -> None:
        """Tests functions with extreme values and boundary conditions."""
        # Test contrast ratio with extreme luminance differences
        extreme_contrast = color_tools.contrast_ratio(0, 0, 1, 255, 255, 254)
        self.assertGreater(extreme_contrast, 15.0, "Near-black and near-white should have very high contrast")
        
        # Test brightness steps with impossible targets
        impossible_steps = color_tools.find_minimum_brightness_steps(250, 250, 250, 300)
        self.assertGreater(impossible_steps, 0, "Should return steps attempted even when target unreachable")
        
        # Test gray compatibility with extreme colors
        extreme_bright_grays = color_tools.calculate_contrast_with_grays(254, 254, 254)
        extreme_dark_grays = color_tools.calculate_contrast_with_grays(1, 1, 1)
        self.assertGreater(extreme_bright_grays, 0, "Near-white should be compatible with some grays")
        self.assertGreater(extreme_dark_grays, 0, "Near-black should be compatible with some grays")


if __name__ == '__main__':
    unittest.main()

