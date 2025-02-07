"""
Comprehensive Python Calculator Library
Supports arithmetic, scientific, financial, geometric, and health calculations.
"""
import datetime
import math
import random


def add(a, b):
    """Returns the sum of two numbers"""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers"""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Returns base raised to the power of exponent"""
    return base ** exponent

def sqrt(n):
    """Returns the square root of a number"""
    if n < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(n)

def pythagorean(a, b):
    """Returns the hypotenuse of a right triangle given two sides"""
    return math.sqrt(a**2 + b**2)

def bmi(weight, height):
    """Calculates Body Mass Index (BMI)"""
    if height <= 0:
        raise ValueError("Height must be positive")
    return weight / (height ** 2)

def simple_interest(principal, rate, time):
    """Calculates simple interest"""
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time, n):
    """Calculates compound interest"""
    return principal * (1 + rate / (n * 100)) ** (n * time)

def area_circle(radius):
    """Calculates the area of a circle"""
    return math.pi * radius ** 2

def volume_sphere(radius):
    """Calculates the volume of a sphere"""
    return (4/3) * math.pi * radius ** 3

def sin_degrees(angle):
    """Returns the sine of an angle in degrees"""
    return math.sin(math.radians(angle))

def cos_degrees(angle):
    """Returns the cosine of an angle in degrees"""
    return math.cos(math.radians(angle))

def tan_degrees(angle):
    """Returns the tangent of an angle in degrees"""
    return math.tan(math.radians(angle))

# Additional Methods

def factorial(n):
    """Returns the factorial of a number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def gcd(a, b):
    """Returns the greatest common divisor of two numbers"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Returns the least common multiple of two numbers"""
    return abs(a * b) // gcd(a, b)

