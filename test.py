import math
import unittest

from project_euler import int_grid_creator, product_series, vertical_product_helper, adjacent_product_helper_up_down, \
    adjacent_product_helper_down_up, find_nth_triangular_number, find_div_of_number, find_highly_div_tri_num

int_series = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
input = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8,
         49, 9, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0, 81, 49, 31,
         73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65,
         52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91,
         22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80,
         24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50,
         32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70,
         67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21,
         24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72,
         21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95,
         78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92,
         16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57,
         86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58,
         19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40,
         4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66,
         88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69,
         4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36,
         20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16,
         20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54,
         1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

grid_input = int_grid_creator(input, 20, 20)


class TestProjectEuler(unittest.TestCase):
    def test_int_grid_creator(self):
        result = int_grid_creator(input, 20, 20)
        assert len(result) == 20
        assert len(result[-1]) == 20

    def test_product_series(self):
        test_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected_result = math.prod(test_row[-4:])
        assert product_series(test_row, 4) == expected_result
        assert product_series(grid_input[0], 4) == 4204200
        test_row.reverse()
        assert product_series(test_row, 4) == expected_result

    def test_vertical_product_helper(self):
        test_column_1 = [[8], [49], [73], [52], [22], [24], [21], [78], [16], [86], [19], [4], [88], [4],
                         [20], [20], [1], [3], [19], [31]]
        test_column_2 = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16],
                         [17], [18], [19]]

        assert vertical_product_helper(test_column_1, 4, 0) == 4092088
        assert vertical_product_helper(test_column_2, 4, 0) == 93024
        assert vertical_product_helper(grid_input, 4, 0) == 4540536

    def test_adjacent_product_helper_up_down(self):
        assert adjacent_product_helper_up_down(grid_input, 4, 0) == 5849100

    def test_adjacent_product_helper_down_up(self):
        assert adjacent_product_helper_down_up(grid_input, 4, 19) == 22289904

    def test_find_nth_triangular_number(self):
        assert find_nth_triangular_number(7) == 28
        assert find_nth_triangular_number(8) == 36

    def test_find_div_of_num(self):
        assert find_div_of_number(28) == {1, 2, 4, 7, 14, 28}
        assert find_div_of_number(21) == {1, 3, 7, 21}
        assert find_div_of_number(15) == {1, 3, 5, 15}
        assert find_div_of_number(10) == {1, 2, 5, 10}
        assert find_div_of_number(6) == {1, 2, 3, 6}
        assert find_div_of_number(3) == {1, 3}
        assert find_div_of_number(1) == {1}

    def test_highly_div_tri_number(self):
        assert find_highly_div_tri_num(5) == 28
        print(find_highly_div_tri_num(500))




if __name__ == '__main__':
    unittest.main()
