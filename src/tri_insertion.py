def tri_insertion(tab):
    """Trie une liste en utilisant le tri par insertion."""
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = x
    return tab

if __name__ == "__main__":
    print(tri_insertion([5, 2, 9, 1, 3]))