def quadratic(a, b, c):
    """Returns the solutions to the quadratic equation ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)

def pythagorean_theorem(a, b):
    """Returns the hypotenuse of a right triangle using Pythagorean theorem"""
    return math.sqrt(a**2 + b**2)

def exponential(n, exp):
    """Returns n raised to the power of exp"""
    return n ** exp

def log_base_n(n, base):
    """Returns the logarithm of n to a given base"""
    return math.log(n, base)

def degree_to_radian(degree):
    """Converts degrees to radians"""
    return math.radians(degree)

def radian_to_degree(radian):
    """Converts radians to degrees"""
    return math.degrees(radian)

def volume_cone(radius, height):
    """Calculates the volume of a cone"""
    return (1/3) * math.pi * radius**2 * height

def surface_area_sphere(radius):
    """Calculates the surface area of a sphere"""
    return 4 * math.pi * radius**2

def area_rectangle(length, width):
    """Calculates the area of a rectangle"""
    return length * width

def perimeter_rectangle(length, width):
    """Calculates the perimeter of a rectangle"""
    return 2 * (length + width)

def area_triangle(base, height):
    """Calculates the area of a triangle"""
    return (base * height) / 2

def volume_cylinder(radius, height):
    """Calculates the volume of a cylinder"""
    return math.pi * radius**2 * height

def perimeter_circle(radius):
    """Calculates the perimeter (circumference) of a circle"""
    return 2 * math.pi * radius

def harmonic_mean(values):
    """Returns the harmonic mean of a list of numbers"""
    if not values:
        raise ValueError("List of values cannot be empty")
    return len(values) / sum(1 / x for x in values)

def arithmetic_mean(values):
    """Returns the arithmetic mean (average) of a list of numbers"""
    if not values:
        raise ValueError("List of values cannot be empty")
    return sum(values) / len(values)

def geometric_mean(values):
    """Returns the geometric mean of a list of numbers"""
    if not values:
        raise ValueError("List of values cannot be empty")
    product = 1
    for x in values:
        product *= x
    return product ** (1 / len(values))

def variance(values):
    """Returns the variance of a list of numbers"""
    if not values:
        raise ValueError("List of values cannot be empty")
    mean = arithmetic_mean(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def standard_deviation(values):
    """Returns the standard deviation of a list of numbers"""
    return math.sqrt(variance(values))

# Advanced Math Functions

def exp(n):
    """Returns the exponential value of a number"""
    return math.exp(n)

def log10(n):
    """Returns the logarithm of a number with base 10"""
    if n <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log10(n)

def sinh_degrees(angle):
    """Returns the hyperbolic sine of an angle in degrees"""
    return math.sinh(math.radians(angle))

def cosh_degrees(angle):
    """Returns the hyperbolic cosine of an angle in degrees"""
    return math.cosh(math.radians(angle))

def tanh_degrees(angle):
    """Returns the hyperbolic tangent of an angle in degrees"""
    return math.tanh(math.radians(angle))

# Time and Date Functions

def seconds_to_hours(seconds):
    """Converts seconds to hours"""
    return seconds / 3600

def minutes_to_hours(minutes):
    """Converts minutes to hours"""
    return minutes / 60

def days_to_seconds(days):
    """Converts days to seconds"""
    return days * 86400

def days_to_minutes(days):
    """Converts days to minutes"""
    return days * 1440

# Complex Number Functions

def complex_conjugate(c):
    """Returns the conjugate of a complex number"""
    return complex(c.real, -c.imag)

def complex_magnitude(c):
    """Returns the magnitude (absolute value) of a complex number"""
    return abs(c)

def complex_argument(c):
    """Returns the argument (angle) of a complex number in radians"""
    return math.atan2(c.imag, c.real)

# Matrix Operations

def matrix_addition(A, B):
    """Returns the sum of two matrices A and B"""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_multiplication(A, B):
    """Returns the product of two matrices A and B"""
    if len(A[0]) != len(B):
        raise ValueError("Matrix multiplication requires A's columns to match B's rows")
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def matrix_transpose(A):
    """Returns the transpose of a matrix A"""
    return [list(x) for x in zip(*A)]

# Probability and Statistics Functions

def permutation(n, r):
    """Returns the number of permutations of n items taken r at a time"""
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    """Returns the number of combinations of n items taken r at a time"""
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def binomial_probability(n, k, p):
    """Returns the binomial probability P(X = k) for a binomial distribution"""
    return (math.comb(n, k)) * (p**k) * ((1 - p)**(n - k))

def poisson_probability(lmbda, k):
    """Returns the Poisson probability P(X = k) for a given lambda"""
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

# Finance Functions

def future_value(principal, rate, time):
    """Calculates the future value of an investment"""
    return principal * (1 + rate)**time

def present_value(future_value, rate, time):
    """Calculates the present value of a future sum"""
    return future_value / (1 + rate)**time

def loan_payment(principal, rate, time):
    """Calculates the payment for a loan"""
    return principal * (rate * (1 + rate)**time) / ((1 + rate)**time - 1)

# Environmental Functions

def carbon_footprint(distance, fuel_efficiency, fuel_type="gasoline"):
    """Calculates carbon footprint based on distance, fuel efficiency, and fuel type"""
    fuel_emission_factors = {
        "gasoline": 2.31,  # kg CO2 per liter of gasoline
        "diesel": 2.68,    # kg CO2 per liter of diesel
    }
    emission_factor = fuel_emission_factors.get(fuel_type.lower(), 2.31)  # Default to gasoline
    fuel_consumed = distance / fuel_efficiency
    return fuel_consumed * emission_factor

def energy_efficiency(power_output, power_input):
    """Calculates the energy efficiency of a system"""
    if power_input == 0:
        raise ValueError("Power input cannot be zero")
    return (power_output / power_input) * 100

# Name Compatibility Percentage
def name_compatibility(name1, name2):
    common_letters = len(set(name1.lower()) & set(name2.lower()))
    max_length = max(len(name1), len(name2))
    return (common_letters / max_length) * 100

# Age Difference
def age_difference(birth_date1, birth_date2):
    # Extract year, month, and day from tuples
    year1, month1, day1 = birth_date1
    year2, month2, day2 = birth_date2

    # Approximate total days lived
    days1 = year1 * 365 + month1 * 30 + day1
    days2 = year2 * 365 + month2 * 30 + day2

    # Convert days to years and return absolute difference
    return abs(days1 - days2) / 365.25


# Star Sign Compatibility (Fictional)
def star_sign_compatibility(sign1, sign2):
    compatibility = {
        ("Aries", "Leo"): 90, ("Aries", "Cancer"): 60, ("Leo", "Sagittarius"): 85,
        ("Taurus", "Virgo"): 80, ("Gemini", "Libra"): 75, ("Cancer", "Pisces"): 95
    }
    return compatibility.get((sign1, sign2), 50)  # Default compatibility

# Random Joke Probability
def joke_probability(humor_rating):
    return min(humor_rating * random.uniform(0.5, 1.5), 100)

# Time Travel Probability (Fictional)
def time_travel_probability(age, speed):
    if speed > 299792458:  # Speed of light in m/s
        return "Time Travel Possible"
    return random.uniform(0, 1) * (age / 100)  # Fictional formula

# Mood Compatibility
def mood_compatibility(mood1, mood2):
    compatible_moods = {
        ("happy", "happy"): 90, ("happy", "sad"): 50, ("sad", "sad"): 60
    }
    return compatible_moods.get((mood1, mood2), 40)  # Default compatibility

# Quantum State Collapse (Fictional)
def quantum_state_collapse(probability):
    return random.uniform(0, 1) < probability  # Fictional simulation

# Virtual Pet Happiness
def pet_happiness(interactions, food_type):
    happiness = (interactions * 10) + (5 if food_type == 'premium' else 3)
    return min(happiness, 100)

# Superhero Power Match
def superhero_power_match(hero1_powers, hero2_powers):
    common_powers = len(set(hero1_powers) & set(hero2_powers))
    total_powers = len(set(hero1_powers) | set(hero2_powers))
    return (common_powers / total_powers) * 100

# Luck Factor
def luck_factor(birth_date):
    """Calculates a 'luck factor' based on birth month and day."""
    month, day = birth_date  # Unpack tuple (month, day)
    lucky_number = sum(int(digit) for digit in str(month)) + day
    return lucky_number % 100  # Fake luck factor

# Weather Probability
def weather_probability(location, historical_data):
    return random.uniform(0, 1) * historical_data.get(location, 0.5)

# Coffee Addiction Probability
def coffee_addiction_probability(daily_cups):
    return min(daily_cups * 10, 100)  # Fictional addiction scale

# Chocolate Enjoyment
def chocolate_enjoyment(sweetness, bitterness):
    return max(0, 100 - abs(sweetness - bitterness))

# Dream Interpretation
def dream_interpretation(dream_description):
    keywords = ["flying", "water", "death", "chasing", "teeth"]
    score = sum(dream_description.count(keyword) for keyword in keywords)
    return score * 10  # Fictional score

# Relationship Forecast
def relationship_forecast(relationship_length, arguments):
    return min(100 - (arguments * 2), 80) + (relationship_length * 2)

# Paradox Resolution Probability
def paradox_resolution_probability(paradox_type):
    resolution_probabilities = {
        "Grandfather": 0.1, "Bootstrap": 0.5, "Many-Worlds": 0.9
    }
    return resolution_probabilities.get(paradox_type, 0.5)

# Astrological Life Path Number
def life_path_number(birth_date):
    year, month, day = birth_date  # Unpack the tuple
    number = sum(int(digit) for digit in str(year) + str(month) + str(day))
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number


# Social Media Success Probability
def social_media_success_probability(followers, posts, engagement):
    return min((followers * 0.01) + (posts * 0.2) + (engagement * 0.5), 100)

# Happiness Quotient
def happiness_quotient(birth_date):
    year, month, day = birth_date  # Unpack the tuple
    base_score = year % 100  # Extract last two digits of the year
    return base_score * random.uniform(0.5, 1.5)


# Speed Calculation
def speed(distance, time):
    """Calculates speed given distance and time"""
    if time == 0:
        raise ValueError("Time cannot be zero")
    return distance / time

# Force Calculation (F = m * a)
def force(mass, acceleration):
    """Calculates force given mass and acceleration"""
    return mass * acceleration

# Energy Calculation (Kinetic Energy = 0.5 * m * v^2)
def energy(mass, velocity):
    """Calculates kinetic energy given mass and velocity"""
    return 0.5 * mass * velocity ** 2

# Power from Energy Calculation (P = E / t)
def power_energy(energy, time):
    """Calculates power from energy and time"""
    if time == 0:
        raise ValueError("Time cannot be zero")
    return energy / time

# Additional Engineering Calculations

# Work Done (W = F * d)
def work_done(force, distance):
    """Calculates work done given force and distance"""
    return force * distance

# Pressure (P = F / A)
def pressure(force, area):
    """Calculates pressure given force and area"""
    if area == 0:
        raise ValueError("Area cannot be zero")
    return force / area

# Gravitational Potential Energy (U = m * g * h)
def gravitational_potential_energy(mass, height, gravity=9.81):
    """Calculates gravitational potential energy given mass, height, and gravity"""
    return mass * gravity * height

# Hooke's Law (F = -k * x)
def spring_force(k, displacement):
    """Calculates spring force using Hooke's Law"""
    return -k * displacement

