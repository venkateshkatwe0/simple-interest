def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest given principal, rate, and time."""
    return (principal * rate * time) / 100


if __name__ == "__main__":
    print("=== Simple Interest Calculator ===")

    # Fixed values (change them anytime)
    p = 1000
    r = 5
    t = 2

    print("\n=== Program Parameters ===")
    print(f"Principal Amount : {p}")
    print(f"Rate of Interest : {r}%")
    print(f"Time in years    : {t}")

    interest = calculate_simple_interest(p, r, t)
    print(f"\nSimple Interest = {interest:.2f}")
