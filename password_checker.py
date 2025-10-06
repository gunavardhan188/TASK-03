import re
import math
import time

# Common passwords list (for cybersecurity weak password detection)
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123", "letmein",
    "111111", "iloveyou", "admin", "welcome", "123123", "password1"
]

def calculate_entropy(password):
    """Calculate password entropy (strength in bits)."""
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): charset += 32
    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def time_to_crack(entropy):
    """Estimate time to crack the password (brute force)."""
    guesses_per_second = 1e9  # assuming 1 billion guesses/sec
    seconds = 2 ** entropy / guesses_per_second
    return convert_time(seconds)

def convert_time(seconds):
    """Convert seconds into a readable format."""
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365

    if seconds < minute:
        return f"{seconds:.2f} seconds"
    elif seconds < hour:
        return f"{seconds / minute:.2f} minutes"
    elif seconds < day:
        return f"{seconds / hour:.2f} hours"
    elif seconds < year:
        return f"{seconds / day:.2f} days"
    else:
        return f"{seconds / year:.2f} years"

def check_password_strength(password):
    """Analyze and score password strength."""
    score = 0
    feedback = []
    
    # Check for common passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("❌ This password is very common. Choose something unique!")
        score -= 2
    
    # Length check
    length = len(password)
    if length < 6:
        feedback.append("❌ Too short! Password should be at least 8 characters.")
    elif 6 <= length < 10:
        feedback.append("⚠️ Decent length, but 12+ characters is better.")
        score += 1
    else:
        feedback.append("✅ Good length.")
        score += 2

    # Character variety checks
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0–9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("❌ Add special characters (!, @, #, $, etc.).")

    # Calculate entropy and crack time
    entropy = calculate_entropy(password)
    crack_time = time_to_crack(entropy)

    # Determine overall strength level
    if score <= 2:
        strength = "Weak 🔴"
    elif 3 <= score <= 5:
        strength = "Moderate 🟠"
    else:
        strength = "Strong 🟢"

    # Display report
    print("\n🔐 PASSWORD ANALYSIS REPORT 🔍")
    print("-" * 40)
    print(f"Password: {'*' * len(password)}")
    print(f"Length: {length}")
    print(f"Entropy: {entropy} bits")
    print(f"Estimated Crack Time: {crack_time}")
    print(f"Strength Level: {strength}")
    print(f"Score: {score}/8")
    print("\n🧩 FEEDBACK:")
    for msg in feedback:
        print("  •", msg)
    print("-" * 40)

def password_suggestions():
    """Provide strong password examples."""
    print("\n💡 STRONG PASSWORD EXAMPLES:")
    suggestions = [
        "P@ssw0rd!2025",
        "Teja#Secure$19",
        "Cyb3r$Guard@2025",
        "My$StrongKey#99"
    ]
    for s in suggestions:
        print("   →", s)

def main():
    print("🧠 CYBER SECURITY PROJECT — PASSWORD STRENGTH CHECKER 🔒")
    print("=" * 60)
    time.sleep(0.5)
    while True:
        password = input("\nEnter a password to analyze (or type 'exit' to quit): ")
        if password.lower() == "exit":
            print("👋 Exiting Password Strength Checker. Stay safe online!")
            break
        check_password_strength(password)
        password_suggestions()

# Run the program
if __name__ == "__main__":
    main()