# Momentum (p = m * v)
def momentum(mass, velocity):
    """Calculates momentum given mass and velocity"""
    return mass * velocity

# Mechanical Advantage (MA = F_out / F_in)
def mechanical_advantage(force_output, force_input):
    """Calculates mechanical advantage"""
    if force_input == 0:
        raise ValueError("Input force cannot be zero")
    return force_output / force_input

# Efficiency (Efficiency = (useful power / total power) * 100)
def efficiency(useful_power, total_power):
    """Calculates the efficiency of a system"""
    if total_power == 0:
        raise ValueError("Total power cannot be zero")
    return (useful_power / total_power) * 100

# Torque (τ = F * r)
def torque(force, radius):
    """Calculates torque given force and radius"""
    return force * radius

# Impulse (I = F * Δt)
def impulse(force, time):
    """Calculates impulse given force and time"""
    return force * time

# Work-Energy Theorem (W = ΔK = 0.5 * m * (v_f^2 - v_i^2))
def work_energy_theorem(mass, initial_velocity, final_velocity):
    """Calculates work done using the work-energy theorem"""
    return 0.5 * mass * (final_velocity ** 2 - initial_velocity ** 2)

# Fluid Flow (Q = A * v)
def fluid_flow(area, velocity):
    """Calculates fluid flow given area and velocity"""
    return area * velocity

