#Version 2
# Συνάρτηση που βρίσκει τους διαιρέτες ενός αριθμού
def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):  # Εξετάζουμε κάθε αριθμό από το 1 μέχρι το number
        if number % i == 0:  # Αν το number διαιρείται ακριβώς με το i
            divisors.append(i)  # Προσθέτουμε το i στους διαιρέτες
    return divisors


# Κύριο πρόγραμμα
try:
    limit = int(input("Δώσε το όριο των φυσικών αριθμών: "))

    if limit <= 0:  # Έλεγχος αν ο αριθμός είναι θετικός
        print("Παρακαλώ δώστε έναν θετικό ακέραιο αριθμό.")
    else:
        for number in range(2, limit + 1):  # Για κάθε αριθμό από το 2 μέχρι το limit (εξαιρούμε το 1)
            divisors = find_divisors(number)  # Βρίσκουμε τους διαιρέτες
            if len(divisors) <= 2:  # Έλεγχος αν οι διαιρέτες είναι δύο ή λιγότεροι (δηλαδή πρώτος αριθμός)
                print(f"Οι διαιρέτες του {number} είναι: {divisors}")
except ValueError:  # Αν η είσοδος δεν είναι έγκυρος ακέραιος αριθμός
    print("Μη έγκυρη είσοδος. Παρακαλώ δώστε έναν ακέραιο αριθμό.")