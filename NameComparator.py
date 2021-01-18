class NameComparator:

    def isSameName(self, name1, name2):
        if name1 == name2 or (name1.casefold() == name2.casefold()):
            return True

        # Otherwise .lower() of 'İ' is a different unicode value.
        name1 = name1.replace('İ', 'i')
        name2 = name2.replace('İ', 'i')

        name1 = ''.join(i for i in name1 if not i.isdigit())
        name2 = ''.join(i for i in name2 if not i.isdigit())

        turkish_letters = {
            'ü': 'u',
            'ö': 'o',
            'ş': 's',
            'ç': 'c',
            'ğ': 'g',
            'ı': 'i',
        }

        cleanedName1 = ''
        cleanedName2 = ''

        for char in name1.lower():
            if char in turkish_letters.keys():
                cleanedName1 += turkish_letters[char]
            else:
                cleanedName1 += char

        for char in name2.lower():
            if char in turkish_letters.keys():
                cleanedName2 += turkish_letters[char]
            else:
                cleanedName2 += char

        if cleanedName1 == cleanedName2:
            return True

        if cleanedName1 in cleanedName2 or cleanedName2 in cleanedName1:
            return True

        list1 = cleanedName1.split(' ')
        list2 = cleanedName2.split(' ')

        hasSameSurname = list1[-1] == list2[-1]

        if not hasSameSurname:
            return False

        list1.pop()
        list2.pop()

        # Checks if list1 and list2 has at least one element in common
        containsName = bool(set(list1) & set(list2))

        if containsName:
            return True

        for element2 in list2:
            for element1 in list1:
                if element1 in element2:
                    return True

        for element1 in list1:
            for element2 in list2:
                if element2 in element1:
                    return True

        return False