# Simple Harmonic Motion (T = 2 * π * √(m / k))
def simple_harmonic_motion_period(mass, spring_constant):
    """Calculates the period of a simple harmonic oscillator"""
    return 2 * math.pi * math.sqrt(mass / spring_constant)

# Centripetal Force (F = m * v^2 / r)
def centripetal_force(mass, velocity, radius):
    """Calculates the centripetal force given mass, velocity, and radius"""
    return mass * velocity ** 2 / radius

# Magnetic Force (F = q * v * B * sin(θ))
def magnetic_force(charge, velocity, magnetic_field, angle):
    """Calculates the magnetic force on a moving charge"""
    return charge * velocity * magnetic_field * math.sin(math.radians(angle))

# Thermal Energy (Q = mcΔT)
def thermal_energy(mass, specific_heat, temperature_change):
    """Calculates thermal energy given mass, specific heat, and temperature change"""
    return mass * specific_heat * temperature_change

# Gravitational Force (F = G * (m1 * m2) / r^2)
def gravitational_force(mass1, mass2, distance):
    """Calculates the gravitational force between two masses"""
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    return G * (mass1 * mass2) / (distance ** 2)

# Electric Field (E = F / q)
def electric_field(force, charge):
    """Calculates the electric field given force and charge"""
    if charge == 0:
        raise ValueError("Charge cannot be zero")
    return force / charge

# Capacitance (C = Q / V)
def capacitance(charge, voltage):
    """Calculates capacitance given charge and voltage"""
    if voltage == 0:
        raise ValueError("Voltage cannot be zero")
    return charge / voltage

# Inductance (L = N * Φ / I)
def inductance(num_turns, flux, current):
    """Calculates inductance given number of turns, magnetic flux, and current"""
    if current == 0:
        raise ValueError("Current cannot be zero")
    return num_turns * flux / current

# Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation
def bmr(weight, height, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR).
    Parameters:
    - weight: weight in kg
    - height: height in cm
    - age: age in years
    - gender: 'male' or 'female'
    Returns: BMR in kcal/day
    """
    if gender == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'.")

# Calculate Heart Rate Reserve (HRR) using Karvonen Formula
def heart_rate_reserve(max_heart_rate, resting_heart_rate):
    """
    Calculate the Heart Rate Reserve (HRR) based on maximum and resting heart rate.
    Parameters:
    - max_heart_rate: maximum heart rate (220 - age)
    - resting_heart_rate: resting heart rate in bpm
    Returns: HRR in bpm
    """
    return max_heart_rate - resting_heart_rate

# Calculate Cell Division Time (Time for mitosis)
def cell_division_time(cells_initiated, cells_after, hours):
    """
    Calculate the time taken for cell division.
    Parameters:
    - cells_initiated: initial number of cells
    - cells_after: number of cells after division
    - hours: time taken in hours
    Returns: Cell division time in hours
    """
    if cells_initiated == 0:
        raise ValueError("Initial number of cells must be greater than zero.")
    division_rate = math.log(cells_after / cells_initiated) / math.log(2)
    return hours / division_rate

# Calculate Dilution Factor
def dilution_factor(concentration_initial, concentration_final):
    """
    Calculate the dilution factor in a solution.
    Parameters:
    - concentration_initial: initial concentration (e.g., in mol/L)
    - concentration_final: final concentration (e.g., in mol/L)
    Returns: Dilution factor
    """
    if concentration_final == 0:
        raise ValueError("Final concentration cannot be zero.")
    return concentration_initial / concentration_final

# Calculate Population Growth using the Exponential Growth Model
def population_growth(initial_population, growth_rate, time):
    """
    Calculate population growth based on the exponential growth model.
    Parameters:
    - initial_population: starting population
    - growth_rate: growth rate per time period (as a decimal)
    - time: time in years or other time unit
    Returns: Population after the given time
    """
    return initial_population * math.exp(growth_rate * time)

# Calculate Respiratory Quotient (RQ)
def respiratory_quotient(co2_produced, o2_consumed):
    """
    Calculate the Respiratory Quotient (RQ).
    Parameters:
    - co2_produced: amount of CO2 produced (in liters)
    - o2_consumed: amount of O2 consumed (in liters)
    Returns: RQ (dimensionless)
    """
    if o2_consumed == 0:
        raise ValueError("Oxygen consumed cannot be zero.")
    return co2_produced / o2_consumed

# Calculate Heart Rate Training Zones (Target heart rate for training)
def heart_rate_training_zone(max_heart_rate, intensity_percentage):
    """
    Calculate the target heart rate zone for training at a given intensity.
    Parameters:
    - max_heart_rate: maximum heart rate (220 - age)
    - intensity_percentage: intensity in percentage (e.g., 0.6 for 60% intensity)
    Returns: Target heart rate in bpm
    """
    return (max_heart_rate - 60) * intensity_percentage + 60

# Calculate Clutch Efficiency of Enzyme
def clutch_efficiency(substrate_concentration, enzyme_concentration):
    """
    Calculate the clutch efficiency of an enzyme based on substrate and enzyme concentrations.
    Parameters:
    - substrate_concentration: concentration of substrate in mol/L
    - enzyme_concentration: concentration of enzyme in mol/L
    Returns: Efficiency factor (dimensionless)
    """
    if enzyme_concentration == 0:
        raise ValueError("Enzyme concentration cannot be zero.")
    return substrate_concentration / enzyme_concentration

# Calculate Oxygen Uptake Efficiency Slope (OUES)
def oxygen_uptake_efficiency(vo2_max, work_rate):
    """
    Calculate Oxygen Uptake Efficiency Slope (OUES) based on VO2 max and work rate.
    Parameters:
    - vo2_max: maximal oxygen consumption in ml/kg/min
    - work_rate: rate of work in watts
    Returns: OUES in ml/kcal
    """
    if work_rate == 0:
        raise ValueError("Work rate cannot be zero.")
    return vo2_max / work_rate

# Calculate Glycolysis Rate (Anaerobic Glycolysis Rate)
def glycolysis_rate(glucose, oxygen_consumption, time):
    """
    Calculate the rate of anaerobic glycolysis.
    Parameters:
    - glucose: amount of glucose used (in mol)
    - oxygen_consumption: amount of oxygen consumed (in ml)
    - time: time period in minutes
    Returns: Glycolysis rate in mol/min
    """
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return glucose / time

# Calculate Oxygen Debt
def oxygen_debt(oxygen_consumed, oxygen_borrowed):
    """
    Calculate the oxygen debt after exercise.
    Parameters:
    - oxygen_consumed: total oxygen consumed (in ml)
    - oxygen_borrowed: oxygen borrowed during anaerobic exercise (in ml)
    Returns: Oxygen debt in ml
    """
    return oxygen_consumed - oxygen_borrowed

# Calculate Cardiac Output (CO)
def cardiac_output(heart_rate, stroke_volume):
    """
    Calculate cardiac output based on heart rate and stroke volume.
    Parameters:
    - heart_rate: heart rate in bpm
    - stroke_volume: stroke volume in ml/beat
    Returns: Cardiac output in L/min
    """
    return (heart_rate * stroke_volume) / 1000

# Calculate Neuron Action Potential
def neuron_action_potential(stimulus_strength, threshold):
    """
    Calculate whether an action potential is generated in a neuron.
    Parameters:
    - stimulus_strength: strength of stimulus in mV
    - threshold: threshold potential for neuron action potential in mV
    Returns: Boolean indicating if action potential occurs
    """
    return stimulus_strength >= threshold

# Calculate DNA Replication Time
def dna_replication_time(nucleotides_per_second, total_nucleotides):
    """
    Calculate the time required for DNA replication based on replication rate.
    Parameters:
    - nucleotides_per_second: rate of DNA replication in nucleotides per second
    - total_nucleotides: total number of nucleotides to replicate
    Returns: Time in seconds for DNA replication
    """
    if nucleotides_per_second == 0:
        raise ValueError("Replication rate cannot be zero.")
    return total_nucleotides / nucleotides_per_second

def big_o_complexity(n, complexity="O(n)"):
    """Estimates the number of operations for different time complexities."""
    complexities = {
        "O(1)": 1,
        "O(log n)": math.log2(n) if n > 0 else 0,
        "O(n)": n,
        "O(n log n)": n * math.log2(n) if n > 0 else 0,
        "O(n^2)": n ** 2,
        "O(2^n)": 2 ** n if n < 20 else float('inf'),  # Limit to prevent overflow
        "O(n!)": math.factorial(n) if n < 10 else float('inf')  # Limit to prevent overflow
    }
    return complexities.get(complexity, None)

def shannon_entropy(data):
    """Calculates the Shannon entropy of a given string."""
    if not data:
        return 0
    freq = {char: data.count(char) / len(data) for char in set(data)}
    return -sum(p * math.log2(p) for p in freq.values())

def hamming_distance(s1, s2):
    """Computes the Hamming distance between two equal-length strings."""
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def network_latency(distance_km, speed_kmps=200000):
    """Estimates network latency based on fiber optic speed (~200,000 km/s)."""
    return (distance_km / speed_kmps) * 1000  # Convert seconds to milliseconds

def rsa_modulus(p, q):
    """Computes the modulus (n) for RSA encryption."""
    return p * q

def rsa_totient(p, q):
    """Computes Euler’s totient function for RSA."""
    return (p - 1) * (q - 1)

def compression_ratio(original_size, compressed_size):
    """Calculates the compression ratio of an algorithm."""
    if original_size == 0:
        raise ValueError("Original size must be greater than zero")
    return original_size / compressed_size

def bit_error_rate(errors, total_bits):
    """Calculates the bit error rate (BER) in a digital transmission."""
    if total_bits == 0:
        raise ValueError("Total bits must be greater than zero")
    return errors / total_bits

def cache_hit_ratio(hits, accesses):
    """Computes the cache hit ratio in memory access."""
    if accesses == 0:
        raise ValueError("Total accesses must be greater than zero")
    return hits / accesses

def cpu_throughput(instructions, time_seconds):
    """Calculates CPU throughput as instructions per second."""
    if time_seconds == 0:
        raise ValueError("Time must be greater than zero")
    return instructions / time_seconds

def bandwidth_utilization(bandwidth, data_rate):
    """Calculates network bandwidth utilization percentage."""
    if bandwidth == 0:
        raise ValueError("Bandwidth must be greater than zero")
    return (data_rate / bandwidth) * 100
