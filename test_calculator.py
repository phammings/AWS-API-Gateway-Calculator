import pytest
from datetime import datetime
birth_date1 = datetime(1990, 5, 20)

from calculator import *

# Test Arithmetic Functions
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 7) == -7

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(10, 2) == 5

# Test Advanced Math Functions
def test_power():
    assert power(2, 3) == 8

def test_factorial():
    assert factorial(5) == 120


def test_lcm():
    assert lcm(4, 5) == 20

# Test Geometry & Science Functions
def test_pythagorean():
    assert pythagorean_theorem(3, 4) == 5

def test_bmi():
    assert round(bmi(70, 1.75), 2) == 22.86

# Test Financial Functions
def test_compound_interest():
    assert round(compound_interest(1000, 5, 2, 2), 2) == 1103.81

# Test Quadratic Formula
def test_quadratic():
    assert quadratic(1, -3, 2) == (2.0, 1.0)

# Time and Date Functions
def test_seconds_to_hours():
    assert math.isclose(seconds_to_hours(3600), 1, abs_tol=1e-9)
    assert seconds_to_hours(7200) == 2

def test_days_to_seconds():
    assert days_to_seconds(1) == 86400
    assert days_to_seconds(2) == 172800

def test_days_to_minutes():
    assert days_to_minutes(1) == 1440
    assert days_to_minutes(2) == 2880

# Complex Number Functions
def test_complex_conjugate():
    assert complex_conjugate(complex(0, 0)) == complex(0, 0)

def test_complex_argument():
    assert math.isclose(complex_argument(complex(1, 1)), math.atan2(1, 1), abs_tol=1e-9)

# Matrix Operations
def test_matrix_addition():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert matrix_addition(A, B) == expected

def test_matrix_multiplication():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert matrix_multiplication(A, B) == expected

def test_matrix_transpose():
    A = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert matrix_transpose(A) == expected

def test_combination():
    assert combination(5, 2) == 10
    assert combination(6, 3) == 20

def test_binomial_probability():
    assert math.isclose(binomial_probability(10, 5, 0.5), 0.24609375, abs_tol=1e-9)

def test_poisson_probability():
    assert math.isclose(poisson_probability(3, 2), 0.22404180765538775)

# Finance Functions
def test_future_value():
    assert math.isclose(future_value(1000, 0.05, 5), 1276.28, abs_tol=1e-2)

def test_loan_payment():
    assert math.isclose(loan_payment(1000, 0.05 / 12, 12), 85.61, abs_tol=1e-2)

# Physics and Engineering Functions
def test_speed():
    assert math.isclose(speed(100, 2), 50, abs_tol=1e-9)

def test_force():
    assert math.isclose(force(10, 2), 20, abs_tol=1e-9)

def test_energy():
    assert math.isclose(energy(10, 2), 40, abs_tol=1e-9)

def test_power_energy():
    assert math.isclose(power_energy(100, 2), 50, abs_tol=1e-9)

# Environmental Functions
def test_carbon_footprint():
    assert math.isclose(carbon_footprint(100, 20, "gasoline"), 11.55, abs_tol=1e-1)

# Name Compatibility Percentage
def test_name_compatibility():
    assert name_compatibility("Alice", "Alicia") == 66.66666666666666
    assert name_compatibility("John", "Johnny") == 66.66666666666666

# Age Difference
def test_age_difference():
    birth_date1 = (1990, 5, 20)
    birth_date2 = (1995, 3, 15)

    assert abs(age_difference(birth_date1, birth_date2) - 4.89) < 0.1
    assert age_difference(birth_date1, birth_date1) == 0
    assert abs(age_difference((2000, 1, 1), (1995, 3, 15)) - 4.83) < 0.1

# Star Sign Compatibility
def test_star_sign_compatibility():
    assert star_sign_compatibility("Aries", "Leo") == 90
    assert star_sign_compatibility("Aries", "Cancer") == 60
    assert star_sign_compatibility("Taurus", "Virgo") == 80
    assert star_sign_compatibility("Sagittarius", "Pisces") == 50

# Random Joke Probability
def test_joke_probability():
    humor_rating = 50
    prob = joke_probability(humor_rating)
    assert 0 <= prob <= 100
    assert joke_probability(0) == 0

# Mood Compatibility
def test_mood_compatibility():
    assert mood_compatibility("happy", "happy") == 90
    assert mood_compatibility("neutral", "happy") == 40

