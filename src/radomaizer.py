import random
from .erros import Less_num


def randomizer(word_list: list[dict[str, list]], num: int, n: int) -> None:
    all_words = []
    for word, translations in word_list[n].items():
        all_words.append((word, translations))
    if len(all_words) < num:
        raise Less_num(f"in dictionary only {len(all_words)}")
    selected_words = random.sample(all_words, num)
    available_words = [w for w in all_words if w not in selected_words]
    print("Type 'skip' instead of an answer to skip a word.")
    while selected_words:
        print(f"Words left : {len(selected_words)}")
        current_item = selected_words.pop(0)
        word, translations = current_item
        arm_words = ", ".join(translations)
        answer = input(
            f"Translate the word \033[31m'{arm_words}':\033[0m "
            ).strip().lower()
        if answer == "skip":
            print(f"Skipped word: {word}")
            if available_words:
                new_item = random.choice(available_words)
                available_words.remove(new_item)
                selected_words.append(new_item)
                print("Added a new random word to the queue!\n")
            else:
                print("No more new words in dictionary to replace it.\n")
            continue
        if answer == word.lower():
            print("\033[32mCorrect :)!\033[0m\n")
        else:
            print(f"Incorrect answer : \033[31m{word}\033[0m\n")
            selected_words.append(current_item)
