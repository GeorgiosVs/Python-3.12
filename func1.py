def func(n):
    if n == 0:
        return 0

    largest_power = 1
    while n % 2 == 0:
        largest_power *= 2
        n //= 2

    return largest_power


print(func(36))
print(func(48))
print(func(7))

#Συνάρτηση η οποία με όρισμα τον ακέραιο ν επιστρέφει τη μεγαλύτερη δύναμη του δύο η οποία διαιρεί
#ακριβώς το ν.