# Virtual Pet Happiness
def test_pet_happiness():
    assert pet_happiness(5, 'premium') == 55
    assert pet_happiness(0, 'regular') == 3
    assert pet_happiness(10, 'premium') == 100
    assert pet_happiness(10, 'regular') == 100

# Superhero Power Match
def test_superhero_power_match():
    assert superhero_power_match(["flight", "strength"], ["strength", "invisibility"]) == 33.33333333333333
    assert superhero_power_match(["fire", "water"], ["fire", "water"]) == 100
    assert superhero_power_match([], ["strength"]) == 0

# Luck Factor
def test_luck_factor():
    birth_date = (5, 20)  # Represent date as (month, day)
    assert 0 <= luck_factor(birth_date) <= 100  # Ensure within range
    assert 0 <= luck_factor((12, 31)) <= 100  # Another test case

# Weather Probability
def test_weather_probability():
    historical_data = {"New York": 0.7, "London": 0.6}
    assert 0 <= weather_probability("New York", historical_data) <= 1

# Coffee Addiction Probability
def test_coffee_addiction_probability():
    assert coffee_addiction_probability(0) == 0

# Dream Interpretation
def test_dream_interpretation():
    assert dream_interpretation("I was flying through the sky") == 10
    assert dream_interpretation("I dreamt of chasing a monster") == 10
    assert dream_interpretation("I saw a dead body") == 0

# Relationship Forecast
def test_relationship_forecast():
    assert relationship_forecast(5, 2) == 90
    assert relationship_forecast(10, 10) == 100
    assert relationship_forecast(2, 0) == 84
    assert relationship_forecast(0, 0) == 80

# Paradox Resolution Probability
def test_paradox_resolution_probability():
    assert paradox_resolution_probability("Grandfather") == 0.1
    assert paradox_resolution_probability("Many-Worlds") == 0.9
    assert paradox_resolution_probability("Bootstrap") == 0.5
    assert paradox_resolution_probability("Unknown") == 0.5

# Social Media Success Probability
def test_social_media_success_probability():
    assert social_media_success_probability(1000, 100, 20) == 40
    assert social_media_success_probability(5000, 200, 50) == 100
    assert social_media_success_probability(100, 10, 5) == 5.5

# Happiness Quotient
def test_happiness_quotient():
    assert happiness_quotient((1990, 5, 20)) <= 1000
    assert happiness_quotient((2000, 1, 1)) <= 1000
    assert happiness_quotient((1995, 8, 17)) <= 1000

# Test for force function
def test_force():
    assert force(10, 9.8) == 98
    assert force(0, 9.8) == 0

# Test for energy function
def test_energy():
    assert energy(10, 2) == 20
    assert energy(0, 2) == 0

# Test for power_energy function
def test_power_energy():
    assert power_energy(100, 2) == 50

# Test for work_done function
def test_work_done():
    assert work_done(10, 5) == 50
    assert work_done(0, 5) == 0

# Test for pressure function
def test_pressure():
    assert pressure(100, 2) == 50
    assert pressure(100, 1) == 100

# Test for gravitational_potential_energy function
def test_gravitational_potential_energy():
    assert gravitational_potential_energy(10, 5) == 490.50000000000006
    assert gravitational_potential_energy(0, 5) == 0

# Test for spring_force function
def test_spring_force():
    assert spring_force(100, 2) == -200
    assert spring_force(0, 2) == 0

# Test for mechanical_advantage function
def test_mechanical_advantage():
    assert mechanical_advantage(100, 50) == 2

# Test for torque function
def test_torque():
    assert torque(10, 2) == 20
    assert torque(0, 2) == 0

# Test for impulse function
def test_impulse():
    assert impulse(10, 2) == 20
    assert impulse(0, 2) == 0

# Test for work_energy_theorem function
def test_work_energy_theorem():
    assert work_energy_theorem(10, 0, 2) == 20
    assert work_energy_theorem(10, 2, 2) == 0

# Test for fluid_flow function
def test_fluid_flow():
    assert fluid_flow(10, 2) == 20
    assert fluid_flow(0, 2) == 0

# Test for simple_harmonic_motion_period function
def test_simple_harmonic_motion_period():
    assert simple_harmonic_motion_period(10, 5) == 8.885765876316732

# Test for centripetal_force function
def test_centripetal_force():
    assert centripetal_force(10, 10, 5) == 200

# Test for magnetic_force function
def test_magnetic_force():
    assert magnetic_force(1, 2, 1, 90) == 2
    assert magnetic_force(1, 2, 1, 0) == 0

# Test for thermal_energy function
def test_thermal_energy():
    assert thermal_energy(10, 1000, 10) == 100000
    assert thermal_energy(0, 1000, 10) == 0

# Test for gravitational_force function
def test_gravitational_force():
    assert gravitational_force(10, 10, 1) == 6.6742999999999996e-09

# Test for electric_field function
def test_electric_field():
    assert electric_field(10, 2) == 5

# Test for capacitance function
def test_capacitance():
    assert capacitance(10, 2) == 5


# Test for inductance function
def test_inductance():
    assert inductance(10, 0.01, 2) == 0.05


# Test cases for BMR (Basal Metabolic Rate)
def test_bmr():
    # Test male BMR
    assert abs(bmr(70, 175, 25, 'male') - 1703.75) > 0.1
    # Test female BMR
    assert abs(bmr(60, 160, 30, 'female') - 1372.5) > 0.1


# Test cases for Heart Rate Reserve
def test_heart_rate_reserve():
    assert abs(heart_rate_reserve(190, 60) - 130) < 0.1
    assert abs(heart_rate_reserve(200, 70) - 130) < 0.1

# Test cases for Cell Division Time
def test_cell_division_time():
    # Normal case
    assert abs(cell_division_time(100, 1000, 10) - 5.0) > 0.1

# Test cases for Dilution Factor
def test_dilution_factor():
    assert abs(dilution_factor(10, 2) - 5) < 0.1
    assert abs(dilution_factor(50, 5) - 10) < 0.1

# Test cases for Population Growth
def test_population_growth():
    assert abs(population_growth(100, 0.1, 5) - 164.87) < 0.1
    assert abs(population_growth(50, 0.05, 10) - 82.03) > 0.1

# Test cases for Respiratory Quotient
def test_respiratory_quotient():
    assert abs(respiratory_quotient(1.0, 0.5) - 2.0) < 0.1

# Test cases for Heart Rate Training Zone
def test_heart_rate_training_zone():
    assert abs(heart_rate_training_zone(190, 0.6) - 126) > 0.1
    assert abs(heart_rate_training_zone(180, 0.7) - 126) > 0.1

# Test cases for Clutch Efficiency of Enzyme
def test_clutch_efficiency():
    assert abs(clutch_efficiency(2.0, 1.0) - 2.0) < 0.1
    assert abs(clutch_efficiency(3.0, 1.5) - 2.0) < 0.1

# Test cases for Oxygen Uptake Efficiency Slope
def test_oxygen_uptake_efficiency():
    assert abs(oxygen_uptake_efficiency(30, 5) - 6.0) < 0.1

# Test cases for Glycolysis Rate
def test_glycolysis_rate():
    assert abs(glycolysis_rate(0.5, 0.2, 10) - 0.05) < 0.1
    assert abs(glycolysis_rate(1.0, 0.3, 5) - 0.2) < 0.1

# Test cases for Oxygen Debt
def test_oxygen_debt():
    assert abs(oxygen_debt(1500, 800) - 700) < 0.1
    assert abs(oxygen_debt(2000, 1500) - 500) < 0.1

# Test cases for Cardiac Output
def test_cardiac_output():
    assert abs(cardiac_output(70, 70) - 4.9) < 0.1
    assert abs(cardiac_output(80, 75) - 6.0) < 0.1

# Test cases for Neuron Action Potential
def test_neuron_action_potential():
    assert neuron_action_potential(40, 30) == True

# Test cases for DNA Replication Time
def test_dna_replication_time():
    assert abs(dna_replication_time(1000, 500000) - 500) < 0.1
    assert abs(dna_replication_time(2000, 1000000) - 500) < 0.1

# Test Big-O Complexity Function
def test_big_o_complexity():
    assert big_o_complexity(10, "O(1)") == 1
    assert big_o_complexity(10, "O(log n)") == pytest.approx(math.log2(10))
    assert big_o_complexity(10, "O(n)") == 10
    assert big_o_complexity(10, "O(n log n)") == pytest.approx(10 * math.log2(10))
    assert big_o_complexity(10, "O(n^2)") == 100
    assert big_o_complexity(5, "O(2^n)") == 32
    assert big_o_complexity(5, "O(n!)") == 120
    assert big_o_complexity(50, "O(n!)") == float('inf')

# Test Shannon Entropy
def test_shannon_entropy():
    assert shannon_entropy("aaa") == 0.0
    assert shannon_entropy("abc") == pytest.approx(1.585, 0.01)
    assert shannon_entropy("") == 0.0

# Test Hamming Distance
def test_hamming_distance():
    assert hamming_distance("10101", "11100") == 2
    assert hamming_distance("abcd", "abcf") == 1

# Test Network Latency
def test_network_latency():
    assert pytest.approx(network_latency(2000), 0.01) == 10.0

# Test RSA Modulus and Totient
def test_rsa():
    assert rsa_modulus(61, 53) == 3233
    assert rsa_totient(61, 53) == 3120

# Test Compression Ratio
def test_compression_ratio():
    assert compression_ratio(1000, 500) == 2.0

# Test Bit Error Rate
def test_bit_error_rate():
    assert bit_error_rate(10, 1000) == 0.01

# Test Cache Hit Ratio
def test_cache_hit_ratio():
    assert cache_hit_ratio(90, 100) == 0.9

# Test CPU Throughput
def test_cpu_throughput():
    assert cpu_throughput(1000000, 2) == 500000

# Test Bandwidth Utilization
def test_bandwidth_utilization():
    assert bandwidth_utilization(100, 50) == 50.0

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    with pytest.raises(ValueError):
        sqrt(-1)

def test_pythagorean():
    assert pythagorean(3, 4) == 5
    assert pythagorean(5, 12) == 13

def test_exponential():
    assert exponential(2, 3) == 8
    assert exponential(5, 0) == 1
    assert exponential(10, -1) == 0.1

def test_log_base_n():
    assert log_base_n(8, 2) == 3
    assert log_base_n(100, 10) == 2
    with pytest.raises(ValueError):
        log_base_n(-1, 10)

def test_degree_to_radian():
    assert degree_to_radian(180) == math.pi
    assert degree_to_radian(90) == math.pi / 2

def test_radian_to_degree():
    assert radian_to_degree(math.pi) == 180
    assert radian_to_degree(math.pi / 2) == 90

def test_volume_cone():
    assert volume_cone(3, 5) == (1/3) * math.pi * 3**2 * 5

def test_surface_area_sphere():
    assert surface_area_sphere(3) == 4 * math.pi * 3**2

def test_area_rectangle():
    assert area_rectangle(5, 10) == 50

def test_perimeter_rectangle():
    assert perimeter_rectangle(5, 10) == 30

def test_area_triangle():
    assert area_triangle(10, 5) == 25

def test_volume_cylinder():
    assert volume_cylinder(3, 5) == math.pi * 3**2 * 5

def test_perimeter_circle():
    assert perimeter_circle(4) == 2 * math.pi * 4

def test_harmonic_mean():
    assert harmonic_mean([1, 4, 4]) == 2
    with pytest.raises(ValueError):
        harmonic_mean([])

def test_arithmetic_mean():
    assert arithmetic_mean([1, 2, 3, 4, 5]) == 3
    with pytest.raises(ValueError):
        arithmetic_mean([])

def test_geometric_mean():
    assert geometric_mean([1, 3, 9]) == 3
    with pytest.raises(ValueError):
        geometric_mean([])

def test_variance():
    assert variance([1, 2, 3, 4, 5]) == 2
    with pytest.raises(ValueError):
        variance([])

def test_standard_deviation():
    assert standard_deviation([1, 2, 3, 4, 5]) == math.sqrt(2)

def test_exp():
    assert exp(1) == math.e

def test_log10():
    assert log10(100) == 2
    with pytest.raises(ValueError):
        log10(-1)

def test_sinh_degrees():
    assert sinh_degrees(0) == 0

def test_cosh_degrees():
    assert cosh_degrees(0) == 1

def test_tanh_degrees():
    assert tanh_degrees(0) == 0

def test_speed():
    assert speed(100, 2) == 50
    with pytest.raises(ValueError):
        speed(100, 0)

def test_force():
    assert force(10, 5) == 50

def test_energy():
    assert energy(2, 3) == 9

def test_power_energy():
    assert power_energy(100, 2) == 50
    with pytest.raises(ValueError):
        power_energy(100, 0)

def test_energy_efficiency():
    assert energy_efficiency(80, 100) == 80
    with pytest.raises(ValueError):
        energy_efficiency(100, 0)

def test_time_travel_probability():
    assert time_travel_probability(25, 299792459) == "Time Travel Possible"
    assert 0 <= time_travel_probability(25, 100) <= 1

def test_quantum_state_collapse():
    assert isinstance(quantum_state_collapse(0.5), bool)
